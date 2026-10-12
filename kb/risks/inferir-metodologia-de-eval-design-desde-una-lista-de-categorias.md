---
id: inferir-metodologia-de-eval-design-desde-una-lista-de-categorias
title: Inferir metodología de diseño de evals desde una lista de categorías de tarea
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-12'
updated: '2026-10-12'
sources:
- 93963a5f93e58d05
tags:
- metodologia
- evals
- fiabilidad
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: afirmar-aptitud-de-modelo-o-agente-desde-categorias-de-eval-sin-mecanismo
  type: relates_to
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
---

## What it is
De cinco nombres de categoría no se sigue ninguna metodología: ni cómo construir el conjunto de datos, ni cómo puntuar, ni cómo decidir qué eval «funciona». Escribir esa metodología y citar este documento como respaldo sería inventarla.

## Evidence
- Solo hay categorías nombradas; no hay criterios ni pasos de construcción — source: 93963a5f93e58d05
- No hay ejemplos de evals que funcionen ni de evals que fallen — source: 93963a5f93e58d05

## Why it matters
Cierra la puerta a la tentación más probable con este documento: usarlo como checklist de diseño. Un checklist exige el «cómo»; aquí solo está el «sobre qué».

`derived_from` la nota de familias declaradas como único contenido verificable. Se relaciona con el riesgo de afirmar aptitud de un agente desde categorías de eval: ambos son puentes que el documento no autoriza.

## Links
- relates_to → [[afirmar-aptitud-de-modelo-o-agente-desde-categorias-de-eval-sin-mecanismo]]
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
