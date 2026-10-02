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
updated: '2026-10-02'
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
last_reinforced: '2026-10-02'
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
`llm-anthropic` 0.29 es una nota de release del plugin que conecta la CLI `llm` con modelos de Anthropic. La versión añade soporte para un modelo identificado en el propio release como «Claude Opus 5.5», invocable con `llm -m claude-opus-5.5 "prompt goes here"`.

## Evidence
- La versión 0.29 del plugin `llm-anthropic` añade soporte para un modelo llamado «Claude Opus 5.5», invocable vía `llm -m claude-opus-5.5 "prompt goes here"` — source: 31820ad25e39a34b
- El documento está etiquetado con las categorías `llm` y `anthropic` y proviene de un feed RSS — source: 31820ad25e39a34b

## Why it matters
Habilita, para quien ya usa la CLI `llm`, apuntar a un modelo de Anthropic más sin cambiar de herramienta. No hay en el documento ningún claim sobre calidad del modelo, coste, latencia ni adecuación a ninguna tarea.

Es la evidencia primaria (y única) del clúster; las notas de contenido-operativo y de singleton sin corroboración la toman como fuente. El match con el brief es el que registra `llm-anthropic-0-29-topic-match-espurio-por-vocabulario`.

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
