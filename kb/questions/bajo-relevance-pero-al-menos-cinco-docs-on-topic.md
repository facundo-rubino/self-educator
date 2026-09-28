---
id: bajo-relevance-pero-al-menos-cinco-docs-on-topic
title: 'Bajo relevance no implica clúster de ruido: al menos cinco documentos on-topic'
type: question
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
- evidencia
- criterios
base_confidence: 0.4
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: cluster-rss-generico-bajo-relevance-novelty-cero
  type: contradicts
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
---

## What it is
El analista etiqueta el clúster como «noise cluster» pese a conceder que cinco documentos son genuinamente on-topic. El critic rechaza esa conversión por ser una afirmación más fuerte de lo que la evidencia sostiene. Queda abierta la pregunta: ¿cuál es el criterio que convierte «insuficiente para hallazgos accionables» en «ruido»?

## Evidence
- El analista afirma que el clúster es un «noise cluster» a pesar de nombrar cinco documentos on-topic — source: sig-3e0fad654f6d
- El critic concluye que el clúster es mixto, no inútil: débil como evidencia directa, pero no «near-zero relevance», y que la confianza 0.15 era demasiado baja (ajustada a 0.38) — source: sig-3e0fad654f6d

## Why it matters
La política de descartar clústeres bajos en relevance antes de la etapa de analista necesita un umbral claro, o corre el riesgo de tirar evidencia secundaria legítima por un criterio arbitrario.

Contradice la etiqueta de «noise cluster» del informe. Se relaciona con la nota de que relevance baja no equivale a ruido.

## Links
- contradicts → [[cluster-rss-generico-bajo-relevance-novelty-cero]]
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
