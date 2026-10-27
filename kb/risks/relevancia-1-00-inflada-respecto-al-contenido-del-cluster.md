---
id: relevancia-1-00-inflada-respecto-al-contenido-del-cluster
title: relevance=1.00 inflada respecto al contenido real del clúster
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-27'
updated: '2026-10-27'
sources:
- d955592a4eb5ee8f
- 0038729e398b77be
- 1ccc8e412cdaa1c4
- 44c8e5ef06e5fbe2
- ae72befeffedbc16
- b647bfde274dd2a1
tags:
- scoring
- relevance
- artefacto-pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-27'
provenance:
  scale: S
  query: null
links:
- to: cluster-discurso-publico-ia-no-evidencia-de-practica
  type: derived_from
- to: corroboracion-ausente-por-sesgo-de-feed-rss-engagement-cero
  type: relates_to
---

## What it is
La señal declarada reposa en un solo documento y sin datos, mientras el resto del clúster trata gobernanza y escepticismo. El score de relevancia=1.00 no refleja el contenido real: mide solapamiento léxico del titular («AI») más que afinidad temática.

## Evidence
- El único ítem sobre matemáticas es un teaser sin datos; el resto del clúster es gobernanza, escepticismo y críticas a labs — source: d955592a4eb5ee8f, 44c8e5ef06e5fbe2
- La relevancia=1.00 asignada al clúster excede lo que su contenido sostiene — source: 1ccc8e412cdaa1c4, ae72befeffedbc16

## Why it matters
Ajustar decisiones sobre el score nominal sin inspeccionar el cuerpo lleva a tratar discurso público como hallazgo técnico. El score debe leerse como artefacto del pipeline.

Se deriva del análisis del clúster como discurso público y se relaciona con la ausencia de corroboración por sesgo de feed.

## Links
- derived_from → [[cluster-discurso-publico-ia-no-evidencia-de-practica]]
- relates_to → [[corroboracion-ausente-por-sesgo-de-feed-rss-engagement-cero]]
