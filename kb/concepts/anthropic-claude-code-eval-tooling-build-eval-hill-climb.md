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
updated: '2026-11-07'
sources:
- 541b1e7161ae8f43
tags:
- evals
- claude-code
- anthropic
- tooling
- single-source
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-07'
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
---

## What it is
Un documento único reporta que el plugin `claude-api` de Anthropic incorpora comandos `build_eval` y `hill-climb` para construir evals, verificar los graders y mejorar la aplicación contra ellos [541b1e7161ae8f43]. El autor declara que normalmente no reseña herramientas de evaluación por su corta vida útil, pero que una herramienta first-party de Anthropic probablemente influya en cómo se hace este trabajo [541b1e7161ae8f43].

## Evidence
- Anthropic publicó nuevo tooling de evaluación para Claude Code — source: 541b1e7161ae8f43
- El plugin `claude-api` incluye los comandos `build_eval` y `hill-climb` para construir evals, revisar los graders y mejorar la aplicación contra ellos — source: 541b1e7161ae8f43
- El autor evita reseñar herramientas de eval por su corta vida útil, pero considera que una herramienta first-party de Anthropic influirá en la práctica — source: 541b1e7161ae8f43

## Why it matters
Si se adopta, construir y verificar evals pasaría de tarea posterior a parte del ciclo de trabajo con agentes de código, desplazando la validación del output de «revisar a ojo» a graders ejecutables. Es una hipótesis del analista, no un resultado del documento [541b1e7161ae8f43].

Se relaciona con las notas sobre evals por tipo de tarea como criterio de aceptación de salidas: ambas tratan la evaluación explícita como infraestructura, pero aquí sin metodología ni datos de eficacia. Los riesgos de fuente única y de alcance quedan en notas separadas.

## Links
- relates_to → [[evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- supports → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- supports → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
