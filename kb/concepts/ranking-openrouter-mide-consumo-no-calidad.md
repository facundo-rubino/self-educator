---
id: ranking-openrouter-mide-consumo-no-calidad
title: El ranking de OpenRouter mide consumo de tokens, no calidad del modelo
type: concept
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
- openrouter
- rankings
- seleccion-de-modelo
- agentes
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: riesgo-de-over-indexar-nombres-de-modelos
  type: relates_to
- to: hy3-lidera-ranking-openrouter-sin-datos-de-capacidades
  type: supports
---

## What it is
Un leaderboard de enrutamiento como el de OpenRouter agrega tokens efectivamente enrutados por el servicio; mide popularidad de consumo, no desempeño en tareas. Un modelo puede encabezarlo por ser gratuito, por promoción, por créditos iniciales o por tráfico sintético, sin ser mejor para programar ni para tool use.

## Evidence
- El reporte advierte que el ranking de OpenRouter mide consumo (tokens enrutados) y no necesariamente calidad — source: sig-368ebd05c66c.
- El reporte atribuye el posible liderazgo a precio gratuito, promoción o tráfico sintético como explicaciones alternativas al mérito técnico — source: sig-368ebd05c66c.

## Why it matters
Antes de adoptar un modelo como motor de agentes de código hay que exigir benchmarks reproducibles de coding, tool use, contexto largo, latencia y costo; un puesto alto en un leaderboard de consumo no es evidencia de ninguna de esas dimensiones y puede inducir una migración de stack prematura.

Se relaciona con el riesgo de over-indexar en nombres de modelos sin evidencia. Es el criterio interpretativo que sostiene la lectura de que el liderazgo de Hy3 no es accionable.

## Links
- relates_to → [[riesgo-de-over-indexar-nombres-de-modelos]]
- supports → [[hy3-lidera-ranking-openrouter-sin-datos-de-capacidades]]
