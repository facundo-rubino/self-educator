---
id: politica-de-agentes-propios-no-se-sostiene-desde-feed-de-releases
title: La política de agentes propios no se sostiene desde un feed de releases MCP
type: risk
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
- riesgo
- evidencia
- brief
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: mcp-release-stub-sin-changelog
  type: supports
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: supports
---

## What it is
Los documentos no contienen changelog más allá de nombres de paquete y versión; cualquier afirmación sobre cambios de comportamiento, deprecaciones o capacidades nuevas sería especulación. Los seis docs son notas de release del mismo feed (engagement=0), sin corroboración independiente ni comentario humano.

## Evidence
- Release 2026.8.31 solo enumera paquetes y versión, sin prosa — source: 30a26335a9988ba2
- Release 2026.8.18 solo enumera paquetes y versión — source: 9750590bbfe6b285
- Release 2026.7.10 solo enumera paquetes y versión — source: 5a4df6bef0a4905f
- Release 2026.7.4 solo enumera paquetes y versión — source: ffbd76916d1dfdc5
- Release 2026.1.26 solo enumera paquetes y versión — source: b9106690f5dfd849
- Release 2026.1.14 solo enumera paquetes y versión — source: 748f8b0a02cd7524

## Why it matters
Usar este clúster como soporte de claims sobre liderazgo técnico, estimación, secuenciación u organización personal sería un error de categoría. La única lectura segura es: "estos paquetes se publican con esta cadencia".

Soporta la nota existente `mcp-release-stub-sin-changelog` (los releases no traen changelog legible) y `afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases` (no se puede inferir práctica desde un feed de releases).

## Links
- supports → [[mcp-release-stub-sin-changelog]]
- supports → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
