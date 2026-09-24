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
updated: '2026-09-24'
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
- paquetes
- patron-estructural
- release-engineering
- release-notes
- releases
- versionado
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-24'
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
- to: cadencia-de-release-unificada-sugiere-monorepo-mcp
  type: supports
- to: mcp-servers-versionado-por-fecha
  type: supports
- to: release-2026-8-31-solo-bumps-mcp-sin-contenido-de-practica
  type: relates_to
---

## What it is
El conjunto de paquetes bumpeados no es fijo entre releases: server-memory y server-sequential-thinking aparecen en algunas versiones y no en otras, y mcp-server-time y mcp-server-fetch aparecen solo en releases tardías del muestreo. La conclusión de qué servers son core versus opcionales no es fiable desde este sample.

## Evidence
- Package sets varían entre releases: memory y sequential-thinking aparecen en unas versiones y no en otras; time/fetch solo en releases tardías — source: 2221814efbefaa3b
- v2026.7.10 incluye mcp-server-time y mcp-server-fetch — source: 5a4df6bef0a4905f
- v2026.8.18 incluye mcp-server-time y mcp-server-fetch — source: 9750590bbfe6b285
- v2026.1.14 no incluye memory ni sequential-thinking — source: 748f8b0a02cd7524

## Why it matters
El bundle publicado no es estable. Un consumidor no puede inferir deprecación ni criticidad de un paquete a partir de su presencia u ausencia en una release concreta.

Refuerza el versionado por fecha como esquema subyacente y se relaciona con la nota de release 2026.8.31 sin contenido de práctica.

## Links
- relates_to → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
- supports → [[cadencia-de-release-unificada-sugiere-monorepo-mcp]]
- supports → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[release-2026-8-31-solo-bumps-mcp-sin-contenido-de-practica]]
