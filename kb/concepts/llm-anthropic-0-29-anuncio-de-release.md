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
updated: '2026-09-29'
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
last_reinforced: '2026-09-29'
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
---

## What it is
La versión 0.29 de `llm-anthropic`, el plugin de acceso a modelos de Anthropic para el CLI `llm`, anuncia soporte para un modelo invocable con `llm -m claude-opus-5.5 "prompt goes here"` [31820ad25e39a34b]. El documento es un changelog operativo de librería: registra un cambio de versión y una etiqueta de modelo, no una afirmación sobre práctica de ingeniería [31820ad25e39a34b].

## Evidence
- `llm-anthropic` 0.29 añade soporte para el modelo 'Claude Opus 5.5', usable vía `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El documento está etiquetado `llm` y `anthropic`: es un release de una herramienta de acceso a modelos, no material sobre ingeniería, liderazgo ni docencia — source: 31820ad25e39a34b

## Why it matters
El único contenido verificable es que un modelo nuevo queda disponible a través de una herramienta ya existente. El documento no dice nada sobre calidad del modelo, costo, latencia, ni sobre cómo un dev-líder o docente debería cambiar su flujo de trabajo; cualquier inferencia de ese tipo es especulación del analista, no del documento [31820ad25e39a34b].

Se relaciona con `llm-anthropic-0-29-singleton-sin-corroboracion` (el mismo artefacto leído como fuente única sin corroboración independiente) y con `llm-anthropic-0-29-topic-match-espurio-por-vocabulario` (el motivo por el que este documento entró al brief: coincidencia de tags `llm`/`anthropic`, no de contenido). También conecta con `modelo-nuevo-en-cli-habilita-sin-demostrar-mejora`: la clase general a la que pertenece este ítem.

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
