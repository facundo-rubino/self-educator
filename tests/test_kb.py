from datetime import date, timedelta

import pytest

from self_educator.kb import Note, parse_note, render_note
from self_educator.learning.decay import current_confidence, flag_decayed
from self_educator.models import GapEntry, GapType, LinkType, NoteLink

from .conftest import make_note


def test_note_round_trips_through_markdown(kb):
    note = make_note("bike-lanes", body="## What it is\nSeparated lanes.")
    kb.save(note)
    reloaded = kb.get("bike-lanes")
    assert reloaded is not None
    assert reloaded.meta.id == "bike-lanes"
    assert "Separated lanes." in reloaded.body


def test_notes_land_in_the_directory_their_type_configures(kb, cfg):
    kb.save(make_note("a-pattern", type_="pattern"))
    assert (cfg.kb_dir / "patterns" / "a-pattern.md").exists()


def test_saving_an_unconfigured_type_fails_loudly(kb):
    with pytest.raises(ValueError, match="unknown note type"):
        kb.save(make_note("x", type_="not-a-configured-type"))


def test_links_are_mirrored_into_the_body_idempotently(kb):
    note = make_note("a", links=[NoteLink(to="b", type=LinkType.relates_to)])
    kb.save(note)
    kb.save(kb.get("a"))  # a second save must not duplicate the section
    body = kb.get("a").body
    assert body.count("## Links") == 1
    assert "[[b]]" in body


def test_content_appended_after_the_links_section_survives_a_resave(kb):
    """Reconcile stamps notes after their links; regenerating must not eat it."""
    note = make_note("a", links=[NoteLink(to="b", type=LinkType.relates_to)])
    kb.save(note)
    stamped = kb.get("a")
    stamped.body += "\n\n## Open tension\nBoth sides stand."
    kb.save(stamped)
    assert "Open tension" in kb.get("a").body


def test_deleting_a_note_leaves_no_dangling_inbound_links(kb):
    kb.save(make_note("target"))
    kb.save(make_note("pointer", links=[NoteLink(to="target",
                                                 type=LinkType.relates_to)]))
    assert kb.delete("target") is True
    assert kb.get("target") is None
    assert kb.get("pointer").meta.links == []
    assert "[[target]]" not in kb.get("pointer").body


def test_deleting_a_note_keeps_the_gap_that_referenced_it(kb):
    """The hole is still a hole once the note is gone."""
    kb.save(make_note("target"))
    kb.write_gaps([GapEntry(id="g1", type=GapType.thin_evidence,
                            description="thin", related_notes=["target", "other"],
                            created=date.today())])
    kb.delete("target")
    gaps = kb.read_gaps()
    assert len(gaps) == 1 and gaps[0].related_notes == ["other"]


def test_gaps_round_trip_and_sort_by_priority(kb):
    kb.write_gaps([
        GapEntry(id="low", type=GapType.orphan, description="l",
                 priority=0.2, created=date.today()),
        GapEntry(id="high", type=GapType.contradiction, description="h",
                 priority=0.9, created=date.today()),
    ])
    assert [g.id for g in kb.read_gaps()] == ["high", "low"]


def test_reading_gaps_before_any_exist_is_empty_not_an_error(kb):
    assert kb.read_gaps() == []


def test_confidence_halves_over_one_half_life():
    today = date(2026, 1, 1)
    assert current_confidence(0.8, 100, today - timedelta(days=100),
                              today) == pytest.approx(0.4)
    assert current_confidence(0.8, 100, today, today) == pytest.approx(0.8)


def test_flag_decayed_finds_only_the_stale_ones():
    fresh = make_note("fresh", confidence=0.9, half_life=365)
    stale = make_note("stale", confidence=0.5, half_life=10,
                      reinforced_days_ago=200)
    assert flag_decayed([fresh, stale]) == ["stale"]


def test_parse_note_rejects_a_file_without_front_matter():
    with pytest.raises(ValueError, match="front-matter"):
        parse_note("# Just a heading\n\nNo metadata here.")


def test_render_then_parse_is_lossless():
    note = make_note("x", links=[NoteLink(to="y", type=LinkType.contradicts)])
    assert parse_note(render_note(note)).meta == note.meta
