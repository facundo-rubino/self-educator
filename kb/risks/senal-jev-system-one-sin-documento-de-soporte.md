---
id: senal-jev-system-one-sin-documento-de-soporte
title: '«Jev / System One / Decision Models»: señal sin documento de soporte'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- sig-450e39a1cef2
tags:
- pipeline
- señal-falsa
- scoring
- firehose-rss
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: ruido-de-agregacion-como-senal-falsa
  type: relates_to
- to: cluster-heterogeneo-como-vertedero-de-firehose
  type: relates_to
- to: a-chain-reaction-metricas-no-son-evidencia-independiente
  type: relates_to
---

## What it is
Ninguno de los ~24 documentos ingeridos en el clúster menciona «Jev», «System One» ni «Decision Models»; la señal se sostiene únicamente sobre texto generado por el scorer. Confirmado por el propio critic: «none of the ~24 ingested documents mention Jev, System One, or Decision Models». Actuar sobre esta señal como si describiera un evento real es perseguir un desarrollo que no existe en los datos.

## Evidence
- El clúster no contiene ningún documento que soporte la señal; solo ítems RSS heterogéneos (CSS, JSON, incidentes, ensayos personales) — source: sig-450e39a1cef2
- El critic califica la base como inexistente: «no cited source, no primary material, and no independent confirmation» — source: sig-450e39a1cef2
- Confianza ajustada del pipeline: 0.02, con veredicto WEAK — source: sig-450e39a1cef2

## Why it matters
Una señal que nombra un producto, un autor o un artefacto concreto puede disparar investigación downstream aunque su soporte documental sea cero. El modo de fallo no es «cluster irrelevante» sino «cluster etiquetado como hallazgo»: el coste se paga en esfuerzo de verificación que nunca debió iniciarse.

Es un caso particular de «ruido-de-agregacion-como-senal-falsa»: la agregación produce una etiqueta plausible sin contenido detrás. Comparte mecanismo con «cluster-heterogeneo-como-vertedero-de-firehose», donde un conjunto sin campo semántico común recibe un nombre que no le corresponde. Se distingue de «a-chain-reaction-metricas-no-son-evidencia-independiente» en que aquí la métrica problemática son corroboración y velocidad del scorer, no las del ítem.

## Links
- relates_to → [[ruido-de-agregacion-como-senal-falsa]]
- relates_to → [[cluster-heterogeneo-como-vertedero-de-firehose]]
- relates_to → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
