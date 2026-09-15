"""The knowledge base: markdown notes with YAML front-matter, plus GAPS.md.

Plain files on purpose. The KB stays readable in an editor, diffable in git,
and openable in any markdown tool — the pipeline is not the only thing allowed
to touch it.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

from .config import NoteTypeSpec
from .learning.decay import current_confidence
from .models import GapEntry, NoteLink, NoteMeta

_FRONT = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
_GAPS_BLOCK = re.compile(r"```yaml\n(.*?)```", re.S)
# Matches the heading and its bullets only: anything a later pass appended
# below the section must survive regeneration.
_LINKS_SECTION = re.compile(r"^## Links\n(?:- .*\n?)*\n?", re.M)


@dataclass
class Note:
    meta: NoteMeta
    body: str


def parse_note(text: str) -> Note:
    match = _FRONT.match(text)
    if not match:
        raise ValueError("note has no YAML front-matter")
    return Note(meta=NoteMeta.model_validate(yaml.safe_load(match.group(1))),
                body=match.group(2).strip())


def body_with_links(body: str, links: list[NoteLink]) -> str:
    """Mirror the typed front-matter links as [[wikilinks]] in the body.

    Front-matter stays the source of truth; this duplication exists so graph
    views in markdown editors can draw the edges. Regenerated on every save.
    """
    body = _LINKS_SECTION.sub("", body).strip()
    if not links:
        return body
    bullets = "\n".join(f"- {l.type.value} → [[{l.to}]]" for l in links)
    return f"{body}\n\n## Links\n{bullets}"


def render_note(note: Note) -> str:
    front = yaml.safe_dump(note.meta.model_dump(mode="json"),
                           sort_keys=False, allow_unicode=True)
    return f"---\n{front}---\n\n{note.body.strip()}\n"


class KnowledgeBase:
    """Notes on disk, one directory per configured note type."""

    def __init__(self, root: Path, note_types: list[NoteTypeSpec]) -> None:
        self.root = Path(root)
        self.note_types = list(note_types)
        self._dirs = {t.name: t.dir for t in self.note_types}
        self._specs = {t.name: t for t in self.note_types}

    # ---------------------------------------------------------- structure ---
    def init_dirs(self) -> list[Path]:
        """Create one directory per note type. Idempotent."""
        created = []
        for directory in self._dirs.values():
            path = self.root / directory
            path.mkdir(parents=True, exist_ok=True)
            created.append(path)
        return created

    def spec(self, type_name: str) -> NoteTypeSpec:
        try:
            return self._specs[type_name]
        except KeyError:
            raise ValueError(
                f"unknown note type «{type_name}». Configured types: "
                f"{', '.join(self._dirs)}") from None

    def note_path(self, meta: NoteMeta) -> Path:
        return self.root / self.spec(meta.type).dir / f"{meta.id}.md"

    # ------------------------------------------------------------- access ---
    def load_all(self) -> list[Note]:
        notes: list[Note] = []
        for directory in self._dirs.values():
            for path in sorted((self.root / directory).glob("*.md")):
                notes.append(parse_note(path.read_text()))
        return notes

    def get(self, note_id: str) -> Note | None:
        for directory in self._dirs.values():
            path = self.root / directory / f"{note_id}.md"
            if path.exists():
                return parse_note(path.read_text())
        return None

    def exists(self, note_id: str) -> bool:
        return self.get(note_id) is not None

    def save(self, note: Note) -> None:
        path = self.note_path(note.meta)  # also validates the type
        path.parent.mkdir(parents=True, exist_ok=True)
        note.body = body_with_links(note.body, note.meta.links)
        path.write_text(render_note(note))

    def incoming_links(self, note_id: str) -> list[Note]:
        return [n for n in self.load_all()
                if any(l.to == note_id for l in n.meta.links)]

    def delete(self, note_id: str) -> bool:
        """Delete a note and leave the graph consistent: no dangling inbound
        links, no gap pointing at a note that is gone. The gaps themselves
        survive — the hole is still a hole once the note leaves."""
        note = self.get(note_id)
        if note is None:
            return False
        self.note_path(note.meta).unlink()
        for other in self.incoming_links(note_id):
            other.meta.links = [l for l in other.meta.links if l.to != note_id]
            self.save(other)
        gaps = self.read_gaps()
        if touched := [g for g in gaps if note_id in g.related_notes]:
            for gap in touched:
                gap.related_notes = [r for r in gap.related_notes if r != note_id]
            self.write_gaps(gaps)
        return True

    def current_confidence(self, note: Note, today: date | None = None) -> float:
        return current_confidence(note.meta.base_confidence,
                                  note.meta.half_life_days,
                                  note.meta.last_reinforced, today)

    # ------------------------------------------------- GAPS.md, the ledger ---
    def read_gaps(self) -> list[GapEntry]:
        path = self.root / "GAPS.md"
        if not path.exists():
            return []
        match = _GAPS_BLOCK.search(path.read_text())
        if not match:
            return []
        return [GapEntry.model_validate(g) for g in (yaml.safe_load(match.group(1)) or [])]

    def write_gaps(self, gaps: list[GapEntry]) -> None:
        gaps = sorted(gaps, key=lambda g: -g.priority)
        payload = [g.model_dump(mode="json") for g in gaps]
        body = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).rstrip()
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "GAPS.md").write_text(
            "# GAPS — what this knowledge base does not know\n\n"
            f"_Updated {date.today().isoformat()} — {len(gaps)} entries, "
            "highest priority first._\n\n"
            f"```yaml\n{body}\n```\n")
