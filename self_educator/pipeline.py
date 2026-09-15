"""The four stages, wired together.

Each stage persists before the next begins, so a run that dies halfway leaves
usable artifacts behind and the surviving stages can be re-run on their own.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable

from .config import SCALE_PRESETS, Config
from .kb import KnowledgeBase
from .learning.decay import flag_decayed
from .learning.gaps import refresh_gaps
from .llm import LLM, BudgetExceeded, make_llm
from .models import (
    Document, GapStatus, Provenance, Report, RunConfig, Scale, Signal, SignalStatus,
)
from .signal.aggregate import effective_threshold
from .signal.embedder import Embedder, get_embedder
from .signal.engine import detect_signals
from .sources import Source, build_sources, excluded_sources
from .storage import Store
from .synthesis.compiler import compile_report
from .enrich import enrich


@dataclass
class RunResult:
    run_id: str
    topic: str
    scale: Scale
    doc_count: int = 0
    signals: list[Signal] = field(default_factory=list)
    reports: list[Report] = field(default_factory=list)
    notes_written: list[str] = field(default_factory=list)
    gaps_open: int = 0
    tokens_used: int = 0
    cost_usd: float = 0.0
    warnings: list[str] = field(default_factory=list)


def run_pipeline(cfg: Config, store: Store, kb: KnowledgeBase, *,
                 topic: str, scale: Scale, query: str | None = None,
                 llm: LLM | None = None, embedder: Embedder | None = None,
                 sources: dict[str, Source] | None = None,
                 log: Callable[[str], None] = lambda m: None) -> RunResult:
    """One full cycle: ingest → signal → enrich → compile, then refresh gaps."""
    preset = SCALE_PRESETS[scale]
    llm = llm or make_llm(cfg.provider, cfg.model or None,
                          token_budget=preset.token_budget)
    embedder = embedder or get_embedder()
    search = query or topic

    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    run_dir = cfg.runs_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "config.json").write_text(RunConfig(
        run_id=run_id, topic=topic, scale=scale, query=query,
        created_at=datetime.now(timezone.utc)).model_dump_json(indent=2))
    result = RunResult(run_id=run_id, topic=topic, scale=scale)

    if sources is None:
        sources = build_sources(cfg)
        for excluded in excluded_sources(cfg):
            result.warnings.append(f"source excluded: {excluded}")
            log(f"! source excluded: {excluded}")

    # Decay is not a command — it is a fact about time, applied on every run.
    if decayed := flag_decayed(kb.load_all()):
        log(f"decay: {len(decayed)} note(s) below threshold → {', '.join(decayed)}")

    # ---- [1] INGEST — deterministic, no LLM --------------------------------
    docs: list[Document] = []
    for name in list(sources)[:preset.sources]:
        try:
            docs += sources[name].fetch(search, limit=preset.docs_per_source,
                                        topic=topic)
        except Exception as exc:  # noqa: BLE001 — collectors are fragile by design
            result.warnings.append(f"source {name} failed: {exc}")
            log(f"! source {name} failed: {exc}")
    seen: set[str] = set()
    docs = [d for d in docs if not (d.id in seen or seen.add(d.id))]
    store.save_documents(run_id, docs)
    result.doc_count = len(docs)
    log(f"[1] ingest: {len(docs)} documents")

    # ---- [2] SIGNAL — deterministic, no LLM; this is where volume dies -----
    threshold = effective_threshold(store.load_calibration(),
                                    cfg.signal.promotion_threshold)
    signals, centroids = detect_signals(
        docs, store.load_baseline(), topic, embedder=embedder,
        themes=cfg.themes,
        weights=cfg.signal.weights,
        cluster_threshold=cfg.signal.cluster_threshold,
        top_n=preset.top_signals, promotion_threshold=threshold)
    for signal in signals:
        store.save_signal(signal)
    # Appended after scoring so a run never competes with itself for novelty.
    store.append_baseline(centroids)
    result.signals = signals
    promoted = [s for s in signals if s.status is SignalStatus.promoted]
    log(f"[2] signal: {len(signals)} clusters, {len(promoted)} promoted "
        f"(threshold {threshold:.2f})")

    # ---- [3] ENRICH — analyst + critic, LLM --------------------------------
    docs_by_id = {d.id: d for d in docs}
    for signal in promoted:
        members = [docs_by_id[i] for i in signal.member_doc_ids if i in docs_by_id]
        try:
            report = enrich(signal, members, llm, query=query,
                            include_critic=preset.critic)
        except BudgetExceeded as exc:
            result.warnings.append(f"budget spent during enrich: {exc}")
            break
        store.save_report(report)
        result.reports.append(report)
        log(f"[3] enriched «{signal.label[:60]}» → confidence {report.confidence:.2f}")

    # ---- [4] COMPILE — reports become notes, LLM ---------------------------
    provenance = Provenance(scale=scale, query=query)
    signals_by_id = {s.id: s for s in signals}
    for report in result.reports:
        try:
            notes = compile_report(report, signals_by_id[report.signal_id],
                                   kb, cfg.kb, llm, provenance)
        except BudgetExceeded as exc:
            result.warnings.append(f"budget spent during compile: {exc}")
            break
        result.notes_written += [n.meta.id for n in notes]
        log(f"[4] compiled {len(notes)} note(s)")

    # ---- Ledger — what the KB now knows it is missing ----------------------
    gaps = refresh_gaps(kb)
    result.gaps_open = sum(1 for g in gaps if g.status is GapStatus.open)
    log(f"[·] gaps: {result.gaps_open} open")

    result.tokens_used = llm.tokens_used
    result.cost_usd = round(llm.cost_usd, 4)
    (run_dir / "summary.json").write_text(json.dumps({
        "run_id": run_id, "topic": topic, "scale": scale.value, "query": query,
        "documents": result.doc_count, "signals": len(signals),
        "promoted": len(promoted), "reports": len(result.reports),
        "notes": result.notes_written, "gaps_open": result.gaps_open,
        "tokens_used": result.tokens_used, "cost_usd": result.cost_usd,
        "warnings": result.warnings,
    }, indent=2, ensure_ascii=False))
    return result
