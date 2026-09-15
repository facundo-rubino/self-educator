"""The end-to-end proof: all four stages, offline, with no API key.

If this test passes, the skeleton actually runs. It is the first thing to
break when someone adapts the template badly, and the first thing to fix.
"""
from __future__ import annotations

import json

import pytest

from self_educator.actions import ask, compile_all
from self_educator.enrich.analyst import Draft
from self_educator.enrich.critic import Review
from self_educator.llm import BudgetExceeded, FakeLLM
from self_educator.models import Evidence, Scale, SignalStatus
from self_educator.pipeline import run_pipeline
from self_educator.sources import build_sources
from self_educator.synthesis.compiler import CompiledNote, CompileResult


def _draft(n: int) -> Draft:
    return Draft(summary=f"Finding {n}.",
                 evidence=[Evidence(claim=f"claim {n}", source_doc_id="doc")],
                 implications=["build more"], risks=["thin sample"],
                 confidence=0.75)


def _review() -> Review:
    return Review(is_weak=False, argument="survives", adjusted_confidence=0.7)


def _compiled(n: int) -> CompileResult:
    return CompileResult(notes=[CompiledNote(
        id=f"finding-{n}", title=f"Finding {n}", type="concept",
        base_confidence=0.7, sources=["doc"], links=[],
        body=f"## What it is\nFinding {n}.")])


class PipelineLLM(FakeLLM):
    """Answers by requested schema instead of by call order.

    The number of analyst/critic/compile calls depends on the scale preset
    (XS runs no critic) and on how many clusters clear the promotion bar — a
    positional script would encode assumptions the pipeline is free to change.
    """

    def __init__(self) -> None:
        super().__init__([])
        self.compiled = 0

    def parse(self, system, prompt, schema, max_tokens=4096):
        self.calls.append((system, prompt))
        self.tokens_used += 100
        if schema is Draft:
            return _draft(len(self.calls))
        if schema is Review:
            return _review()
        if schema is CompileResult:
            self.compiled += 1
            return _compiled(self.compiled)
        raise AssertionError(f"unexpected schema requested: {schema.__name__}")


def test_full_pipeline_runs_offline(cfg, store, kb, embedder):
    llm = PipelineLLM()
    result = run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.XS,
                          llm=llm, embedder=embedder, sources=build_sources(cfg))

    assert result.doc_count > 0, "the files source read the example corpus"
    assert result.signals, "stage 2 produced signals"
    assert any(s.status is SignalStatus.promoted for s in result.signals)
    assert result.reports, "stage 3 produced a report"
    assert result.notes_written, "stage 4 wrote notes to the KB"
    assert kb.load_all(), "the notes are on disk and parse back"
    assert not result.warnings


def test_every_stage_persists_so_it_can_be_re_run(cfg, store, kb, embedder):
    result = run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.XS,
                          llm=PipelineLLM(), embedder=embedder,
                          sources=build_sources(cfg))
    assert store.load_documents(result.run_id)
    assert store.load_signals()
    assert store.load_reports()
    assert store.load_baseline(), "the novelty baseline grew"

    summary = json.loads((cfg.runs_dir / result.run_id / "summary.json").read_text())
    assert summary["documents"] == result.doc_count
    assert summary["topic"] == "urban cycling"


def test_compile_reruns_only_stage_four(cfg, store, kb, embedder):
    run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.XS,
                 llm=PipelineLLM(), embedder=embedder,
                 sources=build_sources(cfg))
    for note in kb.load_all():
        kb.delete(note.meta.id)
    assert kb.load_all() == []

    summary = compile_all(cfg, store, kb, FakeLLM([_compiled(9)] * 5))
    assert summary.reports_total > 0
    assert summary.notes_written > 0
    assert kb.load_all(), "notes were regenerated without re-ingestion"


def test_a_failing_source_is_a_warning_not_a_dead_run(cfg, store, kb, embedder):
    """Collectors are fragile by design; one broken source must not lose the run."""
    class Broken:
        def fetch(self, query, *, limit, topic):
            raise RuntimeError("upstream 503")

    sources = {"broken": Broken(), **build_sources(cfg)}
    result = run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.S,
                          llm=PipelineLLM(), embedder=embedder,
                          sources=sources)
    assert any("upstream 503" in w for w in result.warnings)
    assert result.doc_count > 0, "the surviving source still delivered"


def test_running_out_of_budget_reports_partial_work(cfg, store, kb, embedder):
    class Broke(FakeLLM):
        def parse(self, *args, **kwargs):
            raise BudgetExceeded("spent")

    result = run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.XS,
                          llm=Broke([]), embedder=embedder,
                          sources=build_sources(cfg))
    assert result.doc_count > 0 and result.signals  # the free stages completed
    assert result.reports == [] and result.notes_written == []
    assert any("budget spent" in w for w in result.warnings)


def test_the_run_refreshes_the_gap_ledger(cfg, store, kb, embedder):
    result = run_pipeline(cfg, store, kb, topic="urban cycling", scale=Scale.XS,
                          llm=PipelineLLM(), embedder=embedder,
                          sources=build_sources(cfg))
    assert result.gaps_open > 0, "new single-source notes are thin evidence"
    assert (cfg.kb_dir / "GAPS.md").exists()


def test_ask_answers_only_from_the_notes(cfg, kb, embedder):
    from .conftest import make_note

    kb.save(make_note("bike-lanes", body="## What it is\nSeparated lanes work."))
    llm = FakeLLM(["Separated lanes work [bike-lanes]."])
    answer = ask(kb, llm, "do bike lanes work?")
    assert "bike-lanes" in answer
    _, prompt = llm.calls[0]
    assert "Separated lanes work." in prompt


def test_ask_says_so_when_the_kb_is_empty(cfg, kb):
    assert "empty" in ask(kb, FakeLLM([]), "anything?").lower()
