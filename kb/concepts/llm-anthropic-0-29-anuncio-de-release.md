---
id: llm-anthropic-0-29-anuncio-de-release
title: 'llm-anthropic 0.29: anuncio de release que añade un modelo de Anthropic a
  la CLI de `llm`'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-23'
sources:
- 31820ad25e39a34b
tags:
- llm
- anthropic
- cli
- release
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: a-chain-reaction-metricas-no-son-evidencia-independiente
  type: supports
- to: mcp-servers-sin-changelog-legible
  type: relates_to
- to: claude-opus-5-5-identificador-no-verificable
  type: contradicts
---

## What it is
Un documento único del feed RSS de Simon Willison anuncia la release 0.29 del plugin `llm-anthropic`, que agrega soporte para un modelo etiquetado como `claude-opus-5.5`, invocable desde la CLI con `llm -m claude-opus-5.5 "prompt goes here"`. El documento está tagueado `llm` y `anthropic`, lo que lo ubica en la familia de herramientas de línea de comandos para modelos de Anthropic. No contiene análisis, discusión ni afirmación alguna sobre prácticas de ingeniería, liderazgo, estimación o docencia.

## Evidence
- Se publica la release 0.29 del plugin `llm-anthropic`, que agrega soporte para un modelo identificado como Claude Opus 5.5, invocable con `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El documento está tagueado como `llm` y `anthropic` — source: 31820ad25e39a34b
- Clúster de un solo documento con engagement=0: sin corroboración independiente ni discusión observada — source: 31820ad25e39a34b

## Why it matters
Habilita, pero no demuestra, la posibilidad de invocar ese modelo desde scripts y flujos automatizados de terminal. Para el brief —agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico de equipos chicos, oficio y productividad— el aporte se limita a un dato operativo de disponibilidad de herramienta. No hay ninguna afirmación sobre estimación, secuenciamiento, alcance, organización personal, liderazgo de equipos chicos ni técnicas de estudio; cualquier inferencia sobre mejores prácticas es especulativa respecto a esta evidencia.

Se apoya en la observación general de que las métricas de un singleton RSS son autodescripción del pipeline y no corroboración externa, porque aquí el único dato de engagement disponible es 0. Se relaciona con la ausencia de changelogs legibles en releases de servidores/herramientas de agentes: este anuncio sí nombra la versión y el paquete, pero no aporta rationale ni notas de comportamiento. Contradice —o más bien queda suspendido frente a— la nota sobre la verificabilidad del identificador `claude-opus-5.5`: la plausibilidad del nombre del modelo es una duda abierta, no un hecho resuelto en ninguna de las dos direcciones.

## Links
- supports → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- contradicts → [[claude-opus-5-5-identificador-no-verificable]]
