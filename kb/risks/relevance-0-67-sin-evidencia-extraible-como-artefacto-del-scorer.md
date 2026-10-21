---
id: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
title: 'relevance=0.67 con un solo claim etiquetado: artefacto del scorer'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-21'
sources:
- abf61eeec75462f9
- d2a0c86ca8027978
tags:
- artefacto-de-pipeline
- clustering
- falsos-positivos
- ingesta
- relevance
- relevancia
- scorer
- scoring
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: wandb-llm-as-a-judge-hackathon-sin-corroboracion
  type: supports
- to: relevancia-no-es-verdad
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: relates_to
- to: juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: claude-code-cluster-singleton-engagement-cero-novelty-cero
  type: derived_from
- to: relevancia-1-00-no-es-validacion-del-cluster
  type: relates_to
---

## What it is
Un relevance de 0.67 sostenido por un único claim etiquetado, sin cuerpo recuperado, no indica acuerdo topical: es un artefacto del scorer [abf61eeec75462f9].

## Evidence
- El clúster declara relevancia moderada pero solo aporta un claim extraíble del único documento — source: abf61eeec75462f9

## Why it matters
Sugiere revisar el umbral de contenido mínimo antes de aceptar un clúster como señal; de lo contrario el scoring premia coincidencia léxica del título.

Deriva del caso concreto de Claude Code. Se alinea con la observación general de que relevancia 1.00 no valida un clúster cuando novelty es cero y no hay cuerpo.

## Links
- supports → [[wandb-llm-as-a-judge-hackathon-sin-corroboracion]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- relates_to → [[juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- derived_from → [[claude-code-cluster-singleton-engagement-cero-novelty-cero]]
- relates_to → [[relevancia-1-00-no-es-validacion-del-cluster]]
