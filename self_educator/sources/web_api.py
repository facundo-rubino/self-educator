"""A worked example of a paginated JSON API with engagement metrics.

Points at HackerNews via Algolia (open, no credentials) so it runs out of the
box, but the shape is the point: paginate, normalise to Document, populate
`metrics` with whatever numbers the API gives you. Copy this file, not the
endpoint, when you write your own.
"""
from __future__ import annotations

from datetime import datetime, timezone

from ..models import Document
from .base import Source, utcnow

DEFAULT_ENDPOINT = "https://hn.algolia.com/api/v1/search"
MAX_PAGES = 20


class WebAPISource(Source):
    name = "web_api"

    # If your API needs a key, list its variable here and read it in fetch().
    # A missing variable excludes the source instead of breaking the run.
    required_env: tuple[str, ...] = ()

    def endpoint(self) -> str:
        return str(self.options.get("endpoint", DEFAULT_ENDPOINT))

    def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]:
        docs: list[Document] = []
        page = 0
        while len(docs) < limit and page < MAX_PAGES:
            resp = self.http.get(self.endpoint(), params={
                "query": query,
                "tags": "story",
                "hitsPerPage": min(100, limit),
                "page": page,
            })
            resp.raise_for_status()
            hits = resp.json().get("hits", [])
            if not hits:
                break
            docs += [self._to_document(h, topic) for h in hits]
            page += 1
        return docs[:limit]

    def _to_document(self, hit: dict, topic: str) -> Document:
        sid = str(hit["objectID"])
        metrics = {k: float(v) for k, v in
                   (("points", hit.get("points")),
                    ("comments", hit.get("num_comments")))
                   if v is not None}
        return Document(
            id=Document.make_id(self.name, sid),
            source=self.name,
            source_id=sid,
            url=hit.get("url") or f"https://news.ycombinator.com/item?id={sid}",
            title=hit.get("title") or "(untitled)",
            text=hit.get("story_text") or "",
            author=hit.get("author"),
            created_at=datetime.fromtimestamp(hit["created_at_i"], tz=timezone.utc),
            fetched_at=utcnow(),
            topic=topic,
            metrics=metrics,
        )
