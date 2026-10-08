---
id: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
title: '«Task-Specific LLM Evals that Do & Don''t Work»: título y alcance declarado
  sin contenido ingerido'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-08'
sources:
- 93963a5f93e58d05
tags:
- corpus-truncado
- evals
- ingesta
- ingesta-truncada
- llm
- matching-por-titulo
- modo-de-fallo
- riesgo
- ruido
- titulo-sin-cuerpo
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: relates_to
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: supports
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: relates_to
---

## What it is
El titular «Do & Don't Work» promete un veredicto sobre qué evals funcionan y cuáles no. El cuerpo ingerido no contiene ese veredicto: sólo el alcance declarado. Leer la promesa del título como hallazgo sería codificar un claim que el texto ingerido no sostiene.

## Evidence
- El único contenido ingerido es el titular y la enumeración de tareas cubiertas — source: 93963a5f93e58d05
- El engagement es 0, de modo que no hay señal externa sobre la calidad del tratamiento — source: 93963a5f93e58d05

## Why it matters
El modo de fallo del matching por título: usar «evals that don't work» como guía operativa para decidir qué evals aplicar en un flujo de agentes, cuando el texto que lo argumenta no está en el corpus.

Es la cara de riesgo de la nota de alcance declarado; el paso accionable que el analista identifica (retrieval del texto completo) queda fuera del alcance de compilación.

## Links
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
