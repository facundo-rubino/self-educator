---
id: prompt-a-herramienta-en-feed-rss-como-artefacto-de-ingesta
title: Un prompt a una herramienta en un feed RSS es un artefacto de ingesta, no contenido
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- df4836a1d89bcba4
tags:
- rss
- ingesta
- prompt
- pipeline
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: mcp-release-stubs-como-artefacto-de-feed
  type: relates_to
---

## What it is
Un feed RSS puede estar republicando prompts de IA en lugar de análisis terminados. El ítem [df4836a1d89bcba4] es exactamente eso: la instrucción enviada a la herramienta, no el artefacto producido por ella. La brecha entre el titular («explained with live examples») y el cuerpo (un meta-prompt) es un artefacto de extracción de título/resumen.

## Evidence
- El cuerpo del documento es un prompt a la herramienta «Fable 5.1 Medium», no la explicación prometida por el titular — source: df4836a1d89bcba4

## Why it matters
Si la fuente republica prompts en vez de análisis completos, puede contaminar clústeres futuros con contenido que nunca fue pensado como hallazgo. Vale la pena investigar la extracción en el ingester antes de que el patrón se propague.

Deriva de la nota de título sin contenido ingerido. Apoya el riesgo ya registrado de que el pipeline evalúe clústeres cuyo cuerpo no recuperó, y se relaciona con el patrón conocido de stubs de release que son artefacto de feed y no hallazgo.

## Links
- derived_from → [[shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- relates_to → [[mcp-release-stubs-como-artefacto-de-feed]]
