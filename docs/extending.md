# Extending the pattern

The four stages plus the learning loop are the template. This file describes
extensions that were deliberately left out — each is a real mechanism from the
system this was extracted from, described here with the hook it attaches to, so
you can build the ones your subject actually needs.

They share a premise: **once the knowledge is a typed graph with confidence and
provenance, it is a substrate you can run more things on.** The collector was
never the interesting part.

---

## Cross-topic analogies

**The idea.** When you run the pipeline over two unrelated subjects, the most
valuable connection is not thematic — it is structural. "The same mechanism, in
a different skin." Those edges are knowledge no collector can give you, because
neither corpus contains the comparison.

**How it works.** Take notes of your cross-cutting type (the `pattern` type in
the shipped config) from two different topics, and ask the model whether any pair
shares a *structural* match — not a shared subject, but the same causal shape.
Every proposal goes through the critic before it is written; this is the stage
most prone to producing confident nonsense, because a sufficiently abstract
description makes any two things look alike. Survivors become an
`analogous_to` link.

**Hook.** A new `LinkType.analogous_to` in `models.py`, a module under
`learning/`, and a call from `pipeline.run_pipeline` gated on scale — it only
makes sense once you have material from more than one topic.

**Watch out for.** Analogies proposed without a gate will read as brilliant and
be worthless. Require the model to state *why* the structures match, not just
that they do, and reject anything that would still sound plausible with the
nouns swapped.

---

## Recombination

**The idea.** Cross pairs of notes that are semantically *distant but not alien*
and ask for an idea that exists only because both notes exist. Too similar and
there is no leap; too far apart and there is no bridge. The productive band in
the original system was roughly 0.25–0.60 cosine.

**How it works.** Embed every note, take the pairwise similarity matrix, exclude
pairs already linked in the graph, keep the ones inside the band, and ask for one
idea per pair. Critic gate, then manual approval before anything is written —
this is generative, and generative output does not belong in a sourced KB
without a human deciding.

**Hook.** A `learning/recombine.py` using `signal.embedder`, plus a command that
prints candidates and writes only the ones you approve.

**Watch out for.** Ideas that would have occurred to you without reading either
note. That is the test: if it is generic, it is noise wearing the costume of
insight.

---

## Spawning a project from a note

**The idea.** Some notes are not knowledge, they are a proposal — something you
could go build or investigate. Turning one into a self-contained working
directory (a plan, the constraints, a phased roadmap with acceptance criteria)
makes the KB an input to work rather than an archive of it.

**How it works.** Pick a note, pull its one-hop neighbourhood as context, and
generate a directory containing an instruction file for whoever picks it up plus
notes on approach, structure and phases. Stamp the source note with a link so
the KB remembers what has already become a project.

**Hook.** A module that reads the KB and writes outside it, plus a `spawned`
link type that `lint` knows to exempt from its broken-link check, since it points
out of the graph.

**Watch out for.** Letting the model invent the standards. See the next section.

---

## A standards directory

**The idea.** If you generate plans, the technical decisions should not be
whatever the model felt like today. Keep your own conventions in a directory of
markdown — one file of principles that always applies, plus one per kind of work
— and prepend the relevant ones to the generation prompt.

**Why it is worth the file.** It moves your standards from "re-explained in every
prompt, slightly differently" to one version-controlled place. The model is asked
to work *within* them and to justify any departure explicitly, rather than to
decide from scratch each time.

**Hook.** A loader that reads the directory and a prompt section that pins the
constraints ahead of the task. Seed it with editable starters — a blank page
gets skipped, a wrong-but-concrete file gets fixed.

---

## An interactive interface

**The idea.** The commands map onto a workflow, and a workflow is easier to learn
by walking it than by reading `--help`. A terminal UI organised by stage — where
the home screen reads the KB's state and tells you what to do next — turns the
pipeline into something you can explore.

**Hook.** Textual, one screen per stage, over the same functions the CLI calls.
`edu status` already computes the "what next" logic; a UI is a different
presentation of it, not new behaviour.

**Watch out for.** Business logic drifting into the UI. Everything a screen does
should be a call into `pipeline`, `actions` or `learning`, so the CLI and the UI
cannot disagree about what a command means.

---

## Smaller extensions worth knowing about

**More link types.** The four shipped types are generic graph semantics. A
domain may want `supersedes`, `implements`, `cites`. Add to `LinkType` and teach
`lint` and `reconcile` what each means — an edge nothing reasons about is
decoration.

**A different embedder.** `signal/embedder.py` is a `Protocol`. Anything with
`.embed(list[str]) -> np.ndarray` works, including a hosted embedding API.

**A different clusterer.** `signal/cluster.py` takes vectors and returns groups
of indices. Nothing downstream cares how the groups were formed.

**Multiple knowledge bases.** Every command takes `--root`. Separate directories
give separate `kb/`, `store/` and `config.yaml`. Wrap it in a shell alias, or add
a registry that resolves a name to a path.

**Scheduling.** `edu run --from-gaps --scale S -y` is designed to be run
unattended: the KB picks the target, the scale caps the spend, and `-y` skips
confirmation. Pair it with a periodic `edu review` so calibration keeps up.
