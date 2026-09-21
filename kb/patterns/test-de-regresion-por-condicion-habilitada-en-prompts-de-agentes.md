---
id: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
title: Regresión de prompts de agente por condición habilitada, no una sola vez
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- agentes
- prompts
- testing
- regresion
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
---

## What it is
Si el prompt se ensambla por partes condicionales, su comportamiento varía según las condiciones habilitadas (herramientas, entorno, modo). La consecuencia operativa es testear el prompt a través de esas condiciones en cada cambio, en lugar de validarlo una sola vez.

## Evidence
- El prompt se describe como ensamblado de docenas de partes condicionales, lo que implica comportamiento dependiente de la condición — source: abf61eeec75462f9
- No hay en el cluster lista de condiciones, matriz de casos ni resultado de regresión — source: abf61eeec75462f9

## Why it matters
Afecta la estimación y secuenciación del trabajo de agentes: la superficie de prueba crece con el número de condiciones y hay que reservar presupuesto para mantenerla. La evidencia sostiene el diseño de la prueba, no su eficacia medida, que no está en este cluster.

Deriva del concepto sobre el ensamblado condicional del prompt de Claude Code y se apoya en el system prompt como artefacto de ingeniería. Converge con la evaluación específica por tarea como infraestructura de fiabilidad y topa con el límite ya registrado: la modularidad del prompt no tiene mecánica verificable en esta evidencia.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
