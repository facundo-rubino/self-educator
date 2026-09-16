---
id: ensamblado-condicional-de-prompts
title: 'Ensamblado condicional de prompts: componer el system prompt según contexto'
type: pattern
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
- system-prompt
- prompt-architecture
- pattern
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: derived_from
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
---

## What it is
Patrón de diseño de agentes donde el system prompt no se escribe una vez sino que se ensambla en tiempo de ejecución a partir de bloques activados por condiciones: contexto del repo, fase de la tarea, herramientas disponibles. El objetivo declarado es precisión y menos ruido en la respuesta.

## Evidence
- Adoptar system prompts modulares y condicionales (por contexto de repo, por fase de tarea, por herramientas disponibles) en lugar de un prompt único podría mejorar la precisión de las respuestas y reducir ruido — source: abf61eeec75462f9
- El diseño de prompts en herramientas serias de agentes es un problema de ingeniería de software (composición, condiciones, mantenibilidad), no solo de escribir bien inglés — source: abf61eeec75462f9

## Why it matters
Reencuadra el trabajo de prompt sobre agentes como trabajo de composición: qué bloques existen, qué los activa, cómo se evita que se contradigan entre sí, cómo se testean. Es el punto donde el oficio de software engineering entra de lleno en el diseño de agentes.

Deriva de `system-prompt-como-artefacto-de-ingenieria`: el artefacto es el ensamblador, no el texto. Se relaciona con `claude-code-system-prompt-conditional-composition` como su ejemplo inspirador y con `prompt-modular-sin-mecanica-verificable` como su límite actual: el patrón es razonable, pero la evidencia mecánica todavía no existe.

## Links
- derived_from → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
