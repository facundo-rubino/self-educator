"""Greedy single-pass clustering by cosine similarity. Stage 2 — no LLM.

Deliberately simple: one pass, no k to choose, order-dependent but stable for a
fixed corpus. Swap in HDBSCAN or agglomerative clustering if your corpus is
large enough to justify it — nothing downstream depends on how groups are formed.
"""
from __future__ import annotations

import numpy as np


#: A story worth one brief item is a handful of posts, not the whole corpus.
#: Past this a cluster stops accepting members: with a weak embedder the
#: running centroid drifts toward "generic text" and swallows everything.
MAX_CLUSTER_SIZE = 25


def cluster(vectors: np.ndarray, threshold: float = 0.55,
            max_size: int = MAX_CLUSTER_SIZE) -> list[list[int]]:
    """Return groups of row indices. Every row lands in exactly one group."""
    clusters: list[list[int]] = []
    centroids: list[np.ndarray] = []
    for i in range(vectors.shape[0]):
        v = vectors[i]
        best, best_sim = -1, threshold
        for c, centroid in enumerate(centroids):
            if len(clusters[c]) >= max_size:
                continue
            denom = float(np.linalg.norm(centroid) * np.linalg.norm(v)) + 1e-9
            sim = float(v @ centroid) / denom
            if sim >= best_sim:
                best, best_sim = c, sim
        if best == -1:
            clusters.append([i])
            centroids.append(v.astype(np.float64).copy())
        else:
            clusters[best].append(i)
            k = len(clusters[best])
            centroids[best] = (centroids[best] * (k - 1) + v) / k
    return clusters
