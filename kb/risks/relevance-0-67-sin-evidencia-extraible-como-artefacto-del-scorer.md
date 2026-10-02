---
id: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
title: 'relevance=0.67 sin evidencia extraíble: artefacto del scorer, no acuerdo topical'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-02'
sources:
- d2a0c86ca8027978
tags:
- scoring
- artefacto-de-pipeline
- relevancia
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-02'
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
---

## What it is
Un score de relevancia de 0.67 sin ningún claim extraíble que lo respalde indica que el scorer probablemente está operando por solapamiento de entidades («LLM», «hackathon») y no por evidencia que soporte el brief.

## Evidence
- El reporte declara que la relevancia de 0.67 no está respaldada por evidencia extraíble del documento — source: d2a0c86ca8027978
- Ningún claim del reporte puede fundamentarse en más de un doc_id — source: d2a0c86ca8027978

## Why it matters
Si el ranking del pipeline confía en este score, el clúster puede desplazar material con evidencia real. Es un caso de calibración: la señal de relevancia necesita cotejarse contra claims extraíbles antes de usarse para priorizar.

Soporta la nota de documentación única con engagement cero. Se relaciona con el principio general «relevancia no es verdad» y con la nota que trata corroboración y velocidad como artefactos del scorer.

## Links
- supports → [[wandb-llm-as-a-judge-hackathon-sin-corroboracion]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
