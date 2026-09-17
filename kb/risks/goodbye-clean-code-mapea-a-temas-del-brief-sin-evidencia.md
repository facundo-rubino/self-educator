---
id: goodbye-clean-code-mapea-a-temas-del-brief-sin-evidencia
title: Mapear «Goodbye, Clean Code» a los temas del brief sería invención
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- bc47e7115f9ba8d0
tags:
- brief
- overfitting-tematico
- evidencia
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: overfitting-tematico-desde-mecanica-ajena
  type: derived_from
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
- to: generalizar-desde-goodbye-clean-code-sin-corroboracion
  type: relates_to
---

## What it is
El propio análisis admite que traducir el ítem a los temas del brief (workflows de agentes, estimación, secuenciamiento, alcance, docencia) sería «invención, no evidencia», porque ninguno de esos temas aparece en el texto recuperado [bc47e7115f9ba8d0].

## Evidence
- El texto solo conserva título y tagline; no hay argumentos ni prácticas — source: bc47e7115f9ba8d0.
- relevance=0.33 y novelty=0.00 indican coincidencia léxica débil con la KB — source: bc47e7115f9ba8d0.

## Why it matters
Incluso aceptando la implicación de que las heurísticas de clean code dependen del contexto, el vínculo con agentes de IA o liderazgo técnico es una coincidencia léxica, no una cadena de evidencia. Registrar la tentación como riesgo evita que se cuele en el grafo como hallazgo.

`derived_from` el riesgo de overfitting temático desde mecánica ajena. `contradicts` la nota que sostiene que la relevancia temática baja no es ruido: aquí la relevancia baja, sin cuerpo recuperado, sí es ruido para el brief.

## Links
- derived_from → [[overfitting-tematico-desde-mecanica-ajena]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[generalizar-desde-goodbye-clean-code-sin-corroboracion]]
