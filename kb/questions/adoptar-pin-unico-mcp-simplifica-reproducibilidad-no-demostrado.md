---
id: adoptar-pin-unico-mcp-simplifica-reproducibilidad-no-demostrado
title: Un pin único de versión MCP simplificaría reproducibilidad, pero no está demostrado
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 30a26335a9988ba2
- 9750590bbfe6b285
- 5a4df6bef0a4905f
- ffbd76916d1dfdc5
- b9106690f5dfd849
- 748f8b0a02cd7524
tags:
- mcp
- reproducibilidad
- pregunta
- brief
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: mcp-serie-2026-roster-varia-entre-releases-reforzado
  type: relates_to
---

## What it is
Como memory, filesystem y git se publican a veces en la misma fecha y a veces no, la idea de que un solo pin sincronizado simplifique reproducibilidad y onboarding es plausible pero no está demostrada: los releases muestran subconjuntos de paquetes distintos.

## Evidence
- 2026.8.31 no incluye git; 2026.8.18 incluye git pero no memory — sources: 30a26335a9988ba2, 9750590bbfe6b285
- 2026.1.14 incluye git y filesystem, sin memory ni time — source: 748f8b0a02cd7524

## Why it matters
Quien quiera fijar versiones del stack de agentes necesita decidir entre pin por paquete o pin global; la evidencia no permite afirmar que el pin global sea reproducible sin verificar cada fecha.

Se apoya en `mcp-serie-2026-roster-varia-entre-releases-reforzado`, que documenta la variación del roster; es la pregunta abierta que esa observación deja.

## Links
- relates_to → [[mcp-serie-2026-roster-varia-entre-releases-reforzado]]
