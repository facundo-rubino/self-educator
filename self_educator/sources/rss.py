"""Any RSS/Atom feed. Config-driven, no credentials.

Feeds have no engagement metrics, which is deliberate here: it exercises the
path where metric-based scorers degrade instead of reporting zero interest.

Failures are isolated per feed, not per source. With a couple of dozen feeds
configured, one dead host must cost its own items and nothing else — the
pipeline's own isolation is one level too coarse for that, because it would
drop every feed in the list.
"""
from __future__ import annotations

import re
from datetime import datetime
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree

import httpx

from ..models import Document
from .base import Source, aware, utcnow

_TAG = re.compile(r"<[^>]+>")
_ATOM = "{http://www.w3.org/2005/Atom}"


def _strip(html: str) -> str:
    return _TAG.sub(" ", html or "").strip()


def _parse_date(value: str | None) -> datetime:
    if not value:
        return utcnow()
    try:
        return aware(parsedate_to_datetime(value))
    except (TypeError, ValueError):
        pass
    try:
        return aware(datetime.fromisoformat(value.replace("Z", "+00:00")))
    except ValueError:
        return utcnow()


class RSSSource(Source):
    name = "rss"

    def feeds(self) -> list[str]:
        return [str(f) for f in self.options.get("feeds", [])]

    def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]:
        feeds = self.feeds()
        if not feeds:
            return []
        per_feed = max(1, limit // len(feeds))
        docs: list[Document] = []
        self.failures = []
        for url in feeds:
            try:
                resp = self.http.get(url)
                resp.raise_for_status()
                docs += self._parse(resp.text, per_feed, topic)
            except (httpx.HTTPError, ElementTree.ParseError) as exc:
                self.failures.append((url, f"{type(exc).__name__}: {exc}"))
        if not docs and self.failures:
            raise RuntimeError(
                f"every configured feed failed ({len(self.failures)}); "
                f"first: {self.failures[0][1]}")
        return docs[:limit]

    def check(self) -> list[dict]:
        """HTTP-check every configured feed. Used by `edu sources --check`.

        Reported per feed: whether it answered, whether it parses, how many
        entries it carries and how fresh the newest one is. A feed nobody has
        published to in months is dead weight in the brief even when it is
        still technically up.
        """
        out: list[dict] = []
        for url in self.feeds():
            row = {"url": url, "ok": False, "detail": "", "entries": 0,
                   "latest": None}
            try:
                resp = self.http.get(url)
                resp.raise_for_status()
                docs = self._parse(resp.text, 200, "check")
                row["entries"] = len(docs)
                if docs:
                    latest = max(d.created_at for d in docs)
                    row["latest"] = latest
                    row["ok"] = True
                    row["detail"] = f"{(utcnow() - latest).days}d since last post"
                else:
                    row["detail"] = "parsed, but no entries"
            except Exception as exc:  # noqa: BLE001 - a check reports, never raises
                row["detail"] = f"{type(exc).__name__}: {exc}"
            out.append(row)
        return out

    def _parse(self, body: str, limit: int, topic: str) -> list[Document]:
        root = ElementTree.fromstring(body)
        # One walk handles both dialects: RSS <item> and Atom <entry>.
        entries = root.iter("item") if root.find(".//item") is not None \
            else root.iter(f"{_ATOM}entry")
        docs: list[Document] = []
        for entry in entries:
            if len(docs) >= limit:
                break
            fields = self._fields(entry)
            if not fields["link"]:
                continue
            docs.append(Document(
                id=Document.make_id(self.name, fields["link"]),
                source=self.name,
                source_id=fields["link"],
                url=fields["link"],
                title=fields["title"],
                text=fields["text"],
                author=fields["author"],
                created_at=_parse_date(fields["date"]),
                fetched_at=utcnow(),
                topic=topic,
            ))
        return docs

    @staticmethod
    def _fields(entry) -> dict[str, str]:
        def text_of(*tags: str) -> str:
            for tag in tags:
                el = entry.find(tag)
                if el is not None and (el.text or "").strip():
                    return el.text.strip()
            return ""

        link = text_of("link", f"{_ATOM}id")
        if not link:
            el = entry.find(f"{_ATOM}link")
            link = el.get("href", "") if el is not None else ""
        return {
            "link": link,
            "title": text_of("title", f"{_ATOM}title") or "(untitled)",
            "text": _strip(text_of("description", f"{_ATOM}summary",
                                   f"{_ATOM}content"))[:4000],
            "author": text_of("author", "{http://purl.org/dc/elements/1.1/}creator") or None,
            "date": text_of("pubDate", f"{_ATOM}updated", f"{_ATOM}published"),
        }
