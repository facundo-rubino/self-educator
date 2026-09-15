"""Stage 5. Offline: the brief never calls an LLM, so neither does its test."""
from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pytest

from self_educator.brief import build_brief, render_issue, render_markdown
from self_educator.config import Config, KBConfig, ThemeSpec, best_theme
from self_educator.models import CriticVerdict, Report, Signal, SignalStatus
from self_educator.signal.scorers import ScoringContext, relevance

from .conftest import NOTE_TYPES, make_doc

THEMES = [
    ThemeSpec("ia", "IA y agentes", quota=3,
              keywords=["agent", "llm", "claude", "mcp", "prompt", "eval"]),
    ThemeSpec("lider", "Liderazgo", quota=2,
              keywords=["estimat", "forecast", "throughput", "tech lead"]),
    ThemeSpec("dev", "Oficio dev", quota=2,
              keywords=["javascript", "css", "browser", "typescript"]),
]


def _cfg(tmp_path) -> Config:
    return Config(root=tmp_path, topic="t", themes=list(THEMES),
                  kb=KBConfig(note_types=list(NOTE_TYPES)))


def _signal(sid: str, theme: str, score: float, label: str = "T") -> Signal:
    now = datetime.now(timezone.utc)
    return Signal(id=sid, topic="t", label=f"{label} {sid}", member_doc_ids=[sid],
                  member_sources=["rss"], headline_url=f"https://e.test/{sid}",
                  theme=theme, aggregate_score=score, first_seen=now,
                  sources_count=1, status=SignalStatus.promoted)


def _report(sid: str, summary: str = "Lo que importa. El resto del parrafo.") -> Report:
    return Report(signal_id=sid, summary=summary,
                  critic=CriticVerdict(is_weak=False, argument="ok"),
                  transcript="", confidence=0.8,
                  generated_at=datetime.now(timezone.utc))


def test_quota_caps_each_theme_and_total(tmp_path, store):
    # Ten candidates for a theme that allows three, plus two for each other.
    for i in range(10):
        store.save_signal(_signal(f"ia{i}", "ia", 0.9 - i / 100))
        store.save_report(_report(f"ia{i}"))
    for i in range(4):
        store.save_signal(_signal(f"ld{i}", "lider", 0.5 - i / 100))
        store.save_report(_report(f"ld{i}"))
        store.save_signal(_signal(f"dv{i}", "dev", 0.4 - i / 100))
        store.save_report(_report(f"dv{i}"))

    brief = build_brief(_cfg(tmp_path), store)

    per_theme = {}
    for item in brief.items:
        per_theme[item.theme_label] = per_theme.get(item.theme_label, 0) + 1
    assert per_theme == {"IA y agentes": 3, "Liderazgo": 2, "Oficio dev": 2}
    assert len(brief.items) == 7


def test_highest_scoring_signal_of_a_theme_wins_its_slot(tmp_path, store):
    store.save_signal(_signal("low", "ia", 0.10, label="Low"))
    store.save_report(_report("low"))
    store.save_signal(_signal("high", "ia", 0.99, label="High"))
    store.save_report(_report("high"))

    items = build_brief(_cfg(tmp_path), store).items
    assert [i.title.split()[0] for i in items] == ["High", "Low"]


def test_signal_without_a_theme_is_dropped_as_noise(tmp_path, store):
    store.save_signal(_signal("none", "", 0.99))
    store.save_report(_report("none"))

    brief = build_brief(_cfg(tmp_path), store)
    assert brief.items == []
    assert brief.skipped_no_theme == 1


def test_signal_without_a_report_never_reaches_the_brief(tmp_path, store):
    # Enrichment may have been skipped or have run out of budget.
    store.save_signal(_signal("unenriched", "ia", 0.99))
    assert build_brief(_cfg(tmp_path), store).items == []


def test_empty_brief_says_so_instead_of_rendering_a_blank_page(tmp_path, store):
    brief = build_brief(_cfg(tmp_path), store)
    assert brief.is_empty
    page = render_markdown(brief)
    assert "no pasó nada que pase el filtro" in page
    assert "no pasó nada que pase el filtro" in render_issue(brief)


def test_rendered_page_leads_with_headlines_and_links(tmp_path, store):
    store.save_signal(_signal("a", "ia", 0.9, label="Agentes"))
    store.save_report(_report(
        "a", summary="Menos herramientas rinden mejor. Y el detalle largo."))

    page = render_markdown(build_brief(_cfg(tmp_path), store))
    assert page.index("## Los titulares") < page.index("## IA y agentes")
    assert "[Agentes a](https://e.test/a)" in page
    # The one-line why is the first sentence, not the whole summary.
    assert "Menos herramientas rinden mejor" in page
    assert "Y el detalle largo" not in page


def test_why_does_not_split_on_an_abbreviation(tmp_path, store):
    store.save_signal(_signal("a", "ia", 0.9))
    store.save_report(_report(
        "a", summary="Los agentes p. ej. los de codigo fallan distinto."))

    page = render_markdown(build_brief(_cfg(tmp_path), store))
    assert "fallan distinto" in page


def test_issue_body_is_the_push_half_with_a_link_back(tmp_path, store):
    for i in range(3):
        store.save_signal(_signal(f"a{i}", "ia", 0.9 - i / 100))
        store.save_report(_report(f"a{i}"))
    for i in range(2):
        store.save_signal(_signal(f"l{i}", "lider", 0.5 - i / 100))
        store.save_report(_report(f"l{i}"))

    brief = build_brief(_cfg(tmp_path), store)
    assert len(brief.items) == 5
    body = render_issue(brief, page_url="https://pages.test/", top=3)
    assert body.count("**[") == 3
    assert "y 2 más" in body
    assert "https://pages.test/" in body


# ------------------------------------------------------------- relevance ----
def _ctx(themes):
    return ScoringContext(corpus=[], centroid=np.zeros(4), baseline=[],
                          now=datetime.now(timezone.utc), themes=themes)


def test_relevance_is_neutral_when_no_themes_are_configured():
    docs = [make_doc("d1", "Anything at all")]
    assert relevance(docs, _ctx([])) == pytest.approx(0.5)


def test_relevance_rewards_a_headline_about_a_configured_theme():
    docs = [make_doc("d1", "Building an agent with MCP and eval-driven prompts")]
    assert relevance(docs, _ctx(THEMES)) > 0.9


def test_relevance_punishes_clickbait_even_when_it_is_on_topic():
    on_topic = "Shipping an agent with MCP and eval harnesses"
    bait = "You won't believe this one trick for agents with MCP and evals"
    clean = relevance([make_doc("d1", on_topic)], _ctx(THEMES))
    baited = relevance([make_doc("d2", bait)], _ctx(THEMES))
    assert baited < clean


def test_relevance_punishes_the_self_help_register():
    docs = [make_doc("d1", "The morning routine that will 10x your agent prompts")]
    assert relevance(docs, _ctx(THEMES)) < 0.5


def test_relevance_is_zero_for_something_off_topic():
    docs = [make_doc("d1", "Municipal water infrastructure funding")]
    assert relevance(docs, _ctx(THEMES)) == 0.0


def test_best_theme_picks_the_strongest_match_not_the_first():
    text = "typescript css browser rendering, with one agent mention"
    theme, score = best_theme(text, THEMES)
    assert theme is not None and theme.name == "dev" and score > 0
