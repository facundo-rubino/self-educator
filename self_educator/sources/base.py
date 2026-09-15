"""The contract every source implements. Stage 1 — deterministic, no LLM."""
from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import ClassVar

import httpx

from ..models import Document


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def aware(dt: datetime) -> datetime:
    """Naive datetimes from parsers are assumed UTC."""
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


class Source(ABC):
    """Subclass this, set `name`, implement `fetch`, register it.

    Constructor takes the source's block from config.yaml, so the registry can
    build any source uniformly without knowing its options.
    """

    #: The key used in config.yaml's `sources.order`.
    name: ClassVar[str]

    #: Environment variables this source needs. If any is missing the source
    #: excludes itself from the run with a warning instead of raising.
    required_env: ClassVar[tuple[str, ...]] = ()

    def __init__(self, options: dict | None = None,
                 client: httpx.Client | None = None) -> None:
        self.options = options or {}
        self._client = client

    @property
    def http(self) -> httpx.Client:
        """Lazy so that offline sources never open a connection pool."""
        if self._client is None:
            self._client = httpx.Client(timeout=20, follow_redirects=True)
        return self._client

    @abstractmethod
    def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]:
        """Return at most `limit` documents matching `query`.

        Raising is acceptable — the pipeline isolates each source and records
        the failure as a run warning. Collectors are fragile by nature; one
        broken source must not lose the whole run.
        """
