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
updated: '2026-09-24'
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
last_reinforced: '2026-09-24'
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
---

## What it is
El alcance declarado —clasificación, resumen, traducción, copyright regurgitation, toxicidad [93963a5f93e58d05]— no incluye evals de código ni de asistentes de enseñanza. Queda abierto si existe una extensión de la taxonomía a esos dominios o si el documento simplemente no los trata.

## Evidence
- Las familias de tarea enumeradas son clasificación, resumen, traducción, copyright regurgitation y toxicidad — source: 93963a5f93e58d05
- El análisis señala que estas categorías son adyacentes pero no directamente sobre los temas centrales del brief — source: 93963a5f93e58d05

## Why it matters
El brief que importa aquí es fiabilidad de agentes al programar, gestionar y enseñar. Ninguna de las cinco familias declaradas mide eso, así que este documento no puede sostener conclusiones sobre aceptación de agentes de coding sin un puente que la evidencia no provee.

`derived_from` la nota de alcance declarado, que enumera las tareas. Se relaciona con la nota existente sobre evaluación específica por tarea como infraestructura de fiabilidad: comparten tema, pero esta fuente no aporta el tramo de código o docencia que aquella nota necesitaría.

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
