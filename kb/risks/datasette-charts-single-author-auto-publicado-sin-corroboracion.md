---
id: datasette-charts-single-author-auto-publicado-sin-corroboracion
title: Los release notes de datasette-charts son auto-publicados por el mismo autor,
  sin corroboración independiente
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-24'
updated: '2026-11-24'
sources:
- d768a418ab58a08f
- 27878e595eaaf299
- 9091e8f0745b1341
tags:
- datasette
- willison
- riesgo
- evidencia
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-11-24'
provenance:
  scale: S
  query: null
links:
- to: datasette-charts-ciclo-idea-prototipo-plugin-integracion
  type: contradicts
- to: levantar-un-cluster-de-un-solo-documento
  type: relates_to
---

## What it is
Los tres documentos del clúster son changelogs/release notes del mismo autor, que construyó el plugin, escribió el changelog y narra la línea de tiempo como historia. No hay engagement registrado, ni reproducibilidad de terceros, ni corroboración independiente (corroboration=0.50).

## Evidence
- Los tres documentos son release notes auto-publicadas del mismo autor sobre el mismo proyecto; novelty=0.24 y engagement no registrado — source: d768a418ab58a08f
- No hay fuente secundaria ni reproducción independiente en el clúster — source: 27878e595eaaf299

## Why it matters
Generalizar este caso a «cómo trabaja un dev que lidera y enseña» sería especulativo. La velocidad (0.1a0 y 0.2a0 en días) puede ser fragilidad de versiones alpha, no un ritmo sostenible. El caso depende del stack y de un modelo concreto.

Contradice el claim de patrón (datasette-charts-ciclo-idea-prototipo-plugin-integracion): una sola fuente interesada no sostiene el patrón. Se relaciona con el riesgo general de levantar un clúster de un solo documento (levantar-un-cluster-de-un-solo-documento).

## Links
- contradicts → [[datasette-charts-ciclo-idea-prototipo-plugin-integracion]]
- relates_to → [[levantar-un-cluster-de-un-solo-documento]]
