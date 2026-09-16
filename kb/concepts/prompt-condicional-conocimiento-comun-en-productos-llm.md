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
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- prompt-engineering
- patrones-llm
- novedad
base_confidence: 0.6
half_life_days: 180
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: supports
---

## What it is
En productos LLM, la composición modular y condicional del prompt es un patrón casi universal: esquemas de tool-use, capas de rol, inyección de contexto. Que un system prompt concreto se ensamble por partes condicionales no aporta novedad por sí mismo; la novedad estaría en las condiciones y partes específicas, que aquí no se detallan.

## Evidence
- «El claim (“prompt modular y condicional”) es un patrón conocido en productos LLM» — source: abf61eeec75462f9

## Why it matters
Fija la línea base contra la que medir el claim: sin condiciones ni partes concretas, el dato no distingue este sistema de cualquier otro producto LLM. Impide confundir la coincidencia léxica («decenas de partes condicionales») con evidencia de que este system prompt haga eso.

`relates_to` `claude-code-system-prompt-conditional-composition`: es el contexto que le quita novedad a ese claim. `supports` `ensamblado-condicional-de-prompts`: el patrón general ya está en el grafo y este documento no lo modifica.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[ensamblado-condicional-de-prompts]]
