---
id: quoting-matthew-green-corroboracion-alta-refleja-mismo-tipo-de-feed
title: La corroboración=1.00 del clúster «Quoting Matthew Green» refleja que todos
  los documentos son del mismo tipo de feed
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
- sig-60c5604761f7
tags:
- corroboracion
- metricas
- artefacto-del-scorer
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: quoting-matthew-green-cluster-sin-documento-de-matthew-green
  type: derived_from
- to: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: supports
- to: corroboration-1-00-con-relevance-0-20-metrica-degenerada
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
---

## What it is
La corroboración=1.00 del signal es engañosa: probablemente refleja que todos los documentos son feeds RSS del mismo tipo, no convergencia temática. Con relevance=0.20 y novelty=0.00, la métrica alta no aporta acuerdo sobre el tema declarado.

## Evidence
- El informe señala que corroboración=1.00 probablemente refleja que todos los documentos son feeds RSS del mismo tipo, no convergencia temática — source: sig-60c5604761f7
- El signal tiene relevance=0.20 y novelty=0.00 — source: sig-60c5604761f7

## Why it matters
Un consumidor del grafo que vea corroboración alta podría tratar el clúster como validado. La métrica no distingue acuerdo topical de homogeneidad de fuente; hay que leerla junto con relevance y novelty.

Instancia concreta de `corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching` y `corroboration-1-00-con-relevance-0-20-metrica-degenerada`. Se deriva del hallazgo principal del clúster.

## Links
- derived_from → [[quoting-matthew-green-cluster-sin-documento-de-matthew-green]]
- supports → [[corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
- supports → [[corroboration-1-00-con-relevance-0-20-metrica-degenerada]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
