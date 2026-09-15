# self-educator

A template for a specific shape of program: **ingest sources, filter the noise
cheaply, research what survives, and compile the result into a knowledge base
that improves run over run.**

It runs the moment you clone it — offline, with no API key — over a small
example corpus. Then you point it at your own sources and your own subject.

```
sources/*  →  [1] ingest      Document[]        deterministic, no LLM
              [2] signal      Signal[]          cluster + score + promote, no LLM
              [3] enrich      Report[]          analyst + critic, LLM, budgeted
              [4] compile     Notes in kb/      LLM, guided by kb/SCHEMA.md
```

## The idea

Most "ingest it into an LLM" pipelines spend their money in the wrong place:
they hand raw documents to a model and ask it to find what matters. That is the
most expensive possible way to do the cheapest part of the job.

This flow inverts it. **Stages 1 and 2 contain no LLM call at all.** Hundreds of
ingested documents are clustered and scored by deterministic rules — how fast
engagement is accruing, how many independent sources see it, how different it is
from everything previous runs already covered, how far it beats the norm for its
own source. Only the handful that clear the promotion bar cost a model call.

What reaches the LLM is small, so you can afford to treat it properly: an
analyst drafts a report where every claim cites the document it came from, and
a critic attacks it and adjusts the confidence downward if it does not survive.

Then the surviving reports are **compiled** into a graph of markdown notes.
Compiled, not appended: an incoming report is decomposed into atomic ideas, and
each idea is integrated into the note that already owns it. The reports are the
source code, the model is the compiler, `kb/SCHEMA.md` is the language spec, and
the note graph is the executable.

Around that sits a loop that makes the next run better than the last:

- **Decay.** Every note carries a half-life. Confidence is computed on read, so
  a note nobody has reinforced in six months is visibly weaker than one from
  last week — without anyone maintaining it.
- **Gaps.** The KB derives its own list of what it does not know: contradictions,
  thin evidence, orphans, decayed claims. `edu run --from-gaps` lets the KB
  choose the next target instead of you.
- **Calibration.** Signals promoted weeks ago get re-judged: hit, miss, or too
  early. Each source's track record moves the promotion bar. A source that
  keeps lying has to clear a higher one, automatically.
- **Reconcile.** Contradictions are never overwritten at write time. They are
  recorded and ruled on later, with both bodies of evidence in view — and
  "both stand, and the disagreement is the finding" is a valid ruling.

## Quick start

```bash
uv sync --group dev      # Python 3.13 + dependencies
uv run pytest -q         # 83 tests, all offline
uv run edu init          # create kb/ from the note types in config.yaml
uv run edu sources       # which sources will run, and why the others will not
uv run edu status        # what is in the KB, and what to do next
```

Stages 1 and 2 need no credential. For stages 3 and 4:

```bash
cp .env.example .env     # then add your ANTHROPIC_API_KEY
uv run edu run --scale XS   # ~$0.07 — the cheapest way to see the whole flow
```

Optionally `uv sync --extra ml` for real sentence-transformer embeddings. Without
it a deterministic hashing embedder keeps everything working — less precise, and
it never blocks you on a torch install.

## Commands

| Command | What it does |
|---|---|
| `edu init` | Create one `kb/` directory per note type in `config.yaml`. |
| `edu sources` | Which sources are active, and why the others are excluded. |
| `edu run` | The full pipeline. `--scale XS…XL` is the cost lever; `--from-gaps` lets the KB pick the target. |
| `edu compile` | Re-run **only** stage 4 over stored reports. No ingestion, no enrichment. |
| `edu gaps` | The attention ledger: what the KB does not know, ranked. |
| `edu review` | Calibration — judge old promoted signals, adjust the promotion bar. |
| `edu reconcile` | Rule on the graph's open contradictions. |
| `edu lint` | Broken links, orphans, duplicate titles, decayed notes. Exits non-zero, so CI can gate on it. |
| `edu status` | Current state, and a suggested next step. |
| `edu ask "..."` | Query the KB. It answers only from the notes, or says it cannot. |

Every command that costs money previews the cost before spending it; `L` and
`XL` ask for confirmation.

## Scale — the cost lever

| Scale | docs/source | sources | top signals | critic | token budget |
|-------|------------:|--------:|------------:|:------:|-------------:|
| XS | 50 | 1 | 1 | – | 5,000 |
| S | 150 | 2 | 3 | ✓ | 20,000 |
| M | 400 | 3 | 6 | ✓ | 60,000 |
| L | 1,000 | 4 | 12 | ✓ | 150,000 |
| XL | 3,000 | 6 | 25 | ✓ | 400,000 |

These are starting points, not truths. Tune them in `config.py` for your sources.

## Making it yours

Two files, in this order:

1. **`config.yaml`** — the topic, the note types your subject actually needs,
   the sources to ingest, the scoring weights.
2. **`kb/SCHEMA.md`** — the compiler's system prompt. This is the single
   highest-leverage file in the project: it decides how every note gets written.

Adding a source means copying `self_educator/sources/_template.py`; it does not
mean editing the core. Adding a note type means adding four lines to
`config.yaml`. See **[ADAPTING.md](ADAPTING.md)** for the full checklist.

## Layout

```
config.yaml            what to ingest, and the note-type ontology
kb/                    the knowledge base (the output)
  SCHEMA.md            the compiler contract — edit this
  GAPS.md              the attention ledger (generated)
store/                 documents, signals, reports (regenerable, gitignored)
runs/                  one directory per run, with its summary
examples/corpus/       sample documents, so it runs with no network
self_educator/
  config.py models.py storage.py llm.py kb.py pipeline.py cli.py
  sources/             ingest      — files, rss, web_api, _template.py
  signal/              scoring     — embedder, cluster, scorers, engine
  enrich/              research    — analyst, critic
  synthesis/           compilation — compiler
  learning/            the loop    — decay, gaps, calibration, reconcile
docs/                  architecture.md, extending.md
```

## Documentation

- **[ADAPTING.md](ADAPTING.md)** — "I want to ingest X into a KB": the checklist.
- **[docs/architecture.md](docs/architecture.md)** — how the four stages fit, and why.
- **[docs/extending.md](docs/extending.md)** — extensions of the same graph:
  cross-topic analogies, note recombination, spawning a project from a note.

## Origin

Extracted from TrendFisher/TrendBrain, a working trend-intelligence system, by
lifting the flow out of its domain. Anything that was specific to that subject
is now configuration.
