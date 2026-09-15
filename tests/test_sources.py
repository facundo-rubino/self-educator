from pathlib import Path

import pytest

from self_educator.config import Config, SourcesConfig
from self_educator.models import Document
from self_educator.sources import (
    SOURCE_CLASSES, build_sources, excluded_sources, register,
)
from self_educator.sources.base import Source
from self_educator.sources.files import FilesSource
from self_educator.sources.rss import RSSSource

CORPUS = Path(__file__).resolve().parent.parent / "examples" / "corpus"


def test_files_source_reads_the_example_corpus():
    docs = FilesSource({"paths": [str(CORPUS)]}).fetch("cycling", limit=10,
                                                       topic="urban cycling")
    assert docs
    assert all(isinstance(d, Document) for d in docs)
    assert all(d.source == "files" for d in docs)
    # The .md convention: the H1 becomes the title.
    assert any(d.title == "Protected bike lanes correlate with ridership growth"
               for d in docs)
    # The .json convention: metrics ride along, so scorers have numbers.
    assert any(d.metrics.get("points") for d in docs)


def test_files_source_filters_on_query_terms():
    src = FilesSource({"paths": [str(CORPUS)]})
    hits = src.fetch("helmet", limit=10, topic="t")
    assert hits and all("helmet" in f"{d.title} {d.text}".lower() for d in hits)
    assert src.fetch("quantum chromodynamics", limit=10, topic="t") == []


def test_rss_source_parses_both_dialects():
    rss = """<rss><channel><item>
      <title>An item</title><link>https://a.test/1</link>
      <description>&lt;p&gt;Body&lt;/p&gt;</description>
      <pubDate>Tue, 05 Aug 2025 10:00:00 +0000</pubDate>
    </item></channel></rss>"""
    atom = """<feed xmlns="http://www.w3.org/2005/Atom"><entry>
      <title>An entry</title><link href="https://a.test/2"/>
      <summary>Body</summary><updated>2025-08-05T10:00:00Z</updated>
    </entry></feed>"""
    source = RSSSource({})
    assert source._parse(rss, 5, "t")[0].title == "An item"
    entry = source._parse(atom, 5, "t")[0]
    assert entry.title == "An entry" and entry.url == "https://a.test/2"


def test_missing_credentials_exclude_a_source_instead_of_crashing(monkeypatch):
    class Credentialed(Source):
        name = "credentialed"
        required_env = ("A_KEY_THAT_IS_NOT_SET",)

        def fetch(self, query, *, limit, topic):
            raise AssertionError("must never run without its credential")

    monkeypatch.setitem(SOURCE_CLASSES, "credentialed", Credentialed)
    cfg = Config(root=Path("."),
                 sources=SourcesConfig(order=["files", "credentialed"]))
    monkeypatch.delenv("A_KEY_THAT_IS_NOT_SET", raising=False)

    assert "credentialed" not in build_sources(cfg)
    assert "files" in build_sources(cfg)
    assert any("A_KEY_THAT_IS_NOT_SET" in e for e in excluded_sources(cfg))


def test_unknown_source_is_reported_not_raised():
    cfg = Config(root=Path("."), sources=SourcesConfig(order=["nope"]))
    assert build_sources(cfg) == {}
    assert excluded_sources(cfg) == ["nope (unknown source)"]


def test_register_adds_a_source_without_touching_the_core():
    @register
    class Custom(Source):
        name = "custom_test_source"

        def fetch(self, query, *, limit, topic):
            return []

    try:
        cfg = Config(root=Path("."),
                     sources=SourcesConfig(order=["custom_test_source"]))
        assert "custom_test_source" in build_sources(cfg)
    finally:
        SOURCE_CLASSES.pop("custom_test_source", None)
