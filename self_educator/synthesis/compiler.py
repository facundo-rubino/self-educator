"""Stage 4: Report -> Notes in kb/, guided by kb/SCHEMA.md.

The metaphor worth keeping: the reports are source code, the LLM is the
compiler, and the note graph is the executable. Compile well and the KB is
fast and correct to read; compile badly and you get interconnected noise.

`kb/SCHEMA.md` is the compiler's system prompt and belongs to the user. This
module only supplies the invariants the pipeline itself depends on.
"""
from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from ..config import KBConfig
from ..kb import KnowledgeBase, Note
from ..llm import LLM
from ..models import (
    GapEntry, GapType, LinkType, NoteLink, NoteMeta, Provenance, Report, Signal,
)


class CompiledNote(BaseModel):
    id: str
    title: str
    type: str
    tags: list[str] = []
    base_confidence: float
    sources: list[str] = []
    links: list[NoteLink] = []
    body: str


class CompileResult(BaseModel):
    notes: list[CompiledNote]


#: Used verbatim in the prompt, and as the whole system prompt when the user
#: has no SCHEMA.md yet. These are the rules the rest of the pipeline relies on.
FALLBACK_RULES = (
    "Break the report into ATOMIC notes — one idea per note. If a note's title "
    "needs an 'and', it is two notes. Before creating a note, check the index: "
    "if the concept already exists, reuse its id EXACTLY so the new evidence is "
    "integrated rather than duplicated. Ids are kebab-case. Every claim in the "
    "body cites the doc_id it came from; if you cannot cite it, do not write it. "
    "Link with typed edges. If an idea contradicts an existing note, create a "
    "`contradicts` link — never silently overwrite the older note. Body "
    "structure: ## What it is / ## Evidence / ## Why it matters / ## Links."
)


def _index(kb: KnowledgeBase) -> str:
    notes = kb.load_all()
    if not notes:
        return "(the knowledge base is empty)"
    return "\n".join(f"- {n.meta.id} [{n.meta.type}] {n.meta.title}" for n in notes)


def _vocabulary(kb_config: KBConfig) -> str:
    return "\n".join(f"- {t.name}: {t.description}" for t in kb_config.note_types)


def _register_contradiction_gaps(kb: KnowledgeBase, note_id: str,
                                 links: list[NoteLink], today: date) -> None:
    """A contradiction is not resolved at write time — it is recorded so that
    `edu reconcile` can weigh both sides with the evidence in front of it."""
    contradicted = [l.to for l in links if l.type is LinkType.contradicts]
    if not contradicted:
        return
    gaps = kb.read_gaps()
    known = {g.id for g in gaps}
    for other in contradicted:
        description = f"Unresolved contradiction between '{note_id}' and '{other}'"
        gap_id = GapEntry.make_id(description)
        if gap_id in known:
            continue
        gaps.append(GapEntry(id=gap_id, type=GapType.contradiction,
                             description=description,
                             related_notes=sorted([note_id, other]),
                             priority=0.9, created=today))
    kb.write_gaps(gaps)


def compile_report(report: Report, signal: Signal, kb: KnowledgeBase,
                   kb_config: KBConfig, llm: LLM, provenance: Provenance,
                   today: date | None = None) -> list[Note]:
    """Compile one report into the graph, merging into existing notes."""
    today = today or date.today()
    schema_path = kb.root / "SCHEMA.md"
    system = schema_path.read_text()[:8000] if schema_path.exists() else FALLBACK_RULES

    prompt = (
        f"{FALLBACK_RULES}\n\n"
        f"## Note types you may use (use no others)\n{_vocabulary(kb_config)}\n\n"
        f"## Existing notes\n{_index(kb)}\n\n"
        f"## Topic\n{signal.topic}\n\n"
        f"## Report to compile (signal: {signal.label})\n"
        f"{report.model_dump_json(indent=2)}"
    )
    result = llm.parse(system, prompt, CompileResult, max_tokens=8192)

    written: list[Note] = []
    for compiled in result.notes:
        spec = kb.spec(compiled.type)  # raises on a hallucinated type
        existing = kb.get(compiled.id)
        if existing:
            meta = existing.meta
            meta.title = compiled.title
            meta.updated = today
            meta.last_reinforced = today  # fresh evidence resets the decay clock
            meta.sources = sorted(set(meta.sources) | set(compiled.sources))
            meta.tags = sorted(set(meta.tags) | set(compiled.tags))
            seen = {(l.to, l.type) for l in meta.links}
            meta.links += [l for l in compiled.links if (l.to, l.type) not in seen]
        else:
            meta = NoteMeta(
                id=compiled.id, title=compiled.title, type=compiled.type,
                topic=signal.topic, created=today, updated=today,
                sources=compiled.sources, tags=compiled.tags,
                base_confidence=compiled.base_confidence,
                half_life_days=spec.half_life_days,
                last_reinforced=today, provenance=provenance,
                links=compiled.links,
            )
        note = Note(meta=meta, body=compiled.body)
        kb.save(note)
        written.append(note)
        _register_contradiction_gaps(kb, compiled.id, compiled.links, today)
    return written
