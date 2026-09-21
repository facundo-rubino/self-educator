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
updated: '2026-09-21'
sources:
- 93963a5f93e58d05
tags:
- corpus-truncado
- evals
- ingesta-truncada
- llm
- matching-por-titulo
- modo-de-fallo
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-09-21'
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
---

## What it is
El material recuperado de este documento consiste en título y línea de resumen. El título promete un juicio evaluativo («that Do & Don't Work») y el resumen enumera tareas, pero no hay cuerpo, criterios, autores ni texto que sostenga el juicio prometido.

## Evidence
- El título del documento es «Task-Specific LLM Evals that Do & Don't Work» — source: 93963a5f93e58d05
- El resumen sólo lista tareas evaluadas, sin datos, benchmarks ni metodología — source: 93963a5f93e58d05

## Why it matters
Cualquier afirmación sobre qué evals funcionan y cuáles no, extraída de esta fuente, sería invención: el documento en el pipeline es una cáscara. El riesgo es asimétrico: el título invita a citarlo como marco de criterios y el cuerpo que lo respaldaría no fue ingerido.

`relates_to` la nota que registra el singleton sin engagement; ambas describen el mismo vacío desde ángulos distintos. Se apoya en `mecanica-de-evals-afirmada-desde-solo-titulo-rss` —el modo de fallo nombrado exactamente— y en `pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss`. Se relaciona con `afirmacion-de-capacidad-desde-fragmento-de-una-linea`: afirmar un juicio desde un fragmento de una línea.

## Links
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
