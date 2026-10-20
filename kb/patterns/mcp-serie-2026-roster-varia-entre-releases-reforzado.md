---
id: mcp-serie-2026-roster-varia-entre-releases-reforzado
title: El roster de paquetes MCP varía entre releases de la serie 2026
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 30a26335a9988ba2
- 9750590bbfe6b285
- 5a4df6bef0a4905f
- ffbd76916d1dfdc5
- b9106690f5dfd849
- 748f8b0a02cd7524
tags:
- mcp
- release
- packaging
- patron
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: supports
- to: mcp-servers-versionado-por-fecha
  type: derived_from
---

## What it is
En los seis releases de la serie 2026, el subconjunto de paquetes bumpeados cambia de un release a otro: 2026.8.31 toca filesystem/memory/sequential-thinking/everything; 2026.8.18 toca everything/time/fetch/git; 2026.7.10 toca filesystem/time/fetch/git; 2026.7.4 toca everything/filesystem/sequential-thinking/memory; 2026.1.26 toca everything/memory/time; 2026.1.14 toca everything/filesystem/git.

## Evidence
- Release 2026.8.31: filesystem, memory, sequential-thinking, everything — source: 30a26335a9988ba2
- Release 2026.8.18: everything, time, fetch, git — source: 9750590bbfe6b285
- Release 2026.7.10: filesystem, time, fetch, git — source: 5a4df6bef0a4905f
- Release 2026.7.4: everything, filesystem, sequential-thinking, memory — source: ffbd76916d1dfdc5
- Release 2026.1.26: everything, memory, time — source: b9106690f5dfd849
- Release 2026.1.14: everything, filesystem, git — source: 748f8b0a02cd7524

## Why it matters
Indica que no todos los paquetes se publican en cada fecha; un equipo que quiera fijar versiones debe revisar release por release qué paquete se movió, no asumir un pin único global.

Soporta y refuerza la nota previa `mcp-roster-de-paquetes-varia-entre-releases`, que ya registraba la variación con menos releases. Deriva del patrón de versionado por fecha `mcp-servers-versionado-por-fecha`.

## Links
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
- derived_from → [[mcp-servers-versionado-por-fecha]]
