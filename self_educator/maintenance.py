"""Health of the graph. Local, free, and safe to run in CI or a pre-commit hook."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import date

from .kb import KnowledgeBase
from .learning.decay import STALE_THRESHOLD
from .models import GapType, LinkType


@dataclass
class LintReport:
    broken_links: list[str] = field(default_factory=list)
    orphans: list[str] = field(default_factory=list)
    duplicate_titles: list[str] = field(default_factory=list)
    unregistered_contradictions: list[str] = field(default_factory=list)
    decayed: list[str] = field(default_factory=list)

    @property
    def problems(self) -> int:
        return (len(self.broken_links) + len(self.orphans)
                + len(self.duplicate_titles)
                + len(self.unregistered_contradictions) + len(self.decayed))


def lint(kb: KnowledgeBase, today: date | None = None) -> LintReport:
    today = today or date.today()
    notes = kb.load_all()
    ids = {n.meta.id for n in notes}
    report = LintReport()

    registered = {
        tuple(sorted(g.related_notes))
        for g in kb.read_gaps() if g.type is GapType.contradiction
    }
    inbound: set[str] = {l.to for n in notes for l in n.meta.links}

    for note in notes:
        for link in note.meta.links:
            if link.to not in ids:
                report.broken_links.append(
                    f"{note.meta.id} → {link.to} ({link.type.value})")
            # A contradiction with no gap entry never reaches `edu reconcile`,
            # so it would sit in the graph unresolved and unnoticed.
            if link.type is LinkType.contradicts:
                pair = tuple(sorted([note.meta.id, link.to]))
                if pair not in registered:
                    report.unregistered_contradictions.append(" ↔ ".join(pair))
        if not note.meta.links and note.meta.id not in inbound:
            report.orphans.append(note.meta.id)
        if kb.current_confidence(note, today) < STALE_THRESHOLD:
            report.decayed.append(note.meta.id)

    for title, count in Counter(n.meta.title.strip().lower() for n in notes).items():
        if count > 1:
            report.duplicate_titles.append(f"{title} ({count} notes)")

    report.unregistered_contradictions = sorted(set(report.unregistered_contradictions))
    return report
