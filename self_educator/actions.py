"""Operations that are neither a full run nor pure maintenance."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable

from .config import Config
from .enrich import enrich
from .kb import KnowledgeBase
from .learning.gaps import refresh_gaps
from .llm import LLM, BudgetExceeded
from .models import Document, Provenance, Report, Signal, SignalStatus
from .storage import Store
from .synthesis.compiler import compile_report


@dataclass
class CompileSummary:
    reports_total: int = 0
    reports_compiled: int = 0
    notes_written: int = 0
    cost_usd: float = 0.0


def compile_all(cfg: Config, store: Store, kb: KnowledgeBase, llm: LLM,
                log: Callable[[str], None] = lambda m: None) -> CompileSummary:
    """Re-run stage 4 over reports already on disk. No ingestion, no enrichment.

    Use after editing kb/SCHEMA.md, after deleting notes you want regenerated,
    or when a run ran out of budget partway through compilation.
    """
    reports = store.load_reports()
    summary = CompileSummary(reports_total=len(reports))
    for report in reports:
        signal = store.get_signal(report.signal_id)
        if signal is None:
            log(f"! no signal for report {report.signal_id}; skipped")
            continue
        try:
            # Scale is not recorded on the report, so recompiled notes carry a
            # default provenance rather than a guess at the original run's.
            notes = compile_report(report, signal, kb, cfg.kb, llm, Provenance())
        except BudgetExceeded as exc:
            log(f"! budget spent: {exc}")
            break
        summary.reports_compiled += 1
        summary.notes_written += len(notes)
        log(f"compiled {len(notes)} note(s) from «{signal.label[:60]}»")
    summary.cost_usd = round(llm.cost_usd, 4)
    return summary


def learn(cfg: Config, store: Store, kb: KnowledgeBase, llm: LLM, text: str, *,
         label: str | None = None, include_critic: bool = True) -> Report:
    """A concept the user hands over directly. No ingest, no signal: it is
    already trusted, there is nothing to discover or score."""
    now = datetime.now(timezone.utc)
    doc = Document(
        id=Document.make_id("manual", label or text[:60]),
        source="manual", source_id=label or text[:60], url="manual://learn",
        title=label or text.splitlines()[0][:80], text=text,
        created_at=now, fetched_at=now, topic=cfg.topic,
    )
    signal = Signal(
        id=doc.id, topic=cfg.topic, label=doc.title,
        member_doc_ids=[doc.id], member_sources=["manual"],
        aggregate_score=1.0, first_seen=now, sources_count=1,
        status=SignalStatus.promoted,
    )
    store.save_signal(signal)
    report = enrich(signal, [doc], llm, include_critic=include_critic)
    store.save_report(report)
    compile_report(report, signal, kb, cfg.kb, llm, Provenance())
    refresh_gaps(kb)
    return report


ASK_SYSTEM = (
    "You answer strictly from the knowledge base you are given. Cite the note "
    "ids you used. If the notes do not answer the question, say so plainly and "
    "name what is missing — that is a knowledge gap worth recording, not an "
    "invitation to fill it from memory."
)


def ask(kb: KnowledgeBase, llm: LLM, question: str, limit: int = 40) -> str:
    """Query the KB. Answers only from the notes, or admits it cannot."""
    notes = kb.load_all()
    if not notes:
        return "The knowledge base is empty. Run `edu run` first."
    # Highest live confidence first: a decayed note should not outrank a fresh
    # one just because it sorts earlier on disk.
    notes.sort(key=lambda n: -kb.current_confidence(n))
    context = "\n\n".join(
        f"### {n.meta.id} [{n.meta.type}] "
        f"(confidence {kb.current_confidence(n):.2f})\n{n.meta.title}\n{n.body[:800]}"
        for n in notes[:limit])
    return llm.complete(ASK_SYSTEM,
                        f"## Knowledge base\n{context}\n\n## Question\n{question}")
