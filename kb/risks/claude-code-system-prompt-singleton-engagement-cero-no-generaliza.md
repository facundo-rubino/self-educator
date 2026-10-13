---
id: claude-code-system-prompt-singleton-engagement-cero-no-generaliza
title: 'Claude Code (system prompt): singleton con engagement cero no sostiene generalización
  sobre práctica de ingeniería'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-13'
sources:
- abf61eeec75462f9
tags:
- claude-code
- singleton
- engagement-cero
- generalizacion
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion
  type: supports
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: claude-code-cluster-un-solo-documento-engagement-cero
  type: relates_to
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: contradicts
---

## What it is
El clúster es un único ítem RSS [abf61eeec75462f9] con engagement=0 y novelty=0.00. Levantar desde ese material una generalización sobre cómo se construyen los system prompts de agentes de código de primera línea no está sostenido por el corpus.

## Evidence
- Clúster de un solo documento, engagement 0, novelty 0.00 — source: abf61eeec75462f9 (crítico)
- Sin corroboración real más allá del score 0.50 — source: abf61eeec75462f9

## Why it matters
Impide que "así se construyen los prompts en agentes frontera" entre como práctica establecida; a lo sumo es una hipótesis plausible sobre priors de la disciplina.

Refuerza las reglas ya compiladas `cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion` y `generalizacion-desde-cluster-de-un-solo-documento`, y se relaciona con `claude-code-cluster-un-solo-documento-engagement-cero`. Contradice la lectura como hallazgo del claim principal.

## Links
- supports → [[cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[claude-code-cluster-un-solo-documento-engagement-cero]]
- contradicts → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
