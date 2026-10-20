---
id: ensamblado-condicional-de-prompts-no-es-evidencia-de-eficacia
title: 'Ensamblado condicional de prompts: arquitectura plausible, eficacia no demostrada'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- abf61eeec75462f9
tags:
- prompt-assembly
- efficacy
- evidence-gap
- agents
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: claude-code-system-prompt-sin-datos-de-eficacia
  type: supports
- to: ensamblado-condicional-no-implica-mejor-rendimiento
  type: relates_to
- to: overfitting-tematico-desde-mecanica-ajena
  type: relates_to
---

## What it is
Que un producto comercial de agentes de código componga su prompt condicionalmente no demuestra que esa composición mejore el rendimiento del agente. El clúster ofrece la descripción del mecanismo, no un delta medido.

## Evidence
- El ítem describe composición condicional sin reportar resultados de evaluación asociados. — source: abf61eeec75462f9
- La señal es de confianza 0.04 tras crítica: no hay base para afirmar eficacia. — source: abf61eeec75462f9

## Why it matters
Para un líder técnico es una palanca de productividad solo en hipótesis. Adoptar la maquinaria de selección de módulos sin medir puede costar más en depurabilidad de lo que ahorra.

`derived_from` el patrón `ensamblado-condicional-de-prompts`. `supports` la nota existente sobre ausencia de datos de eficacia. `relates_to` las notas sobre sobreajuste temático desde mecánica ajena y sobre ausencia de implicación de rendimiento.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- supports → [[claude-code-system-prompt-sin-datos-de-eficacia]]
- relates_to → [[ensamblado-condicional-no-implica-mejor-rendimiento]]
- relates_to → [[overfitting-tematico-desde-mecanica-ajena]]
