---
id: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
title: '«Task-Specific LLM Evals that Do & Don''t Work»: título y alcance declarado
  sin contenido ingerido'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-29'
sources:
- 93963a5f93e58d05
tags:
- corpus-truncado
- evals
- ingesta
- ingesta-truncada
- llm
- matching-por-titulo
- modo-de-fallo
- ruido
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: relates_to
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: supports
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: supports
---

## What it is
El título promete un juicio sobre qué evals funcionan y cuáles no, pero no hay cuerpo ingerido que desarrolle ese juicio. Lo único recuperado es la descripción de alcance (clasificación, resumen, traducción, copyright, toxicidad).

## Evidence
- El cluster contiene un único documento titulado «Task-Specific LLM Evals that Do & Don't Work» — source: 93963a5f93e58d05
- Su descripción se limita a enumerar las familias de tarea cubiertas; no se incluye el texto completo — source: 93963a5f93e58d05

## Why it matters
Sin cuerpo no hay «do & don't work» que citar. Cualquier afirmación sobre qué evals fallan o funcionan sería invención a partir del título.

Sostiene el registro del alcance declarado en task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad y se relaciona con task-specific-llm-evals-singleton-engagement-cero, que documenta el otro artefacto de ingesta del mismo documento.

## Links
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
