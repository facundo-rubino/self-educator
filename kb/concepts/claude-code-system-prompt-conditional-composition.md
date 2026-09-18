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
updated: '2026-09-18'
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
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-18'
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
---

## What it is
El system prompt de Claude Code no es un texto monolítico: se ensambla, según una filtración de su código fuente, a partir de docenas de partes condicionales. La composición dependería del contexto de ejecución, no de una redacción fija. La afirmación proviene de una única señal RSS sobre código filtrado.

## Evidence
- El system prompt de Claude Code se ensambla a partir de docenas de partes condicionales — source: abf61eeec75462f9
- La afirmación se basa en código fuente filtrado de Claude Code — source: abf61eeec75462f9
- El documento es de tipo RSS con engagement 0, sin corroboración independiente en el clúster — source: abf61eeec75462f9

## Why it matters
Si el patrón es real, la unidad de diseño de un agente no es «el prompt» sino el conjunto de bloques y sus condiciones de activación. Eso desplaza el trabajo de prompt engineering hacia composición y separación de responsabilidades, no hacia redacción. El valor informativo marginal es bajo (novedad 0.00): el ensamblado condicional ya es un patrón conocido en productos LLM.

Se relaciona con `ensamblado-condicional-de-prompts`, que generaliza el patrón más allá de Claude Code. Se relaciona con `claude-code-source-leak-conditions-parts-unspecified`: el reporte no especifica condiciones, partes ni secuenciación, lo que limita cualquier inferencia mecánica. Se relaciona con `leak-sin-autenticidad-establecida`: sin artefacto verificable no se confirma ni el leak ni la arquitectura descrita.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
