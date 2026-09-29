---
id: arquitectura-de-prompt-cambia-sin-aviso
title: La arquitectura de prompt de un producto comercial cambia sin aviso
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
- agents
- claude-code
- maintenance
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: datasette-alpha-features-no-son-settled
  type: relates_to
---

## What it is
Cualquier estructura de prompt inferida de un producto cerrado puede dejar de reflejar su diseño actual o futuro. La observación sería, en el mejor caso, una foto con fecha, no una propiedad estable de la herramienta.

## Evidence
- El documento no indica versión ni fecha del artefacto descrito — source: abf61eeec75462f9
- El informe señala que la arquitectura de prompt de un producto comercial puede cambiar sin aviso — source: abf61eeec75462f9

## Why it matters
Desaconseja construir flujos propios que dependan de esa estructura concreta: el objeto de estudio se mueve. También limita la vida útil de la lección de docencia basada en este caso.

Contradice la estabilidad implícita de `claude-code-system-prompt-conditional-composition` y comparte forma con `datasette-alpha-features-no-son-settled`: lo observado en un artefacto no asentado no es una base duradera.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[datasette-alpha-features-no-son-settled]]
