---
id: anti-patterns-in-software-blogging-scores-artefacto-no-acuerdo
title: 'corroboration=1.00 con relevance=0.20 y novelty=0.00: artefacto del ingest
  RSS, no acuerdo tópico'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- sig-168dcd41a1e2
tags:
- scoring-artifact
- rss-ingest
- corroboration
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: corroboration-1-0-no-es-validacion-independiente-en-clusters-rss-genericos
  type: supports
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: anti-patterns-in-software-blogging-heterogeneo-sin-ejes-del-brief
  type: relates_to
---

## What it is
El score `corroboration=1.00` del clúster no refleja acuerdo entre fuentes sobre una tesis común, sino que varios feeds RSS publican contenido genérico similar. Con relevance=0.20 y novelty=0.00, la terna es una firma de agregación, no de señal — source: sig-168dcd41a1e2.

## Evidence
- El score de corroboración de 1.00 «probablemente refleja múltiples feeds llevando posts de interés general similares en lugar de acuerdo sobre una tesis compartida» — source: sig-168dcd41a1e2.
- relevance=0.20 y novelty=0.00 acompañan al clúster — source: sig-168dcd41a1e2.

## Why it matters
Tratar corroboración alta como validación independiente sobre un corpus RSS genérico induce a leer consenso donde solo hay coincidencia de plantilla de feed. La única coherencia interna del clúster es que todos son feeds RSS — source: sig-168dcd41a1e2.

Instancia el patrón ya registrado de que corroboration=1.00 no es validación independiente en clústeres RSS genéricos. Conecta con el riesgo de relevancia baja, novedad nula y corroboración alta como no-señal.

## Links
- supports → [[corroboration-1-0-no-es-validacion-independiente-en-clusters-rss-genericos]]
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- relates_to → [[anti-patterns-in-software-blogging-heterogeneo-sin-ejes-del-brief]]
