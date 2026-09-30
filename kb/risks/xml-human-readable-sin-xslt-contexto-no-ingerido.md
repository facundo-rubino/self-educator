---
id: xml-human-readable-sin-xslt-contexto-no-ingerido
title: El contexto que decidiría «JavaScript en lugar de XSLT» no está ingerido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-30'
sources:
- 1bfe45ede61ee575
tags:
- contexto-ausente
- evidence-gap
- evidencia-faltante
- ingesta
- javascript
- recomendacion-no-generalizable
- xml
- xslt
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: relates_to
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: relates_to
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: supports
- to: xml-pretexto-lexico-javascript-en-el-runtime
  type: supports
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: supports
---

## What it is
El documento solo contiene el título «Making XML human-readable without XSLT» y la línea «JavaScript is right there.» [1bfe45ede61ee575]. No trae código, ejemplo, benchmark ni discusión de tradeoffs. El contexto que permitiría leer la frase como una decisión técnica (¿transformar en cliente con DOMParser y recorrido del DOM? ¿usar una librería XML de un lenguaje general en lugar de un motor XSLT en un pipeline?) no está en el texto ingerido y tendría que aportarlo el lector.

## Evidence
- El contenido entero del documento es el título más la línea «JavaScript is right there.» — source: 1bfe45ede61ee575
- El documento no aporta código, ejemplo ni argumento que desarrolle el mecanismo implícito — source: 1bfe45ede61ee575
- El ítem llega por RSS con engagement=0, sin reacción de audiencia medida — source: 1bfe45ede61ee575

## Why it matters
Cualquier afirmación sobre cómo se haría la transformación sin XSLT es extrapolación del lector, no contenido del documento. Reconocer este hueco evita compilar una técnica no observada y protege la trazabilidad del grafo.

Refuerza la nota sobre la afirmación sin cuerpo del mismo documento y la lectura de «JavaScript is right there» como pretexto léxico. Es el mismo hueco ya registrado en la nota de título sin contenido ingerido.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
- relates_to → [[xml-human-readable-singleton-engagement-cero]]
- relates_to → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[xml-pretexto-lexico-javascript-en-el-runtime]]
- supports → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
