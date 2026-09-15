"""Confidence decay. Runs automatically at the start of every run.

Current confidence is always computed, never stored: writing it down would
mean the number is only correct on the day it was written.
"""
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..kb import Note

#: Below this, a note is stale enough to flag for revalidation. It is never
#: deleted — a decayed note is a question, not garbage.
STALE_THRESHOLD = 0.2


def current_confidence(base: float, half_life_days: int,
                       last_reinforced: date, today: date | None = None) -> float:
    """Exponential decay from the last time evidence reinforced the note."""
    today = today or date.today()
    days = max(0, (today - last_reinforced).days)
    return base * 0.5 ** (days / max(1, half_life_days))


def flag_decayed(notes: list["Note"], threshold: float = STALE_THRESHOLD,
                 today: date | None = None) -> list[str]:
    """Ids of notes that have decayed below the threshold."""
    return [
        n.meta.id for n in notes
        if current_confidence(n.meta.base_confidence, n.meta.half_life_days,
                              n.meta.last_reinforced, today) < threshold
    ]
