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
updated: '2026-09-25'
sources:
- 1bfe45ede61ee575
tags:
- matching-lexico
- falsos-positivos
- xml
- javascript
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-09-25'
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
---

## What it is
Regularidad de clasificación: un ítem entra al clúster por co-ocurrencia de vocabulario («JavaScript» y «XML»), no por desarrollar un claim técnico. El documento [1bfe45ede61ee575] no ofrece mecanismo, comparación con XSLT ni evidencia de adopción; su único contenido es una frase de cuatro palabras.

## Evidence
- El payload sustantivo del documento es «JavaScript is right there» — source: 1bfe45ede61ee575
- El crítico del signal califica la inferencia como «pretexto»: presencia léxica confundida con afirmación técnica, sin mecanismo causal ni evaluación comparativa — source: 1bfe45ede61ee575
- El contexto que decidiría la afirmación (por qué JavaScript en lugar de XSLT, en qué caso) no está ingerido — source: 1bfe45ede61ee575

## Why it matters
Es un caso concreto de un modo de fallo recurrente del pipeline: cuando el contexto no se recupera, el solapamiento de vocabulario produce señal aparente. Sirve como ejemplo operativo para calibrar el filtro, no como hallazgo sobre XML.

`supports` la nota sobre el contexto no ingerido: la ausencia de contexto es la condición que habilita el falso positivo. `relates_to` la nota sobre un lenguaje de propósito general ya presente en el runtime, que sí formula un argumento de coste.

## Links
- supports → [[xml-human-readable-sin-xslt-contexto-no-ingerido]]
- derived_from → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- relates_to → [[js-como-lenguaje-general-ya-presente-en-el-runtime]]
