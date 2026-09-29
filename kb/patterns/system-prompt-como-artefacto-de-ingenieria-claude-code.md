---
id: system-prompt-como-artefacto-de-ingenieria-claude-code
title: El system prompt como artefacto de ingeniería, ejemplificado en Claude Code
type: pattern
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
- agents
- engineering-craft
base_confidence: 0.55
half_life_days: 365
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: derived_from
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
---

## What it is
Instancia del patrón ya registrado: un system prompt de producción se versiona, se compone y se ensambla en runtime según señales de entorno, en lugar de ser un texto estático. El caso de Claude Code sirve de ilustración del encuadre, no de prueba.

## Evidence
- El ensamblado condicional descrito implica selección de bloques según contexto — source: abf61eeec75462f9
- La caracterización proviene de una fuente secundaria sobre un leak, sin código ni extracto — source: abf61eeec75462f9

## Why it matters
Refuerza la idea de que la estructura del prompt es una superficie de ingeniería presupuestable, aunque este clúster no aporte evidencia de que la inversión rinda. Útil como ejemplo, no como evidencia.

Deriva de `system-prompt-como-artefacto-de-ingenieria`, que ya recoge el encuadre, y aporta el caso concreto en `claude-code-system-prompt-conditional-composition`. El valor añadido es marginal: el patrón ya estaba en el grafo.

## Links
- derived_from → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
