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
updated: '2026-11-13'
sources:
- 541b1e7161ae8f43
tags:
- anthropic
- claude-code
- corroboracion
- evals
- fuente-unica
- single-source
- verificacion
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-11-13'
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
- to: corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso
  type: supports
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
---

## What it is
La existencia y el alcance de `build_eval` y `hill-climb` provienen de un único documento de feed RSS, sin enlace a documentación oficial de Anthropic ni a un artefacto primario. El resumen del documento está truncado («...likely to influence how»), por lo que el alcance real de la herramienta y sus limitaciones no están descritos. Cualquier afirmación sobre capacidades más allá de «existen estos comandos» sería especulación.

## Evidence
- Toda la evidencia sobre `build_eval` y `hill-climb` proviene de un solo doc_id — source: 541b1e7161ae8f43
- El resumen del documento está truncado en la frase sobre influencia — source: 541b1e7161ae8f43

## Why it matters
Antes de citar esta feature en configuración de equipo o material de docencia hay que verificarla contra upstream (changelog del plugin, repositorio o docs de Anthropic). Un comando de plugin no documentado oficialmente puede no existir con ese nombre en la versión instalada.

Deriva del concepto principal del tooling. Comparte con `documento-unico-sin-engagement-no-sostiene-claim-sobre-practica` el patrón general: un solo documento no sostiene afirmaciones de práctica.

## Links
- contradicts → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- supports → [[corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso]]
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
