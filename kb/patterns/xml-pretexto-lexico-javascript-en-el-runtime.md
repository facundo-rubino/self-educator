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
updated: '2026-10-08'
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
last_reinforced: '2026-10-08'
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
- to: restatement-de-titulo-no-es-hallazgo
  type: supports
- to: umbral-de-contenido-minimo-antes-de-clustering
  type: relates_to
---

## What it is
Salto de categoría en la evidencia: XSLT es un lenguaje de transformación y JavaScript un runtime de propósito general. Decir «usa JS en lugar de XSLT» sin especificar el documento, la transformación ni la salida no es una técnica alternativa, es un enunciado de disponibilidad [1bfe45ede61ee575].

## Evidence
- El único soporte textual de la alternativa a XSLT es «JavaScript is right there.» — source: 1bfe45ede61ee575
- El texto ingerido no incluye manejo de namespaces, streaming, documentos grandes ni tratamiento de errores — source: 1bfe45ede61ee575

## Why it matters
Cuando un ítem afirma sustituir una herramienta especializada por un runtime general, la carga de la prueba es el resultado producido. Sin muestra de salida no hay forma de verificar que el XML resultante sea «legible» en algún sentido operativo, ni de comparar contra XSLT.

Se deriva de `xml-human-readable-without-xslt-afirmacion-sin-cuerpo`. Es un caso particular de `restatement-de-titulo-no-es-hallazgo` y refuerza la necesidad de `umbral-de-contenido-minimo-antes-de-clustering`.

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
- supports → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[umbral-de-contenido-minimo-antes-de-clustering]]
