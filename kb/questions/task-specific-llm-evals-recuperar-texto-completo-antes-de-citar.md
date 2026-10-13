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
updated: '2026-10-13'
sources:
- 93963a5f93e58d05
tags:
- evals
- llm
- ingesta
- citacion
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: relates_to
---

## What it is
El clúster se evaluó sobre un ítem RSS cuyo cuerpo no se recuperó [93963a5f93e58d05]. Antes de citar este documento en decisiones sobre evals, docencia o arneses de calificación, hace falta el texto completo; el resumen disponible no contiene claims sobre agentes ni sobre práctica de ingeniería [93963a5f93e58d05].

## Evidence
- El clúster contiene un único ítem RSS de bajo engagement con solo título y lista de categorías — source: 93963a5f93e58d05
- El clúster no presenta contenido sobre agentes aplicados a programar, estimación, secuenciación, alcance ni técnicas de estudio — source: 93963a5f93e58d05

## Why it matters
El pipeline evalúa clústeres cuyo cuerpo no recuperó; citar sin recuperar convierte el título en fuente. La acción concreta es un retrieval de texto completo antes de que el ítem entre en cualquier brief o material de clase.

Se deriva de la nota sobre las familias de tarea declaradas y se relaciona con el riesgo ya registrado de pipelines que puntúan clústeres RSS sin cuerpo, del que este es un caso más.

## Links
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
- relates_to → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
