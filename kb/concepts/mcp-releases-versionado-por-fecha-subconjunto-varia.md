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
updated: '2026-09-25'
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
- release-cadence
- release-engineering
- versionado
- versionado-por-fecha
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-versionado-por-fecha
  type: supports
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: supports
- to: mcp-release-2026-8-31-bumps
  type: derived_from
- to: mcp-release-stub-sin-changelog
  type: relates_to
---

## What it is
Los documentos de release del ecosistema MCP usan versionado por fecha (YYYY.MM.DD) y, en cada release, bumpean solo un subconjunto de paquetes en lugar del conjunto completo. El subconjunto rota: paquetes presentes en un release faltan en el siguiente y reaparecen después.

## Evidence
- Release 2025.11.25: server-sequential-thinking, server-everything, server-filesystem, server-memory, mcp-server-git — source: 16a4e3995d6c827e
- Release 2025.12.18: server-sequential-thinking, server-everything, server-filesystem, mcp-server-git — source: 2221814efbefaa3b
- Release 2026.1.14: subconjunto menor, solo server-everything, server-filesystem y mcp-server-git — source: 748f8b0a02cd7524
- Release 2026.1.26: server-everything, server-memory y mcp-server-time; introduce mcp-server-time y omite filesystem y git respecto a releases adyacentes — source: b9106690f5dfd849
- Release 2026.7.4: server-everything, server-filesystem, server-sequential-thinking y server-memory — source: ffbd76916d1dfdc5
- Release 2026.7.10: server-filesystem, mcp-server-time, mcp-server-fetch y mcp-server-git; introduce mcp-server-fetch — source: 5a4df6bef0a4905f
- Release 2026.8.18: server-everything, mcp-server-time, mcp-server-fetch y mcp-server-git — source: 9750590bbfe6b285
- Release 2026.8.31: server-filesystem, server-memory, server-sequential-thinking y server-everything — source: 30a26335a9988ba2
- server-memory aparece en 2025.11.25 y 2025.12.18 pero falta en 748f8b0a02cd7524, 5a4df6bef0a4905f y 9750590bbfe6b285: la línea de paquetes no es monótona — source: 16a4e3995d6c827e

## Why it matters
Permite describir la serie como un calendario de bumps, no como un producto con historial acumulativo. Cualquier inferencia sobre madurez, adopción o capacidades del ecosistema a partir de estos documentos excede lo que los documentos dicen.

`derived_from` la nota del release 2026.8.31, que es el caso fechado de la señal. `relates_to` el patrón de release stubs sin changelog, porque ambos describen el mismo formato documental.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
- derived_from → [[mcp-release-2026-8-31-bumps]]
- relates_to → [[mcp-release-stub-sin-changelog]]
