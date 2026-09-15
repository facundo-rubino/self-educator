# ADAPTING.md — "I want to ingest X and put it in a knowledge base"

A checklist, in the order that actually works. Steps 1–3 get you running; steps
4–6 are what make the output good.

---

## 1. Say what the KB is about

`config.yaml`:

```yaml
topic: "municipal water infrastructure"
```

This is the default search query and the `topic` on every note. One KB, one
subject — if you want two subjects, run two copies with separate `kb/` and
`store/` directories. Sharing a KB across unrelated subjects makes clustering
and novelty scoring worse, because both compare against everything.

---

## 2. Decide what a note *is* in your domain

This is the decision with the longest shadow, and it is worth twenty minutes
before you write any code. The shipped types (concept / pattern / actor /
question / risk) fit an open-ended research subject. Yours may not.

```yaml
kb:
  note_types:
    - name: regulation
      dir: regulations
      half_life_days: 730
      description: "A rule, statute or standard, and what it requires."
    - name: incident
      dir: incidents
      half_life_days: 365
      description: "A specific documented failure, with date and location."
    - name: mechanism
      dir: mechanisms
      half_life_days: 1095
      description: "A causal chain that recurs across incidents."
```

Three questions to test a proposed set:

- **Is each type a different *kind* of thing, or just a different topic?**
  "European regulations" and "US regulations" are one type with a tag. Split by
  kind, not by subject.
- **Would you ever want to read all notes of this type together?** If not, it is
  probably a tag rather than a type.
- **Does one type hold the connective tissue?** In most useful KBs one type is
  the cross-cutting one — the pattern, the mechanism, the recurring structure.
  Give it the longest half-life; those observations age slowest, and they are
  what make the graph worth more than the sum of its notes.

Then `edu init` creates the directories.

**On `half_life_days`:** ask how long a claim of this kind stays true without
anyone re-checking it. A statute: years. A market price: weeks. Confidence is
computed from this on every read, so getting it roughly right means stale notes
announce themselves instead of quietly misleading you.

---

## 3. Point it at your sources

Start with what needs no credentials.

**A local directory** — files you already have:

```yaml
sources:
  order: [files]
  files:
    paths: ["~/research/water-notes", "./exports"]
    extensions: [".md", ".txt", ".json"]
```

**Feeds** — anything with RSS/Atom:

```yaml
sources:
  order: [files, rss]
  rss:
    feeds:
      - https://example.gov/water/notices.rss
```

**Your own API or collector** — copy the template:

```bash
cp self_educator/sources/_template.py self_educator/sources/myapi.py
```

Rename the class, set `name`, implement `fetch`, then register it (add it to
`SOURCE_CLASSES` in `sources/__init__.py`, or call `register(MyAPISource)`) and
add its name to `sources.order`. Nothing downstream needs to change: clustering,
scoring, enrichment and compilation only ever see `Document`.

Check your work with `edu sources` before running anything.

Two things worth getting right in a new source:

- **`metrics`** — put whatever engagement numbers the source gives you (upvotes,
  comments, stars, views) in there. They feed the `velocity` and `surprise`
  scorers. If the source has none, leave it empty; those scorers return a
  neutral value rather than reading absence as zero interest.
- **`required_env`** — name the environment variables the source needs. A
  missing one excludes the source with a warning instead of killing the run.

---

## 4. Run the cheapest thing that shows you the whole flow

```bash
uv run edu run --scale XS      # ~$0.07
```

Then read `kb/` in any markdown editor. You are looking for one thing: **do
these notes read like something you would want to keep?** If not, that is a
`SCHEMA.md` problem, not a pipeline problem — go to step 5.

`edu run --scale XS` is also the right thing to re-run while iterating. When you
want to change *how notes are written* without re-ingestion, use `edu compile`:
it re-runs only stage 4 over the reports already on disk.

---

## 5. Tune the compiler contract

`kb/SCHEMA.md` is the system prompt for stage 4 — it is what actually decides
the shape and quality of your KB. Read it, then make it yours:

- Describe **your** note types under "Note types", in the model's terms.
- Add domain-specific rules. If your subject has a convention (always record the
  jurisdiction; always date an incident; never merge two statutes), say so
  there, explicitly.
- Keep the invariants the pipeline depends on: atomicity, mandatory sourcing,
  typed links, and never overwriting a contradiction. `edu lint` and
  `edu reconcile` both assume them.

Iterate: edit `SCHEMA.md`, run `edu compile`, read the diff in `kb/`. That loop
costs a fraction of a full run.

---

## 6. Tune the filter, once you have evidence

Do this **after** a few runs, not before — you need something to tune against.

**Weights** (`signal.weights`) shift what gets promoted:

- Chasing what is breaking now → raise `velocity`.
- Distrust single-source claims → raise `corroboration`.
- Drowning in things you already know → raise `novelty`.
- Looking for outliers rather than volume → raise `surprise`.

Weights are normalised, so they need not sum to 1.

**Thresholds:** `cluster_threshold` too low merges unrelated documents; too high
fragments one story into many clusters. `promotion_threshold` is only the
cold-start bar — once `edu review` has judged ten signals, the bar is learned
per source and this value stops being used.

**A new scorer** is a function and a decorator:

```python
from self_educator.signal.scorers import register, ScoringContext

@register("authority")
def authority(docs, ctx: ScoringContext) -> float:
    """Do these documents come from sources you consider authoritative?"""
    trusted = {"gov_registry", "peer_reviewed"}
    return len([d for d in docs if d.source in trusted]) / max(1, len(docs))
```

Then add `authority: 0.2` to `signal.weights`. A name in `weights` that is not
registered fails loudly — a silent typo there would change every ranking.

---

## 7. Close the loop

The pipeline only gets better if you run the loop, not just the pipeline:

```bash
uv run edu gaps         # what the KB knows it is missing
uv run edu run --from-gaps   # let it choose the next target
uv run edu reconcile    # rule on contradictions
uv run edu review       # weeks later: did the promoted signals hold up?
uv run edu lint         # graph health; exits non-zero for CI
```

`edu review` is the one people skip, and it is the one that makes the system
learn. Without it the promotion threshold never moves off its cold-start value
and the pipeline repeats its mistakes indefinitely.

---

## Common mistakes

| Symptom | Usual cause |
|---|---|
| Every cluster is one document | `cluster_threshold` too high, or too few documents per run |
| One giant cluster | `cluster_threshold` too low |
| Notes are vague and unsourced | `SCHEMA.md` was not adapted; the sourcing rule is not being enforced |
| Duplicate notes about one thing | The compiler is not being shown the existing index — check that `edu compile` sees your `kb/` |
| Nothing ever gets promoted | Cold-start promotes the top signal anyway; if you see none, stage 1 returned nothing — check `edu sources` |
| Everything scores identically | Your sources carry no `metrics`, so two of four scorers are neutral. Add metrics, or reweight toward `corroboration` and `novelty` |
| Confidence never decays | `half_life_days` is very large, or every run reinforces the same notes |
