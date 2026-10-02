---
id: mcp-release-2026-1-26-bumps
title: 'Release 2026.1.26: bump de everything, memory y mcp-server-time'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-02'
sources:
- b9106690f5dfd849
tags:
- changelog
- mcp
- release
- releases
- versionado
base_confidence: 0.78
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
---

## What it is
El release 2026.1.26 lista server-everything, server-memory y mcp-server-time; server-filesystem y git están ausentes de esta entrada.

## Evidence
- El release 2026.1.26 lista server-everything, server-memory y mcp-server-time; server-filesystem y git no aparecen — source: b9106690f5dfd849

## Why it matters
Es el primer punto del corpus donde aparece mcp-server-time y, a la vez, un punto donde dos paquetes estables (filesystem, git) desaparecen del listado.

`mcp-roster-de-paquetes-varia-entre-releases` recoge este caso; la ausencia de filesystem/git aquí sustenta el riesgo asociado a inferir deprecación desde la ausencia.

## Links
- supports → [[mcp-servers-versionado-por-fecha]]
- supports → [[mcp-roster-de-paquetes-varia-entre-releases]]
