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
updated: '2026-11-23'
sources:
- 541b1e7161ae8f43
tags:
- agentes
- agentes-de-codigo
- anthropic
- claude-code
- evals
- graders
- single-source
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-23'
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
- to: eval-discipline-como-capa-de-medicion-del-trabajo-con-agentes
  type: relates_to
- to: anthropic-claude-code-eval-tooling-engagement-cero-sin-corroboracion
  type: supports
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: contradicts
- to: tooling-first-party-como-camino-a-estandarizacion-de-evals-hipotesis
  type: supports
---

## What it is
Anthropic publicó tooling de evaluación para Claude Code dentro del plugin `claude-api`, con los comandos `build_eval` y `hill-climb`. Según la única fuente, esos comandos sirven para construir evals, revisar graders y mejorar una aplicación contra ellos. Es un anuncio de producto, no un resultado medido: no hay benchmark, uso de terceros ni datos de adopción.

## Evidence
- Anthropic publicó nuevo tooling de evaluación para Claude Code — source: 541b1e7161ae8f43
- El plugin `claude-api` incluye `build_eval` y `hill-climb`, que ayudan a construir evals, revisar graders y mejorar una aplicación contra ellos — source: 541b1e7161ae8f43
- El autor trata una herramienta first-party de Anthropic como probablemente influyente en cómo los equipos hacen trabajo de eval — source: 541b1e7161ae8f43

## Why it matters
Un loop de eval first-party (`build_eval` + `hill-climb`) baja la barrera para tratar prompts y agentes como artefactos testeables. Para un dev que lidera y enseña, el detalle operativo útil es «revisar los graders»: la lógica de calificación es ella misma objeto de revisión, y de ahí se deriva disciplina de alcance y estimación. La evidencia disponible solo sostiene la existencia del anuncio, no su eficacia.

`contradicts` con `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad`: ese concepto trataba la evaluación por tarea como infraestructura establecida; aquí solo hay un anuncio sin verificación. `supports` con los riesgos de fuente única, engagement cero, vida útil corta del review y ausencia de documentación oficial, que juntos fijan la confianza baja. `relates_to` con el ciclo `build_eval`/`hill-climb` y con la disciplina de evals como capa de medición. `supports` con la hipótesis de que una herramienta first-party de Anthropic puede estandarizar cómo los equipos chicos escriben evals.

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
- relates_to → [[eval-discipline-como-capa-de-medicion-del-trabajo-con-agentes]]
- supports → [[anthropic-claude-code-eval-tooling-engagement-cero-sin-corroboracion]]
- contradicts → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- supports → [[tooling-first-party-como-camino-a-estandarizacion-de-evals-hipotesis]]
