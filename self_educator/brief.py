"""Stage 5 — the daily brief. Renders, never calls an LLM.

Everything this needs was decided upstream: stage 2 ranked and de-duplicated,
stage 3 wrote the one-line reason each item matters. So the brief is pure
presentation, which is what makes it free to re-render and impossible to break
by running out of API budget.

Shape is set by how it gets read: headlines first, one line of why, a link.
Skim the seven, open the two you care about, close the tab. The quota per
theme is what keeps three subjects from turning into one noisy list — without
it the loudest topic of the week crowds out the other two every time.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone

from .config import Config
from .kb import KnowledgeBase
from .models import Report, Signal
from .storage import Store


@dataclass
class BriefItem:
    title: str
    why: str
    url: str
    theme_label: str
    sources: list[str]
    confidence: float
    note_ids: list[str]


@dataclass
class Brief:
    day: date
    items: list[BriefItem]
    considered: int          # signals looked at before the quota cut
    skipped_no_theme: int

    @property
    def is_empty(self) -> bool:
        return not self.items


#: Shortest head we will accept as a real first sentence. Anything under this
#: is almost always an abbreviation ("e.g.", "vs.", "Inc.") rather than a
#: sentence boundary, and cutting there would lose the actual finding.
_MIN_SENTENCE = 25


def _first_sentence(text: str, limit: int = 220) -> str:
    """The reason, not the essay. Stage 3 summaries open with the finding."""
    clean = " ".join((text or "").split())
    if not clean:
        return ""
    for stop in (". ", "; "):
        head, sep, _ = clean.partition(stop)
        if sep and len(head) >= _MIN_SENTENCE:
            clean = head
            break
    return clean if len(clean) <= limit else clean[: limit - 1].rstrip() + "…"


def build_brief(cfg: Config, store: Store, kb: KnowledgeBase | None = None,
                day: date | None = None) -> Brief:
    """Pick the day's items: best first, capped by each theme's quota."""
    day = day or datetime.now(timezone.utc).date()
    reports = {r.signal_id: r for r in store.load_reports()}
    signals = [s for s in store.load_signals() if s.id in reports]
    signals.sort(key=lambda s: -s.aggregate_score)

    labels = {t.name: t.label for t in cfg.themes}
    remaining = {t.name: t.quota for t in cfg.themes}
    notes_by_source = _notes_by_source(kb) if kb is not None else {}

    items: list[BriefItem] = []
    skipped = 0
    for signal in signals:
        if not signal.theme:
            # No theme means the relevance scorer could not place it. It got
            # this far on velocity alone, which is exactly the noise to cut.
            skipped += 1
            continue
        if remaining.get(signal.theme, 0) <= 0:
            continue
        remaining[signal.theme] -= 1
        report = reports[signal.id]
        items.append(BriefItem(
            title=signal.label,
            why=_first_sentence(report.summary),
            url=signal.headline_url,
            theme_label=labels.get(signal.theme, signal.theme),
            sources=signal.member_sources,
            confidence=report.confidence,
            note_ids=sorted(notes_by_source.get(signal.id, set())),
        ))

    return Brief(day=day, items=items, considered=len(signals),
                 skipped_no_theme=skipped)


def _notes_by_source(kb: KnowledgeBase) -> dict[str, set[str]]:
    """Which KB notes cite which signal, so an item can link to what it grew into."""
    out: dict[str, set[str]] = {}
    for note in kb.load_all():
        for src in note.meta.sources:
            out.setdefault(str(src), set()).add(note.meta.id)
    return out


# --------------------------------------------------------------- rendering ---
def render_markdown(brief: Brief, *, title: str = "Brief") -> str:
    """The full page: what GitHub Pages serves and what briefs/ archives."""
    lines = [f"# {title} — {brief.day.isoformat()}", ""]
    if brief.is_empty:
        lines += [
            "Hoy no pasó nada que pase el filtro.",
            "",
            "No es un error: es el sistema haciendo su trabajo. "
            "Tomate el café tranquilo.",
            "",
        ]
    else:
        by_theme: dict[str, list[BriefItem]] = {}
        for item in brief.items:
            by_theme.setdefault(item.theme_label, []).append(item)

        lines += ["## Los titulares", ""]
        for n, item in enumerate(brief.items, 1):
            link = f"[{item.title}]({item.url})" if item.url else item.title
            lines.append(f"{n}. {link} — *{item.theme_label}*")
        lines += ["", "---", ""]

        for theme_label, group in by_theme.items():
            lines += [f"## {theme_label}", ""]
            for item in group:
                heading = f"### [{item.title}]({item.url})" if item.url \
                    else f"### {item.title}"
                lines.append(heading)
                if item.why:
                    lines += ["", item.why]
                meta = [f"fuentes: {', '.join(item.sources)}",
                        f"confianza: {item.confidence:.0%}"]
                if item.note_ids:
                    meta.append("en el KB: " +
                                ", ".join(f"`{i}`" for i in item.note_ids))
                lines += ["", f"<sub>{' · '.join(meta)}</sub>", ""]

    lines += [
        "---",
        "",
        f"<sub>{brief.considered} señales consideradas, "
        f"{brief.skipped_no_theme} descartadas por no ser de ningún tema. "
        "El KB completo se abre con Obsidian sobre `kb/`.</sub>",
        "",
    ]
    return "\n".join(lines)


def render_issue(brief: Brief, page_url: str | None = None, top: int = 3) -> str:
    """The push half: what lands in the inbox. Three headlines and a link."""
    if brief.is_empty:
        body = ["Hoy no pasó nada que pase el filtro. Tomate el café tranquilo."]
    else:
        body = []
        for item in brief.items[:top]:
            link = f"[{item.title}]({item.url})" if item.url else item.title
            body.append(f"**{link}**")
            if item.why:
                body.append(f"{item.why}")
            body.append("")
        rest = len(brief.items) - top
        if rest > 0:
            body.append(f"…y {rest} más.")
    if page_url:
        body += ["", f"→ [Brief completo]({page_url})"]
    return "\n".join(body).strip()
