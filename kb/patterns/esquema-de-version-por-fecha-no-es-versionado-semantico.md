---
id: esquema-de-version-por-fecha-no-es-versionado-semantico
title: Un esquema de versionado por fecha no comunica compatibilidad semántica
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-12'
updated: '2026-10-12'
sources:
- 30a26335a9988ba2
- 2221814efbefaa3b
- 5a4df6bef0a4905f
tags:
- versionado
- dependencias
- mcp
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: mcp-releases-versionado-por-fecha-subconjunto-varia
  type: derived_from
- to: mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia
  type: relates_to
---

## What it is
Cuando un proyecto publica con etiquetas de fecha (v2026.8.31) en lugar de semver, el número no codifica ninguna promesa de compatibilidad: dos etiquetas consecutivas pueden diferir en cualquier grado de ruptura y el consumidor no puede inferirlo del identificador.

## Evidence
- Las etiquetas de la serie MCP son fechas (2025.12.18 a 2026.8.31), no versiones semánticas — source: 30a26335a9988ba2, 2221814efbefaa3b, 5a4df6bef0a4905f

## Why it matters
Cambia la estrategia de pinneo: con esquema de fecha la única protección contra rupturas es fijar la etiqueta exacta y leer diffs, ya que el identificador no advierte de nada.

`derived_from` la observación empírica de que los releases MCP se versionan por fecha; se relaciona con la cadencia de la serie, que es su consecuencia operativa.

## Links
- derived_from → [[mcp-releases-versionado-por-fecha-subconjunto-varia]]
- relates_to → [[mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia]]
