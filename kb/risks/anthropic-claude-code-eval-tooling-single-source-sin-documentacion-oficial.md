---
id: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
title: El tooling de evals de Claude Code descansa en una sola fuente secundaria,
  sin documentación oficial
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-07'
updated: '2026-11-07'
sources:
- 541b1e7161ae8f43
tags:
- evals
- single-source
- verificacion
- anthropic
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-11-07'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: contradicts
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: relates_to
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
---

## What it is
La afirmación de que `build_eval` y `hill-climb` existen y funcionan se sostiene en un post de reseña/opinión, no en documentación oficial de Anthropic ni en corroboración independiente (corroboration=0.50) [541b1e7161ae8f43].

## Evidence
- El documento es un post de reseña/opinión; los nombres y la función de los comandos descansan en una sola fuente secundaria — source: 541b1e7161ae8f43
- No hay verificación de que los comandos existan, funcionen como se describe ni de su alcance real — source: 541b1e7161ae8f43 (ausencia señalada en el análisis del clúster)

## Why it matters
Cualquier implicación práctica (definir «terminado» con evals, cambiar estimaciones) hereda este déficit de verificación. Mientras no haya fuente primaria, la nota de concepto debe leerse como reporte de tercero, no como capacidad establecida.

Contradice el uso fuerte de la nota de concepto: la misma evidencia que la funda es la que limita su confianza. Coincide en patrón con otras notas sobre documentos únicos que no sostienen claims de práctica.

## Links
- contradicts → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
