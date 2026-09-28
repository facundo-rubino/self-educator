---
id: corroboration-1-00-con-relevance-0-20-metrica-degenerada
title: 'corroboration=1.00 con relevance=0.20: métrica degenerada, no acuerdo entre
  fuentes'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- sig-3e0fad654f6d
tags:
- pipeline
- scoring
- metricas
- falso-positivo
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: supports
---

## What it is
Un corroboration de 1.00 sobre un clúster cuyo relevance es 0.20 y cuyo novelty es 0.00 es más probablemente un artefacto de la métrica que evidencia de convergencia entre fuentes.

## Evidence
- El propio informe advierte que «corroboration=1.00» probablemente refleja una métrica degenerada (muchos documentos, sin acuerdo real) y podría confundirse con evidencia convergente — source: sig-3e0fad654f6d

## Why it matters
Presentar corroboration alta como validación independiente en un clúster donde los temas son dispares lleva a decisiones sobre evidencia inexistente. El score hay que leerlo junto a relevance y novelty, no aislado.

Refuerza la nota preexistente sobre corroboration 1.00 con relevance 0.20 como artefacto de matching léxico. Aplicable al clúster RSS genérico descrito en este informe.

## Links
- supports → [[corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
