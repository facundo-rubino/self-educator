"""Stage 3a: the analyst drafts a report from a promoted signal's documents."""
from __future__ import annotations

from pydantic import BaseModel

from ..llm import LLM
from ..models import Document, Evidence, Signal

SYSTEM = (
    "You are the analyst in a research pipeline. You receive a signal — a "
    "cluster of ingested documents that survived deterministic filtering — and "
    "produce a dense, honest report on it. Every evidence claim MUST cite the "
    "doc_id in square brackets it came from; never write anything from memory. "
    "`confidence` is your honest probability (0-1) that the finding is real "
    "and holds up."
)


class Draft(BaseModel):
    summary: str
    evidence: list[Evidence] = []
    implications: list[str] = []
    risks: list[str] = []
    confidence: float


def analyse(signal: Signal, docs: list[Document], llm: LLM,
            query: str | None = None) -> Draft:
    context = "\n\n".join(
        f"[{d.id}] ({d.source}, engagement={d.engagement():.0f}) {d.title}\n"
        f"{d.text[:400]}"
        for d in docs[:20]  # the cluster's head; the tail rarely adds signal
    )
    scores = " ".join(f"{k}={v:.2f}" for k, v in signal.scores.items())
    prompt = (
        f"Topic: {signal.topic}\n"
        f"Signal: {signal.label}\n"
        f"Scores: {scores}\n\n"
        f"Documents in this cluster:\n{context}\n\n"
        "What is going on here, what evidence supports it, what does it imply, "
        "and what would make it wrong?"
    )
    if query:
        # A lens for reading, never a filter — the candidates are already fixed.
        prompt += (
            f"\n\nOptional framing (guides interpretation; do NOT discard "
            f"anything because of it): read this through the lens of «{query}»."
        )
    return llm.parse(SYSTEM, prompt, Draft)
