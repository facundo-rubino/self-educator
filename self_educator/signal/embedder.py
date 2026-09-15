"""Embeddings for clustering and novelty. Stage 2 — no LLM.

Two implementations on purpose: the template must run with zero setup, and it
must not force a torch install on someone who only wants to see the flow.
"""
from __future__ import annotations

import logging
import zlib
from typing import Protocol

import numpy as np

log = logging.getLogger(__name__)


class Embedder(Protocol):
    def embed(self, texts: list[str]) -> np.ndarray: ...


class HashingEmbedder:
    """Deterministic fallback: character trigrams hashed into buckets.

    Crude but real — it captures lexical overlap, needs no model download, and
    makes tests reproducible.
    """

    def __init__(self, dims: int = 256) -> None:
        self.dims = dims

    def embed(self, texts: list[str]) -> np.ndarray:
        out = np.zeros((len(texts), self.dims), dtype=np.float32)
        for i, text in enumerate(texts):
            t = " ".join(text.lower().split())
            for j in range(max(0, len(t) - 2)):
                out[i, zlib.crc32(t[j:j + 3].encode()) % self.dims] += 1.0
        norms = np.linalg.norm(out, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return out / norms


class SentenceTransformerEmbedder:
    """Real semantic embeddings. Requires the optional `ml` extra."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        from sentence_transformers import SentenceTransformer  # lazy: torch is heavy

        self._model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]) -> np.ndarray:
        return np.asarray(self._model.encode(texts, normalize_embeddings=True))


def get_embedder() -> Embedder:
    """Best available, degrading quietly. Never fails the run."""
    try:
        return SentenceTransformerEmbedder()
    except ImportError:
        log.info("sentence-transformers not installed (extra `ml`); "
                 "using the deterministic HashingEmbedder.")
    except Exception as exc:  # noqa: BLE001 — a broken model must not kill the run
        log.warning("ML embedder unavailable (%s); using HashingEmbedder.", exc)
    return HashingEmbedder()
