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
updated: '2026-10-08'
sources:
- 1bfe45ede61ee575
tags:
- clustering
- filtro-determinista
- matching-lexico
- pipeline
- relevancia
- topico
- xml
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: relates_to
- to: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
  type: supports
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: derived_from
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: relates_to
---

## What it is
Ningún eje del brief (agentes de IA aplicados a programar, gestión, liderazgo técnico, oficio de software, productividad o estudio) aparece en el documento. La conexión observada es vocabulario de plataforma («XML», «JavaScript», «renderizar») que solapa superficialmente con «programar» [1bfe45ede61ee575].

## Evidence
- `relevance=0.33` frente al brief, con `novelty=0.00` y `corroboration=0.50` — source: 1bfe45ede61ee575
- El cuerpo ingerido es una sola frase sin contenido sobre práctica de ingeniería ni docencia — source: 1bfe45ede61ee575

## Why it matters
La pregunta abierta es si el filtro determinista debe admitir ítems cuyo único vínculo con el brief es léxico. Si la respuesta es sí, el costo es ruido de clústeres de un solo documento; si es no, hace falta un criterio de contenido mínimo antes del clustering.

Refuerza `xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro` y deriva del patrón general `validacion-de-senal-por-contenido-no-por-titulo`. Se relaciona con el ítem compilado en `xml-human-readable-without-xslt-afirmacion-sin-cuerpo`.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- relates_to → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
- supports → [[xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro]]
- derived_from → [[validacion-de-senal-por-contenido-no-por-titulo]]
- relates_to → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
