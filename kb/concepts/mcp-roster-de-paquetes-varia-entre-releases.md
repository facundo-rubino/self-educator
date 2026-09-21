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
updated: '2026-09-21'
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
- patron-estructural
- release-engineering
- release-notes
- releases
- versionado
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-21'
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
---

## What it is
Cada release de la suite MCP incluye un subconjunto distinto de paquetes sobre un conjunto base estable (filesystem, everything, memory, sequential-thinking, git, time, fetch). No todos los paquetes se bumpean en todos los releases; el roster rota [5a4df6bef0a4905f] [748f8b0a02cd7524] [9750590bbfe6b285] [b9106690f5dfd849] [ffbd76916d1dfdc5].

## Evidence
- v2026.8.18 cubre everything, time, fetch, git — source: 9750590bbfe6b285
- v2026.1.14 usa la misma plantilla con otro subconjunto — source: 748f8b0a02cd7524
- v2026.1.26 lista everything, memory, time — un tercer subconjunto distinto — source: b9106690f5dfd849
- v2026.7.4 incluye everything, filesystem, sequential-thinking, memory — source: ffbd76916d1dfdc5
- Un release anterior muestra la misma plantilla con otro subconjunto (filesystem, time, fetch, git) — source: 5a4df6bef0a4905f

## Why it matters
Es el único patrón estructural genuinamente extraíble del clúster: hay actividad sostenida sobre un conjunto estable de paquetes, con foco variable por release. Sirve para caracterizar la madurez del ecosistema MCP, pero no para inferir práctica de ingeniería ni decisiones de producto.

`mcp-servers-sin-changelog-legible` explica por qué el roster es lo único observable: falta la prosa que daría sentido a la rotación. `cadencia-de-release-unificada-sugiere-monorepo-mcp` usa este patrón como evidencia de apoyo para la hipótesis de publicación coordinada.

## Links
- relates_to → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
- supports → [[cadencia-de-release-unificada-sugiere-monorepo-mcp]]
