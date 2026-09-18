---
id: mcp-fechas-2026-sinteticas-no-corroborables
title: Las fechas 2026.x del corpus MCP no son corroborables
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-09-18'
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
- datos
- corroboracion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: derived_from
- to: hy3-fuente-primaria-y-metodologia-ausentes
  type: relates_to
---

## What it is
Las versiones y fechas del corpus MCP caen en un rango 2026.x que el reporte califica de sintético o no publicado («synthetic/unreleased-looking»). Eso vuelve la línea temporal poco fiable como base de corroboración de cualquier inferencia sobre cadencia o mantenimiento.

## Evidence
- Las ocho releases cubren 2025.11.25 a 2026.8.31, incluidas fechas futuras respecto a la generación del reporte (2026-09-18) — source: 16a4e3995d6c827e / 2221814efbefaa3b / 30a26335a9988ba2 / 5a4df6bef0a4905f / 748f8b0a02cd7524 / 9750590bbfe6b285 / b9106690f5dfd849 / ffbd76916d1dfdc5
- El reporte lista entre los riesgos: «Version strings and dates in this synthetic/unreleased-looking range (2026.x) make the timeline unreliable for corroboration» — source: sig-d0acf338c3a6

## Why it matters
Impide usar la secuencia temporal como evidencia independiente. Cualquier afirmación sobre evolución del roster MCP depende de fechas que no se pueden verificar contra una fuente externa.

Deriva de `mcp-roster-de-paquetes-varia-entre-releases` (la serie temporal es el objeto afectado) y se relaciona con `hy3-fuente-primaria-y-metodologia-ausentes` por el mismo patrón: metadatos sin fuente primaria verificable.

## Links
- derived_from → [[mcp-roster-de-paquetes-varia-entre-releases]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
