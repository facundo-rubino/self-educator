---
id: mcp-release-2026-8-31-bumps
title: 'Release 2026.8.31: bump de server-filesystem, memory, sequential-thinking
  y everything'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-25'
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
- date-versioned
- dependencias
- mcp
- release-notes
- releases
- versionado
base_confidence: 0.78
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-versionado-por-fecha
  type: supports
- to: release-2026-8-31-bumps-recurrentes-server-everything-filesystem
  type: relates_to
- to: release-2026-8-31-solo-bumps-mcp-sin-contenido-de-practica
  type: relates_to
- to: mcp-releases-versionado-por-fecha-subconjunto-varia
  type: supports
- to: mcp-release-stub-sin-changelog
  type: relates_to
---

## What it is
Release fechada 2026.8.31 de un conjunto de paquetes de MCP servers. El documento es un encabezado de versión más una lista de paquetes bumpeados: server-filesystem, server-memory, server-sequential-thinking y server-everything. No incluye descripción de cambios de comportamiento ni de API.

## Evidence
- Release 2026.8.31 bumpea server-filesystem, server-memory, server-sequential-thinking y server-everything — source: 30a26335a9988ba2
- El documento 30a26335a9988ba2 no nombra mcp-server-time ni mcp-server-fetch en su lista de paquetes, a diferencia de 9750590bbfe6b285 y 5a4df6bef0a4905f — source: 30a26335a9988ba2
- El conjunto de paquetes de la serie rota entre releases en lugar de ser uniforme — source: 30a26335a9988ba2

## Why it matters
Es el artefacto concreto con el que se fecha la señal: sirve de ancla para verificar la cadencia de la serie, no como fuente de contenido técnico. Cualquier afirmación sobre cambios de comportamiento en esta release no está respaldada por el documento.

`supports` la nota sobre versionado por fecha y subconjunto variable: es un caso más donde la lista de paquetes difiere de la de releases adyacentes. `relates_to` el patrón de release stubs sin changelog, porque este documento es exactamente eso.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- relates_to → [[release-2026-8-31-bumps-recurrentes-server-everything-filesystem]]
- relates_to → [[release-2026-8-31-solo-bumps-mcp-sin-contenido-de-practica]]
- supports → [[mcp-releases-versionado-por-fecha-subconjunto-varia]]
- relates_to → [[mcp-release-stub-sin-changelog]]
