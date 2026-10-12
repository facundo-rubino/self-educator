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
updated: '2026-10-12'
sources:
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
tags:
- fechas
- frescura
- mcp
- pipeline
- timestamps
- validez
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: supports
- to: mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia
  type: contradicts
---

## What it is
Las etiquetas de versión del clúster (hasta v2026.8.31) son posteriores a la fecha de generación registrada del informe (2026-10-12). No hay fuente primaria que corrobore que esas fechas correspondan a releases reales y no a un stream mal etiquetado o a timestamps sintéticos.

## Evidence
- Etiquetas de versión 2026.x en los documentos del clúster — source: 30a26335a9988ba2, 2221814efbefaa3b, 5a4df6bef0a4905f

## Why it matters
Si los timestamps no son auténticos, cualquier inferencia de cadencia (volumen mensual, ritmo de mantenimiento) es un artefacto del feed, no una medición.

`contradicts` la lectura de la serie como cadencia de alta frecuencia; `supports` la nota ya existente sobre la no corroborabilidad de las fechas 2026 del corpus MCP.

## Links
- supports → [[mcp-fechas-2026-sinteticas-no-corroborables]]
- contradicts → [[mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia]]
