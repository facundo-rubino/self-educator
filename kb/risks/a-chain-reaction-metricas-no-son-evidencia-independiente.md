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
updated: '2026-09-17'
sources:
- 0715b80a63a796ad
tags:
- metricas
- calibracion
- filtrado-determinista
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-17'
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
---

## What it is
Las métricas relevance=0.33, novelty=0.00, corroboration=0.50 y velocidad/sorpresa neutras provienen del mismo pipeline de filtrado determinista que produjo el artefacto. No son evidencia independiente de significancia: son self-description del pipeline. Con n=1, corroboración 0.50 no está anclada en triangulación.

## Evidence
- La corroboración registrada de 0.50 sobre un único documento carece de base para triangulación cruzada — source: 0715b80a63a796ad
- Las métricas declaradas (relevance 0.33, novelty 0.00, corroboration 0.50) derivan del mismo filtrado determinista que retuvo el ítem — source: 0715b80a63a796ad

## Why it matters
Usar estas métricas para justificar que el ítem es relevante cierra un círculo: el pipeline dice que el pipeline encontró algo. Confiar en ellas como señal temática es un error de calibración.

Soporta la nota de riesgo sobre el título sin contenido: la ausencia de cuerpo combinada con métricas autogeneradas agrava el problema. Refuerza la nota sobre singletons que no generalizan, y se relaciona con la nota sobre confianza inflada en hallazgos por ausencia de contenido.

## Links
- relates_to → [[confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido]]
- supports → [[single-document-cluster-engagement-cero-no-generaliza]]
- supports → [[a-chain-reaction-titulo-sin-contenido-ingerido]]
