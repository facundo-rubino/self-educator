"""Resolving contradictions — or deciding they are worth keeping.

Not every contradiction is an error. Two well-sourced notes that disagree can
be the most interesting thing in the graph, so `open_tension` is a first-class
outcome and not a failure to decide.
"""
from __future__ import annotations

from datetime import date
from enum import Enum

from pydantic import BaseModel

from ..kb import KnowledgeBase, Note
from ..llm import LLM
from ..models import GapEntry, GapStatus, GapType

SYSTEM = (
    "You resolve contradictions in a knowledge graph. You are given two notes "
    "that disagree, with their evidence. Rule on the evidence, not on which "
    "sounds better written: `favor_a` or `favor_b` if one is clearly better "
    "supported, `open_tension` if both stand and the disagreement itself is the "
    "finding. Explain the ruling in one short paragraph."
)

#: The losing note is not deleted — its confidence is halved. It may have been
#: right about something the winner did not cover.
LOSER_PENALTY = 0.5


class Ruling(str, Enum):
    favor_a = "favor_a"
    favor_b = "favor_b"
    open_tension = "open_tension"


class Resolution(BaseModel):
    ruling: Ruling
    reasoning: str


def _describe(note: Note) -> str:
    return (f"### {note.meta.id} [{note.meta.type}] "
            f"(confidence {note.meta.base_confidence:.2f}, "
            f"{len(note.meta.sources)} source(s))\n"
            f"{note.meta.title}\n{note.body[:1200]}")


def resolve_gap(kb: KnowledgeBase, gap: GapEntry, llm: LLM,
                today: date | None = None) -> Resolution | None:
    """Rule on one contradiction gap and write the consequence into the graph."""
    today = today or date.today()
    if gap.type is not GapType.contradiction or len(gap.related_notes) != 2:
        return None
    note_a, note_b = (kb.get(i) for i in gap.related_notes)
    if note_a is None or note_b is None:
        gap.status = GapStatus.resolved  # a side is gone; nothing left to weigh
        return None

    resolution = llm.parse(SYSTEM, (
        f"## Note A\n{_describe(note_a)}\n\n"
        f"## Note B\n{_describe(note_b)}\n\n"
        "Which survives, and why?"
    ), Resolution, max_tokens=2048)

    if resolution.ruling is Ruling.open_tension:
        # Both stand. Record why, on both sides, so a later reader sees the
        # disagreement is deliberate rather than an unprocessed bug.
        stamp = f"\n\n## Open tension ({today.isoformat()})\n{resolution.reasoning}"
        for note in (note_a, note_b):
            if "## Open tension" not in note.body:
                note.body += stamp
                kb.save(note)
        gap.status = GapStatus.investigating
        return resolution

    loser = note_b if resolution.ruling is Ruling.favor_a else note_a
    loser.meta.base_confidence = round(loser.meta.base_confidence * LOSER_PENALTY, 4)
    loser.meta.updated = today
    loser.body += (f"\n\n## Downgraded ({today.isoformat()})\n"
                   f"{resolution.reasoning}")
    kb.save(loser)
    gap.status = GapStatus.resolved
    return resolution
