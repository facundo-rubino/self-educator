---
id: mcp-serie-2025-11-a-2026-8-lectura-como-serie-de-tiempo-fragil
title: La serie MCP 2025.11–2026.8 se lee como serie temporal frágil, no como hallazgo
  de tema
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-10-07'
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
- artefacto-de-feed
- mcp
- muestreo
- riesgo
- serie-temporal
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: mcp-releases-versionado-por-fecha-subconjunto-varia
  type: contradicts
- to: feed-de-dependencias-no-es-evidencia-de-practica-profesional
  type: relates_to
- to: mcp-release-stub-sin-changelog
  type: relates_to
- to: mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia
  type: relates_to
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: supports
---

## What it is
El único hecho estructural que el clúster expone es qué paquetes aparecen en cada release con fecha. El conjunto rastreado varía entre releases: uno de diciembre de 2025 lista sequential-thinking, everything, filesystem y git, mientras que uno de julio de 2026 incluye time y fetch. La ausencia de paquetes en un release no es un hecho del mundo, es selección por release.

## Evidence
- Un release de diciembre de 2025 lista server-sequential-thinking, server-everything, server-filesystem y mcp-server-git en la misma fecha versionada — source: 2221814efbefaa3b
- Un release de julio de 2026 incluye mcp-server-time y mcp-server-fetch, mostrando que el conjunto de paquetes varía — source: 5a4df6bef0a4905f
- Un release de enero de 2026 omite paquetes (p. ej. time, fetch) que sí aparecen en otros, indicando selección por release y no un ensamble fijo — source: 748f8b0a02cd7524

## Why it matters
Trazar una serie temporal con estos puntos produce una curva sobre el formato del feed, no sobre el ecosistema. Cualquier tendencia que se lea —adopción, madurez, actividad— sería un artefacto del subconjunto elegido en cada publicación.

Comparte territorio con la nota sobre la cadencia date-versioned de MCP, pero el foco aquí es distinto: allí la cadencia, aquí la fragilidad de tratar los puntos como serie. `supports` el riesgo de que las fechas 2026 no sean corroborables.

## Links
- contradicts → [[mcp-releases-versionado-por-fecha-subconjunto-varia]]
- relates_to → [[feed-de-dependencias-no-es-evidencia-de-practica-profesional]]
- relates_to → [[mcp-release-stub-sin-changelog]]
- relates_to → [[mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia]]
- supports → [[mcp-fechas-2026-sinteticas-no-corroborables]]
