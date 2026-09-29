---
id: claude-code-system-prompt-sin-datos-de-eficacia
title: El ensamblado condicional no viene acompañado de datos de eficacia
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- abf61eeec75462f9
tags:
- prompt-engineering
- evidence-quality
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: mejora-de-rendimiento-sin-delta-post-cambio
  type: relates_to
- to: composicion-condicional-de-prompts-ensenable-a-principiantes
  type: relates_to
---

## What it is
El claim describe una arquitectura, no un resultado. No hay ningún dato que muestre que el ensamblado condicional produzca mejores resultados que un prompt monolítico, ni en qué tareas ni con qué coste.

## Evidence
- El clúster no aporta ninguna medición, comparación ni delta de rendimiento — source: abf61eeec75462f9
- La única evidencia es una descripción estructural de una fuente secundaria sobre un leak — source: abf61eeec75462f9

## Why it matters
Sin delta medido, presupuestar tiempo de ingeniería en «estructura de prompt» como superficie de trabajo es una apuesta de fe. El encuadre pedagógico de `composicion-condicional-de-prompts-ensenable-a-principiantes` queda sin respaldo de eficacia.

Contradice la utilidad práctica que se atribuye a `claude-code-system-prompt-conditional-composition` e instancia el patrón ya registrado en `mejora-de-rendimiento-sin-delta-post-cambio`: una afirmación estructural sin «after» cuantificado no es un resultado establecido.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[mejora-de-rendimiento-sin-delta-post-cambio]]
- relates_to → [[composicion-condicional-de-prompts-ensenable-a-principiantes]]
