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
updated: '2026-09-24'
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
last_reinforced: '2026-09-24'
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
- to: mcp-serie-2026-sin-diffs-ni-fuente-primaria
  type: relates_to
- to: mcp-release-2026-8-31-bumps
  type: relates_to
---

## What it is
Las versiones de la suite MCP de referencia reflejan exactamente la fecha de publicación: v2026.1.26 con paquetes a 2026.1.26, v2026.8.31 con paquetes a 2026.8.31. Es un esquema date-driven completamente automatizado, no semver.

## Evidence
- Las cadenas de versión replican exactamente la fecha de release (v2026.1.26 con paquetes @2026.1.26), indicando cadencia date-driven automatizada — source: b9106690f5dfd849
- v2026.8.31 bumpea paquetes a la date-version 2026.8.31 — source: 30a26335a9988ba2

## Why it matters
Un esquema date-versioned comunica cuándo se publicó, no qué cambió; no hay señal de breaking change ni de tipo de cambio en la versión misma.

Se relaciona con la nota de la serie 2026 sin diffs, que cubre la ausencia de fuente primaria verificable de los cambios.

## Links
- relates_to → [[mcp-servers-sin-changelog-legible]]
- relates_to → [[mcp-roster-de-paquetes-varia-entre-releases]]
- supports → [[release-de-parche-no-revela-practica-de-ingenieria]]
- relates_to → [[mcp-serie-2026-sin-diffs-ni-fuente-primaria]]
- relates_to → [[mcp-release-2026-8-31-bumps]]
