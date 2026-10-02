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
updated: '2026-10-02'
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
- versionado
- versionado-por-fecha
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-10-02'
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
---

## What it is
Cada release de la serie numera sus paquetes con la propia fecha (v2025.11.25, v2026.8.31, etc.). El conjunto concreto de paquetes listados no es estable: git aparece en 2025.11.25, 2025.12.18, 2026.1.14, 2026.7.10 y 2026.8.18 pero no en 2026.1.26, 2026.7.4 ni 2026.8.31.

## Evidence
- Todos los paquetes de cada release se versionan con la fecha del release (p. ej. v2025.11.25, v2026.8.31) — sources: 16a4e3995d6c827e, 30a26335a9988ba2
- mcp-server-git aparece en 2025.11.25, 2025.12.18, 2026.1.14, 2026.7.10 y 2026.8.18, y no en 2026.1.26, 2026.7.4 ni 2026.8.31 — sources: 16a4e3995d6c827e, 2221814efbefaa3b, 748f8b0a02cd7524, 5a4df6bef0a4905f, 9750590bbfe6b285, b9106690f5dfd849, ffbd76916d1dfdc5, 30a26335a9988ba2
- server-memory está en 2025.11.25 y desaparece en 2025.12.18, y reaparece en 2026.1.26 y 2026.7.4 — sources: 16a4e3995d6c827e, 2221814efbefaa3b, b9106690f5dfd849, ffbd76916d1dfdc5

## Why it matters
Fija el hecho verificable de la serie: versionado por fecha y roster fluctuante. No autoriza a leer entradas/salidas como deprecaciones ni como señales de salud del proyecto.

`mcp-servers-versionado-por-fecha` es el esquema base; `mcp-roster-de-paquetes-varia-entre-releases` generaliza el mismo patrón; `mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion` marca el límite inferencial.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
- derived_from → [[mcp-release-2026-8-31-bumps]]
- relates_to → [[mcp-release-stub-sin-changelog]]
- derived_from → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[mcp-roster-de-paquetes-varia-entre-releases]]
- relates_to → [[mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion]]
