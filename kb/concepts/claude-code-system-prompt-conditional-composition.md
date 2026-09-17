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
updated: '2026-09-17'
sources:
- abf61eeec75462f9
tags:
- agentic-coding
- claude-code
- composicion-condicional
- leak
- prompt-architecture
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-17'
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
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
---

## What it is
Una fuente afirma que el system prompt de Claude Code no es una cadena estática única, sino el resultado de ensamblar docenas de partes condicionales — secciones que se activan o desactivan según contexto. El documento no especifica cuáles son esas condiciones ni cuántas partes hay. La afirmación es una descripción arquitectónica interna, no una capacidad documentada hacia el desarrollador.

## Evidence
- «Claude Code's leaked source shows a system prompt assembled from dozens of conditional parts» — source: abf61eeec75462f9 (documento único, sin corroboración; corroboration score 0.50, novelty 0.00).

## Why it matters
Si fuera cierto, el prompt de un agente de coding sería un artefacto componible y no un bloque monolítico, lo que abriría la puerta a razonar sobre control por secciones en lugar de sobre una instrucción única. Pero con esta evidencia la implicación es una extrapolación plausible, no un hallazgo: sin las condiciones de gating la afirmación no es falsable ni operable.

`ensamblado-condicional-de-prompts` ya registra el patrón general de composición condicional; esta nota sería una instancia concreta si la fuente especificara la mecánica. `system-prompt-como-artefacto-de-ingenieria` es el marco que esta observación apoyaría como caso. La laguna sobre qué condiciones gatean qué partes está registrada en `claude-code-source-leak-conditions-parts-unspecified`.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
