---
id: xml-human-readable-entra-por-coincidencia-lexica
title: El ítem de XML entró al brief por coincidencia léxica con «programar»
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 1bfe45ede61ee575
tags:
- clustering
- pipeline
- relevancia
- topico
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: relates_to
---

## What it is
El documento no tiene relación temática con el brief declarado (agentes de IA aplicados a programar, liderazgo técnico, oficio, productividad). Entró pese a relevancia=0.33 y novedad=0.00, lo que apunta a solapamiento por vocabulario genérico.

## Evidence
- El tema del pipeline (agentes de IA, liderazgo técnico, docencia, productividad) no tiene relación temática con el contenido del clúster, que trata presentación/formateo de XML — source: 1bfe45ede61ee575
- Cayó en el clúster pese a relevancia=0.33 y novedad=0.00, probablemente por coincidencia léxica con términos genéricos («programar», «hacer mejor») — source: 1bfe45ede61ee575

## Why it matters
Si el agrupamiento es por similitud léxica, conviene revisar el criterio: el ítem debería descartarse o reencolarse en un topic de tooling/XML. La pregunta abierta es qué umbral deja pasar vocabulario genérico.

Deriva del diagnóstico de ingesta del propio documento. Resuena con el patrón de «afirmar-constraint-de-diseno-desde-solo-titulo-rss»: ambos son fallos de precisión del pipeline, no hallazgos del brief.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- relates_to → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
