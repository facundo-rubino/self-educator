---
id: task-specific-llm-evals-relevance-0-67-como-artefacto-del-scorer-nueva-evidencia
title: 'relevance=0.67 sin claims extraíbles: artefacto del scorer, no conexión temática'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 93963a5f93e58d05
tags:
- pipeline-artifact
- scoring
- brief-mismatch
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: task-specific-llm-evals-relevancia-0-67-como-artefacto-del-scorer
  type: supports
- to: task-specific-llm-evals-relevancia-lexica-no-tematica
  type: supports
- to: task-specific-llm-evals-sin-conexion-con-agentes-o-docencia
  type: supports
---

## What it is
La relevance de 0.67 del clúster está inflada respecto a la admisión explícita del propio análisis de que la fuente no dice «nada explícito» sobre enseñanza, liderazgo técnico, estimación ni organización personal: los cuatro ejes del brief. El payload sustantivo es cero y sólo lo transporta un puente retórico.

## Evidence
- El documento no dice nada explícito sobre enseñanza, liderazgo técnico, estimación u organización personal — source: 93963a5f93e58d05
- El resumen del clúster reconoce relevance directa «modesta» (0.67) pese a esa ausencia — source: 93963a5f93e58d05

## Why it matters
Un 0.67 sin claims mapeables a los ejes del brief no debe usarse para asignar cupo ni para justificar una recomendación de práctica. La coincidencia es léxica («LLM», «evals») y el costo de confundirla con afinidad temática es recomendar evaluación como tema de liderazgo cuando el documento no lo trata.

Sostiene y refuerza `task-specific-llm-evals-relevancia-0-67-como-artefacto-del-scorer`, `task-specific-llm-evals-relevancia-lexica-no-tematica` y `task-specific-llm-evals-sin-conexion-con-agentes-o-docencia`, que registran la misma objeción desde el pipeline y desde el mapeo léxico.

## Links
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- supports → [[task-specific-llm-evals-relevancia-0-67-como-artefacto-del-scorer]]
- supports → [[task-specific-llm-evals-relevancia-lexica-no-tematica]]
- supports → [[task-specific-llm-evals-sin-conexion-con-agentes-o-docencia]]
