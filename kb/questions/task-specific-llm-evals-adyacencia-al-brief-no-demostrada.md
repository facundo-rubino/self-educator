---
id: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
title: '«Task-Specific LLM Evals»: la adyacencia al brief es léxica, no demostrada'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-10-02'
sources:
- 93963a5f93e58d05
tags:
- brief
- clustering
- evals
- fuera-del-brief
- llm
- matching
- matching-lexico
- relevancia
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: relevancia-no-es-verdad
  type: relates_to
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo
  type: relates_to
- to: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
- to: confirmacion-de-evaluacion-por-terceros-no-es-adopcion
  type: relates_to
---

## What it is
Ninguna evidencia del clúster conecta evaluación específica por tarea con agentes de código, liderazgo técnico, craft o productividad. La adyacencia al brief es léxica («evals», «LLM»), no semántica.

## Evidence
- El alcance declarado son tareas NLP generales (clasificación, resumen, traducción, copyright regurgitation, toxicidad) — source: 93963a5f93e58d05
- No hay claim en el clúster que ligue esas tareas a los ejes del brief — source: 93963a5f93e58d05

## Why it matters
Importar este ítem como si abordara el brief sería un error de categoría. La pregunta operativa es si el término «eval» funciona como match léxico suficiente o si el pipeline debería filtrar por eje temático.

Depende de `task-specific-llm-evals-titulo-sin-contenido-ingerido` y `task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo`. Análoga a `matching-llm-patterns-relevancia-lexica-al-brief-de-agentes` y a `evals-llm-genericas-fuera-del-alcance-del-brief`. Conecta con `confirmacion-de-evaluacion-por-terceros-no-es-adopcion`: cosignar categorías de eval no es adoptar práctica.

## Links
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-no-es-verdad]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo]]
- relates_to → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
- relates_to → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- relates_to → [[confirmacion-de-evaluacion-por-terceros-no-es-adopcion]]
