---
id: task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo
title: Las tareas de eval declaradas son NLP general, no evals de código ni de asistentes
  de enseñanza
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-21'
sources:
- 93963a5f93e58d05
tags:
- brief
- cobertura
- codigo
- coding-agents
- docencia
- evals
- llm
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
  type: derived_from
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
- to: task-families-evaluadas-en-el-documento-evals
  type: contradicts
- to: task-families-evaluadas-en-el-documento-evals
  type: derived_from
- to: task-specific-llm-evals-singleton-engagement-cero
  type: supports
- to: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
  type: supports
- to: matching-llm-patterns-relevancia-baja-sin-ejes-del-topic
  type: relates_to
---

## What it is
Las cinco tareas que el documento declara evaluar (classification, summarization, translation, copyright regurgitation, toxicity) son familias de NLP general. Ninguna de ellas es una eval de generación o revisión de código, ni de calidad de un output educativo, ni de comportamiento de un agente sobre un repositorio.

## Evidence
- El resumen del documento enumera classification, summarization, translation, copyright regurgitation y toxicity — source: 93963a5f93e58d05
- El documento no menciona programación, docencia, gestión de equipos ni productividad — source: 93963a5f93e58d05

## Why it matters
Queda abierto si el documento completo —no recuperado— cubre evals de código, y esa laguna es la que decidiría su utilidad para el brief. Mientras no se recupere cuerpo, tratar la enumeración como un marco aplicable a agentes de coding sería sustituir una lista de tareas NLP por una promesa que la fuente no hace.

`derived_from` la nota que fija la enumeración literal. Se apoya en `task-specific-llm-evals-singleton-engagement-cero` y `task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido`, que documentan la ausencia de cuerpo y de apoyo cruzado. Se relaciona con `matching-llm-patterns-relevancia-baja-sin-ejes-del-topic`: misma forma de fallo, un documento que no toca ningún eje del topic.

## Links
- derived_from → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- contradicts → [[task-families-evaluadas-en-el-documento-evals]]
- derived_from → [[task-families-evaluadas-en-el-documento-evals]]
- supports → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[matching-llm-patterns-relevancia-baja-sin-ejes-del-topic]]
