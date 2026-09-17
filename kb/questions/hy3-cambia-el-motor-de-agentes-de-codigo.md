---
id: hy3-cambia-el-motor-de-agentes-de-codigo
title: 'Hipótesis: un cambio en el ranking de modelos obliga a reelegir el motor de
  agentes de código'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- sig-368ebd05c66c
tags:
- agentes-de-codigo
- seleccion-de-modelo
- tool-use
base_confidence: 0.2
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: hy3-lidera-ranking-openrouter-sin-datos-de-capacidades
  type: derived_from
- to: ranking-openrouter-mide-consumo-no-calidad
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
---

## What it is
Si Hy3 resultara tener buen desempeño en código y tool use, podría volverse candidato al motor de agentes de programación de un equipo. El cluster no aporta ninguna medición de esas capacidades, así que la hipótesis queda planteada y sin resolver.

## Evidence
- El reporte sostiene que si Hy3 muestra buen desempeño en código y tool use podría convertirse en candidato para el motor de agentes, pero el cluster no aporta medición alguna de esas capacidades — source: sig-368ebd05c66c.
- El reporte afirma que la señal es de infraestructura de modelos, no de práctica de docencia o liderazgo técnico — source: sig-368ebd05c66c.

## Why it matters
Para un dev que lidera proyectos y agentes, la pregunta operativa no es quién lidera un ranking sino qué modelo conviene para cada tarea. Contestarla requiere el mismo tipo de prueba acotada que se usa antes de comprometer features dependientes del proveedor.

Se deriva de la falta de datos de capacidades de Hy3. Comparte método con el patrón de spike por proveedor: medir antes de comprometer.

## Links
- derived_from → [[hy3-lidera-ranking-openrouter-sin-datos-de-capacidades]]
- relates_to → [[ranking-openrouter-mide-consumo-no-calidad]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
