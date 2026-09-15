"""Data schemas for every artifact the pipeline produces.

Two fields are deliberately plain strings rather than enums: `Document.source`
and `NoteMeta.type`. They are validated against config, not against a
compiled-in list, so adding a source or a note type never means editing this
file.
"""
from __future__ import annotations

import hashlib
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class Scale(str, Enum):
    """The cost lever. See config.SCALE_PRESETS."""

    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"


# ---------------------------------------------------------------- stage 1 ---
class Document(BaseModel):
    """One ingested item. Every source normalises to this."""

    id: str
    source: str  # a registered source name; not an enum, by design
    source_id: str
    url: str
    title: str
    text: str = ""
    author: str | None = None
    created_at: datetime
    fetched_at: datetime
    topic: str
    # Free-form engagement numbers: points, comments, stars, reactions...
    # Sources that have none leave this empty and metric-based scorers
    # degrade to a neutral value rather than reporting zero interest.
    metrics: dict[str, float] = Field(default_factory=dict)
    embedding: list[float] | None = None  # filled in stage 2, never before

    @staticmethod
    def make_id(source: str, source_id: str) -> str:
        return hashlib.sha256(f"{source}:{source_id}".encode()).hexdigest()[:16]

    def engagement(self) -> float:
        """Total engagement, or 0.0 when the source reports none."""
        return float(sum(self.metrics.values()))

    def has_metrics(self) -> bool:
        return bool(self.metrics)


# ---------------------------------------------------------------- stage 2 ---
class SignalStatus(str, Enum):
    candidate = "candidate"
    promoted = "promoted"
    rejected = "rejected"


class Verdict(str, Enum):
    hit = "hit"
    miss = "miss"
    too_early = "too_early"
    unclear = "unclear"


class Outcome(BaseModel):
    """Filled in by `edu review`, weeks after the signal was promoted."""

    reviewed_at: datetime | None = None
    verdict: Verdict | None = None
    notes: str | None = None


class Signal(BaseModel):
    id: str
    topic: str
    label: str
    member_doc_ids: list[str]
    # Kept alongside the doc ids because calibration attributes hit/miss per
    # source long after the ephemeral corpus has been purged.
    member_sources: list[str] = []
    # Carried on the signal so the brief can render weeks after the ephemeral
    # corpus dump for that run was pruned.
    headline_url: str = ""
    theme: str = ""
    scores: dict[str, float] = Field(default_factory=dict)
    aggregate_score: float
    first_seen: datetime
    sources_count: int
    status: SignalStatus = SignalStatus.candidate
    outcome: Outcome = Field(default_factory=Outcome)


# ---------------------------------------------------------------- stage 3 ---
class Evidence(BaseModel):
    claim: str
    source_doc_id: str


class CriticVerdict(BaseModel):
    is_weak: bool
    argument: str


class Report(BaseModel):
    signal_id: str
    summary: str
    evidence: list[Evidence] = []
    implications: list[str] = []
    risks: list[str] = []
    critic: CriticVerdict
    transcript: str
    confidence: float
    generated_at: datetime
    token_cost: int = 0


# ---------------------------------------------------------------- stage 4 ---
class LinkType(str, Enum):
    """Generic graph semantics. Unlike note types, these are fixed: they are
    what the lint and reconcile passes reason about."""

    relates_to = "relates_to"
    derived_from = "derived_from"
    supports = "supports"
    contradicts = "contradicts"


class NoteLink(BaseModel):
    to: str
    type: LinkType


class Provenance(BaseModel):
    scale: Scale = Scale.M
    query: str | None = None


class NoteMeta(BaseModel):
    id: str
    title: str
    type: str  # one of config.kb.note_types; validated on save
    topic: str
    created: date
    updated: date
    sources: list[str] = []
    tags: list[str] = []
    base_confidence: float = 0.5
    half_life_days: int = 180
    last_reinforced: date
    provenance: Provenance = Field(default_factory=Provenance)
    links: list[NoteLink] = []


# ------------------------------------------------------------- the ledger ---
class GapType(str, Enum):
    contradiction = "contradiction"
    open_question = "open_question"
    thin_evidence = "thin_evidence"
    orphan = "orphan"


class GapStatus(str, Enum):
    open = "open"
    investigating = "investigating"
    resolved = "resolved"


class GapEntry(BaseModel):
    id: str
    type: GapType
    description: str
    related_notes: list[str] = []
    priority: float = 0.5
    status: GapStatus = GapStatus.open
    created: date

    @staticmethod
    def make_id(description: str) -> str:
        return "gap-" + hashlib.sha256(description.encode()).hexdigest()[:10]


class CalibrationRecord(BaseModel):
    """Per-source track record. Drives the learned promotion threshold."""

    source: str
    signals_reviewed: int = 0
    hits: int = 0
    misses: int = 0
    too_early: int = 0
    hit_rate: float = 0.0
    learned_threshold: float = 0.6
    updated: datetime


class RunConfig(BaseModel):
    run_id: str
    topic: str
    scale: Scale
    query: str | None = None
    created_at: datetime
