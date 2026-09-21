---
id: evals-llm-genericas-fuera-del-alcance-del-brief
title: Las evals de LLM genéricas quedan fuera del alcance del brief de agentes para
  coding
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-21'
sources:
- 93963a5f93e58d05
tags:
- alcance
- alcance-del-brief
- brief
- evals
- llm-evals
- topic-drift
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
- to: bridge-especulativo-de-eval-por-tarea-a-practica-de-liderazgo
  type: derived_from
- to: gobernanza-de-evaluaciones-ia-fuera-del-brief-de-dev
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: contradicts
---

## What it is
El brief cubre agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico de equipos chicos, oficio de software engineering, productividad y técnicas de estudio. La evaluación genérica de LLM por familia de tarea no es ninguno de esos ejes tal como se presenta aquí.

## Evidence
- El documento no menciona programación, docencia, gestión de equipos ni productividad — source: 93963a5f93e58d05
- El resumen enumera tareas de NLP general, no evals de código ni de asistentes de enseñanza — source: 93963a5f93e58d05

## Why it matters
Queda abierto si existe una variante de este tema que sí entre al brief: evals construidas para asistentes de código, para revisión de PRs o para calidad de material didáctico. Hasta que aparezca, corresponde dejar el tema fuera del cupo en lugar de estirar su alcance. La docencia de programación entry-level se sigue en el profile `teaching` de pogba, así que el ángulo educativo tampoco compite aquí.

`derived_from` la nota que marca el puente especulativo. Se relaciona con `gobernanza-de-evaluaciones-ia-fuera-del-brief-de-dev`, que ya registró un desplazamiento parecido. Se marca `contradicts` contra la nota con el mismo id ya existente: esa nota afirma el cierre del tema como fuera de alcance, mientras esta evidencia sólo permite decir que el documento no lo cubre —una diferencia entre ausencia en la fuente y exclusión del brief que `edu reconcile` debe resolver con ambas a la vista.

## Links
- derived_from → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[relevancia-no-es-verdad]]
- derived_from → [[bridge-especulativo-de-eval-por-tarea-a-practica-de-liderazgo]]
- relates_to → [[gobernanza-de-evaluaciones-ia-fuera-del-brief-de-dev]]
- contradicts → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
