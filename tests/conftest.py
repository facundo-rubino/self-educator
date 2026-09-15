"""Shared fixtures. Everything here runs offline — no network, no API key."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from self_educator.config import Config, KBConfig, NoteTypeSpec, SourcesConfig
from self_educator.kb import KnowledgeBase, Note
from self_educator.models import Document, NoteMeta
from self_educator.signal.embedder import HashingEmbedder
from self_educator.storage import Store

REPO_ROOT = Path(__file__).resolve().parent.parent

NOTE_TYPES = [
    NoteTypeSpec("concept", "concepts", 180, "An idea or term."),
    NoteTypeSpec("pattern", "patterns", 365, "A recurring regularity."),
    NoteTypeSpec("risk", "risks", 120, "A reason a claim may not hold."),
]


@pytest.fixture
def note_types() -> list[NoteTypeSpec]:
    return list(NOTE_TYPES)


@pytest.fixture
def cfg(tmp_path: Path) -> Config:
    return Config(
        root=tmp_path,
        topic="urban cycling",
        kb=KBConfig(note_types=list(NOTE_TYPES)),
        sources=SourcesConfig(
            order=["files"],
            options={"files": {"paths": [str(REPO_ROOT / "examples" / "corpus")]}},
        ),
    )


@pytest.fixture
def kb(cfg: Config) -> KnowledgeBase:
    knowledge_base = KnowledgeBase(cfg.kb_dir, cfg.kb.note_types)
    knowledge_base.init_dirs()
    return knowledge_base


@pytest.fixture
def store(cfg: Config) -> Store:
    return Store(cfg.store_dir)


@pytest.fixture
def embedder() -> HashingEmbedder:
    return HashingEmbedder()


def make_note(note_id: str, *, type_: str = "concept", title: str | None = None,
              body: str = "## What it is\nA note.", sources: list[str] | None = None,
              confidence: float = 0.8, half_life: int = 180,
              reinforced_days_ago: int = 0, links: list | None = None) -> Note:
    today = datetime.now(timezone.utc).date()
    return Note(meta=NoteMeta(
        id=note_id, title=title or note_id.replace("-", " ").title(), type=type_,
        topic="urban cycling", created=today, updated=today,
        sources=sources if sources is not None else ["doc-1", "doc-2"],
        base_confidence=confidence, half_life_days=half_life,
        last_reinforced=today - timedelta(days=reinforced_days_ago),
        links=links or [],
    ), body=body)


def make_doc(doc_id: str, title: str, *, source: str = "files",
             text: str = "", metrics: dict | None = None,
             age_hours: float = 10.0) -> Document:
    now = datetime.now(timezone.utc)
    return Document(
        id=doc_id, source=source, source_id=doc_id,
        url=f"https://example.test/{doc_id}", title=title, text=text,
        created_at=now - timedelta(hours=age_hours), fetched_at=now,
        topic="urban cycling", metrics=metrics or {},
    )
