"""Stage 3b: the critic red-teams the draft.

A gate, not decoration: where it runs, its adjusted confidence is what the
report carries downstream. Reused wherever the pipeline produces something
hallucination-prone.
"""
from __future__ import annotations

from pydantic import BaseModel

from ..llm import LLM

SYSTEM = (
    "You are the critic in a research pipeline. Attack the claim you are given: "
    "is the evidence circular, thin, self-promotional, or a lexical coincidence "
    "rather than a real finding? Argue the strongest case AGAINST it, then rule. "
    "`is_weak` means the claim does not survive scrutiny. "
    "`adjusted_confidence` is what remains standing after your attack (0-1)."
)


class Review(BaseModel):
    is_weak: bool
    argument: str
    adjusted_confidence: float


def challenge(claim: str, llm: LLM, confidence: float) -> Review:
    prompt = (
        f"Claim under scrutiny (stated confidence {confidence:.2f}):\n\n"
        f"{claim}\n\nAttack it without mercy, then rule."
    )
    return llm.parse(SYSTEM, prompt, Review, max_tokens=2048)
