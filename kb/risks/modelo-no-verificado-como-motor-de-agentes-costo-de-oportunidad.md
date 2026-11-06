---
id: modelo-no-verificado-como-motor-de-agentes-costo-de-oportunidad
title: 'Reelegir el motor de agentes por un titular de release no verificado: costo
  de oportunidad'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-06'
updated: '2026-11-06'
sources:
- 382d9b6490c36fd5
tags:
- seleccion-de-modelo
- agentes
- costo-de-oportunidad
- verificacion
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-11-06'
provenance:
  scale: S
  query: null
links:
- to: inkling-2-small-anuncio-de-modelo-sin-benchmarks
  type: derived_from
- to: muse-wonder-evaluar-modelo-no-verificado-como-coste-de-oportunidad
  type: supports
- to: senal-de-corte-de-proveedor-vs-desarrollo-no-verificado
  type: supports
- to: separacion-cerebro-manos-modelo-harness-agente
  type: relates_to
---

## What it is
Adoptar un modelo «que gana» en un titular, sin replicar la evaluación en las tareas reales del equipo o del aula, es un riesgo de sobreajuste a novedades. Los benchmarks y nombres de modelos cambian rápido; cualquier decisión de arquitectura de agentes basada solo en este anuncio puede quedar obsoleta en semanas.

## Evidence
- Adoptar un modelo «que gana» en un titular sin replicar la evaluación en las tareas reales del equipo o del aula es un riesgo de sobreajuste a novedades — source: 382d9b6490c36fd5
- Los benchmarks y nombres de modelos cambian rápido; una decisión de arquitectura basada en este anuncio puede quedar obsoleta en semanas — source: 382d9b6490c36fd5

## Why it matters
La mitigación estructural es separar la lógica del flujo (prompts, herramientas, verificación) del proveedor concreto, de modo que el cambio de motor sea barato. Sin esa separación, cada anuncio de modelo arrastra una migración que consume exactamente el cupo que el brief quiere proteger.

Se deriva de `inkling-2-small-anuncio-de-modelo-sin-benchmarks`. Duplica el razonamiento de `muse-wonder-evaluar-modelo-no-verificado-como-coste-de-oportunidad` para otro modelo, y coincide con `senal-de-corte-de-proveedor-vs-desarrollo-no-verificado`. La mitigación se apoya en `separacion-cerebro-manos-modelo-harness-agente`: modelo desacoplado del harness.

## Links
- derived_from → [[inkling-2-small-anuncio-de-modelo-sin-benchmarks]]
- supports → [[muse-wonder-evaluar-modelo-no-verificado-como-coste-de-oportunidad]]
- supports → [[senal-de-corte-de-proveedor-vs-desarrollo-no-verificado]]
- relates_to → [[separacion-cerebro-manos-modelo-harness-agente]]
