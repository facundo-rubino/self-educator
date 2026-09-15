# self-educator — Design

**Date:** 2026-08-30
**Status:** approved
**Derived from:** the TrendFisher/TrendBrain project, genericized.

## Problem

The collector → knowledge-base pattern in TrendBrain works, but it is welded to one
domain (AI-devtools trend hunting). Its note types, its sources, and its scoring
vocabulary live in Python enums and `if` chains. Someone who wants to point the
same machinery at a different subject has to edit the core to do it.

This template extracts the *flow* and makes the domain a matter of configuration.

## Goal

An executable Python package that a new user clones, points at their own sources,
and adapts by editing two files: `config.yaml` (what to ingest, what note types
exist) and `kb/SCHEMA.md` (how the compiler writes notes). Everything else is the
pipeline, unchanged.

## The four stages

```
sources/*  →  [1] ingest      Document[]      deterministic, no LLM
              [2] signal      Signal[]        embed → cluster → score → promote, no LLM
              [3] enrich      Report[]        analyst + critic, LLM + token budget
              [4] compile     Note[] in kb/   LLM, guided by kb/SCHEMA.md
```

Each stage persists its output under `store/` and can be re-run in isolation.
`edu compile` re-runs only stage 4 over reports already on disk — the cheap half
of the pipeline, useful after editing `SCHEMA.md` or deleting notes.

Stage 2 is where the volume dies: a corpus of hundreds of documents becomes a
handful of scored clusters, and only the ones above the promotion threshold reach
the LLM. That ordering is the whole cost model, and it is why stages 1–2 contain
no LLM call at all.

The token budget is per-run and enforced by the LLM client. When it is exhausted,
`BudgetExceeded` stops the current stage and the run reports what it completed
rather than failing outright.

## Genericization decisions

| TrendFisher | Template | Rationale |
|---|---|---|
| `market` | `topic` | domain-neutral |
| `hunt` | `run` | an ingest cycle, not a hunt |
| `brain/` | `kb/` | the KB is the artifact |
| `connectors/` | `sources/` | matches the user's mental model |
| `Source` enum (8 members) | `Document.source: str` | **a new source needs no core edit** |
| `NoteType` enum (6 members) | `config.yaml → kb.note_types` | **the user owns their ontology** |
| investigator / skeptic | `analyst` / `critic` | roles, not characters |
| `scope` XS–XL | `scale` XS–XL | same cost lever |
| `Scores` (4 fixed fields) | `scores: dict[str, float]` | scorers are a registry |
| neuron / hypothalamus / synapse | out of scope | documented as extensions |

The two rows in bold are the substance of the work. In TrendFisher, adding a
source means editing an enum, a class map, and a builder; adding a note type means
editing an enum, a half-life table, and a directory map. Here both are data.

## Components

**`config.py`** — `Config.load(root)` reads `config.yaml`, merges `.env`, and
returns typed settings: note-type specs, scale presets, scoring weights and
thresholds, and the ordered source list with per-source options.

**`models.py`** — pydantic schemas for every artifact. Note type and source are
plain `str`, validated against config rather than a compiled-in enum.

**`sources/`** — a `Source` ABC (`fetch(query, *, limit, topic) -> list[Document]`)
plus a name→class registry. Three shipped implementations: `files` (a local
directory, so the pipeline is testable offline with no network and no keys),
`rss` (any feed list from config), and `web_api` (HN/Algolia, as a worked example
of pagination and engagement metrics). `_template.py` is the copy-me starting
point. Sources declare `required_env`; missing credentials exclude the source
with a warning instead of crashing the run.

**`signal/`** — `embedder` (sentence-transformers when the `ml` extra is
installed, deterministic hashing fallback otherwise), `cluster` (greedy cosine
against running centroids), `scorers` (a registry: velocity, corroboration,
novelty, surprise), `aggregate` (weighted sum + calibration-adjusted threshold),
`engine` (ties them together). Metric-dependent scorers degrade to a neutral
value when a source carries no engagement numbers, so an RSS-only setup still
works.

**`enrich/`** — `analyst` drafts a report with per-claim source citations;
`critic` attacks it and returns an adjusted confidence. The critic is a gate, not
decoration: at scales where it runs, its verdict caps the report's confidence.

**`synthesis/compiler.py`** — feeds `kb/SCHEMA.md` as the system prompt, the
existing note index as context, and the report as the payload. Returns notes that
either create or *merge into* existing ids. Contradictions become typed links plus
a gap entry; they are never silently overwritten.

**`kb.py`** — markdown notes with YAML front-matter on disk, one directory per
note type, plus `GAPS.md` as the attention ledger. Confidence is computed on read
from `base_confidence`, `half_life_days`, and `last_reinforced` — never stored.

**`learning/`** — `decay` (runs at the start of every run), `gaps` (thin evidence,
orphans, contradictions, decayed notes → priority-ordered ledger, and
`run --from-gaps` lets the KB pick its own next target), `calibration` (hit/miss
per source → learned promotion threshold), `reconcile` (resolve a contradiction or
record it as an open tension).

**`cli.py`** — `edu init | sources | run | compile | gaps | review | reconcile |
lint | ask | status`.

## Testing

`pytest`, with a `FakeLLM` returning canned structured outputs and the hashing
embedder. The end-to-end test runs the full four-stage pipeline over
`examples/corpus/` with no network and no API key, and asserts notes land in a
temp `kb/`. That test is the template's proof that the skeleton actually runs.

## Out of scope (documented in `docs/extending.md`)

Cross-topic analogies, note recombination, project spawning from an opportunity
note, the standards directory that regulates it, and a TUI. Each is described as
an extension of the same graph, with the hook it would attach to.
