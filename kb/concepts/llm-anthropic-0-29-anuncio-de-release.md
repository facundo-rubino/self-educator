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
updated: '2026-09-25'
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
last_reinforced: '2026-09-25'
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
---

## What it is
El documento anuncia la release `llm-anthropic 0.29`, que añade soporte para el modelo «Claude Opus 5.5» en la CLI `llm` de Simon Willison. El uso documentado es el comando `llm -m claude-opus-5.5 "prompt goes here"` [31820ad25e39a34b].

## Evidence
- El documento anuncia la release llm-anthropic 0.29 con soporte para el modelo «Claude Opus 5.5» — source: 31820ad25e39a34b
- El uso documentado es `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El ítem está etiquetado `llm` y `anthropic`, lo que lo ubica en el ecosistema de herramientas CLI — source: 31820ad25e39a34b

## Why it matters
Habilita invocar un modelo adicional desde la misma CLI sin cambiar de herramienta, para quien ya usa `llm` en scripts o prototipado. No es evidencia de mejora en la forma de trabajar: el documento prueba que existe un comando, no que el modelo sea mejor para ninguna tarea.

Contradice a `claude-opus-5-5-identificador-no-verificable`: el anuncio afirma la existencia del identificador pero el nombre no corresponde a ningún modelo público conocido. Se relaciona con `modelo-nuevo-en-cli-habilita-sin-demostrar-mejora`, que generaliza este patrón.

## Links
- supports → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- contradicts → [[claude-opus-5-5-identificador-no-verificable]]
- supports → [[modelo-nuevo-en-cli-habilita-sin-demostrar-mejora]]
- supports → [[release-de-plugin-no-es-evidencia-de-practica]]
- relates_to → [[modelo-nuevo-en-cli-habilita-sin-demostrar-mejora]]
