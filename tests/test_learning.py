from datetime import date, datetime, timedelta, timezone

import pytest

from self_educator.learning.calibration import (
    due_for_review, record_outcome, _learned_threshold,
)
from self_educator.learning.gaps import find_gaps, refresh_gaps, target_from_gaps
from self_educator.learning.reconcile import Resolution, Ruling, resolve_gap
from self_educator.llm import FakeLLM
from self_educator.maintenance import lint
from self_educator.models import (
    GapEntry, GapStatus, GapType, LinkType, NoteLink, Signal, SignalStatus, Verdict,
)

from .conftest import make_note


# ------------------------------------------------------------------ gaps ---
def test_thin_evidence_and_orphans_are_detected(kb):
    kb.save(make_note("thin", sources=["only-one"],
                      links=[NoteLink(to="other", type=LinkType.relates_to)]))
    kb.save(make_note("other"))
    types = {(g.type, tuple(g.related_notes)) for g in find_gaps(kb)}
    assert (GapType.thin_evidence, ("thin",)) in types
    assert (GapType.orphan, ("thin",)) not in types  # it links out


def test_a_note_nobody_links_to_and_that_links_nowhere_is_an_orphan(kb):
    kb.save(make_note("lonely"))
    assert any(g.type is GapType.orphan and g.related_notes == ["lonely"]
               for g in find_gaps(kb))


def test_a_contradiction_yields_one_gap_not_two(kb):
    kb.save(make_note("a", links=[NoteLink(to="b", type=LinkType.contradicts)]))
    kb.save(make_note("b", links=[NoteLink(to="a", type=LinkType.contradicts)]))
    contradictions = [g for g in find_gaps(kb) if g.type is GapType.contradiction]
    assert len(contradictions) == 1


def test_refresh_preserves_status_and_keeps_resolved_history(kb):
    kb.save(make_note("thin", sources=["one"]))
    first = refresh_gaps(kb)
    thin = next(g for g in first if g.type is GapType.thin_evidence)
    thin.status = GapStatus.investigating
    resolved = GapEntry(id="old-resolved", type=GapType.open_question,
                        description="answered long ago",
                        status=GapStatus.resolved, created=date.today())
    kb.write_gaps(first + [resolved])

    second = {g.id: g for g in refresh_gaps(kb)}
    assert second[thin.id].status is GapStatus.investigating
    assert "old-resolved" in second  # history survives


def test_from_gaps_takes_the_top_priority_and_marks_it_investigating(kb):
    kb.save(make_note("a", links=[NoteLink(to="b", type=LinkType.contradicts)]))
    kb.save(make_note("b", sources=["one"]))
    refresh_gaps(kb)
    target = target_from_gaps(kb)
    assert target is not None
    topic, query = target
    assert topic == "urban cycling" and "contradiction" in query.lower()
    assert any(g.status is GapStatus.investigating for g in kb.read_gaps())


def test_from_gaps_returns_nothing_when_the_kb_has_no_questions(kb):
    assert target_from_gaps(kb) is None


# ----------------------------------------------------------- calibration ---
def _signal(days_old: int, verdict=None) -> Signal:
    signal = Signal(id=f"sig-{days_old}", topic="t", label="l",
                    member_doc_ids=["a"], member_sources=["files"], scores={},
                    aggregate_score=0.7,
                    first_seen=datetime.now(timezone.utc) - timedelta(days=days_old),
                    sources_count=1, status=SignalStatus.promoted)
    if verdict:
        signal.outcome.verdict = verdict
    return signal


def test_only_old_unjudged_promoted_signals_are_due():
    candidate = _signal(60)
    candidate.status = SignalStatus.candidate
    pool = [_signal(60), _signal(1), _signal(60, Verdict.hit), candidate]
    assert [s.id for s in due_for_review(pool, 28)] == ["sig-60"]


def test_a_verdict_updates_the_sources_track_record(store):
    signal = _signal(60)
    record_outcome(store, signal, Verdict.hit, "it happened")
    record_outcome(store, _signal(61), Verdict.miss, "it did not")
    record = store.load_calibration()["files"]
    assert record.signals_reviewed == 2 and record.hits == 1 and record.misses == 1
    assert record.hit_rate == pytest.approx(0.5)
    assert store.get_signal(signal.id).outcome.verdict is Verdict.hit


def test_a_worse_hit_rate_raises_the_bar():
    """The loop closing: a source that keeps lying has to clear more."""
    assert _learned_threshold(0.0) > _learned_threshold(1.0)


# ------------------------------------------------------------- reconcile ---
def _contradiction(kb) -> GapEntry:
    kb.save(make_note("a", confidence=0.8,
                      links=[NoteLink(to="b", type=LinkType.contradicts)]))
    kb.save(make_note("b", confidence=0.8,
                      links=[NoteLink(to="a", type=LinkType.contradicts)]))
    return next(g for g in refresh_gaps(kb) if g.type is GapType.contradiction)


def test_favouring_one_side_halves_the_other_instead_of_deleting_it(kb):
    gap = _contradiction(kb)
    llm = FakeLLM([Resolution(ruling=Ruling.favor_a, reasoning="a is better sourced")])
    resolve_gap(kb, gap, llm)
    assert gap.status is GapStatus.resolved
    assert kb.get("b").meta.base_confidence == pytest.approx(0.4)
    assert kb.get("b") is not None and kb.get("a").meta.base_confidence == 0.8
    assert "Downgraded" in kb.get("b").body


def test_open_tension_keeps_both_notes_and_records_why(kb):
    gap = _contradiction(kb)
    llm = FakeLLM([Resolution(ruling=Ruling.open_tension,
                              reasoning="both hold in different contexts")])
    resolve_gap(kb, gap, llm)
    assert gap.status is GapStatus.investigating
    for note_id in ("a", "b"):
        note = kb.get(note_id)
        assert note.meta.base_confidence == 0.8
        assert "Open tension" in note.body


def test_a_contradiction_whose_note_vanished_resolves_without_an_llm_call(kb):
    gap = _contradiction(kb)
    kb.delete("b")
    llm = FakeLLM([])  # any call would raise
    assert resolve_gap(kb, gap, llm) is None
    assert gap.status is GapStatus.resolved


# ------------------------------------------------------------------ lint ---
def test_lint_finds_broken_links_and_unregistered_contradictions(kb):
    kb.save(make_note("a", links=[
        NoteLink(to="does-not-exist", type=LinkType.relates_to),
        NoteLink(to="b", type=LinkType.contradicts),
    ]))
    kb.save(make_note("b"))
    report = lint(kb)
    assert report.broken_links == ["a → does-not-exist (relates_to)"]
    assert report.unregistered_contradictions == ["a ↔ b"]
    assert report.problems > 0


def test_lint_is_quiet_on_a_healthy_graph(kb):
    kb.save(make_note("a", links=[NoteLink(to="b", type=LinkType.supports)]))
    kb.save(make_note("b", links=[NoteLink(to="a", type=LinkType.relates_to)]))
    assert lint(kb).problems == 0


def test_lint_flags_duplicate_titles_as_merge_candidates(kb):
    kb.save(make_note("a", title="Protected Lanes",
                      links=[NoteLink(to="b", type=LinkType.relates_to)]))
    kb.save(make_note("b", title="protected lanes  ",
                      links=[NoteLink(to="a", type=LinkType.relates_to)]))
    assert lint(kb).duplicate_titles
