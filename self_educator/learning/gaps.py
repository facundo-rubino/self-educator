"""The attention ledger: what the KB does not know, ranked.

This is the mechanism that lets the knowledge base steer its own next run.
`edu run --from-gaps` takes the highest-priority open gap and ingests against
it instead of against whatever the user happened to type.
"""
from __future__ import annotations

from collections import Counter
from datetime import date

from ..kb import KnowledgeBase
from ..models import GapEntry, GapStatus, GapType, LinkType

#: Contradictions first: an unresolved contradiction poisons everything that
#: reads either side. Orphans last: usually a linking oversight, not a hole.
PRIORITY: dict[GapType, float] = {
    GapType.contradiction: 0.9,
    GapType.open_question: 0.7,
    GapType.thin_evidence: 0.5,
    GapType.orphan: 0.4,
}

MIN_SOURCES = 2
MIN_TOPIC_NOTES = 3
STALE_CONFIDENCE = 0.3


def _gap(gap_type: GapType, description: str, related: list[str],
         today: date) -> GapEntry:
    return GapEntry(id=GapEntry.make_id(description), type=gap_type,
                    description=description, related_notes=related,
                    priority=PRIORITY[gap_type], created=today)


def find_gaps(kb: KnowledgeBase, today: date | None = None) -> list[GapEntry]:
    """Derive gaps from the current state of the graph. Pure — writes nothing."""
    today = today or date.today()
    notes = kb.load_all()
    gaps: list[GapEntry] = []
    seen_pairs: set[tuple[str, str]] = set()

    for note in notes:
        if len(note.meta.sources) < MIN_SOURCES:
            gaps.append(_gap(
                GapType.thin_evidence,
                f"Note '{note.meta.id}' rests on {len(note.meta.sources)} source(s)",
                [note.meta.id], today))
        if not note.meta.links and not kb.incoming_links(note.meta.id):
            gaps.append(_gap(
                GapType.orphan,
                f"Note '{note.meta.id}' connects to nothing in the graph",
                [note.meta.id], today))
        if kb.current_confidence(note, today) < STALE_CONFIDENCE:
            gaps.append(_gap(
                GapType.open_question,
                f"Note '{note.meta.id}' has decayed — does it still hold?",
                [note.meta.id], today))
        for link in note.meta.links:
            if link.type is LinkType.contradicts:
                pair = tuple(sorted([note.meta.id, link.to]))
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                gaps.append(_gap(
                    GapType.contradiction,
                    f"Unresolved contradiction between '{pair[0]}' and '{pair[1]}'",
                    list(pair), today))

    for topic, count in Counter(n.meta.topic for n in notes).items():
        if count < MIN_TOPIC_NOTES:
            gaps.append(_gap(
                GapType.thin_evidence,
                f"Topic '{topic}' is thinly covered ({count} note(s))", [], today))
    return gaps


def refresh_gaps(kb: KnowledgeBase, today: date | None = None) -> list[GapEntry]:
    """Re-derive gaps, preserving the status and creation date of known ones.

    Resolved gaps that no longer re-derive are kept as history — they record
    that the question was asked and answered.
    """
    existing = {g.id: g for g in kb.read_gaps()}
    merged: dict[str, GapEntry] = {}
    for gap in find_gaps(kb, today):
        if prior := existing.get(gap.id):
            gap.status = prior.status
            gap.created = prior.created
        merged[gap.id] = gap
    for gap_id, gap in existing.items():
        if gap_id not in merged and gap.status is GapStatus.resolved:
            merged[gap_id] = gap
    result = list(merged.values())
    kb.write_gaps(result)
    return result


def target_from_gaps(kb: KnowledgeBase) -> tuple[str, str] | None:
    """Let the KB choose the next run's target. Returns (topic, query).

    Marks the chosen gap `investigating` so successive runs move down the
    ledger instead of hammering the same hole.
    """
    gaps = kb.read_gaps()
    open_gaps = sorted([g for g in gaps if g.status is GapStatus.open],
                       key=lambda g: -g.priority)
    if not open_gaps:
        return None
    top = open_gaps[0]
    topic = ""
    for note_id in top.related_notes:
        if note := kb.get(note_id):
            topic = note.meta.topic
            break
    top.status = GapStatus.investigating
    kb.write_gaps(gaps)
    return topic, top.description
