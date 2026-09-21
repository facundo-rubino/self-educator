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
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentic-coding
- claude-code
- composicion-condicional
- filtracion
- leak
- prompt-architecture
- prompt-engineering
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-21'
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
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
---

## What it is
Claude Code ensambla su system prompt a partir de docenas de partes condicionales, según una fuente filtrada. El documento que lo afirma no aporta fragmentos citados del prompt, ni los disparadores condicionales nombrados, ni metodología de obtención del leak.

## Evidence
- El system prompt de Claude Code se describe como ensamblado a partir de docenas de partes condicionales, atribuido a fuente filtrada — source: abf61eeec75462f9
- El documento es el único miembro del clúster, con engagement=0, por lo que no existe corroboración independiente dentro de la señal — source: abf61eeec75462f9

## Why it matters
Si el diseño es real, el prompt deja de ser un bloque monolítico y pasa a ser una superficie de configuración con comportamiento dependiente de condiciones habilitadas (herramientas, entorno, modo). Eso implica que validar el prompt una sola vez no basta: habría que probarlo por condición. Para el brief, el uso correcto es como patrón didáctico y como hipótesis a testear, no como cita en documentación de equipo ni en currícula sobre cómo funciona Claude Code.

Es una instancia concreta del ensamblado condicional de prompts como patrón general, y coincide con la observación ya registrada de que el prompt modular y condicional es conocido en productos LLM. La pregunta sobre el leak de Claude Code registra precisamente las condiciones y partes no especificadas que faltan aquí. Se relaciona con el riesgo de sobre-generalizar el diseño de Claude Code a agentes propios y con el riesgo de que la modularidad de prompts sea plausible pero no verificable en esta evidencia.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
