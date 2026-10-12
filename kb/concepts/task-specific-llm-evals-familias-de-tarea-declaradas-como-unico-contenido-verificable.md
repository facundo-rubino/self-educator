---
id: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
title: Las familias de tarea declaradas son el único contenido verificable del documento
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-10-12'
sources:
- 93963a5f93e58d05
tags:
- alcance
- bajo-contenido
- contenido-verificable
- evals
- evidence-scope
- evidencia
- ingesta
- llm
- llm-evals
- pipeline
- task-specific
- taxonomia
base_confidence: 0.1
half_life_days: 180
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: supports
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: task-families-evaluadas-en-el-documento-evals
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: derived_from
---

## What it is
La lista de categorías de tarea (clasificación, resumen, traducción, regurgitación de copyright, toxicidad) es lo único que el documento [93963a5f93e58d05] enuncia de forma verificable. Todo lo demás — criterios, resultados, argumento comparativo — está ausente.

## Evidence
- Cinco categorías de tarea nombradas explícitamente: classification, summarization, translation, copyright regurgitation, toxicity — source: 93963a5f93e58d05
- No se aportan definiciones operativas, métricas ni ejemplos para ninguna de las cinco — source: 93963a5f93e58d05

## Why it matters
Sirve como inventario nominal, no como guía. Tratarlo como guía de selección de evals sería atribuirle al texto una metodología que no contiene. Como inventario, además, estas familias son NLP general: no cubren evals de código ni de asistentes de enseñanza, que son los que tocarían el brief.

`derived_from` la nota de riesgo sobre el mismo documento, porque esta observación solo tiene sentido como descripción de lo poco que el documento sí entrega. Se relaciona con las notas existentes sobre familias de tarea y sobre el alcance declarado del documento de evals: son la misma observación registrada antes, y esta nota la repite sin añadir evidencia nueva.

## Links
- supports → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[task-families-evaluadas-en-el-documento-evals]]
- derived_from → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
