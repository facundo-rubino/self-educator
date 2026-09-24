---
id: task-specific-llm-evals-singleton-rss-engagement-cero-novelty-cero
title: '«Task-Specific LLM Evals»: singleton RSS con engagement cero y novelty 0.00'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-24'
sources:
- 93963a5f93e58d05
tags:
- corpus
- corroboracion
- engagement
- evals
- llm
- rss
- singleton
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
---

## What it is
El clúster de «Task-Specific LLM Evals» es un singleton: un solo documento RSS [93963a5f93e58d05], con novelty 0.00 y corroboración 0.50, es decir sin fuente independiente que lo respalde. Un documento único con engagement nulo no sostiene generalización sobre práctica de evaluación.

## Evidence
- El clúster contiene un único documento — source: 93963a5f93e58d05
- La corroboración reportada es 0.50 desde una sola fuente y la novedad es 0.00 — source: 93963a5f93e58d05
- El crítico ajustó la confianza de 0.30 a 0.05 — source: 93963a5f93e58d05

## Why it matters
Cualquier conclusión extraída de este clúster es provisional por construcción. El riesgo no es que el artículo sea falso, sino que este KB lo trate como evidencia cuando solo hay una superficie de una fuente.

`supports` la nota de título sin contenido ingerido, que documenta la misma carencia desde el lado de la evidencia. Se relaciona con las notas sobre afirmaciones poblacionales desde una sola fuente y sobre ingesta truncada como riesgo sistémico: aquí se combinan ambos modos de fallo.

## Links
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques]]
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
