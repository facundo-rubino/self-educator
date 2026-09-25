---
id: shadow-roots-mismatch-lexico-clustering-css-frente-brief
title: «Shadow» como falso positivo léxico de clustering frente al brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- df4836a1d89bcba4
tags:
- falso-positivo-clustering
- mismatch-lexico
- css
- gating-topico
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: derived_from
---

## What it is
El ítem entró al brief pese a concernir autoría de artefactos alrededor de un concepto CSS, con solapamiento topical casi nulo respecto a agentes de IA, liderazgo técnico, docencia u oficio de ingeniería. Es un fallo de gating topológico del pipeline.

## Evidence
- El clúster contiene un único ítem RSS de bajo engagement cuyo contenido es un prompt a un modelo de IA para construir un artefacto CSS — source: df4836a1d89bcba4
- El documento está etiquetado solo con «css», sin relación con los ejes declarados del brief — source: df4836a1d89bcba4
- El ítem tiene novelty 0.00 y surprise 0.50: scores neutros que no aportan información nueva — source: df4836a1d89bcba4

## Why it matters
Si el pipeline debe alimentar briefs sobre oficio de ingeniería y desarrollo asistido por IA, este ítem es probablemente un miss de clustering o de filtrado por relevancia, y puede indicar una laguna en el gating topológico. Anclar al lector en un ejemplo CSS irrelevante diluye el brief.

Se relaciona con el patrón general de solapamiento léxico como falso positivo de clustering («agents»/«servers»). Deriva del singleton CSS sin engagement, cuyo score neutro es el síntoma de la misma falla.

## Links
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- derived_from → [[shadow-roots-live-examples-singleton-sin-engagement]]
