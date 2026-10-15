---
id: how-to-match-llm-patterns-taxonomia-externo-interno-datos
title: 'Taxonomía de dos ejes para elegir patrones de LLM: externo/interno y datos/no-datos'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-15'
sources:
- 0248fdb60811e91e
tags:
- artefacto-de-ingesta
- llm-patterns
- seleccion-de-tooling
- sin-cuerpo
- taxonomia
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-10-15'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-taxonomia-sin-contenido
  type: relates_to
- to: taxonomia-por-tipo-de-problema-como-criterio-de-secuenciacion
  type: derived_from
- to: how-to-match-llm-patterns-taxonomia-dos-ejes-enunciada-sin-clases-de-problema
  type: relates_to
- to: how-to-match-llm-patterns-candidato-a-retrieval-no-a-insight
  type: relates_to
- to: ranking-openrouter-mide-consumo-no-calidad
  type: relates_to
---

## What it is
El único contenido atribuible al documento [0248fdb60811e91e] es una taxonomía de dos ejes para clasificar patrones de uso de LLM: externo vs. interno, y con datos vs. sin datos. No se describe ninguna clase de problema, ni criterio de decisión, ni tradeoff entre las cuatro casillas.

## Evidence
- El sujeto declarado del documento es distinguir problemas con LLMs externos vs. internos, y patrones con datos vs. sin datos — source: 0248fdb60811e91e
- El ítem es un RSS con engagement=0, sin interacción observada en el pipeline — source: 0248fdb60811e91e
- Scores deterministas: relevance=0.33, novelty=0.00, corroboration=0.50, velocity=0.50, surprise=0.50 — source: 0248fdb60811e91e

## Why it matters
Una taxonomía de dos ejes sin clases de problema no permite decidir nada: para elegir tooling de agentes de código o de enseñanza haría falta el mapeo «problema → patrón», y ese mapeo no está en la evidencia. Queda como vocabulario de referencia, no como criterio operativo.

Se relaciona con `taxonomia-por-tipo-de-problema-como-criterio-de-secuenciacion` (el mismo hueco: falta el mapeo por tipo de problema) y con `how-to-match-llm-patterns-candidato-a-retrieval-no-a-insight` (mismo veredicto de uso: retrieval, no hallazgo). También conecta con `ranking-openrouter-mide-consumo-no-calidad` como caso del mismo patrón general: métricas de selección de modelo que no informan aptitud.

## Links
- relates_to → [[how-to-match-llm-patterns-taxonomia-sin-contenido]]
- derived_from → [[taxonomia-por-tipo-de-problema-como-criterio-de-secuenciacion]]
- relates_to → [[how-to-match-llm-patterns-taxonomia-dos-ejes-enunciada-sin-clases-de-problema]]
- relates_to → [[how-to-match-llm-patterns-candidato-a-retrieval-no-a-insight]]
- relates_to → [[ranking-openrouter-mide-consumo-no-calidad]]
