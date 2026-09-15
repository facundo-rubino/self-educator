# Architecture

## The shape of the problem

A collector produces volume. A knowledge base needs judgement. Putting those two
things next to each other naively means paying a language model to read
everything, which is both the most expensive part of the job and the part
deterministic code does best.

The whole design follows from inverting that:

```
                      no LLM                    │            LLM
  ────────────────────────────────────────────  │  ─────────────────────────
  [1] ingest              [2] signal            │  [3] enrich    [4] compile
  hundreds of docs   →    a handful of scored   │  → reports  →  notes in kb/
                          clusters              │
```

Everything cheap happens before anything expensive. By the time a model is
involved, the corpus has already been reduced by one to two orders of magnitude,
which is what makes it affordable to treat each survivor carefully.

---

## Stage 1 — ingest

Every source implements one method:

```python
def fetch(self, query: str, *, limit: int, topic: str) -> list[Document]
```

and normalises whatever it ingests into `Document`. Nothing downstream ever asks
where a document came from, except to count distinct sources.

Two deliberate choices:

**`Document.source` is a plain string, not an enum.** Adding a source is a new
file plus a registry entry; the core never changes. In the project this template
came from, that field was an enum and adding a source meant editing three files.

**Sources are isolated.** A collector that raises is recorded as a run warning and
the run continues with what the others returned. Collectors break — upstream
changes a selector, an API rate-limits, a feed 503s — and a pipeline that loses
an entire run to one flaky source is not usable in practice.

Missing credentials are handled before the run, not during it: a source declares
`required_env`, and if any variable is absent the source excludes itself with a
warning. `edu sources` shows you this before you spend anything.

---

## Stage 2 — signal

This is where the volume dies, and it contains no model call.

**Embed.** Title plus a slice of body, through sentence-transformers if the `ml`
extra is installed, or a deterministic hashing embedder otherwise. The fallback
is not a toy: it captures lexical overlap, needs no download, and makes tests
reproducible.

**Cluster.** Greedy single-pass cosine against running centroids. No `k` to
choose. Swap it for HDBSCAN if your corpus justifies it — nothing downstream
depends on how the groups were formed.

**Score.** Each cluster gets a number in `[0,1]` from each registered scorer:

| Scorer | Question it answers |
|---|---|
| `velocity` | Is engagement accruing fast, or is this merely old and large? |
| `corroboration` | How many *independent* sources see this? |
| `novelty` | How different is this from everything previous runs covered? |
| `surprise` | How far does the best document beat the norm *for its own source*? |

Scorers are a registry, and `signal.weights` in config decides which run and how
much each counts. Two of them depend on engagement metrics; when a cluster's
documents carry none — an RSS-only corpus has no upvotes — they return a neutral
`0.5` rather than `0.0`. Scoring absence-of-data as absence-of-interest would
silently bury everything from sources that do not publish numbers.

`novelty` is the one with memory: it compares this cluster's centroid against a
rolling baseline of centroids from previous runs. That baseline is appended
*after* scoring, so a run never competes with itself.

**Promote.** Weighted sum, ranked, and the top *n* above the threshold are
promoted. If nothing clears the bar, the top signal is promoted anyway — on a
cold start, zero promotions means zero reports, zero notes, and zero calibration
data, so the learning loop would never start.

---

## Stage 3 — enrich

Two roles, one after the other.

The **analyst** reads the cluster's documents and drafts a report. Every
evidence claim must cite the `doc_id` it came from; nothing may come from the
model's own memory.

The **critic** then attacks that draft and returns an adjusted confidence. It is
a gate, not commentary: where it runs, its number is what the report carries
downstream, and a claim it judges weak is capped low no matter how confident the
analyst was.

The critic is skipped at scale XS, which is the honest trade — XS exists to show
you the flow for five cents, not to produce trustworthy output.

A `--query` different from the topic acts as a lens on interpretation, never as
a filter: by stage 3 the candidate set is already fixed, and letting a framing
phrase discard candidates would quietly narrow the pipeline to whatever you
already suspected.

---

## Stage 4 — compile

The reports are source code, the model is a compiler, `kb/SCHEMA.md` is the
language spec, and the note graph is the executable. Compile well and the graph
is fast and correct to read; compile badly and you get interconnected noise.

The model receives `SCHEMA.md` verbatim as its system prompt, the configured
note-type vocabulary, an index of every existing note, and the report. It
returns notes that either create a new id or reuse an existing one — and reusing
an existing id **merges**: sources and tags union, `last_reinforced` resets, the
original `base_confidence` is left alone. Confidence is a judgement about
evidence, not something a re-run should quietly inflate.

Note types are validated against config, so a hallucinated type fails loudly
rather than writing a file into a directory nobody reads.

**Contradictions are never resolved here.** A conflicting claim gets typed
`contradicts` links on both sides and registers a gap. The ruling happens later,
in `edu reconcile`, with both bodies of evidence in view. Deciding at write
time — with only the incoming report visible — systematically favours whatever
arrived most recently.

---

## The knowledge base

Markdown with YAML front-matter, one directory per note type, plus `GAPS.md`.
Plain files on purpose: the KB stays readable in an editor, diffable in git, and
openable in any markdown tool. The pipeline is not the only thing allowed to
touch it — you can edit a note by hand and the next run will merge into it.

Links are typed (`relates_to`, `derived_from`, `supports`, `contradicts`).
Front-matter is the source of truth; the `## Links` section mirrors them as
wikilinks so graph views can draw the edges, and is regenerated on every save.

**Confidence is computed, never stored.** A note has `base_confidence`,
`half_life_days` and `last_reinforced`; the live number is derived on read.
Storing it would mean the number is only correct on the day it was written.

---

## The learning loop

Four mechanisms, each closing a different feedback path:

**Decay** runs automatically at the start of every run. It is not a command
because it is not an action — it is a fact about elapsed time.

**Gaps** derives, from the current graph, what the KB does not know:
contradictions (0.9), decayed claims (0.7), thin evidence (0.5), orphans (0.4).
`edu run --from-gaps` takes the top one and ingests against it, so the KB
directs its own attention. The chosen gap is marked `investigating` so successive
runs move down the ledger instead of re-hitting the same hole.

**Calibration** is the loop most people skip and the one that makes the system
learn. Signals promoted more than `review_after_days` ago get judged — hit,
miss, or too early — and each source's hit rate maps onto a learned promotion
threshold. A source that keeps lying has to clear a higher bar; a reliable one
gets an easier ride. Below ten reviewed signals the learned value is noise, so
the configured cold-start threshold is used instead.

**Reconcile** rules on contradictions. The losing note is not deleted — its
confidence is halved and the reasoning is stamped into its body, because it may
still be right about something the winner did not cover. And `open_tension` is a
first-class outcome: two well-sourced notes that disagree can be the most
interesting thing in the graph.

---

## What each stage costs, and how to re-run it

| Stage | LLM | Persisted to | Re-run with |
|---|:---:|---|---|
| 1 ingest | no | `store/corpus/` | `edu run` |
| 2 signal | no | `store/signals/` | `edu run` |
| 3 enrich | yes | `store/reports/` | `edu run` |
| 4 compile | yes | `kb/` | `edu compile` |

Because every stage persists before the next begins, a run that dies halfway
leaves usable artifacts behind. `edu compile` exists because stage 4 is the one
you iterate on: it re-runs compilation over reports ingested weeks ago, without
touching the network or the analyst. Editing `SCHEMA.md` and re-compiling costs
a fraction of a full run.

The token budget is per run and enforced in the LLM client — the single place
every call passes through. When it is exhausted, `BudgetExceeded` stops the
current stage and the run reports what it completed, rather than failing whole.
