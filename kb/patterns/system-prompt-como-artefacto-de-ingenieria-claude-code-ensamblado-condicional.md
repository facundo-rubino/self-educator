---
id: system-prompt-como-artefacto-de-ingenieria-claude-code-ensamblado-condicional
title: 'El system prompt como artefacto de ingeniería: el caso Claude Code como ejemplo
  condicional'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- abf61eeec75462f9
tags:
- prompts
- ingenieria
- claude-code
- composicion
base_confidence: 0.15
half_life_days: 365
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: supports
- to: ensamblado-condicional-de-prompts
  type: supports
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: derived_from
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: contradicts
---

## What it is
El system prompt de un producto LLM es tratado como artefacto de ingeniería compuesto por partes que se activan condicionalmente según contexto, en lugar de un bloque estático único. El clúster ofrece Claude Code como ejemplo de este patrón, aunque el ejemplo concreto provenga de una fuente no verificada.

## Evidence
- «Claude Code's system prompt is assembled from dozens of conditional parts rather than being a single static block», atribuido a «leaked source». — source: abf61eeec75462f9
- El documento es un ítem RSS con engagement=0, sin corroboración independiente. — source: abf61eeec75462f9

## Why it matters
Si el patrón se sostiene, el artefacto a revisar no es «el prompt» sino la matriz de condiciones que deciden qué se inyecta. Eso cambia cómo se depura («¿qué capa no se activó?») y cómo se versiona. Pero en este clúster el patrón llega sin mecánica verificable: solo el enunciado de que existen partes condicionales.

Refuerza (`supports`) `system-prompt-como-artefacto-de-ingenieria` y `ensamblado-condicional-de-prompts`, ambos ya existentes en el grafo. Hereda su base de `claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente` (un solo documento, sin artefacto). Contradice `restatement-de-titulo-como-evidencia-de-composicion-condicional`: decir «hay docenas de partes condicionales» sin mostrar ninguna es reformulación, no hallazgo.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- supports → [[ensamblado-condicional-de-prompts]]
- derived_from → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- contradicts → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
