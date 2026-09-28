---
id: cluster-rss-generico-bajo-relevance-novelty-cero
title: Clúster RSS genérico con relevance=0.20, novelty=0.00 y corroboration=1.00
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
- clustering
- ruido
- scoring
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: supports
- to: cluster-heterogeneo-como-vertedero-de-firehose
  type: relates_to
---

## What it is
El clúster es un ingesta genérica de ítems RSS de blogs de programadores que sobrevivió al filtrado determinista con relevance=0.20, novelty=0.00 y corroboration=1.00. La mayoría de documentos son posts de CSS/JSON/modelos de IA sin relación con agentes de IA en contextos de liderazgo o docencia.

## Evidence
- El clúster ingiere ítems RSS de blogs de programadores con relevance=0.20, novelty=0.00 y corroboration=1.00 según los scores del pipeline — source: sig-3e0fad654f6d
- Un puñado de ítems sí toca temas del brief: agentes y mantenimiento [01910c0f29cb0570], LLM y especificación formal [031a4bc33d0c2230], complejidad esencial/accidental [01f4d4dfc39f3469], entrevistas de algoritmos [02664c7040e371be] y disposición a parecer estúpido [058fd9b64413d16f] — source: sig-3e0fad654f6d

## Why it matters
Si clústeres así llegan a la etapa de analista, consumen atención y producen informes que no sostienen decisiones. Pero el propio critic advierte que el clúster es **mixto, no ruido**: al menos cinco documentos son genuinamente on-topic aunque no sean estudios de liderazgo o docencia.

Refuerza la caracterización de corroboration=1.00 como artefacto de matching degenerado. Se relaciona con la noción de clúster-vertedero de firehose.

## Links
- supports → [[corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
- relates_to → [[cluster-heterogeneo-como-vertedero-de-firehose]]
