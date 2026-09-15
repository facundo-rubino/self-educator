"""The scorer registry. Stage 2 — deterministic, no LLM.

A scorer answers one question about a cluster with a number in [0, 1]. Four
ship with the template; `register` adds your own, and `config.yaml`'s
`signal.weights` decides which ones run and how much each counts.

Metric-dependent scorers return NEUTRAL when the cluster's documents carry no
engagement numbers. An RSS-only corpus has no upvotes, and scoring that as zero
interest would bury every signal from it.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable

import numpy as np

from ..config import ThemeSpec, best_theme
from ..models import Document

NEUTRAL = 0.5

#: Headline shapes that signal a piece is written to be clicked rather than
#: read. Deterministic on purpose: this is stage 2, and it costs nothing.
_CLICKBAIT = (
    "you won't believe", "you wont believe", "this one trick", "shocking",
    "will blow your mind", "what happened next", "nobody is talking about",
    "the truth about", "everyone is wrong", "changed my life", "in 2026",
    "must-read", "must read", "game changer", "game-changer", "goes viral",
)

#: Self-help and motivational register. Facundo ruled this out explicitly, so
#: it is filtered at the cheap stage rather than argued with at the expensive
#: one.
_SELF_HELP = (
    "morning routine", "rutina matutina", "productivity hack", "life hack",
    "mindset", "habits that", "habitos que", "unlock your", "10x your",
    "secrets of", "secretos de", "millionaire", "millonario", "manifest",
    "discipline equals", "grind", "hustle",
)


@dataclass
class ScoringContext:
    """Everything a scorer may look at beyond its own cluster."""

    corpus: list[Document]          # every document in this run
    centroid: np.ndarray            # this cluster's mean embedding
    baseline: list[list[float]]     # centroids from previous runs
    now: datetime
    themes: list[ThemeSpec] = field(default_factory=list)


Scorer = Callable[[list[Document], ScoringContext], float]

SCORERS: dict[str, Scorer] = {}


def register(name: str) -> Callable[[Scorer], Scorer]:
    """Decorator. The name is what you reference in `signal.weights`."""

    def wrap(fn: Scorer) -> Scorer:
        SCORERS[name] = fn
        return fn

    return wrap


@register("velocity")
def velocity(docs: list[Document], ctx: ScoringContext) -> float:
    """Engagement per hour since publication, squashed with tanh.

    Answers: is this accelerating, or merely old and large?
    """
    scored = [d for d in docs if d.has_metrics()]
    if not scored:
        return NEUTRAL
    rates = []
    for d in scored:
        created = d.created_at if d.created_at.tzinfo else \
            d.created_at.replace(tzinfo=timezone.utc)
        age_hours = max(1.0, (ctx.now - created).total_seconds() / 3600)
        rates.append(d.engagement() / age_hours)
    return float(np.tanh(float(np.mean(rates)) / 5.0))


@register("corroboration")
def corroboration(docs: list[Document], ctx: ScoringContext) -> float:
    """How many distinct sources see the same thing.

    A cluster drawn from one source is one perspective, not a consensus.
    """
    if not docs:
        return 0.0
    available = len({d.source for d in ctx.corpus}) or 1
    return min(1.0, len({d.source for d in docs}) / available)


@register("novelty")
def novelty(docs: list[Document], ctx: ScoringContext) -> float:
    """Distance from everything previous runs already covered.

    Without a baseline (the first run) everything is new, which is correct.
    """
    if not ctx.baseline or len(ctx.baseline[0]) != ctx.centroid.shape[0]:
        return 1.0
    base = np.asarray(ctx.baseline, dtype=np.float64)
    c = ctx.centroid.astype(np.float64)
    denom = np.linalg.norm(base, axis=1) * np.linalg.norm(c)
    denom[denom == 0] = 1e-12
    return float(np.clip(1.0 - float(np.max((base @ c) / denom)), 0.0, 1.0))


@register("surprise")
def surprise(docs: list[Document], ctx: ScoringContext) -> float:
    """How far the cluster's best document beats the norm for its own source.

    Normalising per source keeps a busy source from dominating a quiet one.
    """
    scored = [d for d in docs if d.has_metrics()]
    if not scored:
        return NEUTRAL
    top = max(scored, key=lambda d: d.engagement())
    peers = [d.engagement() for d in ctx.corpus
             if d.source == top.source and d.has_metrics()]
    median = float(np.median(peers)) if peers else 0.0
    if median <= 0:
        return NEUTRAL
    ratio = top.engagement() / median
    return float(ratio / (ratio + 1.0))


def score_all(docs: list[Document], ctx: ScoringContext,
              weights: dict[str, float]) -> dict[str, float]:
    """Run every scorer named in `weights`. Unknown names raise loudly —
    a typo there would silently change how everything is ranked."""
    unknown = set(weights) - set(SCORERS)
    if unknown:
        raise KeyError(
            f"unregistered scorer(s) in signal.weights: {', '.join(sorted(unknown))}. "
            f"Registered: {', '.join(sorted(SCORERS))}")
    return {name: round(float(SCORERS[name](docs, ctx)), 4) for name in weights}


def _cluster_text(docs: list[Document]) -> str:
    return " ".join(f"{d.title} {d.text[:300]}" for d in docs)


@register("relevance")
def relevance(docs: list[Document], ctx: ScoringContext) -> float:
    """Is this about what I am actually learning, and is it written to be read?

    Three deterministic judgements in one number: how well the cluster matches
    a configured theme, minus a penalty for clickbait phrasing, minus one for
    the self-help register. With no themes configured it returns NEUTRAL, so a
    fresh install behaves exactly as it did before this scorer existed.
    """
    if not ctx.themes:
        return NEUTRAL

    text = _cluster_text(docs)
    _, score = best_theme(text, ctx.themes)

    low = text.lower()
    titles = " ".join(d.title for d in docs).lower()
    penalty = 0.0
    if any(p in low for p in _CLICKBAIT):
        penalty += 0.4
    if any(p in low for p in _SELF_HELP):
        penalty += 0.4
    # A headline that is only a question is usually withholding the answer.
    if titles.count("?") >= max(1, len(docs)):
        penalty += 0.15

    return float(max(0.0, min(1.0, score - penalty)))
