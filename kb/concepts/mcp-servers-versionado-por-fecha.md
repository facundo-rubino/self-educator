---
id: mcp-servers-versionado-por-fecha
title: Los MCP servers de referencia se versionan por fecha, no semánticamente
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-22'
sources:
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
tags:
- mcp
- release-engineering
- releases
- versionado
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-sin-changelog-legible
  type: relates_to
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: relates_to
- to: release-de-parche-no-revela-practica-de-ingenieria
  type: supports
---

## What it is
La serie de releases de los MCP servers de referencia se identifica por fecha (p. ej. «Release 2026.8.31»), no por versión semántica. Cada entrada es un encabezado de versión más una lista de paquetes `@modelcontextprotocol/server-*` actualizados.

## Evidence
- El documento de release 2026.8.31 lista únicamente paquetes actualizados del ecosistema MCP (filesystem, memory, sequential-thinking, everything), sin contenido editorial — source: 30a26335a9988ba2
- Releases anteriores de la misma serie (2025.11.25 y 2025.12.18) tienen idéntica estructura: encabezado de versión y lista de paquetes MCP actualizados — source: 16a4e3995d6c827e
- El release 2026.7.10 también lista `server-memory`, `mcp-server-time` y `mcp-server-fetch` — source: 5a4df6bef0a4905f

## Why it matters
Versionar por fecha impide inferir compatibilidad o semver desde el identificador de release; para consumir estos paquetes hay que leer la lista de bumps caso por caso.

Se relaciona con la observación de que el roster de paquetes bumpeados varía entre releases (mcp-roster-de-paquetes-varia-entre-releases) y con la ausencia de changelog legible (mcp-servers-sin-changelog-legible): ambos son consecuencias del mismo formato de release.

## Links
- relates_to → [[mcp-servers-sin-changelog-legible]]
- relates_to → [[mcp-roster-de-paquetes-varia-entre-releases]]
- supports → [[release-de-parche-no-revela-practica-de-ingenieria]]
