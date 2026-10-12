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
updated: '2026-10-12'
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
- packaging
- release-cadence
- release-engineering
- releases
- versionado
- versionado-por-fecha
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-10-12'
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
- to: mcp-servers-versionado-por-fecha
  type: derived_from
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: relates_to
- to: mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion
  type: relates_to
- to: mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia
  type: relates_to
---

## What it is
Los releases de los MCP servers de referencia usan versionado por fecha (p. ej. v2025.12.18, v2026.1.14, v2026.1.26, v2026.7.4, v2026.7.10, v2026.8.18, v2026.8.31) y cada release lista un subconjunto distinto de paquetes actualizados. El roster recurrente incluye server-filesystem, server-sequential-thinking, server-everything, server-memory, server-git, mcp-server-time y mcp-server-fetch, pero ningún release cubre los siete a la vez.

## Evidence
- v2025.12.18 lista sequential-thinking, everything, filesystem y git — source: 2221814efbefaa3b
- v2026.8.31 lista filesystem, memory, sequential-thinking y everything — source: 30a26335a9988ba2
- v2026.7.10 lista filesystem, time, fetch y git — source: 5a4df6bef0a4905f
- v2026.1.14 lista everything, filesystem y git — source: 748f8b0a02cd7524
- v2026.8.18 lista everything, time, fetch y git — source: 9750590bbfe6b285
- v2026.1.26 lista everything, memory y time — source: b9106690f5dfd849
- v2026.7.4 lista everything, filesystem, sequential-thinking y memory — source: ffbd76916d1dfdc5

## Why it matters
Un dev que fija versiones no puede apoyarse en una interfaz estable por paquete: el conjunto que se mueve cambia cada release. Lo único predecible es la etiqueta de fecha.

Se relaciona con la cadencia de alta frecuencia y con la observación de que el roster de paquetes varía; ambas describen el mismo esquema de publicación.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
- derived_from → [[mcp-release-2026-8-31-bumps]]
- relates_to → [[mcp-release-stub-sin-changelog]]
- derived_from → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-roster-de-paquetes-varia-entre-releases]]
- relates_to → [[mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion]]
- relates_to → [[mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia]]
