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
updated: '2026-10-12'
sources:
- 93963a5f93e58d05
tags:
- agentes
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
- pregunta-abierta
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-10-12'
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
- to: task-specific-llm-evals-sin-conexion-con-agentes-o-docencia
  type: relates_to
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
---

## What it is
Las cinco familias declaradas (clasificación, resumen, traducción, copyright, toxicidad) son tareas de NLP general. Ninguna de ellas es una eval de generación o edición de código, y ninguna es una eval de un asistente de enseñanza. Queda abierto si el documento completo las cubriría.

## Evidence
- El documento solo nombra clasificación, resumen, traducción, regurgitación de copyright y toxicidad — source: 93963a5f93e58d05
- No aparece en el extracto ninguna familia de tarea de código, depuración, estimación ni docencia — source: 93963a5f93e58d05

## Why it matters
Si un dev-líder quiere evaluar un agente antes de confiarle código o material de clase, este listado no le da la familia de tarea que necesita. La pregunta abierta es si eso es un límite del documento o de la extracción; el extracto actual no permite distinguirlo.

`derived_from` la nota sobre las familias declaradas como único contenido verificable. Se relaciona con la nota ya existente sobre la falta de conexión del documento con agentes o docencia, sin contradecirla: aquí la pregunta es más estrecha — el desajuste está en la nomenclatura de tareas, no solo en la relevancia al brief.

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
- relates_to → [[task-specific-llm-evals-sin-conexion-con-agentes-o-docencia]]
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
