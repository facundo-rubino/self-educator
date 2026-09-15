from datetime import datetime, timezone

import pytest

from self_educator.enrich import WEAK_CONFIDENCE_CAP, enrich
from self_educator.enrich.analyst import Draft
from self_educator.enrich.critic import Review
from self_educator.llm import BudgetExceeded, FakeLLM
from self_educator.models import Evidence, Signal

from .conftest import make_doc


def _signal() -> Signal:
    return Signal(id="sig-1", topic="urban cycling", label="Protected lanes",
                  member_doc_ids=["a"], member_sources=["files"],
                  scores={"velocity": 0.7}, aggregate_score=0.7,
                  first_seen=datetime.now(timezone.utc), sources_count=1)


def _draft(confidence: float = 0.8) -> Draft:
    return Draft(summary="Lanes grow ridership.",
                 evidence=[Evidence(claim="ridership rose", source_doc_id="a")],
                 implications=["build more"], risks=["selection bias"],
                 confidence=confidence)


def test_critic_caps_confidence_on_a_weak_claim():
    llm = FakeLLM([_draft(0.9),
                   Review(is_weak=True, argument="single source",
                          adjusted_confidence=0.7)])
    report = enrich(_signal(), [make_doc("a", "Lanes")], llm)
    assert report.critic.is_weak
    assert report.confidence <= WEAK_CONFIDENCE_CAP


def test_critic_confidence_wins_when_the_claim_survives():
    llm = FakeLLM([_draft(0.9),
                   Review(is_weak=False, argument="holds", adjusted_confidence=0.6)])
    report = enrich(_signal(), [make_doc("a", "Lanes")], llm)
    assert report.confidence == pytest.approx(0.6)
    assert "## Analyst" in report.transcript and "## Critic" in report.transcript


def test_skipping_the_critic_keeps_the_analyst_confidence():
    llm = FakeLLM([_draft(0.9)])
    report = enrich(_signal(), [make_doc("a", "Lanes")], llm, include_critic=False)
    assert report.confidence == pytest.approx(0.9)
    assert not report.critic.is_weak
    assert "## Critic" not in report.transcript


def test_report_records_what_it_cost():
    llm = FakeLLM([_draft(), Review(is_weak=False, argument="ok",
                                    adjusted_confidence=0.8)])
    report = enrich(_signal(), [make_doc("a", "Lanes")], llm)
    assert report.token_cost == llm.tokens_used > 0


def test_query_is_framing_and_never_a_filter():
    llm = FakeLLM([_draft(), Review(is_weak=False, argument="ok",
                                    adjusted_confidence=0.8)])
    enrich(_signal(), [make_doc("a", "Lanes")], llm, query="winter maintenance")
    _, analyst_prompt = llm.calls[0]
    assert "winter maintenance" in analyst_prompt
    assert "do NOT discard" in analyst_prompt


def test_budget_exhaustion_raises_rather_than_silently_truncating():
    class Broke(FakeLLM):
        def parse(self, *args, **kwargs):
            raise BudgetExceeded("spent")

    with pytest.raises(BudgetExceeded):
        enrich(_signal(), [make_doc("a", "Lanes")], Broke([]))
