---
id: how-to-match-llm-patterns-candidato-a-retrieval-o-descarte
title: '«How to Match LLM Patterns to Problems»: candidato a retrieval de texto completo
  o a descarte, no a insight corroborado'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- 0248fdb60811e91e
tags:
- llm-patterns
- retrieval
- pipeline
- stub
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido
  type: derived_from
- to: pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques
  type: relates_to
- to: argumento-ex-silentio-en-corpus-truncado
  type: contradicts
---

## What it is
Dado que la señal solo ofrece título y una línea de ingest, la acción correcta es recuperar el texto completo del documento [0248fdb60811e91e] o depriorizarlo. Elevarlo a hallazgo sin cuerpo sería un error de categoría: una taxonomía de arquitectura no es evidencia sobre liderazgo técnico, estimación ni pedagogía.

## Evidence
- El documento carece de cuerpo, autor, benchmarks y casos de estudio en la señal entregada — source: 0248fdb60811e91e
- La propia señal lo marca como candidato a retrieval del texto completo o a depriorización, con confianza 0.05 tras el verdict WEAK del crítico — source: 0248fdb60811e91e

## Why it matters
Si el texto completo está paywalled o truncado, la reingesta repetida seguirá produciendo el mismo stub no accionable e inflará la cobertura aparente del topic.

Deriva del ítem sin cuerpo y del patrón general de pipeline que no recupera fuente primaria antes de evaluar. Se marca como contradictoria frente al riesgo de argumento ex silentio sobre corpus truncado: descartar este documento no equivale a probar que su contenido carezca de valor, y la decisión queda abierta hasta el retrieval.

## Links
- derived_from → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido]]
- relates_to → [[pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques]]
- contradicts → [[argumento-ex-silentio-en-corpus-truncado]]
