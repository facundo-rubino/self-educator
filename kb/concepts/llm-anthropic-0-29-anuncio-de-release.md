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
updated: '2026-09-24'
sources:
- 31820ad25e39a34b
tags:
- anthropic
- cli
- llm
- llm-cli
- release
- releases
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-09-24'
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
- to: modelo-nuevo-en-cli-habilita-sin-demostrar-mejora
  type: supports
- to: release-de-plugin-no-es-evidencia-de-practica
  type: supports
---

## What it is
El release 0.29 de `llm-anthropic`, plugin de la CLI `llm` de Simon Willison para modelos de Anthropic, añade soporte para un modelo etiquetado `claude-opus-5.5`. La invocación documentada es `llm -m claude-opus-5.5 "prompt goes here"`. El anuncio viene etiquetado `llm` y `anthropic`.

## Evidence
- La nota de release indica que 0.29 añade soporte para `Claude Opus 5.5`, invocable con `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El ítem está etiquetado `llm` y `anthropic`, lo que lo identifica como entrada de changelog del ecosistema de plugins de la CLI `llm` — source: 31820ad25e39a34b
- El documento es un aviso de release sin discusión de agentes de IA para programar, gestionar o enseñar, ni de liderazgo técnico, oficio o técnicas de estudio — source: 31820ad25e39a34b

## Why it matters
Es un hecho de disponibilidad de herramienta, no un hallazgo sobre práctica de ingeniería ni sobre cómo un dev-líder-docente trabaja mejor. A lo sumo es un input para futuras evaluaciones de flujos asistidos por IA; por sí mismo no demuestra ninguna mejora de productividad ni beneficio pedagógico.

`contradicts` con `claude-opus-5-5-identificador-no-verificable`: el identificador tomado verbatim del anuncio no tiene confirmación externa en este clúster. `supports` a `modelo-nuevo-en-cli-habilita-sin-demostrar-mejora` y a `release-de-plugin-no-es-evidencia-de-practica`, que describen exactamente la clase de inferencia que esta evidencia no permite hacer.

## Links
- supports → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- contradicts → [[claude-opus-5-5-identificador-no-verificable]]
- supports → [[modelo-nuevo-en-cli-habilita-sin-demostrar-mejora]]
- supports → [[release-de-plugin-no-es-evidencia-de-practica]]
