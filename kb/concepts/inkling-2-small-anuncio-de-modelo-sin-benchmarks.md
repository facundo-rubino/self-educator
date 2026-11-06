---
id: inkling-2-small-anuncio-de-modelo-sin-benchmarks
title: '«Inkling 2 Small»: anuncio de modelo 17A-594B sin benchmarks verificables'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-06'
updated: '2026-11-06'
sources:
- 382d9b6490c36fd5
tags:
- ainews
- modelo-moe
- entrenamiento
- benchmark-sin-verificar
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-06'
provenance:
  scale: S
  query: null
links:
- to: muse-wonder-wonder-full-anuncio-de-modelo-meta-sin-benchmarks
  type: relates_to
- to: muse-wonder-admision-de-anuncios-de-modelo-sin-benchmarks
  type: supports
- to: hy3-lidera-ranking-openrouter-sin-datos-de-capacidades
  type: relates_to
- to: ranking-openrouter-mide-consumo-no-calidad
  type: relates_to
---

## What it is
Una entrada de AINews anuncia «Inkling 2 Small» como un modelo de arquitectura MoE (17A-594B, presumiblemente ~17B activos de ~594B totales) entrenado en 68 horas sobre 12T tokens y presentado como superador de «Muse Spark». El documento no incluye suite de evaluación, semillas, baseline comparable ni tamaño de clúster. Las cifras funcionan como framing de vendor, no como resultado reproducible.

## Evidence
- Se anuncia «Inkling 2 Small» como modelo 17A-594B entrenado en 68 horas sobre 12T tokens, con rendimiento superior a «Muse Spark» — source: 382d9b6490c36fd5
- El ítem es una entrada RSS de AINews sin engagement registrado, sin discusión ni validación de la comunidad — source: 382d9b6490c36fd5

## Why it matters
Ninguna de las cifras es verificable desde el documento: 12T tokens en 68 horas implica un throughput agregado enorme cuya plausibilidad depende de un tamaño de clúster nunca especificado, y «superar a Muse Spark» es un superlativo comparativo sin eval suite divulgada. Tratar este anuncio como medición de capacidad sería confundir marketing con resultado.

Mismo modo de fallo que los anuncios de modelo Meta sin benchmarks (`muse-wonder-wonder-full-anuncio-de-modelo-meta-sin-benchmarks`): titular de frontera sin datos operacionales. Refuerza la regla de admisión de `muse-wonder-admision-de-anuncios-de-modelo-sin-benchmarks`. Comparte con `hy3-lidera-ranking-openrouter-sin-datos-de-capacidades` el patrón de ranking/claim sin identidad ni metodología, y con `ranking-openrouter-mide-consumo-no-calidad` la distinción entre señal de mercado y capacidad medida.

## Links
- relates_to → [[muse-wonder-wonder-full-anuncio-de-modelo-meta-sin-benchmarks]]
- supports → [[muse-wonder-admision-de-anuncios-de-modelo-sin-benchmarks]]
- relates_to → [[hy3-lidera-ranking-openrouter-sin-datos-de-capacidades]]
- relates_to → [[ranking-openrouter-mide-consumo-no-calidad]]
