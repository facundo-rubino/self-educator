---
id: jev-herramientas-de-tooling-open-source-envejecen-rapido-conclusiones-fragiles
title: El churn del tooling open source hace frágiles las conclusiones específicas
  de herramienta
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-15'
updated: '2026-11-15'
sources:
- ee7d97417bb16595
- sig-ebbcc7fc0414
tags:
- jev
- churn
- herramientas
- fragilidad
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-11-15'
provenance:
  scale: S
  query: null
links:
- to: jev-seleccion-de-herramientas-como-cuello-de-botella
  type: derived_from
- to: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
  type: relates_to
- to: mcp-serie-2026-cadencia-de-releases-confirmada-sin-impacto-medido
  type: relates_to
---

## What it is
La encuesta de ~900 repos (ahora ~15K) implica que cualquier herramienta citada hoy puede volverse obsoleta pronto. Las conclusiones específicas de herramienta envejecen más rápido que los patrones.

## Evidence
- El ecosistema pasó de ~900 a ~15K repos según el survey, señal de churn alto — source: ee7d97417bb16595
- El crítico: «Tool survey churn (~900 repos, now ~15K) means specific tools cited today may be obsolete quickly, making tool-specific conclusions fragile» — source: sig-ebbcc7fc0414

## Why it matters
Un líder que fije recetas de herramienta desde este clúster construirá sobre arena. Vale más registrar el criterio de selección que el nombre del tool de moda.

Deriva de la lectura de selección como cuello de botella. Comparte mecanismo con la nota sobre el shelf-life corto del tooling de evals y con la cadencia MCP: los feeds y herramientas caducan, los patrones no.

## Links
- derived_from → [[jev-seleccion-de-herramientas-como-cuello-de-botella]]
- relates_to → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
- relates_to → [[mcp-serie-2026-cadencia-de-releases-confirmada-sin-impacto-medido]]
