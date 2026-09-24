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
updated: '2026-09-24'
sources:
- abf61eeec75462f9
tags:
- evidencia-circular
- evidencia-debil
- metodo
- patron
- prompt-engineering
- restatement
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-09-24'
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
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: supports
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
---

## What it is
Cuando una fuente dice que un system prompt se compone de «decenas de partes condicionales» y no aporta ninguna parte, condición o versión, lo que se está repitiendo es la definición de un system prompt modular, no un hallazgo sobre un producto concreto. La regularidad: el restatement de una descripción genérica se presenta como evidencia y sobrevive al filtrado por parecer específico.

## Evidence
- La única afirmación del clúster es que el system prompt de Claude Code se ensambla de decenas de partes condicionales, según una filtración — source: abf61eeec75462f9
- El clúster tiene corroboración=0.50 y un único documento con engagement=0 — source: abf61eeec75462f9
- El crítico la clasifica como «non-finding»: descripción de la arquitectura de un producto propietario, sin validación independiente ni medición — source: abf61eeec75462f9

## Why it matters
Un dev que diseñe sus propios flujos con agentes obtiene de aquí solo la confirmación de algo ya sabido: los prompts de producto se componen por ramas. Confundir eso con evidencia sobre cómo se construye Claude Code infla el valor de la fuente y contamina el grafo con un `concept` que describe un mecanismo no observado.

Es un caso particular de `restatement-de-titulo-no-es-hallazgo`, aplicado al vocabulario de prompts condicionales. Se relaciona con `ensamblado-condicional-de-prompts` (el patrón real) y con `prompt-condicional-conocimiento-comun-en-productos-llm` (el patrón ya conocido en productos LLM). Sustenta `prompt-modular-sin-mecanica-verificable` y comparte método con `validacion-de-senal-por-contenido-no-por-titulo`.

## Links
- derived_from → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- supports → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
