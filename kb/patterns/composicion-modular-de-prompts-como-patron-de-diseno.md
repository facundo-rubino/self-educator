---
id: composicion-modular-de-prompts-como-patron-de-diseno
title: La composición modular de prompts como patrón de diseño de tooling de agentes
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-12'
updated: '2026-10-12'
sources:
- abf61eeec75462f9
tags:
- prompt-engineering
- agentes
- diseno
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
---

## What it is
La idea de componer las instrucciones de un agente a partir de muchos fragmentos condicionales pequeños en lugar de un prompt monolítico. Es una intuición genérica de ingeniería (separación de concerns) que el clúster de Claude Code ejemplifica, pero no demuestra como hallazgo sobre un sistema concreto.

## Evidence
- El clúster sugiere la composición de instrucciones de agente a partir de fragmentos condicionales pequeños como patrón a estudiar para quien construye tooling de agentes — source: abf61eeec75462f9

## Why it matters
Unidades condicionales chicas son más fáciles de estimar, testear y reordenar que un monolito, lo cual conecta con secuenciamiento y alcance en liderazgo técnico. Pero el valor del patrón no depende de que Claude Code lo use: es una heurística general, y este clúster no añade evidencia de que funcione mejor.

Deriva del claim sobre Claude Code como caso citado. Refuerza el patrón ya existente de ensamblado condicional de prompts y se relaciona con la nota que trata el system prompt como artefacto de ingeniería.

## Links
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
