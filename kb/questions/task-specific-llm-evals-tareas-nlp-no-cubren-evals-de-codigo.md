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
updated: '2026-09-29'
sources:
- 93963a5f93e58d05
tags:
- alcance
- brief
- cobertura
- codigo
- coding-agents
- docencia
- evals
- llm
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-29'
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
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: derived_from
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: task-families-evaluadas-en-el-documento-evals
  type: relates_to
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: embedding-de-eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion
  type: relates_to
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: contradicts
---

## What it is
El documento trata sobre metodología de evaluación de LLM en tareas de NLP genéricas, no sobre agentes de IA aplicados a programar, gestionar o enseñar, ni sobre liderazgo técnico, oficio de software engineering o productividad personal.

## Evidence
- El documento trata sobre metodología de evaluación de LLMs en tareas de NLP genéricas y no sobre agentes de IA aplicados a programar, gestionar o enseñar, ni sobre liderazgo técnico, oficio o productividad — source: 93963a5f93e58d05
- El alcance declarado del documento son clasificación, resumen, traducción, regurgitación de copyright y toxicidad — source: 93963a5f93e58d05

## Why it matters
Marca la frontera entre «metodología de evals de NLP» y «evals de agentes de código o de asistentes de enseñanza». Importa porque el salto entre ambas no está autorizado por este documento: cualquier puente habría que construirlo, no citarlo.

Deriva de task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad: sin la lista de tareas no se puede afirmar esta exclusión. Se relaciona con aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion, que registra el modo de fallo si se ignora esta frontera.

## Links
- derived_from → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- contradicts → [[task-families-evaluadas-en-el-documento-evals]]
- derived_from → [[task-families-evaluadas-en-el-documento-evals]]
- supports → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[matching-llm-patterns-relevancia-baja-sin-ejes-del-topic]]
- derived_from → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[task-families-evaluadas-en-el-documento-evals]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[embedding-de-eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion]]
- contradicts → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
