---
id: feed-de-dependencias-no-es-evidencia-de-practica-profesional
title: Un feed de releases de dependencias no es evidencia de práctica profesional
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-23'
sources:
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- b9106690f5dfd849
tags:
- metodologia
- evidencia
- infraestructura
base_confidence: 0.75
half_life_days: 365
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: mcp-release-stub-sin-changelog
  type: derived_from
- to: mcp-release-bumps-no-revelan-practica-de-ingenieria
  type: supports
- to: mcp-release-stubs-como-artefacto-de-feed
  type: supports
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: supports
---

## What it is
Un corpus compuesto exclusivamente por notas de release de paquetes versionados documenta mecanismos de publicación, no prácticas de ingeniería, liderazgo ni docencia. La coincidencia de vocabulario con el brief ('agentes', 'MCP') es nominal.

## Evidence
- La nota 2026.8.31 solo enumera paquetes y versión, sin describir uso ni resultado — source: 30a26335a9988ba2
- La nota 2026.7.10 solo enumera paquetes y versión — source: 5a4df6bef0a4905f
- La nota 2026.1.26 solo enumera paquetes y versión — source: b9106690f5dfd849

## Why it matters
Reasigna este tipo de corpus a un feed de dependencias y evita usarlo como evidencia sobre el brief. La autodescripción del pipeline (relevancia, novedad, corroboración) no es validación externa.

Deriva de `mcp-release-stub-sin-changelog` (sin changelog, no hay práctica que extraer) y refuerza los riesgos ya registrados `mcp-release-bumps-no-revelan-practica-de-ingenieria`, `mcp-release-stubs-como-artefacto-de-feed` y `afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases`.

## Links
- derived_from → [[mcp-release-stub-sin-changelog]]
- supports → [[mcp-release-bumps-no-revelan-practica-de-ingenieria]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
- supports → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
