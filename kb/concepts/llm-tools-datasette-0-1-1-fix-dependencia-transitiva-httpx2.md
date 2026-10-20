---
id: llm-tools-datasette-0-1-1-fix-dependencia-transitiva-httpx2
title: 'llm-tools-datasette 0.1.1: parche por dependencia transitiva no declarada
  (httpx → httpx2)'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 22e0e79c5f31252d
tags:
- datasette
- llm
- dependencias
- release
- mantenimiento
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: mcp-servers-sin-changelog-legible
  type: relates_to
- to: release-de-parche-no-revela-practica-de-ingenieria
  type: relates_to
---

## What it is
llm-tools-datasette 0.1.1 es un release de parche que corrige una rotura de compatibilidad provocada por el cambio de LLM 0.33 a httpx2. El plugin usaba httpx de forma transitiva sin declararlo como dependencia directa, de modo que el cambio aguas arriba lo rompió. Es un único ítem RSS de bajo engagement, sin corroboración independiente.

## Evidence
- llm-tools-datasette 0.1.1 se publicó para arreglar la rotura causada cuando LLM 0.33 pasó a httpx2 — source: 22e0e79c5f31252d
- Los plugins que usaban httpx sin depender de él directamente se rompieron con ese cambio; llm-tools-datasette fue uno de ellos — source: 22e0e79c5f31252d

## Why it matters
No aporta nada sobre agentes de IA, liderazgo técnico, estimación, oficio ni estudio: es mantenimiento de un plugin. Su único contenido reutilizable es el hecho concreto del acoplamiento por dependencia transitiva, no un principio general demostrado.

Se relaciona con las notas de releases de tooling sin changelog legible (mismo género de artefacto de feed) y con la nota de que un release de parche no revela práctica de ingeniería. La conexión con el brief es léxica por «LLM», no temática.

## Links
- relates_to → [[mcp-servers-sin-changelog-legible]]
- relates_to → [[release-de-parche-no-revela-practica-de-ingenieria]]
