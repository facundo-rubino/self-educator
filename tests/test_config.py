from pathlib import Path

import yaml

from self_educator.config import Config, estimate_cost
from self_educator.models import Scale


def test_defaults_apply_when_no_config_file(tmp_path: Path):
    cfg = Config.load(tmp_path)
    assert cfg.kb.names  # a usable ontology out of the box
    assert cfg.signal.weights["velocity"] > 0
    assert cfg.sources.order


def test_note_types_come_from_config(tmp_path: Path):
    (tmp_path / "config.yaml").write_text(yaml.safe_dump({
        "topic": "mycology",
        "kb": {"note_types": [
            {"name": "species", "dir": "species", "half_life_days": 3650,
             "description": "One organism."},
            {"name": "habitat", "half_life_days": 700},
        ]},
    }))
    cfg = Config.load(tmp_path)
    assert cfg.topic == "mycology"
    assert cfg.kb.names == ["species", "habitat"]
    # `dir` defaults to a naive plural so a minimal entry still works.
    assert cfg.kb.get("habitat").dir == "habitats"
    assert cfg.kb.get("species").half_life_days == 3650


def test_source_options_are_passed_through(tmp_path: Path):
    (tmp_path / "config.yaml").write_text(yaml.safe_dump({
        "sources": {"order": ["rss"], "rss": {"feeds": ["https://a.test/feed"]}},
    }))
    cfg = Config.load(tmp_path)
    assert cfg.sources.order == ["rss"]
    assert cfg.sources.for_source("rss")["feeds"] == ["https://a.test/feed"]
    assert cfg.sources.for_source("nothing") == {}


def test_every_scale_previews_a_cost():
    for scale in Scale:
        tokens, usd = estimate_cost(scale)
        assert tokens > 0 and usd > 0
