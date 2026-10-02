---
id: throughput-local-5090-96gb-ddr5-sin-replicacion
title: 'Throughput de inferencia local (150-200 tok/s decode en 5090 con 96GB DDR5):
  dato autodeclarado sin replicación'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-02'
sources:
- 4b74420b2d25f1da
tags:
- inferencia-local
- hardware
- throughput
- sin-replicacion
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: benchmark-pp512-no-informa-generacion-interactiva
  type: relates_to
- to: delta-de-rendimiento-triangulado-por-una-sola-maquina
  type: relates_to
---

## What it is
Un post autodeclarado reporta 150-200 tok/s de decode y 5-6k de prefill en una 5090 con límite de potencia y 96GB DDR5. Sugiere que cargas de agente en hardware de consumo se están volviendo viables, pero es un único punto de medida sin replicación de terceros.

## Evidence
- Cifras de throughput local (150-200 tok/s decode, 5-6k prefill en una 5090 con límite de potencia y 96GB DDR5) provienen de un post autodeclarado — fuente: 4b74420b2d25f1da.

## Why it matters
Los números de una sola máquina no deben dirigir compras ni compromisos de flujo de trabajo sin replicación independiente. Es el único ítem del clúster que toca prácticas de productividad.

Comparte con la nota sobre pp512 el problema de leer métricas aisladas, y con la nota sobre deltas triangulados por una sola máquina el mismo sesgo de generalización.

## Links
- relates_to → [[benchmark-pp512-no-informa-generacion-interactiva]]
- relates_to → [[delta-de-rendimiento-triangulado-por-una-sola-maquina]]
