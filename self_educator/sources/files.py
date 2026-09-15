"""A local directory of documents. No network, no credentials.

This is what makes the template runnable and testable the moment it is cloned,
and it is a real source in its own right: plenty of knowledge bases are built
from a folder of notes, transcripts or exports rather than from the web.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ..models import Document
from .base import Source, utcnow

DEFAULT_EXTENSIONS = (".md", ".txt", ".json")


class FilesSource(Source):
    name = "files"

    def _paths(self) -> list[Path]:
        return [Path(p) for p in self.options.get("paths", [])]

    def _extensions(self) -> tuple[str, ...]:
        return tuple(self.options.get("extensions", DEFAULT_EXTENSIONS))

    def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]:
        terms = [t for t in query.lower().split() if len(t) > 2]
        exts = self._extensions()
        docs: list[Document] = []
        for root in self._paths():
            if not root.is_dir():
                continue
            for path in sorted(root.rglob("*")):
                if len(docs) >= limit:
                    break
                if not path.is_file() or path.suffix.lower() not in exts:
                    continue
                doc = self._read(path, topic)
                # The path counts as content: people name local files
                # meaningfully, and "notes/cycling/lanes.md" is a real signal
                # about what the file is even when the body never says it.
                # A query too short to yield terms matches everything, which is
                # the right default for a corpus this small.
                haystack = f"{path} {doc.title} {doc.text}".lower()
                if terms and not any(t in haystack for t in terms):
                    continue
                docs.append(doc)
        return docs[:limit]

    def _read(self, path: Path, topic: str) -> Document:
        raw = path.read_text(errors="replace")
        title, text, metrics = path.stem, raw, {}
        if path.suffix.lower() == ".json":
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                data = {}
            if isinstance(data, dict):
                title = str(data.get("title") or title)
                text = str(data.get("text") or data.get("body") or raw)
                metrics = {k: float(v) for k, v in (data.get("metrics") or {}).items()}
        elif raw.startswith("# "):
            # Markdown convention: the H1 is the title.
            title = raw.splitlines()[0][2:].strip() or title
        stat = path.stat()
        return Document(
            id=Document.make_id(self.name, str(path)),
            source=self.name,
            source_id=str(path),
            url=path.resolve().as_uri(),
            title=title,
            text=text,
            created_at=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
            fetched_at=utcnow(),
            topic=topic,
            metrics=metrics,
        )
