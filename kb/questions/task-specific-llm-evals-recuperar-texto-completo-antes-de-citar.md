---
id: task-specific-llm-evals-recuperar-texto-completo-antes-de-citar
title: Recuperar el texto completo antes de citar «Task-Specific LLM Evals»
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-14'
sources:
- 93963a5f93e58d05
tags:
- citacion
- evals
- evidencia
- ingesta
- llm
- recuperacion
- task-specific-evals
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: derived_from
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
---

## What it is
Pregunta abierta que deja este clúster: ¿el artículo completo contiene guía concreta de «do/don't» para evals por tarea, o es una taxonomía sin veredicto? La evidencia capturada solo enumera categorías.

## Evidence
- El cuerpo ingerido solo enumera familias de tarea, sin métodos, resultados ni recomendaciones — source: 93963a5f93e58d05
- El título promete un veredicto que la evidencia capturada no entrega — source: 93963a5f93e58d05

## Why it matters
Solo tras recuperar el texto completo se puede decidir si el documento pertenece al brief de agentes, liderazgo y docencia, o a un clúster más amplio de evaluación de LLM sin aplicación al brief.

Se deriva de la nota que registra el título sin contenido ingerido. Comparte con `ingesta-truncada-como-riesgo-sistemico-de-cobertura` la dependencia de un paso de recuperación antes de emitir cualquier claim.

## Links
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
- relates_to → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- derived_from → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
