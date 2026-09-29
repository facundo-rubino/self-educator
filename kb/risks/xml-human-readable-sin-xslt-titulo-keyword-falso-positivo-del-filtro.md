---
id: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
title: El ítem de XML sobrevivió al filtro determinista por solapamiento de keywords
  del título
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-29'
sources:
- 1bfe45ede61ee575
tags:
- falso-positivo
- falsos-positivos
- filtrado
- pipeline
- xml
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-solo-afirmacion-javascript
  type: derived_from
- to: xml-human-readable-entra-por-coincidencia-lexica
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: supports
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: relates_to
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: supports
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: supports
---

## What it is
Riesgo de precisión del pipeline: un ítem cuyo cuerpo es una sola línea pasa el filtrado y llega a revisión. Las palabras clave de programación en el título bastan para que el documento sobreviva aunque no contenga información.

## Evidence
- El documento tiene como único cuerpo «JavaScript is right there.» — source: 1bfe45ede61ee575
- El documento es de origen rss y tiene engagement cero — source: 1bfe45ede61ee575
- Relevance 0.33 (débil) y novelty 0.00 según el scoring del clúster — source: 1bfe45ede61ee575

## Why it matters
Confirma un coste operativo ya observado: abrir la compuerta por coincidencia léxica obliga a gastar tiempo de revisión en stubs. Un umbral de longitud mínima de cuerpo, antes del análisis, eliminaría este caso sin pérdida.

Es el ejemplo concreto detrás de `xml-human-readable-without-xslt-afirmacion-sin-cuerpo`. Apoya a `relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista` y a `etiqueta-determinista-como-falso-positivo-de-categoria`: el filtro por keywords de título es la causa común de estos falsos positivos.

## Links
- derived_from → [[xml-human-readable-sin-xslt-solo-afirmacion-javascript]]
- supports → [[xml-human-readable-entra-por-coincidencia-lexica]]
- supports → [[xml-human-readable-singleton-engagement-cero]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- relates_to → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- supports → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
