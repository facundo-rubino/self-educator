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
updated: '2026-09-17'
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
- versionado
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-17'
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
El conjunto de MCP servers de referencia se publica con versiones derivadas de la fecha de release (p. ej. `v2025.11.25`, `v2025.12.18`, `v2026.8.31`) en lugar de versionado semántico atado a cambios incompatibles. Las releases abarcan al menos de 2025-11-25 a 2026-08-31 y cada una lista únicamente los paquetes bumpeados y su nueva versión date-stamped [16a4e3995d6c827e][2221814efbefaa3b][30a26335a9988ba2].

## Evidence
- Cadencia con versionado por fecha: `v2025.11.25` — source: 16a4e3995d6c827e
- La release `v2025.12.18` repite la misma convención — source: 2221814efbefaa3b
- `v2026.8.31` bumpea `@modelcontextprotocol/server-filesystem`, `server-memory`, `server-sequential-thinking` y `server-everything` a la versión 2026.8.31 — source: 30a26335a9988ba2
- Todos los documentos del clúster son ítems de feed (rss) con engagement=0 — source: ffbd76916d1dfdc5

## Why it matters
Una versión que codifica la fecha no comunica compatibilidad ni ruptura: un consumidor no puede decidir si actualizar es seguro a partir del número de versión, solo a partir del diff del paquete. Implica un proceso de publicación agendado de alta cadencia, no un versionado semántico.

Se relaciona con `mcp-servers-sin-changelog-legible` (ambos son propiedades del formato de release que degradan la información disponible al consumidor) y con `mcp-roster-de-paquetes-varia-entre-releases` (misma fuente de releases, distinta propiedad observada). Refuerza `release-de-parche-no-revela-practica-de-ingenieria`: una convención de versionado por fecha es evidencia aún más pobre sobre práctica de ingeniería que un patch release.

## Links
- relates_to → [[mcp-servers-sin-changelog-legible]]
- relates_to → [[mcp-roster-de-paquetes-varia-entre-releases]]
- supports → [[release-de-parche-no-revela-practica-de-ingenieria]]
