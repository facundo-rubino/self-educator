---
id: restatement-de-titulo-como-evidencia-de-composicion-condicional
title: '«Docenas de partes condicionales» no es hallazgo: es la descripción genérica
  del ensamblado de prompts'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-23'
sources:
- abf61eeec75462f9
tags:
- evidencia-circular
- prompt-engineering
- metodo
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: restatement-de-titulo-no-es-hallazgo
  type: derived_from
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: supports
---

## What it is
Que un system prompt se ensamble condicionalmente es cómo funciona cualquier aplicación LLM por capas, no algo que el documento haya establecido sobre Claude Code. Decir «docenas de partes condicionales» coincide léxicamente con vocabulario genérico de ingeniería de prompts; esa coincidencia no convierte la frase en evidencia sobre un producto concreto.

## Evidence
- Afirmar que Claude Code ensambla su prompt de «docenas de partes condicionales» es reformular cómo funciona el ensamblado condicional en cualquier aplicación LLM por capas, no un hallazgo — source: abf61eeec75462f9 (crítica del crítico sobre el clúster)
- El material no aporta código, método, mediciones, autoría ni verificación independiente que ancle la afirmación a Claude Code — source: abf61eeec75462f9

## Why it matters
Una generalidad que podría inferirse sin el documento no puede cargar el peso de «se sabe esto sobre Claude Code». Es el modo de fallo clásico de la evidencia circular: la afirmación se sostiene en su propio enunciado. Para un dev que lidera, la consecuencia es práctica: antes de copiar un supuesto patrón de un producto a propio agente, exigir el artefacto (config, diff, reproducción), no el titular.

`derived_from` la nota general sobre reformular un título como no-hallazgo: este es un caso instanciado. `relates_to` las notas sobre afirmar práctica desde ausencia de contenido en feeds y sobre la composición condicional de Claude Code. `supports` la nota sobre el prompt condicional como patrón conocido en productos LLM: confirma que la idea no es novedosa.

## Links
- derived_from → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
