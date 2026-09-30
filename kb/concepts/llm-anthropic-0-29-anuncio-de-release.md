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
updated: '2026-09-30'
sources:
- 31820ad25e39a34b
tags:
- anthropic
- cli
- llm
- llm-anthropic
- llm-cli
- release
- release-note
- releases
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-09-30'
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
- to: modelo-nuevo-en-cli-habilita-sin-demostrar-mejora
  type: relates_to
- to: llm-anthropic-0-29-singleton-sin-corroboracion
  type: supports
- to: llm-anthropic-0-29-topic-match-espurio-por-vocabulario
  type: supports
- to: feed-de-dependencias-no-es-evidencia-de-practica-profesional
  type: relates_to
- to: claude-opus-5-5-identificador-no-verificable
  type: supports
- to: llm-anthropic-0-29-singleton-sin-corroboracion
  type: relates_to
- to: llm-anthropic-0-29-topic-match-espurio-por-vocabulario
  type: relates_to
- to: llm-anthropic-0-29-contenido-solo-operativo-sin-claims-sobre-practica
  type: relates_to
---

## What it is
La release 0.29 del plugin `llm-anthropic` agrega soporte para invocar el modelo `claude-opus-5.5` desde la CLI de `llm`, con la forma `llm -m claude-opus-5.5 "prompt goes here"` [31820ad25e39a34b]. El documento es un anuncio de integración y versionado de tooling: declara compatibilidad con un identificador de modelo y aporta los tags `llm` y `anthropic` [31820ad25e39a34b].

## Evidence
- La release 0.29 de llm-anthropic agrega soporte para Claude Opus 5.5, invocable vía `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El documento está etiquetado con los tags `llm` y `anthropic`, y proviene de un feed RSS con engagement=0 — source: 31820ad25e39a34b

## Why it matters
Es el único contenido verificable del clúster: una capacidad de acceso a un modelo desde terminal, sin benchmark, latencia, costo ni calidad de código generado [31820ad25e39a34b]. No contiene afirmaciones sobre liderazgo técnico, docencia, estimación, secuenciamiento, productividad ni técnicas de estudio.

Se relaciona con el resto del clúster `llm-anthropic 0.29`, que documenta que este changelog no aporta claims sobre práctica (`llm-anthropic-0-29-contenido-solo-operativo-sin-claims-sobre-practica`), que es un singleton sin corroboración (`llm-anthropic-0-29-singleton-sin-corroboracion`) y cuyo match con el topic es léxico por vocabulario `llm`/`anthropic` (`llm-anthropic-0-29-topic-match-espurio-por-vocabulario`).

## Links
- supports → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- contradicts → [[claude-opus-5-5-identificador-no-verificable]]
- supports → [[modelo-nuevo-en-cli-habilita-sin-demostrar-mejora]]
- supports → [[release-de-plugin-no-es-evidencia-de-practica]]
- relates_to → [[modelo-nuevo-en-cli-habilita-sin-demostrar-mejora]]
- supports → [[llm-anthropic-0-29-singleton-sin-corroboracion]]
- supports → [[llm-anthropic-0-29-topic-match-espurio-por-vocabulario]]
- relates_to → [[feed-de-dependencias-no-es-evidencia-de-practica-profesional]]
- supports → [[claude-opus-5-5-identificador-no-verificable]]
- relates_to → [[llm-anthropic-0-29-singleton-sin-corroboracion]]
- relates_to → [[llm-anthropic-0-29-topic-match-espurio-por-vocabulario]]
- relates_to → [[llm-anthropic-0-29-contenido-solo-operativo-sin-claims-sobre-practica]]
