---
id: xml-human-readable-sin-xslt-asuncion-de-runtime-js
title: La frase «JavaScript is right there» asume un runtime JS que el documento no
  declara
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-06'
sources:
- 1bfe45ede61ee575
tags:
- xml
- xslt
- javascript
- supuestos
base_confidence: 0.2
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: derived_from
- to: xml-human-readable-sin-xslt-contexto-no-ingerido
  type: relates_to
---

## What it is
Riesgo inferencial: la recomendación implícita de usar JavaScript en lugar de XSLT descansa en el supuesto no declarado de que el entorno de destino ya ejecuta JavaScript. En pipelines estáticos o consumidores sin runtime JS, XSLT u otro tooling pueden seguir siendo la opción adecuada, y el documento no lo aborda.

## Evidence
- El cuerpo del documento es la frase «JavaScript is right there» sin condiciones de entorno — source: 1bfe45ede61ee575
- No hay especificación de audiencia, pipeline ni consumidor en el cuerpo ingerido — source: 1bfe45ede61ee575

## Why it matters
Tomar la frase como regla general produciría una recomendación mal calibrada en contextos sin JS. El riesgo no es que la frase sea falsa, sino que su validez está acotada por un supuesto que el documento no explicita.

Deriva de la nota principal del ítem. Se relaciona con la nota de contexto no ingerido: ambas señalan que la decisión real depende de información que el documento no aporta.

## Links
- derived_from → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- relates_to → [[xml-human-readable-sin-xslt-contexto-no-ingerido]]
