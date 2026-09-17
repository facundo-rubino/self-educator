---
id: task-specific-llm-evals-singleton-engagement-cero
title: '«Task-Specific LLM Evals»: singleton con engagement=0 y novelty=0.00'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 93963a5f93e58d05
tags:
- senal
- corroboracion
- engagement
- clustering
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
  type: supports
- to: functional-html-singleton-engagement-cero
  type: relates_to
- to: relevancia-no-es-verdad
  type: supports
- to: single-document-cluster-engagement-cero-no-generaliza
  type: supports
---

## What it is
El clúster consta de un único documento con engagement=0, novelty=0.00 y corroboración 0.50 [93963a5f93e58d05]. La relevancia declarada de 0.67 no está respaldada por corroboración: no hay un segundo documento que confirme el encuadre temático del primero.

## Evidence
- El clúster contiene un solo documento, con engagement=0 — source: 93963a5f93e58d05
- novelty=0.00 y corroboración=0.50 sobre esa única fuente — source: 93963a5f93e58d05

## Why it matters
Un singleton sin engagement no sostiene generalización alguna sobre el tema del brief. Tratar la relevancia de 0.67 como validación temática sería leer un puntaje de similitud como si fuera evidencia corroborada.

Se apoya en [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]] porque la ausencia de cuerpo y la ausencia de corroboración se refuerzan mutuamente. Es el mismo patrón que [[functional-html-singleton-engagement-cero]] y la misma regla que [[single-document-cluster-engagement-cero-no-generaliza]] y [[relevancia-no-es-verdad]].

## Links
- supports → [[task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido]]
- relates_to → [[functional-html-singleton-engagement-cero]]
- supports → [[relevancia-no-es-verdad]]
- supports → [[single-document-cluster-engagement-cero-no-generaliza]]
