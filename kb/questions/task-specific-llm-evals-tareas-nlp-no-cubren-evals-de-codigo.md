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
updated: '2026-10-02'
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
last_reinforced: '2026-10-02'
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
---

## What it is
La lista de categorías declarada (clasificación, resumen, traducción, copyright regurgitation, toxicidad) es de NLP general. No incluye evaluación de código generado, de asistentes de coding ni de asistentes de enseñanza.

## Evidence
- Tareas enumeradas: clasificación, summarization, translation, copyright regurgitation, toxicity — source: 93963a5f93e58d05
- No aparece ninguna categoría de eval de código ni de docencia — source: 93963a5f93e58d05

## Why it matters
Para un dev que lidera y enseña, ninguna de estas tareas mapea directamente a los artefactos que quiere evaluar (parches, specs, explicaciones didácticas). Pretender transferirlas sin más sería extrapolación no sostenida.

Deriva de `task-families-evaluadas-en-el-documento-evals` y refina `task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad`. Conecta con `aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion` como su versión negativa explícita. Se relaciona con `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad` (la idea metodológica sí podría ser transferible, no las tareas concretas) y con `task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto` (una categoría sí toca un riesgo de producto, pero un solo documento no lo sustenta).

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
