from datetime import datetime, timezone

import pytest

from self_educator.kb import Note
from self_educator.llm import FakeLLM
from self_educator.models import (
    CriticVerdict, GapType, LinkType, NoteLink, Provenance, Report, Signal,
)
from self_educator.synthesis.compiler import CompiledNote, CompileResult, compile_report

from .conftest import make_note


def _signal() -> Signal:
    return Signal(id="sig-1", topic="urban cycling", label="Protected lanes",
                  member_doc_ids=["a"], member_sources=["files"], scores={},
                  aggregate_score=0.7, first_seen=datetime.now(timezone.utc),
                  sources_count=1)


def _report() -> Report:
    return Report(signal_id="sig-1", summary="Lanes grow ridership.",
                  critic=CriticVerdict(is_weak=False, argument="holds"),
                  transcript="", confidence=0.8,
                  generated_at=datetime.now(timezone.utc))


def _compiled(note_id: str, *, type_: str = "concept", links=None,
              sources=None, body="## What it is\nx") -> CompiledNote:
    return CompiledNote(id=note_id, title=note_id.title(), type=type_,
                        base_confidence=0.7, sources=sources or ["a"],
                        links=links or [], body=body)


def test_compile_writes_notes_with_the_configured_half_life(kb, cfg):
    llm = FakeLLM([CompileResult(notes=[_compiled("bike-lanes", type_="pattern")])])
    notes = compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())
    assert [n.meta.id for n in notes] == ["bike-lanes"]
    # 365 comes from the `pattern` entry in config, not from a table in code.
    assert kb.get("bike-lanes").meta.half_life_days == 365


def test_recompiling_an_existing_id_merges_instead_of_duplicating(kb, cfg):
    kb.save(make_note("bike-lanes", sources=["old"], confidence=0.4,
                      reinforced_days_ago=90))
    llm = FakeLLM([CompileResult(notes=[_compiled("bike-lanes", sources=["new"])])])
    compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())
    merged = kb.get("bike-lanes")
    assert merged.meta.sources == ["new", "old"]
    # Fresh evidence resets the decay clock, but does not rewrite the original
    # confidence — that judgement belongs to the evidence, not to a re-run.
    assert merged.meta.last_reinforced == datetime.now(timezone.utc).date()
    assert merged.meta.base_confidence == pytest.approx(0.4)


def test_a_contradiction_registers_a_gap_and_never_overwrites(kb, cfg):
    kb.save(make_note("helmet-laws"))
    llm = FakeLLM([CompileResult(notes=[_compiled(
        "bike-lanes",
        links=[NoteLink(to="helmet-laws", type=LinkType.contradicts)])])])
    compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())
    assert kb.get("helmet-laws") is not None  # the older note still stands
    gaps = kb.read_gaps()
    assert len(gaps) == 1
    assert gaps[0].type is GapType.contradiction
    assert gaps[0].related_notes == ["bike-lanes", "helmet-laws"]


def test_the_same_contradiction_is_not_registered_twice(kb, cfg):
    kb.save(make_note("helmet-laws"))
    link = [NoteLink(to="helmet-laws", type=LinkType.contradicts)]
    for _ in range(2):
        llm = FakeLLM([CompileResult(notes=[_compiled("bike-lanes", links=link)])])
        compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())
    assert len(kb.read_gaps()) == 1


def test_a_hallucinated_note_type_is_rejected(kb, cfg):
    llm = FakeLLM([CompileResult(notes=[_compiled("x", type_="invented")])])
    with pytest.raises(ValueError, match="unknown note type"):
        compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())


def test_the_prompt_carries_schema_vocabulary_and_the_existing_index(kb, cfg):
    kb.save(make_note("already-here"))
    (kb.root / "SCHEMA.md").write_text("CUSTOM COMPILER CONTRACT")
    llm = FakeLLM([CompileResult(notes=[_compiled("new-note")])])
    compile_report(_report(), _signal(), kb, cfg.kb, llm, Provenance())
    system, prompt = llm.calls[0]
    assert system == "CUSTOM COMPILER CONTRACT"   # the user's file, verbatim
    assert "already-here" in prompt               # integrate, don't accumulate
    assert "- pattern:" in prompt                 # the configured vocabulary
