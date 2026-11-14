---
id: fuente-unica-duplicada-y-sin-engagement-como-techo-de-corroboracion
title: Dos ítems casi duplicados sin engagement no son corroboración independiente
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-14'
updated: '2026-11-14'
sources:
- b8a2ffe60796b1b8
- 48abbf91d3309b20
tags:
- corroboracion
- rss
- engagement
- metodologia
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-11-14'
provenance:
  scale: S
  query: null
links:
- to: harness-agentico-de-seis-pasos-para-asegurar-codigo
  type: supports
- to: singleton-rss-engagement-cero-novelty-cero-no-sostiene-generalizacion
  type: supports
---

## What it is
Los dos documentos del clúster son el mismo ítem bajo dos feeds, ambos con engagement cero. El tamaño aparente del clúster es ilusorio y no existe corroboración independiente del harness ni señal de validación en producción.

## Evidence
- Los dos documentos son el mismo ítem bajo dos feeds; el tamaño del clúster es ilusorio y no hay corroboración independiente — source: b8a2ffe60796b1b8
- Engagement cero en ambos ítems: ninguna señal de que practitioners validaran los seis pasos en producción — source: 48abbf91d3309b20

## Why it matters
Fija el techo de confianza del harness de seis pasos en ~0.08. Cualquier uso del harness en un equipo o en clase debe tratarse como lectura de fuente promocional, no como práctica establecida.

Sostiene directamente la nota del harness al limitar su confianza. Confirma el patrón ya registrado de que un singleton RSS con engagement cero y novelty cero no sostiene generalización.

## Links
- supports → [[harness-agentico-de-seis-pasos-para-asegurar-codigo]]
- supports → [[singleton-rss-engagement-cero-novelty-cero-no-sostiene-generalizacion]]
