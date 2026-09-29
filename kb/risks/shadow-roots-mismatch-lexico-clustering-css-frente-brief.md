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
updated: '2026-09-29'
sources:
- df4836a1d89bcba4
tags:
- clustering
- css
- falso-positivo
- falso-positivo-clustering
- filtro
- gating-topico
- matching-lexico
- mismatch-lexico
- precisión
- shadow-roots
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: derived_from
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: relates_to
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
- to: shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido
  type: relates_to
- to: shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada
  type: relates_to
- to: hypothe-rewrite-not-a-real-id
  type: relates_to
---

## What it is
Un ítem de CSS sobre shadow roots entró al pipeline pese a relevance=0.33 y novelty=0.00. El solapamiento léxico de vocabulario técnico genérico es un mecanismo plausible de admisión, pero el reporte no demuestra que el filtro determinista haya fallado más allá de este ítem aislado.

## Evidence
- Relevancia marginal (0.33) y novedad nula (0.00) para un documento etiquetado «css», sin relación declarada con agentes de IA, liderazgo o docencia — source: df4836a1d89bcba4
- El clúster contiene un solo documento: no hay corroboración interna — source: df4836a1d89bcba4

## Why it matters
Un único ítem fuera de tema es un artefacto de recuperación común y benigno, no por sí solo una prueba de defecto del filtro. La conclusión generalizable que sí sostiene la evidencia es más estrecha: la etiqueta «css» de un título no implica pertenencia al tema del brief.

Se apoya en el mismo documento único que `shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido` y `shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada`. Comparte el modo de fallo «coincidencia léxica en el título» con otros falsos positivos del corpus.

## Links
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- derived_from → [[shadow-roots-live-examples-singleton-sin-engagement]]
- relates_to → [[shadow-roots-live-examples-singleton-sin-engagement]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido]]
- relates_to → [[shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada]]
- relates_to → [[hypothe-rewrite-not-a-real-id]]
