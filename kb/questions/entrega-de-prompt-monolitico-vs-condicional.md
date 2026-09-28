---
id: entrega-de-prompt-monolitico-vs-condicional
title: 'Prompt monolítico frente a prompt condicional: diferencia sin efecto medido'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- abf61eeec75462f9
tags:
- prompting
- system-prompt
- evals
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: supports
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: prompts-no-portables-entre-agentes-por-ensamblado-condicional
  type: relates_to
---

## What it is
El documento afirma que el prompt se compone de «docenas de partes condicionales» [abf61eeec75462f9], pero no establece ninguna diferencia funcional frente a un prompt monolítico: ni latencia, ni calidad, ni coste, ni facilidad de mantenimiento. La pregunta que el brief necesitaría responder —si esa estructura cambia el resultado o solo la organización interna— queda sin datos.

## Evidence
- «a system prompt assembled from dozens of conditional parts» — source: abf61eeec75462f9

## Why it matters
Para un dev que lidera y enseña, la modularidad del prompt solo importa si es inspeccionable, versionable y testeable. Sin un efecto medido ni una mecánica descrita, la distinción es vocabulario, no práctica. Esta nota no sostiene ninguna recomendación de diseño de agentes.

Deriva de `claude-code-system-prompt-conditional-composition` como su consecuencia pendiente. `restatement-de-titulo-como-evidencia-de-composicion-condicional` la respalda al señalar que la descripción es genérica; `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes` sería la prueba necesaria para responderla.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- supports → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- relates_to → [[prompts-no-portables-entre-agentes-por-ensamblado-condicional]]
