---
id: claude-code-system-prompt-conditional-composition
title: El system prompt de Claude Code se ensambla de partes condicionales
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- agentic-coding
- claude-code
- prompt-architecture
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: supports
- to: prompt-modular-sin-mecanica-verificable
  type: contradicts
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
---

## What it is
Un documento reporta que el código fuente filtrado de Claude Code muestra que su system prompt se ensambla a partir de decenas de partes condicionales. Es la única afirmación sustantiva disponible en el clúster: no se especifican qué condiciones, qué partes, cómo se secuencian ni cómo se verificó el «filtrado». El contenido de la nota se limita a ese claim, sin mecanismo verificable.

## Evidence
- «El código fuente filtrado de Claude Code muestra que su system prompt se ensambla a partir de decenas de partes condicionales» — source: abf61eeec75462f9

## Why it matters
Si la modularidad condicional del prompt fuera real y estuviera publicada, un dev que lidera y enseña podría adoptar el patrón para sus propias instrucciones de agentes (activar secciones de estimación, secuenciamiento o revisión de código según contexto). Pero el documento no extrae ninguna implicación de ese tipo, no hay corroboración independiente y la novedad es nula: es un patrón conocido en productos LLM. La confianza se fija en 0.05 porque, tras descartar la procedencia no establecida del leak y el patrón trivial de «prompt modular», lo que queda es una reformulación de conocimiento común con envoltorio anecdótico.

`supports` hacia `ensamblado-condicional-de-prompts`: es una instancia concreta del patrón general de componer el system prompt según contexto, aunque de baja calidad probatoria. `relates_to` con `system-prompt-como-artefacto-de-ingenieria`: ambos tratan el system prompt como objeto diseñado, no como texto improvisado. `contradicts` con `prompt-modular-sin-mecanica-verificable`: esa nota sostiene que la modularidad de prompts es plausible pero no verificable en esta evidencia, lo que choca con cualquier lectura de este documento como confirmación del mecanismo.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
