---
id: anthropic-claude-code-eval-tooling-build-eval-hill-climb
title: 'Tooling de evaluación de Anthropic para Claude Code: `build_eval` y `hill-climb`
  en el plugin `claude-api`'
type: concept
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
- agentes
- agentes-de-codigo
- anthropic
- claude-code
- evals
- single-source
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-17'
provenance:
  scale: S
  query: null
links:
- to: evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas
  type: relates_to
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
  type: supports
- to: anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia
  type: supports
- to: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
  type: derived_from
- to: anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia
  type: derived_from
- to: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
  type: derived_from
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
  type: supports
- to: build-eval-y-hill-climb-como-ciclo-de-mejora-iterativa-contra-graders
  type: relates_to
---

## What it is
Anthropic publicó, según un único post de blog, tooling de evaluación para Claude Code dentro de un plugin `claude-api` con dos comandos: `build_eval` para construir evals y `hill-climb` para verificar los graders y mejorar la aplicación contra ellos. El post no describe el mecanismo, los límites, el coste ni la fiabilidad de ninguno de los dos comandos.

## Evidence
- Anthropic lanzó tooling de evaluación para Claude Code con comandos `build_eval` y `hill-climb` en el plugin `claude-api`, para construir evals, chequear graders y mejorar la aplicación contra ellos — fuente: 541b1e7161ae8f43
- El autor declara que no suele reseñar herramientas de evaluación por su corta vida útil, pero que una herramienta first-party de Anthropic probablemente influya en cómo se hacen las evals — fuente: 541b1e7161ae8f43
- El post se interrumpe justo en la frase sobre la influencia esperada; no incluye benchmarks, comparaciones ni resultados medidos — fuente: 541b1e7161ae8f43

## Why it matters
Si el tooling fuera real y funcionara como se describe, bajaría el coste de montar evals para agentes de código: un dev que usa agentes para programar podría exigir graders y medir mejoras en vez de confiar en demos. La descripción existente no permite verificar esa utilidad.

`build-eval-y-hill-climb-como-ciclo-de-mejora-iterativa-contra-graders` describe el mismo ciclo en abstracto a partir de esta misma fuente. `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad` es el concepto general de evals como capa de fiabilidad al que este tooling se adscribiría si existiera evidencia de su funcionamiento. `anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial` registra el riesgo de descansar en una sola fuente secundaria sin documentación oficial.

## Links
- relates_to → [[evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- supports → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- supports → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- derived_from → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- supports → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
- relates_to → [[build-eval-y-hill-climb-como-ciclo-de-mejora-iterativa-contra-graders]]
