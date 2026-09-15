"""`edu` — the command surface.

Every command that costs money says so before it spends it.
"""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.table import Table

from .config import SCALE_PRESETS, Config, estimate_cost
from .kb import KnowledgeBase
from .models import GapStatus, Scale
from .storage import Store

app = typer.Typer(
    help="self-educator — brief diario y base de conocimiento en Obsidian.",
    no_args_is_help=True)
console = Console()

RootOpt = Annotated[Path, typer.Option("--root", help="Project root.")]


def _ctx(root: Path) -> tuple[Config, Store, KnowledgeBase]:
    cfg = Config.load(root)
    return cfg, Store(cfg.store_dir), KnowledgeBase(cfg.kb_dir, cfg.kb.note_types)


def _llm(cfg: Config, budget: int | None = None):
    from .llm import make_llm

    return make_llm(cfg.provider, cfg.model or None, token_budget=budget)


@contextmanager
def _llm_errors():
    """Turn a missing credential into one clear line, not a traceback.

    Stages 1 and 2 need no key, so a new user can get quite far before this
    matters — which is exactly why the message has to say what to do.
    """
    from .llm import MissingCredentials

    try:
        yield
    except MissingCredentials as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from None


# --------------------------------------------------------------- setup -----
@app.command()
def init(root: RootOpt = Path(".")) -> None:
    """Create kb/ directories from the note types in config.yaml."""
    cfg, _, kb = _ctx(root)
    created = kb.init_dirs()
    for path in created:
        (path / ".gitkeep").touch()
    console.print(f"[green]✓[/] {len(created)} note-type director"
                  f"{'y' if len(created) == 1 else 'ies'} under {cfg.kb_dir}:")
    for spec in cfg.kb.note_types:
        console.print(f"    {spec.dir}/  [dim]{spec.name} — {spec.description}[/]")
    schema = cfg.kb_dir / "SCHEMA.md"
    console.print(f"\nNext: edit [bold]{schema}[/] (how notes get written) "
                  f"and [bold]config.yaml[/] (what gets ingested).")


@app.command()
def sources(root: RootOpt = Path("."),
            check: bool = typer.Option(
                False, "--check",
                help="HTTP-check every RSS feed: does it answer, parse, and "
                     "has anyone published to it lately?")) -> None:
    """Show which sources will run, and why the others will not."""
    from .sources import SOURCE_CLASSES, build_sources, excluded_sources

    cfg, _, _ = _ctx(root)
    active = build_sources(cfg)

    if check:
        rss = active.get("rss")
        if rss is None:
            console.print("[yellow]No active rss source to check.[/]")
            raise typer.Exit(0)
        table = Table(title="Feed check")
        table.add_column("feed", style="cyan", overflow="fold")
        table.add_column("status")
        table.add_column("items", justify="right")
        table.add_column("detail", style="dim", overflow="fold")
        dead = stale = 0
        for row in rss.check():
            if not row["ok"]:
                status, dead = "[red]dead[/]", dead + 1
            elif (days := (row["detail"].split("d ")[0])).isdigit() and int(days) > 120:
                status, stale = "[yellow]stale[/]", stale + 1
            else:
                status = "[green]ok[/]"
            table.add_row(row["url"], status, str(row["entries"]), row["detail"])
        console.print(table)
        console.print(f"{dead} dead, {stale} stale (no post in 120+ days).")
        if dead:
            console.print("[dim]A dead feed costs only its own items — the run "
                          "continues without it. Remove it from config.yaml "
                          "once you are sure it is not coming back.[/]")
        raise typer.Exit(1 if dead else 0)

    table = Table(title="Sources")
    table.add_column("name", style="cyan")
    table.add_column("status")
    table.add_column("options", style="dim")
    for name in cfg.sources.order:
        if name in active:
            status = "[green]active[/]"
        elif name not in SOURCE_CLASSES:
            status = "[red]unknown[/]"
        else:
            status = "[yellow]excluded[/]"
        options = ", ".join(cfg.sources.for_source(name)) or "—"
        table.add_row(name, status, options)
    console.print(table)
    for excluded in excluded_sources(cfg):
        console.print(f"[yellow]![/] {excluded}")
    unused = sorted(set(SOURCE_CLASSES) - set(cfg.sources.order))
    if unused:
        console.print(f"[dim]Available but not in sources.order: {', '.join(unused)}[/]")


# ----------------------------------------------------------- the pipeline --
@app.command()
def run(topic: Annotated[Optional[str], typer.Option("--topic")] = None,
        scale: Annotated[Scale, typer.Option("--scale")] = Scale.M,
        query: Annotated[Optional[str], typer.Option(
            "--query", help="Search string, if different from the topic.")] = None,
        from_gaps: Annotated[bool, typer.Option(
            "--from-gaps", help="Let the KB pick the target from GAPS.md.")] = False,
        yes: Annotated[bool, typer.Option("--yes", "-y")] = False,
        root: RootOpt = Path(".")) -> None:
    """Run the full pipeline: ingest → signal → enrich → compile."""
    from .learning.gaps import target_from_gaps
    from .pipeline import run_pipeline

    cfg, store, kb = _ctx(root)
    if from_gaps:
        target = target_from_gaps(kb)
        if target is None:
            console.print("[yellow]No open gaps — the KB is not asking for anything.[/]")
            raise typer.Exit(0)
        gap_topic, query = target
        topic = topic or gap_topic or cfg.topic
        console.print(f"[bold]--from-gaps[/] → «{topic}»: {query}")
    topic = topic or cfg.topic

    tokens, usd = estimate_cost(scale, cfg.provider)
    preset = SCALE_PRESETS[scale]
    console.print(f"Scale [bold]{scale.value}[/] ({cfg.provider}): ~{tokens:,} tokens ≈ [bold]${usd}[/] "
                  f"({preset.sources} source(s), top {preset.top_signals} signals"
                  f"{'' if preset.critic else ', no critic'})")
    if scale in (Scale.L, Scale.XL) and not yes:
        if not typer.confirm(f"Confirm a {scale.value} run?"):
            console.print("[red]Aborted.[/]")
            raise typer.Exit(1)

    with _llm_errors():
        result = run_pipeline(cfg, store, kb, topic=topic, scale=scale, query=query,
                              llm=_llm(cfg, preset.token_budget),
                              log=lambda m: console.print(f"  {m}"))
    table = Table(title=f"Run {result.run_id} — {topic} [{scale.value}]")
    table.add_column("metric", style="cyan")
    table.add_column("value", justify="right")
    for key, value in [("documents", result.doc_count),
                       ("signals", len(result.signals)),
                       ("reports", len(result.reports)),
                       ("notes", len(result.notes_written)),
                       ("open gaps", result.gaps_open),
                       ("tokens", f"{result.tokens_used:,}"),
                       ("cost", f"${result.cost_usd}")]:
        table.add_row(key, str(value))
    console.print(table)
    for warning in result.warnings:
        console.print(f"[yellow]![/] {warning}")


@app.command("compile")
def compile_cmd(root: RootOpt = Path(".")) -> None:
    """Re-run only stage 4 over stored reports. The cheap half of the pipeline."""
    from .actions import compile_all

    cfg, store, kb = _ctx(root)
    if not store.load_reports():
        console.print("[yellow]No reports in store/. Run `edu run` first.[/]")
        raise typer.Exit(0)
    with _llm_errors():
        summary = compile_all(cfg, store, kb, _llm(cfg),
                              log=lambda m: console.print(f"  {m}"))
    console.print(f"[green]✓[/] {summary.notes_written} note(s) from "
                  f"{summary.reports_compiled}/{summary.reports_total} report(s) "
                  f"(${summary.cost_usd:.2f}).")


# ------------------------------------------------------- the learning loop --
@app.command()
def gaps(root: RootOpt = Path(".")) -> None:
    """Show the attention ledger: what the KB does not know, ranked."""
    from .learning.gaps import refresh_gaps

    _, _, kb = _ctx(root)
    entries = refresh_gaps(kb)
    open_gaps = [g for g in entries if g.status is GapStatus.open]
    if not open_gaps:
        console.print("[green]No open gaps.[/]")
        raise typer.Exit(0)
    table = Table(title=f"{len(open_gaps)} open gap(s)")
    table.add_column("prio", justify="right")
    table.add_column("type", style="cyan")
    table.add_column("description")
    for gap in sorted(open_gaps, key=lambda g: -g.priority):
        table.add_row(f"{gap.priority:.2f}", gap.type.value, gap.description)
    console.print(table)
    console.print("[dim]`edu run --from-gaps` targets the top one.[/]")


@app.command()
def review(limit: Annotated[int, typer.Option("--limit")] = 10,
           root: RootOpt = Path(".")) -> None:
    """Calibration: judge old promoted signals, then adjust the promotion bar."""
    from .learning.calibration import due_for_review, record_outcome, review_signal

    cfg, store, _ = _ctx(root)
    pending = due_for_review(store.load_signals(), cfg.review_after_days)[:limit]
    if not pending:
        console.print(f"[yellow]No signals older than {cfg.review_after_days} "
                      "days awaiting a verdict.[/]")
        raise typer.Exit(0)
    llm = _llm(cfg)
    with _llm_errors():
        for signal in pending:
            verdict = review_signal(signal, llm)
            record_outcome(store, signal, verdict.verdict, verdict.notes)
            console.print(f"  [cyan]{verdict.verdict.value}[/] «{signal.label[:60]}»")
    console.print(f"[green]✓[/] {len(pending)} signal(s) reviewed "
                  f"(${llm.cost_usd:.2f}). Thresholds updated.")


@app.command()
def reconcile(root: RootOpt = Path(".")) -> None:
    """Rule on the graph's open contradictions."""
    from .learning.reconcile import resolve_gap
    from .models import GapType

    cfg, _, kb = _ctx(root)
    entries = kb.read_gaps()
    pending = [g for g in entries
               if g.type is GapType.contradiction and g.status is GapStatus.open]
    if not pending:
        console.print("[green]No open contradictions.[/]")
        raise typer.Exit(0)
    llm = _llm(cfg)
    with _llm_errors():
        for gap in pending:
            resolution = resolve_gap(kb, gap, llm)
            if resolution is None:
                console.print(f"  [dim]skipped: {gap.description}[/]")
                continue
            console.print(f"  [cyan]{resolution.ruling.value}[/] — {gap.description}")
            console.print(f"    [dim]{resolution.reasoning[:200]}[/]")
    kb.write_gaps(entries)
    console.print(f"[green]✓[/] {len(pending)} contradiction(s) processed "
                  f"(${llm.cost_usd:.2f}).")


# ------------------------------------------------------------ inspection ---
@app.command()
def lint(root: RootOpt = Path(".")) -> None:
    """Graph health: broken links, orphans, duplicates, decayed notes."""
    from .maintenance import lint as run_lint

    _, _, kb = _ctx(root)
    report = run_lint(kb)
    sections = [
        ("broken links", report.broken_links),
        ("orphans", report.orphans),
        ("duplicate titles", report.duplicate_titles),
        ("contradictions without a gap", report.unregistered_contradictions),
        ("decayed, needs revalidation", report.decayed),
    ]
    for label, items in sections:
        if items:
            console.print(f"[yellow]{label}[/] ({len(items)})")
            for item in items:
                console.print(f"  - {item}")
    if report.problems == 0:
        console.print("[green]✓ The graph is clean.[/]")
        raise typer.Exit(0)
    console.print(f"\n[yellow]{report.problems} problem(s).[/]")
    raise typer.Exit(1)  # non-zero so CI and pre-commit hooks can gate on it


@app.command()
def status(root: RootOpt = Path(".")) -> None:
    """What is in the KB right now, and what to do next."""
    from .maintenance import lint as run_lint

    cfg, store, kb = _ctx(root)
    notes = kb.load_all()
    open_gaps = [g for g in kb.read_gaps() if g.status is GapStatus.open]
    reports = store.load_reports()
    problems = run_lint(kb).problems if notes else 0

    table = Table(title=f"{cfg.topic}")
    table.add_column("", style="cyan")
    table.add_column("", justify="right")
    table.add_row("notes", str(len(notes)))
    for spec in cfg.kb.note_types:
        count = sum(1 for n in notes if n.meta.type == spec.name)
        table.add_row(f"  {spec.name}", str(count))
    table.add_row("stored reports", str(len(reports)))
    table.add_row("open gaps", str(len(open_gaps)))
    table.add_row("lint problems", str(problems))
    console.print(table)

    if not notes:
        nxt = "`edu run` — the KB is empty."
    elif problems:
        nxt = "`edu lint` — the graph has problems worth fixing first."
    elif open_gaps:
        nxt = "`edu run --from-gaps` — let the KB choose what to look at."
    else:
        nxt = "`edu ask \"...\"` — the KB has no open questions; use it."
    console.print(f"Next: [bold]{nxt}[/]")


@app.command()
def ask(question: Annotated[str, typer.Argument()],
        root: RootOpt = Path(".")) -> None:
    """Ask the KB. It answers only from the notes, or says it cannot."""
    from .actions import ask as ask_kb

    cfg, _, kb = _ctx(root)
    with _llm_errors():
        console.print(ask_kb(kb, _llm(cfg), question))


@app.command()
def brief(root: RootOpt = Path("."),
          page_url: Optional[str] = typer.Option(
              None, "--page-url", help="Link to the published page, for the issue body."),
          issue_out: Optional[Path] = typer.Option(
              None, "--issue-out", help="Write the short issue body here too.")) -> None:
    """Render today's brief. No LLM call, no cost — pure presentation."""
    from .brief import build_brief, render_issue, render_markdown

    cfg, store, kb = _ctx(root)
    today = build_brief(cfg, store, kb)

    page = render_markdown(today, title="Brief")
    docs_dir = Path(root) / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "index.md").write_text(page, encoding="utf-8")

    archive = Path(root) / "briefs"
    archive.mkdir(parents=True, exist_ok=True)
    (archive / f"{today.day.isoformat()}.md").write_text(page, encoding="utf-8")

    if issue_out:
        issue_out.parent.mkdir(parents=True, exist_ok=True)
        issue_out.write_text(render_issue(today, page_url), encoding="utf-8")

    if today.is_empty:
        console.print("[yellow]Nada pasó el filtro hoy.[/] "
                      f"({today.considered} señales, "
                      f"{today.skipped_no_theme} sin tema)")
    else:
        table = Table(title=f"Brief {today.day.isoformat()}")
        table.add_column("#", justify="right", style="dim")
        table.add_column("titular", style="cyan", overflow="fold")
        table.add_column("tema")
        for n, item in enumerate(today.items, 1):
            table.add_row(str(n), item.title, item.theme_label)
        console.print(table)
    console.print(f"[green]→[/] docs/index.md · briefs/{today.day.isoformat()}.md")
