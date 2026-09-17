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
updated: '2026-09-17'
sources:
- 93963a5f93e58d05
tags:
- evals
- codigo
- docencia
- cobertura
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-17'
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
---

## What it is
Las tareas declaradas por el documento (clasificación, resumen, traducción, regurgitación de copyright, toxicidad) [93963a5f93e58d05] no incluyen evaluación de generación de código, revisión de código, tests, ni evaluación de asistentes de enseñanza. Queda abierto si el documento cubre esas tareas más allá del alcance declarado o si simplemente no las aborda.

## Evidence
- Alcance declarado del documento: clasificación, resumen, traducción, regurgitación de copyright y toxicidad — source: 93963a5f93e58d05
- El clúster no aporta ningún otro documento que amplíe esa lista — source: 93963a5f93e58d05

## Why it matters
Si el pipeline necesitaba evals para tareas de código o para evaluar asistentes de enseñanza, este documento no las cubre. La pregunta es si esa ausencia es del documento o del muestreo del clúster.

Deriva de [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]: solo se puede contrastar contra el alcance declarado, no contra el cuerpo. Marca una discrepancia con [[task-families-evaluadas-en-el-documento-evals]], que enumera familias de tarea distintas; la contradicción es de cobertura, no de hecho, y se deja sin resolver. Se alinea con [[evals-llm-genericas-fuera-del-alcance-del-brief]].

## Links
- derived_from → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- contradicts → [[task-families-evaluadas-en-el-documento-evals]]
