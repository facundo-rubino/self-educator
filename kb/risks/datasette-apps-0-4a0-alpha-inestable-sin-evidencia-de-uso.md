---
id: datasette-apps-0-4a0-alpha-inestable-sin-evidencia-de-uso
title: 'datasette-apps 0.4a0 y datasette-agent 0.6a0 son alphas: inferencia provisional
  y sin uso demostrado'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-16'
updated: '2026-11-16'
sources:
- 34ebd7c4756f64e9
- 783baeb398598850
tags:
- datasette
- alpha
- single-source
- release-notes
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-11-16'
provenance:
  scale: S
  query: null
links:
- to: datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes
  type: relates_to
- to: datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage
  type: relates_to
- to: datasette-cluster-low-novelty-engagement-zero
  type: relates_to
- to: datasette-cluster-mezcla-alpha-patch-y-plugin
  type: supports
---

## What it is
Las releases 0.4a0 y 0.6a0 son alphas: APIs y comportamiento inestables, sujetos a reversión o reescritura. La evidencia es de una sola fuente (las notas de release del propio autor), sin corroboración independiente ni evidencia de uso en el clúster.

## Evidence
- 0.4a0 y 0.6a0 son releases alpha — source: 34ebd7c4756f64e9, 783baeb398598850
- La fuente es única (notas de release del autor), sin corroboración ni uptake de terceros en el clúster — source: 34ebd7c4756f64e9, 783baeb398598850
- El propio análisis declara low-novelty maintenance signal, no una tesis nueva — source: 34ebd7c4756f64e9, 783baeb398598850

## Why it matters
Cualquier inferencia sobre el «modelo de dos capas agente/app» derivada de dos alphas es provisional como máximo. La afirmación «small incremental alpha releases» se lee directamente de los números de versión: descripción, no inferencia. La confianza ajustada a 0.18 es la correcta para el claim analítico.

Coincide con la nota existente sobre el clúster Datasette como resumen de changelog sin corroboración externa ni impacto medible, y refuerza la observación de que el clúster mezcla alpha, parche y plugin bajo una etiqueta.

## Links
- relates_to → [[datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes]]
- relates_to → [[datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage]]
- relates_to → [[datasette-cluster-low-novelty-engagement-zero]]
- supports → [[datasette-cluster-mezcla-alpha-patch-y-plugin]]
