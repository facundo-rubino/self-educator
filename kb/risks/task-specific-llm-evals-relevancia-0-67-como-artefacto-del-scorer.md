---
id: task-specific-llm-evals-relevancia-0-67-como-artefacto-del-scorer
title: 'relevance=0.67 sin claims extraíbles: artefacto del scorer, no conexión temática'
type: risk
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
- scoring
- filtro
- evals
- llm
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
- to: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
  type: relates_to
- to: task-specific-llm-evals-relevancia-lexica-no-tematica
  type: supports
---

## What it is
La relevance de 0.67 del clúster no se corresponde con contenido extraíble: no hay documento que discuta agentes de código, estimación, secuenciación, alcance ni técnicas de estudio [93963a5f93e58d05]. El match parece venir del vocabulario de superficie («evals», «LLM») frente al tópico, no de solapamiento semántico [93963a5f93e58d05].

## Evidence
- El clúster tiene novelty 0.00, corroboración 0.50 y relevance 0.67 para un tópico centrado en agentes de IA para programar, gestionar y enseñar — source: 93963a5f93e58d05
- El documento no discute por sí mismo agentes aplicados a programación, estimación, secuenciación, alcance ni técnicas de estudio — source: 93963a5f93e58d05

## Why it matters
Un score medio-alto que no se traduce en claims invita a colar el ítem en análisis donde no aporta. Conviene tratar la relevance como techo de cribado, no como permiso de promoción al brief.

Se deriva de la nota sobre las familias de tarea declaradas y refuerza el riesgo previamente registrado de relevance 0.67 sin evidencia extraíble. También apoya la nota que ya califica este match como léxico y no temático.

## Links
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
- relates_to → [[relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer]]
- supports → [[task-specific-llm-evals-relevancia-lexica-no-tematica]]
