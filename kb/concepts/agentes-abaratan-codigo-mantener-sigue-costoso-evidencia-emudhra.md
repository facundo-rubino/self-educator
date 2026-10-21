---
id: agentes-abaratan-codigo-mantener-sigue-costoso-evidencia-emudhra
title: '«Code is cheap but maintenance isn''t»: evidencia repetida del argumento mantenimiento-vs-generación'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 01910c0f29cb0570
tags:
- agentes
- mantenimiento
- electron
- coste
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: supports
- to: coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron
  type: supports
- to: generacion-barata-no-elimina-coste-de-mantenimiento
  type: supports
- to: complejidad-esencial-vs-accidental-brooks
  type: relates_to
---

## What it is
Aunque los agentes de codificación abaraten los ports nativos, Anthropic sigue enviando Claude como app Electron porque el código es barato y el mantenimiento no. Es un argumento de coste de ownership, no de capacidad de generación.

## Evidence
- Si los agentes abaratan los ports nativos, la razón de seguir con Electron es que «code is cheap but maintenance isn't» — source: 01910c0f29cb0570

## Why it matters
Desplaza la pregunta de adopción de agentes: el cuello de botella no es escribir el código inicial sino el mantenimiento y el ownership post-entrega, que no se abaratan proporcionalmente.

Refuerza `agentes-abatatan-ports-mantener-sigue-costoso`, `coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron` y `generacion-barata-no-elimina-coste-de-mantenimiento`. Es un caso concreto del marco de `complejidad-esencial-vs-accidental-brooks`.

## Links
- supports → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- supports → [[coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron]]
- supports → [[generacion-barata-no-elimina-coste-de-mantenimiento]]
- relates_to → [[complejidad-esencial-vs-accidental-brooks]]
