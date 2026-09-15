"""Combining scores, and the threshold that decides what reaches the LLM."""
from __future__ import annotations

import numpy as np

from ..models import CalibrationRecord

#: Below this many reviewed signals the learned threshold is noise, so the
#: configured cold-start value is used instead.
MIN_REVIEWED_FOR_LEARNED = 10


def aggregate_score(scores: dict[str, float], weights: dict[str, float]) -> float:
    """Weighted sum, normalised so weights need not total 1.0."""
    total = sum(weights.values()) or 1.0
    return float(sum(scores.get(k, 0.0) * w for k, w in weights.items()) / total)


def effective_threshold(records: dict[str, CalibrationRecord],
                        default: float) -> float:
    """The promotion bar, raised or lowered by the sources' track record.

    This is the loop closing: `edu review` records whether promoted signals
    panned out, and the next run's bar moves accordingly.
    """
    reviewed = sum(r.signals_reviewed for r in records.values())
    if reviewed < MIN_REVIEWED_FOR_LEARNED:
        return default
    learned = [r.learned_threshold for r in records.values() if r.signals_reviewed]
    if not learned:
        return default
    return float(np.clip(float(np.mean(learned)), 0.3, 0.9))
