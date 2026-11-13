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
updated: '2026-11-13'
sources:
- 541b1e7161ae8f43
tags:
- evals
- hill-climb
- graders
- agentes
base_confidence: 0.25
half_life_days: 180
last_reinforced: '2026-11-13'
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
El reporte describe una secuencia: construir la eval (`build_eval`), verificar que los graders puntúan correctamente, y mejorar la aplicación iterando contra esos graders (`hill-climb`). Esta secuencia tiene la forma clásica de un ciclo de verificación antes de escalar, aplicado al output de un agente de código. El documento no detalla cómo se implementan los graders ni cómo se mide la mejora entre iteraciones.

## Evidence
- `build_eval` construye evals y `hill-climb` mejora la aplicación iterando contra los graders — source: 541b1e7161ae8f43
- El flujo incluye verificar los graders además de construir la eval — source: 541b1e7161ae8f43

## Why it matters
Es la única idea transferible del clúster: la disciplina de definir el criterio de aceptación (el grader) y verificar el criterio antes de iterar. Esa estructura es independiente de Claude Code y de su plugin; la herramienta solo la hace más barata si los comandos existen y se mantienen.

Deriva del concepto del tooling. Se relaciona con `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad` por la idea de evals por tarea como capa de fiabilidad, y con `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes` por el uso de tests para gobernar cambios en un agente.

## Links
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
