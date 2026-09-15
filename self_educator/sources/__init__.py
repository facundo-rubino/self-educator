"""The source registry: config-driven, extensible without editing the core."""
from __future__ import annotations

import os
from typing import TYPE_CHECKING

from ..config import SourcesConfig
from .base import Source
from .files import FilesSource
from .rss import RSSSource
from .web_api import WebAPISource

if TYPE_CHECKING:
    from ..config import Config

SOURCE_CLASSES: dict[str, type[Source]] = {
    FilesSource.name: FilesSource,
    RSSSource.name: RSSSource,
    WebAPISource.name: WebAPISource,
}


def register(cls: type[Source]) -> type[Source]:
    """Add a source at import time. Usable as a decorator."""
    SOURCE_CLASSES[cls.name] = cls
    return cls


def _config(cfg: "Config | None") -> SourcesConfig:
    return cfg.sources if cfg is not None else SourcesConfig()


def _missing_env(name: str) -> list[str]:
    return [v for v in SOURCE_CLASSES[name].required_env if not os.environ.get(v)]


def excluded_sources(cfg: "Config | None" = None) -> list[str]:
    """Configured sources that will not run, each with its reason."""
    out: list[str] = []
    for name in _config(cfg).order:
        if name not in SOURCE_CLASSES:
            out.append(f"{name} (unknown source)")
        elif missing := _missing_env(name):
            out.append(f"{name} (missing {', '.join(missing)})")
    return out


def build_sources(cfg: "Config | None" = None) -> dict[str, Source]:
    """Instantiate the configured sources, in configured order.

    Sources whose required env vars are absent are dropped; ask
    `excluded_sources()` for the reasons.
    """
    sources = _config(cfg)
    return {
        name: SOURCE_CLASSES[name](sources.for_source(name))
        for name in sources.order
        if name in SOURCE_CLASSES and not _missing_env(name)
    }


__all__ = [
    "Source", "SOURCE_CLASSES", "register",
    "build_sources", "excluded_sources",
    "FilesSource", "RSSSource", "WebAPISource",
]
