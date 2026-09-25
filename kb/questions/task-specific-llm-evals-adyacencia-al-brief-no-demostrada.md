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
updated: '2026-09-25'
sources:
- 93963a5f93e58d05
tags:
- brief
- evals
- llm
- matching
- relevancia
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-09-25'
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
---

## What it is
Pregunta abierta: el ítem entra al brief por la palabra «evals», pero no hay evidencia ingerida de que trate sobre evals de agentes de código, de gestión o de docencia. La proximidad temática es de vocabulario compartido, no de contenido.

## Evidence
- El ítem es un único documento RSS con novelty=0.00 y corroboración=0.50 — source: 93963a5f93e58d05
- El documento no aporta evidencia directa sobre cómo un líder técnico o docente usa agentes — source: 93963a5f93e58d05

## Why it matters
Si el match fuera solo léxico, revisar este ítem tiene retorno esperado bajo frente a material que sí cubre los ejes del brief. Queda como pregunta porque el texto completo, si se ingiere, podría cambiar el veredicto.

`derived_from` el alcance declarado: la lista de familias de tarea es lo que permite sospechar que el match es léxico. Se relaciona con el patrón de falsos positivos por vocabulario genérico de infraestructura.

## Links
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-no-es-verdad]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo]]
- relates_to → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
- relates_to → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
