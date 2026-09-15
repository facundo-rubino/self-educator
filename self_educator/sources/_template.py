"""Copy this file to add a source. Three steps, no core edits.

    1. cp _template.py mysource.py, rename the class, set `name`.
    2. Register it — either import it in sources/__init__.py and add it to
       SOURCE_CLASSES, or call register(MySource) from your own module.
    3. Add its name to `sources.order` in config.yaml, with an options block
       if it needs one.

Everything downstream (clustering, scoring, enrichment, compilation) works on
Documents and never asks where they came from.
"""
from __future__ import annotations

from ..models import Document
from .base import Source, utcnow


class MySource(Source):
    #: Must match the key you put in config.yaml's `sources.order`.
    name = "my_source"

    #: Environment variables required to operate. Missing ones exclude this
    #: source from the run with a warning; they never crash it.
    required_env: tuple[str, ...] = ()  # e.g. ("MY_SOURCE_TOKEN",)

    def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]:
        # `self.options` is this source's block from config.yaml.
        # `self.http` is a lazily-created httpx.Client with sane timeouts.
        raw_items: list[dict] = []  # ← your API call goes here

        docs: list[Document] = []
        for item in raw_items[:limit]:
            sid = str(item["id"])
            docs.append(Document(
                id=Document.make_id(self.name, sid),
                source=self.name,
                source_id=sid,
                url=item["url"],
                title=item["title"],
                text=item.get("body", ""),
                author=item.get("author"),
                created_at=item["created_at"],   # must be timezone-aware
                fetched_at=utcnow(),
                topic=topic,
                # Any engagement numbers you have. Leave empty if there are
                # none — the metric-based scorers degrade rather than reading
                # the absence as zero interest.
                metrics={"upvotes": float(item.get("upvotes", 0))},
            ))
        return docs
