"""The budget gate and the credential guard — both are first-run experiences."""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from pydantic import BaseModel

from self_educator.llm import (PRICES, AnthropicLLM, BudgetExceeded, DeepSeekLLM,
                               FakeLLM, MissingCredentials, make_llm)


class Shape(BaseModel):
    value: str


def test_budget_gate_fires_before_spending_more():
    llm = AnthropicLLM(token_budget=100)
    llm.tokens_used = 100
    with pytest.raises(BudgetExceeded, match="100/100"):
        llm.parse("s", "p", Shape)


def test_budget_of_none_never_gates():
    llm = AnthropicLLM(token_budget=None)
    llm.tokens_used = 10**9
    llm._gate()  # no raise


def test_a_401_becomes_an_actionable_message_not_a_traceback():
    import anthropic
    import httpx

    response = httpx.Response(
        401, request=httpx.Request("POST", "https://api.anthropic.com/v1/messages"))

    def unauthorized(**kwargs):
        raise anthropic.AuthenticationError(
            message="invalid x-api-key", response=response, body=None)

    with pytest.raises(MissingCredentials) as excinfo:
        AnthropicLLM._call(unauthorized)
    message = str(excinfo.value)
    assert "ANTHROPIC_API_KEY" in message
    assert "Stages 1 and 2 need no credential" in message


def test_other_api_errors_are_not_swallowed():
    def boom(**kwargs):
        raise ValueError("something else went wrong")

    with pytest.raises(ValueError, match="something else"):
        AnthropicLLM._call(boom)


def test_fake_llm_accepts_instances_and_dicts():
    llm = FakeLLM([Shape(value="a"), {"value": "b"}])
    assert llm.parse("s", "p", Shape).value == "a"
    assert llm.parse("s", "p", Shape).value == "b"


def test_fake_llm_refuses_the_wrong_shape():
    llm = FakeLLM(["not a model"])
    with pytest.raises(TypeError, match="expected Shape"):
        llm.parse("s", "p", Shape)


def test_fake_llm_running_dry_is_an_explicit_failure():
    with pytest.raises(AssertionError, match="ran out of canned outputs"):
        FakeLLM([]).parse("s", "p", Shape)


def test_an_unresolvable_credential_is_caught_before_the_network_call():
    """The SDK raises TypeError, not a 401, when there is no key at all —
    which is exactly the first-run case."""
    def unresolvable(**kwargs):
        raise TypeError('"Could not resolve authentication method. Expected '
                        'one of api_key, auth_token, or credentials to be set."')

    with pytest.raises(MissingCredentials, match="ANTHROPIC_API_KEY"):
        AnthropicLLM._call(unresolvable)


def test_an_unrelated_type_error_still_surfaces_as_a_bug():
    def bad_call(**kwargs):
        raise TypeError("parse() got an unexpected keyword argument 'nonsense'")

    with pytest.raises(TypeError, match="unexpected keyword"):
        AnthropicLLM._call(bad_call)


# --------------------------------------------------------------- DeepSeek ---
# DeepSeek has no typed structured-output endpoint, so `parse` carries the
# schema in the prompt and validates the reply itself. That validation and its
# single retry are the only real logic in the client, so they are what is
# tested here — offline, with a stub in place of the SDK.


class Parsed(BaseModel):
    name: str
    size: int


class StubChat:
    """Stands in for `openai.OpenAI().chat.completions`."""

    def __init__(self, replies: list[str]) -> None:
        self.replies = list(replies)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(
                content=self.replies.pop(0)))],
            usage=SimpleNamespace(prompt_tokens=10, completion_tokens=5),
        )


def _stubbed(replies: list[str], **kw) -> tuple[DeepSeekLLM, StubChat]:
    llm = DeepSeekLLM(**kw)
    chat = StubChat(replies)
    llm._client = SimpleNamespace(chat=SimpleNamespace(completions=chat))
    return llm, chat


def test_parse_validates_good_json_into_the_schema():
    llm, chat = _stubbed(['{"name": "circle", "size": 3}'])
    out = llm.parse("sys", "prompt", Parsed)
    assert out == Parsed(name="circle", size=3)
    assert len(chat.calls) == 1
    assert chat.calls[0]["response_format"] == {"type": "json_object"}


def test_parse_sends_the_schema_so_the_model_can_comply():
    llm, chat = _stubbed(['{"name": "a", "size": 1}'])
    llm.parse("be terse", "go", Parsed)
    system = chat.calls[0]["messages"][0]["content"]
    assert "be terse" in system
    assert '"size"' in system          # the JSON Schema itself
    assert "json" in system.lower()    # DeepSeek's JSON mode requires the word


def test_parse_retries_once_on_malformed_json_and_recovers():
    llm, chat = _stubbed(["not json at all", '{"name": "square", "size": 4}'])
    assert llm.parse("sys", "prompt", Parsed).name == "square"
    assert len(chat.calls) == 2
    # The retry hands the model its own error, rather than asking again blind.
    assert "did not validate" in chat.calls[1]["messages"][1]["content"]


def test_parse_gives_up_after_the_second_failure():
    llm, chat = _stubbed(["nope", "still nope"])
    with pytest.raises(RuntimeError, match="no parseable Parsed"):
        llm.parse("sys", "prompt", Parsed)
    assert len(chat.calls) == 2       # one retry, not a loop


def test_parse_retry_respects_a_spent_budget():
    # The first call spends the budget; the retry must not be attempted.
    llm, chat = _stubbed(["bad json"], token_budget=12)
    with pytest.raises(BudgetExceeded):
        llm.parse("sys", "prompt", Parsed)
    assert len(chat.calls) == 1


def test_complete_returns_text_and_meters_tokens_and_cost():
    llm, _ = _stubbed(["plain answer"])
    assert llm.complete("sys", "prompt") == "plain answer"
    assert llm.tokens_used == 15
    price_in, price_out = PRICES["deepseek"]
    assert llm.cost_usd == pytest.approx(10 * price_in + 5 * price_out)


def test_missing_key_names_the_variable_to_set(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    with pytest.raises(MissingCredentials, match="DEEPSEEK_API_KEY"):
        _ = DeepSeekLLM().client


def test_deepseek_is_cheaper_than_anthropic_which_is_why_it_is_the_default():
    assert PRICES["deepseek"] < PRICES["anthropic"]


def test_make_llm_builds_the_provider_named_in_config():
    assert isinstance(make_llm("deepseek"), DeepSeekLLM)
    assert make_llm("deepseek", "deepseek-reasoner").model == "deepseek-reasoner"


def test_make_llm_rejects_an_unknown_provider_by_name():
    with pytest.raises(ValueError, match="unknown provider"):
        make_llm("gpt-please")
