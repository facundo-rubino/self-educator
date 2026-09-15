"""Calibration: did the signals we promoted actually pan out?

Without this the pipeline never learns from being wrong. Old promoted signals
are re-examined, the verdict is recorded per source, and each source's hit rate
moves the promotion bar for the next run. A source that keeps lying gets a
higher bar automatically.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from pydantic import BaseModel

from ..llm import LLM
from ..models import CalibrationRecord, Signal, Verdict
from ..storage import Store

SYSTEM = (
    "You are the calibration reviewer. You are shown a signal that was promoted "
    "some weeks ago. Judge, with what you know: did it materialise (`hit`), was "
    "it noise (`miss`), is it real but too early (`too_early`), or can you not "
    "tell (`unclear`)? Be honest — the point of this pass is to catch the "
    "pipeline's own mistakes, not to defend them."
)

#: Hit rate maps onto the promotion bar: a source at 0% accuracy gets the
#: maximum bar, a perfect source the minimum. Never fully trusted, never
#: fully silenced.
MIN_LEARNED, MAX_LEARNED = 0.4, 0.85


class ReviewVerdict(BaseModel):
    verdict: Verdict
    notes: str


def due_for_review(signals: list[Signal], review_after_days: int,
                   now: datetime | None = None) -> list[Signal]:
    """Promoted signals old enough to judge and not yet judged."""
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=review_after_days)
    out = []
    for signal in signals:
        if signal.status.value != "promoted" or signal.outcome.verdict is not None:
            continue
        first_seen = signal.first_seen
        if first_seen.tzinfo is None:
            first_seen = first_seen.replace(tzinfo=timezone.utc)
        if first_seen <= cutoff:
            out.append(signal)
    return out


def review_signal(signal: Signal, llm: LLM) -> ReviewVerdict:
    scores = " ".join(f"{k}={v:.2f}" for k, v in signal.scores.items())
    return llm.parse(SYSTEM, (
        f"Topic: {signal.topic}\n"
        f"Signal promoted on {signal.first_seen.date()}: {signal.label}\n"
        f"Scores at the time: {scores}\n"
        f"Sources: {', '.join(signal.member_sources)}\n\n"
        "Did this hold up?"
    ), ReviewVerdict, max_tokens=1024)


def _learned_threshold(hit_rate: float) -> float:
    return round(MAX_LEARNED - (MAX_LEARNED - MIN_LEARNED) * hit_rate, 4)


def record_outcome(store: Store, signal: Signal, verdict: Verdict,
                   notes: str, now: datetime | None = None) -> None:
    """Persist the verdict on the signal and fold it into each source's record."""
    now = now or datetime.now(timezone.utc)
    signal.outcome.verdict = verdict
    signal.outcome.reviewed_at = now
    signal.outcome.notes = notes
    store.save_signal(signal)

    records = store.load_calibration()
    for source in signal.member_sources:
        record = records.get(source) or CalibrationRecord(source=source, updated=now)
        record.signals_reviewed += 1
        if verdict is Verdict.hit:
            record.hits += 1
        elif verdict is Verdict.miss:
            record.misses += 1
        elif verdict is Verdict.too_early:
            record.too_early += 1
        decided = record.hits + record.misses
        record.hit_rate = round(record.hits / decided, 4) if decided else 0.0
        record.learned_threshold = _learned_threshold(record.hit_rate)
        record.updated = now
        store.save_calibration(record)
