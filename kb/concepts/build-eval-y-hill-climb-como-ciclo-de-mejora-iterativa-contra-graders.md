---
id: build-eval-y-hill-climb-como-ciclo-de-mejora-iterativa-contra-graders
title: '`build_eval` y `hill-climb` como ciclo de mejora iterativa contra graders'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-13'
updated: '2026-11-17'
sources:
- 541b1e7161ae8f43
tags:
- agentes
- agentes-de-codigo
- ciclo-de-mejora
- evals
- graders
- hill-climb
base_confidence: 0.25
half_life_days: 180
last_reinforced: '2026-11-17'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
---

## What it is
El anuncio describe implícitamente un ciclo de dos fases: `build_eval` construye el conjunto de evaluación y `hill-climb` mejora la aplicación contra los graders ya verificados. El ciclo completo —construir eval, verificar el grader, mejorar contra él— es la estructura descrita, sin detalles mecánicos ni resultados.

## Evidence
- El tooling anunciado incluye comandos para construir evals, chequear los graders y mejorar la aplicación contra ellos — fuente: 541b1e7161ae8f43
- El post se corta antes de aportar mecanismos, benchmarks o resultados — fuente: 541b1e7161ae8f43

## Why it matters
Un ciclo formalizado de "construir eval → verificar grader → mejorar contra él" es la abstracción mínima que hace verificable el trabajo con agentes de código. La fuente solo nombra los comandos y el propósito; no demuestra que el ciclo funcione.

`anthropic-claude-code-eval-tooling-build-eval-hill-climb` es la nota-madre con la descripción del plugin y los comandos. `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad` es la capa conceptual a la que este ciclo pertenece.

## Links
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
