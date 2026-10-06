---
id: xml-pretexto-lexico-javascript-en-el-runtime
title: «JavaScript is right there» como pretexto léxico, no como técnica de transformación
  de XML
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-10-06'
sources:
- 1bfe45ede61ee575
tags:
- corpus
- falsos-positivos
- heuristica
- javascript
- matching
- matching-lexico
- patron-de-ingesta
- stub
- xml
- xslt
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-contexto-no-ingerido
  type: supports
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: derived_from
- to: js-como-lenguaje-general-ya-presente-en-el-runtime
  type: relates_to
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: relates_to
- to: js-como-lenguaje-general-ya-presente-en-el-runtime
  type: supports
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: supports
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: supports
- to: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
  type: supports
- to: xml-human-readable-without-xslt-fuera-del-brief-de-agentes-y-liderazgo
  type: supports
---

## What it is
Patrón de ingest: un ítem cuyo único contenido es una apelación a la disponibilidad del lenguaje («JavaScript is right there») se registra como argumento de sustitución de herramienta, pero no contiene método, benchmark ni caso. El reclamo es un pretexto léxico —el runtime ya tiene JS, luego úsalo— y no una técnica de transformación.

## Evidence
- El cuerpo del documento es solo la frase «JavaScript is right there» — source: 1bfe45ede61ee575
- No hay benchmarks, ejemplos, ni razonamiento en el cuerpo ingerido — source: 1bfe45ede61ee575
- El ítem entra al clúster con relevance=0.33 y novelty=0.00 — source: 1bfe45ede61ee575

## Why it matters
Reconocer este patrón evita promover apelaciones al lenguaje disponible como hallazgos de ingeniería. La heurística yace sin argumentar en el documento; citarla como si el documento la sostuviera sería circular.

Soporta la nota de falso positivo léxico del filtro y la de fuera-de-brief. Se relaciona con `js-como-lenguaje-general-ya-presente-en-el-runtime` en tanto comparten la premisa de disponibilidad del runtime, pero aquí es un reclamo sin evidencia y allí una observación distinta del corpus.

## Links
- supports → [[xml-human-readable-sin-xslt-contexto-no-ingerido]]
- derived_from → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- relates_to → [[js-como-lenguaje-general-ya-presente-en-el-runtime]]
- relates_to → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[js-como-lenguaje-general-ya-presente-en-el-runtime]]
- supports → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro]]
- supports → [[xml-human-readable-without-xslt-fuera-del-brief-de-agentes-y-liderazgo]]
