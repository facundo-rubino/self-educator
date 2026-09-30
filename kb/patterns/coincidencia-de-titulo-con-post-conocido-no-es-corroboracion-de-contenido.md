---
id: coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido
title: Una coincidencia de título con un post conocido no es corroboración de su contenido
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- dec9f3cc9a87f904
tags:
- pipeline
- evidencia
- clustering
- falsos-positivos
base_confidence: 0.85
half_life_days: 365
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: afirmar-contenido-de-react-for-two-computers-seria-especulacion
  type: supports
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: derived_from
- to: falso-positivo-de-clustering-por-similitud-de-plantilla
  type: supports
---

## What it is
Que el título de un documento coincida con el de una pieza publicada en otro sitio no convierte al documento en esa pieza. El cuerpo ingerido sigue siendo el que es, y la inferencia de contenido a partir del título es circular.

## Evidence
- El título «React for Two Computers» coincide con un post conocido, pero el cuerpo ingerido es solo «Two things, one origin.», sin autoría verificable — fuente: dec9f3cc9a87f904
- El engagement es 0 y el novelty del cluster es 0.00 — fuente: dec9f3cc9a87f904

## Why it matters
Es un modo de fallo concreto del pipeline: el score y el filtro pueden dejar pasar un item por vocabulario del título y luego permitir que el analista atribuya al documento un contenido que proviene de su memoria del post original, no del corpus.

Se deriva del patrón `validacion-de-senal-por-contenido-no-por-titulo`: la validación exige solapamiento de contenido, no de título. Apoya a `afirmar-contenido-de-react-for-two-computers-seria-especulacion` y refuerza `falso-positivo-de-clustering-por-similitud-de-plantilla`.

## Links
- supports → [[afirmar-contenido-de-react-for-two-computers-seria-especulacion]]
- derived_from → [[validacion-de-senal-por-contenido-no-por-titulo]]
- supports → [[falso-positivo-de-clustering-por-similitud-de-plantilla]]
