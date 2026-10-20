---
id: generacion-barata-no-elimina-coste-de-mantenimiento
title: La generación barata de código no elimina el coste de mantenimiento
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 01910c0f29cb0570
tags:
- mantenimiento
- coste
- arquitectura
- agentes
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
- to: coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron
  type: relates_to
- to: complejidad-esencial-vs-accidental-brooks
  type: relates_to
- to: agentes-ia-aceleran-trabajo-acotado-y-verificable
  type: relates_to
---

## What it is
Aunque los agentes hagan baratas las reescrituras y la generación de código, el mantenimiento no es barato. El argumento «el código es barato» no debe usarse para justificar complejidad evitable en decisiones de arquitectura.

## Evidence
- Incluso si los agentes abaratan las reescrituras nativas, el mantenimiento no es barato; el reencuadre «el código es barato» no justifica complejidad evitable en arquitectura — source: 01910c0f29cb0570

## Why it matters
En una revisión de liderazgo técnico, «el agente lo puede portar» no es un argumento de mantenimiento. El costo de mantenimiento sigue siendo el lente con el que se evalúa la deuda que se asume.

Es la misma tensión que `agentes-abatatan-ports-mantener-sigue-costoso` y `coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron`. Se ancla en `complejidad-esencial-vs-accidental-brooks`: lo que el agente ahorra es complejidad accidental. Limita la lectura optimista de `agentes-ia-aceleran-trabajo-acotado-y-verificable`.

## Links
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- relates_to → [[coste-de-mantenimiento-frente-a-coste-de-generacion-de-codigo-electron]]
- relates_to → [[complejidad-esencial-vs-accidental-brooks]]
- relates_to → [[agentes-ia-aceleran-trabajo-acotado-y-verificable]]
