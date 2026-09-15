"""Configuration: everything a new user changes without touching the core.

`config.yaml` supplies the topic, the note-type ontology, the scoring weights
and the source list. This module turns it into typed settings and supplies the
defaults for anything the file leaves out.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .models import Scale

# Which provider stages 3-4 talk to. DeepSeek by default: this workload only
# ever sends it what survived stage 2, so the bill is cents per month.
DEFAULT_PROVIDER = "deepseek"
DEFAULT_MODEL = ""  # empty = the provider's own default, see llm.PROVIDERS


@dataclass(frozen=True)
class NoteTypeSpec:
    """One entry in the KB ontology. Defined in config, not in code."""

    name: str
    dir: str
    half_life_days: int
    description: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "NoteTypeSpec":
        name = str(data["name"])
        return cls(
            name=name,
            dir=str(data.get("dir") or f"{name}s"),
            half_life_days=int(data.get("half_life_days", 180)),
            description=str(data.get("description", "")),
        )


DEFAULT_NOTE_TYPES: list[NoteTypeSpec] = [
    NoteTypeSpec("concept", "concepts", 180, "A single idea, term, technology or entity."),
    NoteTypeSpec("pattern", "patterns", 365, "A regularity that recurs across cases."),
    NoteTypeSpec("actor", "actors", 120, "A person, organization or product."),
    NoteTypeSpec("question", "questions", 120, "Something the evidence raises but does not answer."),
    NoteTypeSpec("risk", "risks", 120, "A reason a claim here might be wrong or short-lived."),
]

DEFAULT_WEIGHTS = {
    "velocity": 0.30,
    "corroboration": 0.25,
    "novelty": 0.25,
    "surprise": 0.20,
}

DEFAULT_SOURCE_ORDER = ["files", "rss", "web_api"]


@dataclass(frozen=True)
class ScalePreset:
    """How much of the world to look at, and how much to spend looking."""

    docs_per_source: int
    sources: int
    top_signals: int
    critic: bool
    token_budget: int


# Tuned for the daily brief: `S` is what the cron runs every morning, so it
# has to promote at least as many signals as the themes' quotas add up to
# (7 today) or the brief can never fill. Three sources so `files` gets read
# alongside rss and web_api. The budget is DeepSeek tokens: ~US$0.015 a run.
SCALE_PRESETS: dict[Scale, ScalePreset] = {
    Scale.XS: ScalePreset(50, 1, 1, False, 5_000),
    Scale.S: ScalePreset(250, 3, 9, True, 25_000),
    Scale.M: ScalePreset(600, 3, 14, True, 60_000),
    Scale.L: ScalePreset(1_000, 4, 12, True, 150_000),
    Scale.XL: ScalePreset(3_000, 6, 25, True, 400_000),
}


def estimate_cost(scale: Scale, provider: str = DEFAULT_PROVIDER) -> tuple[int, float]:
    """Shown before every run. Assumes a ~60/40 input/output split."""
    from .llm import PRICES

    tokens = SCALE_PRESETS[scale].token_budget
    price_in, price_out = PRICES.get(provider, PRICES[DEFAULT_PROVIDER])
    usd = tokens * 0.6 * price_in + tokens * 0.4 * price_out
    return tokens, round(usd, 4)


@dataclass
class ThemeSpec:
    """One subject the brief is allowed to be about.

    Used twice, which is why it is a type and not a loose list: stage 2 scores
    a cluster's relevance against these, and the brief uses the same match to
    fill each theme's quota. Change the themes here and both follow.
    """

    name: str
    label: str
    quota: int = 2
    keywords: list[str] = field(default_factory=list)

    #: Hits needed for a full relevance score. Low on purpose — a headline is
    #: short, and three of the right words is already a strong match.
    SATURATION = 3

    def score(self, text: str) -> float:
        if not self.keywords:
            return 0.0
        low = text.lower()
        hits = sum(1 for k in self.keywords if k.lower() in low)
        return min(1.0, hits / self.SATURATION)


def best_theme(text: str, themes: list[ThemeSpec]) -> tuple[ThemeSpec | None, float]:
    """The theme this text belongs to, and how strongly. The single classifier."""
    best: ThemeSpec | None = None
    best_score = 0.0
    for theme in themes:
        s = theme.score(text)
        if s > best_score:
            best, best_score = theme, s
    return best, best_score


@dataclass
class KBConfig:
    note_types: list[NoteTypeSpec] = field(
        default_factory=lambda: list(DEFAULT_NOTE_TYPES))

    @classmethod
    def from_dict(cls, data: dict) -> "KBConfig":
        raw = data.get("note_types")
        if not raw:
            return cls()
        return cls(note_types=[NoteTypeSpec.from_dict(d) for d in raw])

    def get(self, name: str) -> NoteTypeSpec | None:
        return next((t for t in self.note_types if t.name == name), None)

    @property
    def names(self) -> list[str]:
        return [t.name for t in self.note_types]


@dataclass
class SignalConfig:
    cluster_threshold: float = 0.55
    promotion_threshold: float = 0.6
    weights: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_WEIGHTS))

    @classmethod
    def from_dict(cls, data: dict) -> "SignalConfig":
        kwargs: dict = {}
        for key in ("cluster_threshold", "promotion_threshold"):
            if key in data:
                kwargs[key] = float(data[key])
        if weights := data.get("weights"):
            kwargs["weights"] = {str(k): float(v) for k, v in weights.items()}
        return cls(**kwargs)


@dataclass
class SourcesConfig:
    """`order` both enables and prioritises: presets take order[:n]."""

    order: list[str] = field(default_factory=lambda: list(DEFAULT_SOURCE_ORDER))
    options: dict[str, dict] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> "SourcesConfig":
        order = [str(s) for s in data.get("order", DEFAULT_SOURCE_ORDER)]
        options = {k: dict(v) for k, v in data.items()
                   if k != "order" and isinstance(v, dict)}
        return cls(order=order, options=options)

    def for_source(self, name: str) -> dict:
        return dict(self.options.get(name, {}))


_TOP_LEVEL_KEYS = {"topic", "provider", "model", "review_after_days"}


@dataclass
class Config:
    root: Path
    topic: str = "your topic here"
    provider: str = DEFAULT_PROVIDER
    model: str = DEFAULT_MODEL
    review_after_days: int = 28
    themes: list[ThemeSpec] = field(default_factory=list)
    kb: KBConfig = field(default_factory=KBConfig)
    signal: SignalConfig = field(default_factory=SignalConfig)
    sources: SourcesConfig = field(default_factory=SourcesConfig)

    @property
    def kb_dir(self) -> Path:
        return self.root / "kb"

    @property
    def store_dir(self) -> Path:
        return self.root / "store"

    @property
    def runs_dir(self) -> Path:
        return self.root / "runs"

    @classmethod
    def load(cls, root: Path) -> "Config":
        root = Path(root)
        # Credentials: <root>/.env first, then the cwd's — so a KB kept outside
        # the repo can still borrow the repo's keys. Shell env always wins.
        load_dotenv(root / ".env")
        load_dotenv(Path.cwd() / ".env")

        path = root / "config.yaml"
        data: dict = yaml.safe_load(path.read_text()) if path.exists() else {}
        data = data or {}

        kwargs: dict = {k: v for k, v in data.items() if k in _TOP_LEVEL_KEYS}
        if isinstance(data.get("kb"), dict):
            kwargs["kb"] = KBConfig.from_dict(data["kb"])
        if isinstance(data.get("signal"), dict):
            kwargs["signal"] = SignalConfig.from_dict(data["signal"])
        if isinstance(data.get("sources"), dict):
            kwargs["sources"] = SourcesConfig.from_dict(data["sources"])
        if isinstance(data.get("themes"), list):
            kwargs["themes"] = [
                ThemeSpec(name=t["name"], label=t.get("label", t["name"]),
                          quota=int(t.get("quota", 2)),
                          keywords=list(t.get("keywords", [])))
                for t in data["themes"] if isinstance(t, dict) and "name" in t
            ]
        return cls(root=root, **kwargs)
