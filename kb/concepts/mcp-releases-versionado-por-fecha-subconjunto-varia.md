---
id: mcp-releases-versionado-por-fecha-subconjunto-varia
title: Los releases MCP se versionan por fecha y el subconjunto de paquetes varía
  entre releases
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
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 9750590bbfe6b285
- b9106690f5dfd849
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 748f8b0a02cd7524
- ffbd76916d1dfdc5
tags:
- mcp
- release-engineering
- versionado
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-versionado-por-fecha
  type: supports
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: supports
---

## What it is
Cada nota de release del ecosistema MCP lleva un número de versión en formato fecha (p. ej. 2026.8.31) y ese mismo valor se aplica a todos los paquetes incluidos en ese release. El subconjunto de paquetes versionados conjuntamente no es fijo.

## Evidence
- Release 2026.8.31 actualiza server-filesystem, server-memory, server-sequential-thinking y server-everything con la misma versión 2026.8.31 — source: 30a26335a9988ba2
- Release 2026.7.10 aplica la versión única 2026.7.10 a server-filesystem, mcp-server-time, mcp-server-fetch y mcp-server-git — source: 5a4df6bef0a4905f
- Release 2026.8.18 versiona conjuntamente server-everything, mcp-server-time, mcp-server-fetch y mcp-server-git — source: 9750590bbfe6b285
- Release 2026.1.26 solo incluye server-everything, server-memory y mcp-server-time — source: b9106690f5dfd849
- Release 2025.11.25 lista cinco paquetes (server-sequential-thinking, server-everything, server-filesystem, server-memory, mcp-server-git) con versión 2025.11.25 — source: 16a4e3995d6c827e
- Release 2025.12.18 versiona server-sequential-thinking, server-everything, server-filesystem y mcp-server-git con 2025.12.18 — source: 2221814efbefaa3b
- Release 2026.1.14 incluye server-everything, server-filesystem y mcp-server-git con 2026.1.14 — source: 748f8b0a02cd7524
- Release 2026.7.4 versiona server-everything, server-filesystem, server-sequential-thinking y server-memory con 2026.7.4 — source: ffbd76916d1dfdc5

## Why it matters
Fija el hecho observable del corpus: versionado por fecha y composición de paquetes variable. No autoriza inferir qué cambió en cada paquete ni coordinar releases como hallazgo: el matching versión-paquete es definicional cuando el esquema ya es date-versioned.

Refuerza `mcp-servers-versionado-por-fecha` y `mcp-roster-de-paquetes-varia-entre-releases` con la serie completa de instancias. No se enlaza a `cadencia-de-release-unificada-sugiere-monorepo-mcp` como supports: la cadencia unificada es conducta esperada de un esquema de versionado único, no evidencia independiente de monorepo.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
