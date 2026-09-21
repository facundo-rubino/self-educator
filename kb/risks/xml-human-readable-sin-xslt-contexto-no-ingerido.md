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
updated: '2026-09-21'
sources:
- 1bfe45ede61ee575
tags:
- xml
- xslt
- contexto-ausente
- recomendacion-no-generalizable
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: supports
---

## What it is
La recomendación implícita —renderizar XML con JavaScript en vez de XSLT— solo sería evaluable sabiendo dónde ocurre la transformación (cliente o build time), el tamaño de los documentos XML, el volumen de código JS necesario frente a una hoja XSLT declarativa y si el XML es de confianza. Nada de eso aparece en la fuente.

## Evidence
- El documento no ofrece código, ejemplo ni argumento: todo el apoyo es «JavaScript is right there» — source: 1bfe45ede61ee575
- El crítico observa que el contexto (SSR, transform en build, seguridad de renderizar XML no confiable en cliente) está ausente, por lo que la recomendación puede no generalizar — source: 1bfe45ede61ee575
- El crítico señala que XSLT está hecho precisamente para transformación declarativa XML→XML/HTML, algo que el documento no aborda — source: 1bfe45ede61ee575

## Why it matters
Fija explícitamente el techo epistémico del ítem: no es evidencia de que JavaScript sea mejor opción, solo de que alguien lo afirmó sin argumento. Evita que el grafo herede una heurística de selección tecnológica sin condiciones.

Deriva de `xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido`, que documenta la ausencia de cuerpo. Es una instancia de `afirmar-constraint-de-diseno-desde-solo-titulo-rss`.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
