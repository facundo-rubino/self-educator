---
id: mcp-roster-de-paquetes-varia-entre-releases
title: El roster de paquetes bumpeados varía entre releases de MCP servers
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
tags:
- mcp
- release-engineering
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-versionado-por-fecha
  type: relates_to
- to: mcp-servers-sin-changelog-legible
  type: relates_to
---

## What it is
El conjunto de paquetes incluido en cada release de MCP servers no es fijo. Recurrentemente aparecen filesystem, everything, sequential-thinking, memory, git, time y fetch, pero cada release incluye un subconjunto distinto sin explicación del criterio [30a26335a9988ba2][5a4df6bef0a4905f][748f8b0a02cd7524][9750590bbfe6b285][b9106690f5dfd849].

## Evidence
- `v2026.8.31` incluye filesystem, memory, sequential-thinking y everything — source: 30a26335a9988ba2
- `v2026.7.10` incluye filesystem, time, fetch y git — source: 5a4df6bef0a4905f
- `v2026.1.14` incluye server-everything, server-filesystem y mcp-server-git — source: 748f8b0a02cd7524
- `v2026.8.18` incluye server-everything, mcp-server-time, mcp-server-fetch y mcp-server-git — source: 9750590bbfe6b285
- `v2026.1.26` lista solo everything, memory y time — source: b9106690f5dfd849

## Why it matters
La ausencia de un paquete en una release no puede leerse como deprecación: el roster simplemente varía. Cualquier inferencia sobre el estado de un paquete a partir de una sola release es inválida.

Se relaciona con `mcp-servers-versionado-por-fecha` y `mcp-servers-sin-changelog-legible`: las tres son propiedades observadas del mismo corpus de release notes, ninguna sostiene conclusiones sobre el tema del brief.

## Links
- relates_to → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
