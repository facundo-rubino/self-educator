---
id: mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion
title: La ausencia de un paquete en una release no prueba deprecación ni remoción
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
- release-notes
- inferencia
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: mcp-roster-de-paquetes-varia-entre-releases
  type: derived_from
- to: mcp-servers-sin-changelog-legible
  type: relates_to
- to: mcp-release-stubs-como-artefacto-de-feed
  type: supports
---

## What it is
Las listas de paquetes en notas de release pueden ser parciales (solo paquetes «actualizados»), de modo que la ausencia de un paquete en una release dada no demuestra su deprecación ni su remoción. Las deltas de presencia observadas en el corpus MCP quedan así sin explicación: podrían ser artefacto de qué paquetes cambiaron esa semana.

## Evidence
- server-memory está ausente en 2025.12.18 y 2026.1.14, pero reaparece en 2026.1.26, 2026.7.4 y 2026.8.31 — source: 2221814efbefaa3b / 748f8b0a02cd7524 / b9106690f5dfd849 / ffbd76916d1dfdc5 / 30a26335a9988ba2
- mcp-server-git está ausente en 2026.8.18 y 2026.8.31 pese a aparecer en 2025.11.25, 2025.12.18, 2026.1.14 y 2026.8.18 — source: 9750590bbfe6b285 / 30a26335a9988ba2
- El reporte advierte explícitamente que las deltas podrían reflejar «which packages changed that week rather than any real portfolio shift» — source: sig-d0acf338c3a6

## Why it matters
Bloquea la inferencia «paquete ausente ⇒ paquete muerto». Cualquier lectura de roadmap o mantenimiento a partir de estas notas requiere evidencia adicional (changelog, commits, issues) que el corpus no aporta.

Deriva de `mcp-roster-de-paquetes-varia-entre-releases`: la variación observada es el hecho; la imposibilidad de leerla como deprecación es la consecuencia. Se apoya en `mcp-servers-sin-changelog-legible` porque la falta de changelog es lo que deja la ausencia sin interpretación.

## Links
- derived_from → [[mcp-roster-de-paquetes-varia-entre-releases]]
- relates_to → [[mcp-servers-sin-changelog-legible]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
