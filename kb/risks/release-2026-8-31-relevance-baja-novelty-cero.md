---
id: release-2026-8-31-relevance-baja-novelty-cero
title: 'Scoring del release 2026.8.31: novelty 0.00, relevance 0.33, corroboración
  plana 0.50'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- sig-d0acf338c3a6
tags:
- scoring
- mcp
- filtro-determinista
- artefacto-de-ingesta
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: cluster-rss-generico-bajo-relevance-novelty-cero
  type: supports
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: release-2026-8-31-stub-sin-changelog
  type: relates_to
---

## What it is
El scorer del clúster asigna a esta señal novelty=0.00, relevance=0.33 y corroboration/velocity/surprise=0.50. Es el perfil típico de un artefacto de feed genérico que sobrevive al filtro determinista sin aportar contenido temático.

## Evidence
- novelty=0.00, relevance=0.33 y corroboration/velocity/surprise=0.50 en la señal sig-d0acf338c3a6 — fuente: sig-d0acf338c3a6.
- Los valores de engagement RSS son 0 en el clúster — fuente: sig-d0acf338c3a6.

## Why it matters
Un relevance de 0.33 es solapamiento léxico con el token «MCP», no acuerdo topical. Que novelty sea 0.00 y corroboration 0.50 indica ausencia de señal nueva y de confirmación independiente, respectivamente: los tres scores juntos describen un ítem que ocupa cupo sin generar hallazgo.

`supports` los patrones existentes cluster-rss-generico-bajo-relevance-novelty-cero, relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal y corroboracion-y-velocidad-como-artefactos-del-scorer. Se relaciona con release-2026-8-31-stub-sin-changelog porque ambos describen el mismo artefacto de ingesta desde planos distintos (contenido y scoring).

## Links
- supports → [[cluster-rss-generico-bajo-relevance-novelty-cero]]
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[release-2026-8-31-stub-sin-changelog]]
