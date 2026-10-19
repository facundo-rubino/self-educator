---
id: task-specific-llm-evals-relevancia-lexica-no-tematica
title: '«Task-Specific LLM Evals»: relevance 0.67 por coincidencia léxica en «evals»,
  no por conexión temática'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-19'
sources:
- 93963a5f93e58d05
tags:
- evals
- falso-positivo-lexico
- lexical-match
- llm-evals
- pipeline
- relevance-scoring
- scoring
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
  type: supports
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: relates_to
- to: how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: derived_from
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: contradicts
---

## What it is
La relevancia 0.67 del clúster no está demostrada por contenido: el vínculo declarado al brief (un dev que lidera, programa con agentes y enseña necesita saber qué evals son fiables) es un puente construido por el analista, no evidencia del documento. Las cinco familias de tarea del artículo son NLP general, no evals de código ni de docencia.

## Evidence
- La relevance declarada (0.67) se afirma, no se demuestra; el vínculo metodológico al brief es un puente construido, no evidencia del clúster — source: 93963a5f93e58d05
- Las familias de tarea cubiertas (clasificación, summarization, traducción, copyright, toxicidad) no incluyen código ni práctica de enseñanza — source: 93963a5f93e58d05

## Why it matters
El solapamiento en la palabra «evals» basta para elevar el score, pero el contenido declarado del artículo no toca ningún eje operativo del brief. Tratar este clúster como señal de evaluación aplicable a agentes de código o docencia sería un falso positivo léxico.

Se deriva del registro de ausencia de contenido ingerido. Comparte el problema de scoring con el singleton sin engagement. Contradice cualquier lectura de que relevance alta equivalga a evidencia temática: aquí la relevance no es verdad operativa.

## Links
- supports → [[task-specific-llm-evals-adyacencia-al-brief-no-demostrada]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- relates_to → [[how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief]]
- derived_from → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- contradicts → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
