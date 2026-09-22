---
id: timestamps-2026-de-la-serie-mcp-posiblemente-sinteticos
title: 'Riesgo: los timestamps 2026 de la serie MCP pueden ser sintéticos o estar
  mal parseados'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- 9750590bbfe6b285
- 748f8b0a02cd7524
- b9106690f5dfd849
tags:
- timestamps
- frescura
- pipeline
- mcp
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: supports
---

## What it is
La serie cubre releases etiquetadas de 2025.11 a 2026.8, un rango futuro respecto a una lectura ingenua de «hoy». Si los timestamps son sintéticos o están mal parseados, la lógica de frescura del pipeline también opera sobre datos incorrectos.

## Evidence
- El release 2026.8.18 actualiza `server-everything`, `mcp-server-time`, `mcp-server-fetch` y `mcp-server-git`, dentro del mismo patrón de changelog — source: 9750590bbfe6b285
- El release 2026.1.14 lista `server-everything`, `server-filesystem` y `mcp-server-git`, sin texto temático asociado — source: 748f8b0a02cd7524
- El release 2026.1.26 actualiza `server-everything`, `server-memory` y `mcp-server-time` — source: b9106690f5dfd849

## Why it matters
Un error sistemático en los timestamps afectaría a la frescura de todo el corpus, no solo a este clúster: las releases parecerían más recientes (o más antiguas) de lo que son.

Es una instancia concreta del riesgo ya registrado sobre las fechas 2026 del corpus MCP (mcp-fechas-2026-sinteticas-no-corroborables); aquí se añade la observación del rango 2025.11–2026.8.

## Links
- supports → [[mcp-fechas-2026-sinteticas-no-corroborables]]
