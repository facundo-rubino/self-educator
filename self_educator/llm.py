"""The single LLM client: budget, cost tracking, structured output.

Every LLM call in the pipeline goes through here, which is what makes the
per-run token budget enforceable at all. When the budget runs out the current
stage raises BudgetExceeded and the run reports what it managed to finish.

Two providers implement the same `LLM` protocol. DeepSeek is the default
because it is roughly two orders of magnitude cheaper for this workload, and
stages 3-4 only ever see the handful of items that survived stage 2.
"""
from __future__ import annotations

import json
import os
from typing import Any, Protocol, TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)

ANTHROPIC_MODEL = "claude-opus-5"
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# USD per token. Update alongside the model. Only used for the cost preview
# the CLI shows before spending anything, so being approximately right is the
# requirement — being silently stale is the failure.
PRICES = {
    "anthropic": (5 / 1_000_000, 25 / 1_000_000),
    "deepseek": (0.27 / 1_000_000, 1.10 / 1_000_000),
}


class BudgetExceeded(RuntimeError):
    """The run spent its token allowance (set by the scale preset)."""


class MissingCredentials(RuntimeError):
    """No usable credential. Raised instead of a raw 401 so the first thing a
    new user sees is what to do about it, not a traceback."""


class LLM(Protocol):
    tokens_used: int
    cost_usd: float

    def parse(self, system: str, prompt: str, schema: type[T],
              max_tokens: int = 4096) -> T: ...

    def complete(self, system: str, prompt: str, max_tokens: int = 2048) -> str: ...


class _BudgetedLLM:
    """The half both real clients share: the gate and the meter.

    Extracted once there were two implementations, not before.
    """

    provider: str = ""

    def __init__(self, model: str, token_budget: int | None = None) -> None:
        self.model = model
        self.token_budget = token_budget
        self.tokens_used = 0
        self.cost_usd = 0.0
        self._client = None  # lazy: no API key needed until the first call

    def _gate(self) -> None:
        if self.token_budget is not None and self.tokens_used >= self.token_budget:
            raise BudgetExceeded(
                f"budget spent: {self.tokens_used}/{self.token_budget} tokens")

    def _track_tokens(self, n_in: int, n_out: int) -> None:
        price_in, price_out = PRICES[self.provider]
        self.tokens_used += n_in + n_out
        self.cost_usd += n_in * price_in + n_out * price_out


class AnthropicLLM(_BudgetedLLM):
    """Structured output via `messages.parse`; adaptive thinking throughout."""

    provider = "anthropic"

    def __init__(self, model: str = ANTHROPIC_MODEL,
                 token_budget: int | None = None) -> None:
        super().__init__(model, token_budget)

    @property
    def client(self):
        if self._client is None:
            import anthropic

            self._client = anthropic.Anthropic()
        return self._client

    @staticmethod
    def _call(fn, /, **kwargs):
        """Run an API call, translating an auth failure into a clear error."""
        import anthropic

        message = (
            "No usable Anthropic credential. Set ANTHROPIC_API_KEY in your "
            "environment or in .env (see .env.example). Stages 1 and 2 need no "
            "credential; stages 3 and 4 do."
        )
        try:
            return fn(**kwargs)
        except anthropic.AuthenticationError as exc:
            # A key exists but the API rejected it.
            raise MissingCredentials(message) from exc
        except TypeError as exc:
            # The SDK raises this before any network call when it cannot
            # resolve a credential at all. Narrow it by the SDK's own wording;
            # any other TypeError is a genuine bug and must surface as one.
            if "authentication" not in str(exc).lower():
                raise
            raise MissingCredentials(message) from exc

    def _track(self, usage: Any) -> None:
        self._track_tokens(usage.input_tokens, usage.output_tokens)

    def parse(self, system: str, prompt: str, schema: type[T],
              max_tokens: int = 4096) -> T:
        self._gate()
        resp = self._call(
            self.client.messages.parse,
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
            output_format=schema,
        )
        self._track(resp.usage)
        if resp.parsed_output is None:
            raise RuntimeError(f"model returned no parseable {schema.__name__}")
        return resp.parsed_output

    def complete(self, system: str, prompt: str, max_tokens: int = 2048) -> str:
        self._gate()
        resp = self._call(
            self.client.messages.create,
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        )
        self._track(resp.usage)
        return "".join(b.text for b in resp.content if b.type == "text")


class DeepSeekLLM(_BudgetedLLM):
    """OpenAI-compatible client against DeepSeek.

    DeepSeek has no typed structured-output endpoint, so `parse` carries the
    schema in the system prompt and validates the reply. A model that returns
    malformed JSON gets exactly one more try, with the validation error handed
    back to it — past that the run should fail loudly rather than burn budget.
    """

    provider = "deepseek"

    def __init__(self, model: str = DEEPSEEK_MODEL,
                 token_budget: int | None = None) -> None:
        super().__init__(model, token_budget)

    @property
    def client(self):
        if self._client is None:
            from openai import OpenAI

            key = os.environ.get("DEEPSEEK_API_KEY")
            if not key:
                raise MissingCredentials(
                    "No usable DeepSeek credential. Set DEEPSEEK_API_KEY in your "
                    "environment or in .env (see .env.example). Stages 1 and 2 "
                    "need no credential; stages 3 and 4 do."
                )
            self._client = OpenAI(api_key=key, base_url=DEEPSEEK_BASE_URL)
        return self._client

    def _chat(self, system: str, prompt: str, max_tokens: int,
              json_mode: bool = False) -> str:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": prompt}],
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        resp = self.client.chat.completions.create(**kwargs)
        usage = resp.usage
        if usage is not None:
            self._track_tokens(usage.prompt_tokens, usage.completion_tokens)
        return resp.choices[0].message.content or ""

    def parse(self, system: str, prompt: str, schema: type[T],
              max_tokens: int = 4096) -> T:
        self._gate()
        # DeepSeek's JSON mode requires the word "json" in the prompt, which
        # the schema instruction below supplies.
        instructed = (
            f"{system}\n\n"
            "Reply with a single valid JSON object conforming to this JSON "
            "Schema. No markdown, no code fences, no prose before or after.\n\n"
            f"{json.dumps(schema.model_json_schema(), ensure_ascii=False)}"
        )
        raw = self._chat(instructed, prompt, max_tokens, json_mode=True)
        try:
            return schema.model_validate_json(raw)
        except (ValidationError, ValueError) as exc:
            self._gate()
            retry = (
                f"{prompt}\n\n---\nYour previous reply did not validate against "
                f"the schema:\n{exc}\n\nReturn corrected JSON only."
            )
            raw = self._chat(instructed, retry, max_tokens, json_mode=True)
            try:
                return schema.model_validate_json(raw)
            except (ValidationError, ValueError) as exc2:
                raise RuntimeError(
                    f"model returned no parseable {schema.__name__}: {exc2}"
                ) from exc2

    def complete(self, system: str, prompt: str, max_tokens: int = 2048) -> str:
        self._gate()
        return self._chat(system, prompt, max_tokens)


PROVIDERS = {"anthropic": AnthropicLLM, "deepseek": DeepSeekLLM}


def make_llm(provider: str, model: str | None = None,
             token_budget: int | None = None) -> LLM:
    """Build the client named in config.yaml. The single place that decides."""
    try:
        cls = PROVIDERS[provider]
    except KeyError:
        raise ValueError(
            f"unknown provider {provider!r}; known: {', '.join(sorted(PROVIDERS))}"
        ) from None
    return cls(model=model, token_budget=token_budget) if model else cls(
        token_budget=token_budget)


class FakeLLM:
    """Test double: hands back canned outputs in order.

    Keeps the whole pipeline testable offline — see tests/test_pipeline.py.
    """

    def __init__(self, outputs: list[Any]) -> None:
        self.outputs = list(outputs)
        self.calls: list[tuple[str, str]] = []
        self.tokens_used = 0
        self.cost_usd = 0.0

    def _next(self, system: str, prompt: str) -> Any:
        self.calls.append((system, prompt))
        self.tokens_used += 100
        if not self.outputs:
            raise AssertionError("FakeLLM ran out of canned outputs")
        return self.outputs.pop(0)

    def parse(self, system: str, prompt: str, schema: type[T],
              max_tokens: int = 4096) -> T:
        out = self._next(system, prompt)
        if isinstance(out, schema):
            return out
        if isinstance(out, dict):
            return schema.model_validate(out)
        raise TypeError(f"FakeLLM: expected {schema.__name__}, got {type(out).__name__}")

    def complete(self, system: str, prompt: str, max_tokens: int = 2048) -> str:
        out = self._next(system, prompt)
        if not isinstance(out, str):
            raise TypeError("FakeLLM: expected a str for complete()")
        return out
