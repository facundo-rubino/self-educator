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
updated: '2026-09-28'
sources:
- 31820ad25e39a34b
tags:
- anthropic
- cli
- llm
- llm-cli
- release
- release-note
- releases
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-09-28'
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
---

## What it is
El documento [31820ad25e39a34b] es una nota de release del plugin `llm-anthropic`, versión 0.29, que añade soporte para un modelo de Anthropic en la CLI `llm`. No contiene relato de práctica, ni metodología, ni medición: es un bump de versión con un identificador de modelo.

## Evidence
- El documento es el anuncio de release de `llm-anthropic 0.29`, un bump de versión de plugin — source: 31820ad25e39a34b
- El release añade soporte para un modelo denominado `Claude Opus 5.5`, invocado como `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El documento está etiquetado `llm` y `anthropic`, lo que lo sitúa en el ecosistema de tooling de CLI para LLMs, no en una discusión de práctica de ingeniería — source: 31820ad25e39a34b

## Why it matters
Lo único que establece es que un identificador de modelo nuevo pasó a estar disponible en un plugin de CLI ya existente: una opción de tooling incremental, no un cambio de método para programar, gestionar o enseñar. Cualquier consecuencia práctica se limita a poder seleccionar ese modelo en `llm`.

Es un ítem de feed de dependencias, y como tal se apoya en `feed-de-dependencias-no-es-evidencia-de-practica-profesional`. Ejemplifica el patrón `modelo-nuevo-en-cli-habilita-sin-demostrar-mejora`: habilita un flujo, no demuestra mejora. Su condición de singleton con novelty 0.00 y engagement 0 sostiene `llm-anthropic-0-29-singleton-sin-corroboracion`, y su encaje temático por vocabulario (`llm`, `anthropic`) sostiene `llm-anthropic-0-29-topic-match-espurio-por-vocabulario`. El identificador del modelo queda soportado como ítem de evidencia en `claude-opus-5-5-identificador-no-verificable`.

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
