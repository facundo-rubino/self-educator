"""Stage 2: Document[] -> Signal[]. Deterministic, no LLM.

This is where the volume dies. Hundreds of documents become a handful of scored
clusters, and only those above the promotion threshold cost an LLM call. Getting
this ordering right is the entire cost model of the pipeline.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from ..config import ThemeSpec, best_theme
from ..models import Document, Signal, SignalStatus
from .aggregate import aggregate_score
from .cluster import cluster
from .embedder import Embedder
from .scorers import ScoringContext, score_all


def _dedupe(docs: list[Document]) -> list[Document]:
    seen: set[str] = set()
    return [d for d in docs if not (d.id in seen or seen.add(d.id))]


def detect_signals(
    docs: list[Document],
    baseline: list[list[float]],
    topic: str,
    *,
    embedder: Embedder,
    weights: dict[str, float],
    cluster_threshold: float = 0.55,
    top_n: int = 6,
    promotion_threshold: float = 0.6,
    themes: list["ThemeSpec"] | None = None,
    now: datetime | None = None,
) -> tuple[list[Signal], list[list[float]]]:
    """Return the scored signals plus this run's centroids (for the baseline)."""
    themes = themes or []
    docs = _dedupe(docs)
    if not docs:
        return [], []
    now = now or datetime.now(timezone.utc)

    # Title carries most of the signal; a slice of body disambiguates.
    vectors = embedder.embed([f"{d.title}\n{d.text[:500]}" for d in docs])
    for doc, vec in zip(docs, vectors):
        doc.embedding = [float(x) for x in vec]

    signals: list[Signal] = []
    centroids: list[list[float]] = []
    for group in cluster(vectors, cluster_threshold):
        members = [docs[i] for i in group]
        centroid = vectors[group].mean(axis=0)
        centroids.append([float(x) for x in centroid])
        ctx = ScoringContext(corpus=docs, centroid=centroid,
                             baseline=baseline, now=now, themes=themes)
        scores = score_all(members, ctx, weights)
        headline = max(members, key=lambda d: d.engagement())
        member_ids = sorted(d.id for d in members)
        signals.append(Signal(
            id="sig-" + hashlib.sha256("|".join(member_ids).encode()).hexdigest()[:12],
            topic=topic,
            label=headline.title[:120],
            member_doc_ids=member_ids,
            member_sources=sorted({d.source for d in members}),
            headline_url=headline.url,
            theme=(matched.name if (matched := best_theme(
                " ".join(f"{d.title} {d.text[:300]}" for d in members),
                themes)[0]) else ""),
            scores=scores,
            aggregate_score=round(aggregate_score(scores, weights), 4),
            first_seen=min(d.created_at for d in members),
            sources_count=len({d.source for d in members}),
        ))

    signals.sort(key=lambda s: -s.aggregate_score)
    promoted = 0
    for signal in signals[:top_n]:
        if signal.aggregate_score >= promotion_threshold:
            signal.status = SignalStatus.promoted
            promoted += 1
    if promoted == 0 and signals:
        # Cold start: with nothing promoted there is no report, no note, and
        # no calibration data — so the learning loop would never get going.
        signals[0].status = SignalStatus.promoted
    return signals, centroids
