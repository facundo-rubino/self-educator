---
id: prompt-condicional-conocimiento-comun-en-productos-llm
title: El prompt modular y condicional es un patrón conocido en productos LLM
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-30'
sources:
- abf61eeec75462f9
tags:
- agentes
- artefacto-de-ingesta
- llm
- novedad
- patrones
- patrones-llm
- prompt-engineering
base_confidence: 0.6
half_life_days: 180
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria
  type: supports
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: relates_to
---

## What it is
El «system prompt ensamblado de docenas de partes condicionales» (abf61eeec75462f9) es una descripción genérica de cualquier pipeline de prompt-engineering no trivial. Sería verdad de innumerables aplicaciones LLM, no solo de Claude Code.

## Evidence
- El documento abf61eeec75462f9 describe el system prompt de Claude Code como ensamblado de docenas de partes condicionales.
- La descripción no aporta información discriminante sobre Claude Code en particular: aplica a cualquier sistema de plantillas condicionales (abf61eeec75462f9, inferencia del crítico).

## Why it matters
Un claim que sería cierto de casi cualquier producto LLM no informa sobre el producto concreto. Enseñarlo como hallazgo sobre Claude Code propaga un modelo mental erróneo.

Refuerza el patrón `ensamblado-condicional-de-prompts` (la composición condicional como abstracción). Se relaciona con `restatement-de-titulo-como-evidencia-de-composicion-condicional` (circularidad) y con `claude-code-system-prompt-conditional-composition` (el mismo artefacto de ingesta).

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[ensamblado-condicional-de-prompts]]
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
