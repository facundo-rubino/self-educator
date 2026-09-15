"""Stage 3: a promoted Signal becomes a Report, with the debate on record."""
from __future__ import annotations

from datetime import datetime, timezone

from ..llm import LLM
from ..models import CriticVerdict, Document, Report, Signal
from .analyst import analyse
from .critic import challenge

#: A claim the critic rejects cannot carry high confidence downstream, however
#: sure the analyst was.
WEAK_CONFIDENCE_CAP = 0.3


def enrich(signal: Signal, docs: list[Document], llm: LLM, *,
           query: str | None = None, include_critic: bool = True) -> Report:
    tokens_before = llm.tokens_used
    draft = analyse(signal, docs, llm, query=query)
    transcript = [f"## Analyst\n{draft.summary}\n\n"
                  f"Initial confidence: {draft.confidence:.2f}"]

    if include_critic:
        review = challenge(f"{signal.label}\n\n{draft.summary}", llm, draft.confidence)
        transcript.append(
            f"## Critic\n{review.argument}\n\n"
            f"Verdict: {'WEAK' if review.is_weak else 'survives'} — "
            f"adjusted confidence: {review.adjusted_confidence:.2f}")
        verdict = CriticVerdict(is_weak=review.is_weak, argument=review.argument)
        confidence = (min(review.adjusted_confidence, WEAK_CONFIDENCE_CAP)
                      if review.is_weak else review.adjusted_confidence)
    else:
        verdict = CriticVerdict(is_weak=False,
                                argument="(scale XS: no critic pass)")
        confidence = draft.confidence

    return Report(
        signal_id=signal.id,
        summary=draft.summary,
        evidence=draft.evidence,
        implications=draft.implications,
        risks=draft.risks,
        critic=verdict,
        transcript="\n\n".join(transcript),
        confidence=confidence,
        generated_at=datetime.now(timezone.utc),
        token_cost=llm.tokens_used - tokens_before,
    )
