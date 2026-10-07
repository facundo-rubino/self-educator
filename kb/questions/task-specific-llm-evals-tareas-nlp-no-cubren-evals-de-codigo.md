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
updated: '2026-10-07'
sources:
- 93963a5f93e58d05
tags:
- agentes-de-codigo
- alcance
- brief
- cobertura
- codigo
- coding-agents
- docencia
- evals
- llm
- nlp
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-10-07'
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
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto
  type: relates_to
- to: task-specific-llm-evals-sin-conexion-con-agentes-o-docencia
  type: supports
---

## What it is
Las familias de tarea que el documento enumera —clasificación, resumen, traducción, regurgitación de copyright, toxicidad— son tareas de NLP general [93963a5f93e58d05]. Ninguna de ellas es evaluación de generación de código, de resolución de issues ni de asistencia a la enseñanza. El documento no menciona evals de código ni de docencia.

## Evidence
- Las familias de tarea declaradas por el resumen son clasificación, resumen, traducción, regurgitación de copyright y toxicidad — fuente: 93963a5f93e58d05

## Why it matters
Corrige el paso habitual de «evals de LLM» a «evals de agentes que programan o enseñan»: la lista declarada no contiene esas tareas, así que ninguna conclusión sobre evals de código o de docencia se apoya en este documento.

Se deriva del alcance declarado del documento. Respalda la nota sobre la ausencia de conexión del documento con agentes de código y docencia.

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
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto]]
- supports → [[task-specific-llm-evals-sin-conexion-con-agentes-o-docencia]]
