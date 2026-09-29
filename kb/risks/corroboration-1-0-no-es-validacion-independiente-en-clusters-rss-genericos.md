---
id: corroboration-1-0-no-es-validacion-independiente-en-clusters-rss-genericos
title: corroboration=1.00 en un clúster RSS genérico no es validación independiente
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- sig-c718e5611ff4
tags:
- corroboration
- scorer
- metricas
- falso-positivo
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: corroboration-1-00-con-relevance-0-20-metrica-degenerada
  type: relates_to
---

## What it is
Una corroboración de 1.00 en un clúster de documentos dev-blog genéricos refleja la representación amplia de ese contenido en el feed, no que fuentes independientes confirmen un hallazgo [sig-c718e5611ff4].

## Evidence
- El clúster reporta corroboration=1.00 con relevance=0.20 y novelty=0.00 sobre 20 ítems RSS heterogéneos — source: sig-c718e5611ff4
- El crítico marca el score alto como engañoso: indica prevalencia de contenido genérico, no acuerdo entre fuentes — source: sig-c718e5611ff4

## Why it matters
Un score de corroboración leído como validación haría pasar por hallazgo corroborado un conjunto que no converge en ningún punto. El scorer necesita distinguir «mucho contenido similar en el feed» de «varias fuentes independientes confirman lo mismo».

Este caso refuerza la nota existente `corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching` y el patrón `corroboracion-y-velocidad-como-artefactos-del-scorer`; es un caso concreto del mismo modo de fallo.

## Links
- supports → [[corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[corroboration-1-00-con-relevance-0-20-metrica-degenerada]]
