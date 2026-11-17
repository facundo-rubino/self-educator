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
updated: '2026-11-17'
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
last_reinforced: '2026-11-17'
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
Todo lo afirmado sobre el tooling de evals de Anthropic proviene de un solo post de blog, truncado, sin documentación oficial enlazada. No hay segunda fuente en el clúster ni referencia a la documentación de Anthropic que confirme la existencia o el comportamiento de `build_eval` y `hill-climb`.

## Evidence
- El clúster contiene un único documento sobre el tema — fuente: 541b1e7161ae8f43
- La corroboración reportada por el pipeline es 0.50 y la novedad 0.00 — fuente: 541b1e7161ae8f43
- El post está cortado antes de la tesis del autor y no incluye benchmark ni comparación — fuente: 541b1e7161ae8f43

## Why it matters
Cualquier recomendación operativa —adoptar `build_eval` como criterio de aceptación, enseñar el flujo, presupuestar tiempo de evals— descansaría sobre una fuente única no verificada. La verificación contra documentación oficial de Anthropic es requisito antes de cualquier uso.

`anthropic-claude-code-eval-tooling-build-eval-hill-climb` es la afirmación que este riesgo condiciona. `afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases` documenta el mismo modo de fallo: tomar un anuncio como evidencia de práctica.

## Links
- contradicts → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- supports → [[corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso]]
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
