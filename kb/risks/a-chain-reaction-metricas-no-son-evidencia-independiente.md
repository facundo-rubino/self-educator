---
id: a-chain-reaction-metricas-no-son-evidencia-independiente
title: Las métricas de un singleton RSS son autodescripción del pipeline, no corroboración
  externa
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-24'
sources:
- 0715b80a63a796ad
tags:
- a-chain-reaction
- calibracion
- corroboracion
- corroboración
- filtrado-determinista
- metodología
- metricas
- pipeline
- rss
- scoring
- singleton
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido
  type: relates_to
- to: single-document-cluster-engagement-cero-no-generaliza
  type: supports
- to: a-chain-reaction-titulo-sin-contenido-ingerido
  type: supports
- to: a-chain-reaction-titulo-sin-contenido-ingerido
  type: derived_from
- to: a-chain-reaction-cita-sin-argumento-desarrollado
  type: derived_from
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
- to: a-chain-reaction-fuera-del-topic-sin-conexion-explicita
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
- to: scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido
  type: supports
---

## What it is
Las cifras que acompañan al clúster (relevance 0.33, novelty 0.00, corroboration 0.50, engagement 0) no son evidencia independiente sobre el documento: son la salida del propio scorer del pipeline. Citarlas como prueba de que el documento es irrelevante incurre en circularidad, porque la conclusión y la premisa provienen del mismo sistema.

## Evidence
- El documento lleva relevance 0.33, novelty 0.00 y corroboration 0.50, con engagement=0 — source: 0715b80a63a796ad
- El clúster se compone de un único documento — source: 0715b80a63a796ad

## Why it matters
Un score bajo no es un hallazgo sobre el mundo ni sobre el contenido; es una medida interna. Tratarlo como corroboración convierte la calibración del pipeline en la conclusión del análisis, lo que impide detectar falsos positivos y hace irrefutable cualquier descarte.

`supports` la nota de que el clúster queda fuera del topic sin conexión explícita, porque retira la única «prueba» que se esgrimía. `relates_to` la observación general de que corroboración y velocidad son artefactos del scorer. `supports` la nota sobre scores en línea base neutra que no corroboran ninguna lectura de contenido.

## Links
- relates_to → [[confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido]]
- supports → [[single-document-cluster-engagement-cero-no-generaliza]]
- supports → [[a-chain-reaction-titulo-sin-contenido-ingerido]]
- derived_from → [[a-chain-reaction-titulo-sin-contenido-ingerido]]
- derived_from → [[a-chain-reaction-cita-sin-argumento-desarrollado]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
- supports → [[a-chain-reaction-fuera-del-topic-sin-conexion-explicita]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- supports → [[scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido]]
