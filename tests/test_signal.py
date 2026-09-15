import numpy as np
import pytest

from self_educator.models import CalibrationRecord, SignalStatus
from self_educator.signal.aggregate import aggregate_score, effective_threshold
from self_educator.signal.cluster import cluster
from self_educator.signal.embedder import HashingEmbedder
from self_educator.signal.engine import detect_signals
from self_educator.signal.scorers import NEUTRAL, ScoringContext, score_all
from datetime import datetime, timezone

from .conftest import make_doc

WEIGHTS = {"velocity": 0.3, "corroboration": 0.25, "novelty": 0.25, "surprise": 0.2}


def _ctx(corpus, centroid=None, baseline=None):
    return ScoringContext(
        corpus=corpus,
        centroid=centroid if centroid is not None else np.zeros(4),
        baseline=baseline or [],
        now=datetime.now(timezone.utc),
    )


def test_hashing_embedder_is_normalised_and_deterministic():
    emb = HashingEmbedder(dims=64)
    a = emb.embed(["protected bike lanes"])
    b = emb.embed(["protected bike lanes"])
    assert np.allclose(a, b)
    assert pytest.approx(1.0, abs=1e-5) == float(np.linalg.norm(a[0]))


def test_cluster_groups_similar_and_separates_different():
    vectors = np.array([[1.0, 0.0], [0.98, 0.02], [0.0, 1.0]])
    groups = cluster(vectors, threshold=0.8)
    assert sorted(len(g) for g in groups) == [1, 2]


def test_metric_scorers_stay_neutral_without_metrics():
    """An RSS-only corpus has no upvotes; scoring that as zero interest would
    bury every signal that came from it."""
    docs = [make_doc("a", "One"), make_doc("b", "Two")]
    scores = score_all(docs, _ctx(docs), WEIGHTS)
    assert scores["velocity"] == NEUTRAL
    assert scores["surprise"] == NEUTRAL


def test_velocity_rewards_recent_engagement():
    fresh = [make_doc("a", "Hot", metrics={"points": 900}, age_hours=1)]
    stale = [make_doc("b", "Cold", metrics={"points": 900}, age_hours=5000)]
    corpus = fresh + stale
    assert (score_all(fresh, _ctx(corpus), WEIGHTS)["velocity"]
            > score_all(stale, _ctx(corpus), WEIGHTS)["velocity"])


def test_corroboration_rewards_multiple_sources():
    corpus = [make_doc("a", "x", source="files"), make_doc("b", "y", source="rss")]
    one = score_all([corpus[0]], _ctx(corpus), WEIGHTS)["corroboration"]
    both = score_all(corpus, _ctx(corpus), WEIGHTS)["corroboration"]
    assert both > one


def test_novelty_is_total_without_a_baseline_and_drops_against_one():
    docs = [make_doc("a", "x")]
    centroid = np.array([1.0, 0.0])
    assert score_all(docs, _ctx(docs, centroid), WEIGHTS)["novelty"] == 1.0
    seen = score_all(docs, _ctx(docs, centroid, [[1.0, 0.0]]), WEIGHTS)["novelty"]
    assert seen < 0.1


def test_unknown_scorer_name_fails_loudly():
    """A typo in signal.weights would silently change every ranking."""
    docs = [make_doc("a", "x")]
    with pytest.raises(KeyError, match="typoo"):
        score_all(docs, _ctx(docs), {"typoo": 1.0})


def test_aggregate_normalises_weights():
    scores = {"a": 1.0, "b": 0.0}
    assert aggregate_score(scores, {"a": 2.0, "b": 2.0}) == pytest.approx(0.5)


def test_threshold_ignores_calibration_until_there_is_enough_of_it():
    now = datetime.now(timezone.utc)
    thin = {"files": CalibrationRecord(source="files", signals_reviewed=2,
                                       learned_threshold=0.85, updated=now)}
    assert effective_threshold(thin, 0.6) == 0.6
    rich = {"files": CalibrationRecord(source="files", signals_reviewed=20,
                                       learned_threshold=0.85, updated=now)}
    assert effective_threshold(rich, 0.6) == pytest.approx(0.85)


def test_detect_signals_promotes_something_on_a_cold_start(embedder):
    """With nothing promoted there is no report, no note and no calibration
    data — the learning loop would never start."""
    docs = [make_doc("a", "Bike lanes and ridership"),
            make_doc("b", "Something else entirely")]
    signals, centroids = detect_signals(
        docs, [], "urban cycling", embedder=embedder, weights=WEIGHTS,
        promotion_threshold=0.99)
    assert signals and centroids
    assert sum(s.status is SignalStatus.promoted for s in signals) == 1


def test_detect_signals_handles_an_empty_corpus(embedder):
    assert detect_signals([], [], "t", embedder=embedder, weights=WEIGHTS) == ([], [])
