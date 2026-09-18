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
updated: '2026-09-18'
sources:
- abf61eeec75462f9
tags:
- agentes
- novedad
- patrones
- patrones-llm
- prompt-engineering
base_confidence: 0.6
half_life_days: 180
last_reinforced: '2026-09-18'
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
---

## What it is
La composición del system prompt a partir de partes condicionales no es un hallazgo nuevo: es una práctica establecida en productos LLM. El reporte lo registra explícitamente como novedad 0.00 respecto de la práctica de agentes. El caso de Claude Code sería una instancia del patrón, no su origen.

## Evidence
- El reporte califica la novedad del ensamblado condicional de prompts como 0.00: el patrón ya es conocido en la práctica de agentes — source: abf61eeec75462f9
- El system prompt de Claude Code se ensambla de partes condicionales según una filtración — source: abf61eeec75462f9

## Why it matters
Desplaza la pregunta de «¿existe este patrón?» a «¿cómo se gobierna?»: versionado, revisión y testeo de bloques condicionales pasan a ser el problema real. Un dev que construye agentes no necesita justificar la modularidad; necesita decidir qué bloques existen y cómo se testean.

Sostiene a `ensamblado-condicional-de-prompts` como patrón y a `system-prompt-como-artefacto-de-ingenieria` como consecuencia de gobernanza. Se relaciona con `claude-code-system-prompt-conditional-composition` como caso particular dentro del patrón general.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[ensamblado-condicional-de-prompts]]
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
