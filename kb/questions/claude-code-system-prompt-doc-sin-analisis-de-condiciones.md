---
id: claude-code-system-prompt-doc-sin-analisis-de-condiciones
title: 'Qué condiciones gatean qué secciones en Claude Code: sin observación directa'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- abf61eeec75462f9
tags:
- claude-code
- prompt-engineering
- pregunta-abierta
base_confidence: 0.4
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
---

## What it is
El clúster afirma que el system prompt está hecho de partes condicionales, pero no enumera las condiciones, las partes ni la secuencia de ensamblado. La observación directa está ausente.

## Evidence
- abf61eeec75462f9 no especifica qué condiciones gatean qué secciones.
- El crítico señala que el contenido sustantivo es genérico y no discrimina sobre Claude Code (transcript del reporte).

## Why it matters
Sin las condiciones y las partes, no se puede inventariar el flujo de ensamblado para revisión de código o triaje de incidentes, que era el ángulo práctico propuesto por el analista.

Se relaciona con `claude-code-condiciones-que-gatean-secciones-sin-observar` y `claude-code-source-leak-condiciones-parts-unspecified`, notas ya existentes sobre la misma laguna, y con `claude-code-system-prompt-conditional-composition`.

## Links
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
