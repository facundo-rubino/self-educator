---
id: gate-de-cobertura-tematica-en-el-filtro-determinista
title: 'Gate de cobertura temática: un post personal no corroborado no debe pasar
  el filtro'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- d2a0c86ca8027978
tags:
- pipeline
- filtrado
- cobertura-tematica
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: juez-humano-we-and-b-llm-evaluator-hackathon-sin-contenido-para-el-brief
  type: derived_from
- to: umbral-de-contenido-minimo-antes-de-clustering
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
---

## What it is
Un ítem con relevance 0.67 y novelty 0.00, de un solo documento y sin corroboración, no cubre ningún eje del brief pero sobrevive al filtro determinista. La implicación de pipeline es un gate de cobertura temática: si el documento no toca al menos un eje declarado, no compite por cupo.

## Evidence
- El ítem es un post personal de juicio, no una pieza sobre agentes, gestión, docencia, liderazgo ni técnicas de estudio — source: d2a0c86ca8027978
- El análisis señala que el filtro que admitió el clúster necesita un gate de cobertura temática — source: d2a0c86ca8027978

## Why it matters
Diluye la base de evidencia sin añadir señal. Es una decisión de muestreo, no un hallazgo del tema: no debe citarse como evidencia en las líneas centrales del brief.

Derivado del caso W&B ([[juez-humano-we-and-b-llm-evaluator-hackathon-sin-contenido-para-el-brief]]). Se relaciona con el umbral de contenido mínimo antes de agrupar ([[umbral-de-contenido-minimo-antes-de-clustering]]) y apoya validar la señal por contenido y no por título ([[validacion-de-senal-por-contenido-no-por-titulo]]).

## Links
- derived_from → [[juez-humano-we-and-b-llm-evaluator-hackathon-sin-contenido-para-el-brief]]
- relates_to → [[umbral-de-contenido-minimo-antes-de-clustering]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
