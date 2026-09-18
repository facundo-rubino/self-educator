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
updated: '2026-09-18'
sources:
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
- ffbd76916d1dfdc5
tags:
- mcp
- release-engineering
- release-notes
- versionado
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-versionado-por-fecha
  type: relates_to
- to: mcp-servers-sin-changelog-legible
  type: relates_to
- to: mcp-release-stubs-como-artefacto-de-feed
  type: supports
---

## What it is
En el conjunto de notas de release de MCP servers de referencia, la lista de paquetes incluidos cambia de release a release: server-memory desaparece en 2025.12.18 y 2026.1.14; server-sequential-thinking y server-memory faltan en 2026.7.10 y 2026.8.18; server-filesystem falta en 2026.1.26; mcp-server-git falta en 2026.8.18 y 2026.8.31. La lista de paquetes es, por tanto, una variable, no un roster fijo.

## Evidence
- Release v2025.11.25 lista server-sequential-thinking, server-everything, server-filesystem, server-memory y mcp-server-git — source: 16a4e3995d6c827e
- Release v2025.12.18 lista server-sequential-thinking, server-everything, server-filesystem y mcp-server-git; server-memory cae — source: 2221814efbefaa3b
- Release v2026.1.14 lista server-everything, server-filesystem y mcp-server-git, sin server-memory — source: 748f8b0a02cd7524
- Release v2026.1.26 lista server-everything, server-memory y mcp-server-time; faltan server-filesystem y mcp-server-git — source: b9106690f5dfd849
- Release v2026.7.10 introduce mcp-server-time y mcp-server-fetch y omite server-memory y server-sequential-thinking — source: 5a4df6bef0a4905f
- Release v2026.7.4 lista server-everything, server-filesystem, server-sequential-thinking y server-memory, sin mcp-server-git ni time/fetch — source: ffbd76916d1dfdc5
- Release v2026.8.18 lista server-everything, mcp-server-time, mcp-server-fetch y mcp-server-git, sin filesystem, memory ni sequential-thinking — source: 9750590bbfe6b285
- Release v2026.8.31 lista solo filesystem, memory, sequential-thinking y everything; mcp-server-git ausente — source: 30a26335a9988ba2

## Why it matters
Un roster cambiante impide leer una lista de release como inventario estable de paquetes mantenidos. Cualquier inferencia sobre deprecaciones, adopción o roadmap a partir de estas listas necesita una regla explícita de qué significa «ausente» — y la evidencia no la provee. La única lectura defendible es que el conjunto de paquetes listados por release es variable.

Se relaciona con `mcp-servers-versionado-por-fecha` (mismo corpus, misma cadencia date-versioned) y con `mcp-servers-sin-changelog-legible` (si no hay changelog, la lista de paquetes es el único campo y aun así varía). Es evidencia de apoyo para `mcp-release-stubs-como-artefacto-de-feed`: si el roster varía sin rationale, el clúster se lee como salida de feed, no como hallazgo.

## Links
- relates_to → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
