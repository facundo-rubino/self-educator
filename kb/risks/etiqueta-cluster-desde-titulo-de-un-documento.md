---
id: etiqueta-cluster-desde-titulo-de-un-documento
title: La etiqueta de un clúster puede venir del título de uno solo de sus documentos
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
- sig-9f3c75dfc038
tags:
- clustering
- etiquetado
- rss
- pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: cluster-precios-suben-incoherente-sin-cuerpo
  type: derived_from
- to: cluster-heterogeneo-como-vertedero-de-firehose
  type: supports
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
---

## What it is
En el clúster «How it feels watching prices go up», la etiqueta se extrae del título de una sola submission [d1527a2b6941e00b] y no describe a los otros tres documentos, que tratan sobre hardware, antitrust y un videojuego [7bdc84910064aa0e; da14fa21b0ee5332; f4b8430ad9b92d01]. La «señal» es una coincidencia de nombres, no un hallazgo compartido.

## Evidence
- La etiqueta del clúster coincide con el título de un único documento — source: sig-9f3c75dfc038
- Los otros tres documentos no comparten ese tema — source: 7bdc84910064aa0e; da14fa21b0ee5332; f4b8430ad9b92d01

## Why it matters
Un etiquetado que hereda el título de un solo miembro produce la apariencia de un tema común donde no lo hay. Hace que un artefacto de agregación pase por hallazgo semántico y contamina los filtros aguas abajo.

Deriva del caso concreto del clúster de precios y soporta la caracterización general de clústeres heterogéneos como vertederos de firehose y la de falsos positivos por embeddings.

## Links
- derived_from → [[cluster-precios-suben-incoherente-sin-cuerpo]]
- supports → [[cluster-heterogeneo-como-vertedero-de-firehose]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
