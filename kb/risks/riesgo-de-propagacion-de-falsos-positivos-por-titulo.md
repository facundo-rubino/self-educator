---
id: riesgo-de-propagacion-de-falsos-positivos-por-titulo
title: Riesgo de propagación en cascada de falsos positivos por similitud de título
type: risk
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
- clustering
- falsos-positivos
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido
  type: derived_from
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters
  type: supports
- to: react-for-two-computers-titulo-formula-sin-argumento
  type: supports
---

## What it is
Un documento que entra al pipeline solo por su título puede reaparecer en clusters vecinos por similitud léxica del encabezado, arrastrando el mismo vacío de contenido a cada cluster que toca.

## Evidence
- El documento [dec9f3cc9a87f904] tiene novelty 0.00 y relevancia 0.33: umbral de descarte por contenido, no por título — fuente: dec9f3cc9a87f904
- El cluster se sostiene en un único documento, sin corroboración independiente — fuente: dec9f3cc9a87f904

## Why it matters
Si una pieza vacía se propaga a otros clusters por título, cada propagación hereda el mismo problema. La mitigación apunta al filtro determinista: umbral mínimo de cuerpo sustantivo antes del clustering.

Se deriva de `coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido`. Apoya `clustering-por-embedding-produce-falsos-positivos` y `titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters`.

## Links
- derived_from → [[coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- supports → [[titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters]]
- supports → [[react-for-two-computers-titulo-formula-sin-argumento]]
