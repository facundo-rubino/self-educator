---
id: how-to-match-llm-patterns-taxonomia-externo-interno-datos
title: 'Taxonomía de dos ejes para elegir patrones de LLM: externo/interno y datos/no-datos'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-13'
sources:
- 0248fdb60811e91e
tags:
- llm-patterns
- taxonomia
- sin-cuerpo
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-taxonomia-sin-contenido
  type: relates_to
- to: taxonomia-por-tipo-de-problema-como-criterio-de-secuenciacion
  type: derived_from
---

## What it is
El único contenido verificable del documento es un alcance de dos ejes declarado en una línea: distinguir problemas que piden LLMs externos frente a internos, y patrones con datos frente a sin datos. No hay cuerpo que desarrolle la taxonomía, ni ejemplos, ni criterios de decisión, ni benchmarks — solo el titular y ese encuadre de una línea.

## Evidence
- El alcance declarado del documento es distinguir problemas con LLM externo vs. interno, y patrones con datos vs. sin datos — source: 0248fdb60811e91e
- No hay contenido de cuerpo, ejemplos, benchmarks ni criterios reproducibles más allá del título y un encuadre de una línea — source: 0248fdb60811e91e

## Why it matters
Los dos ejes son plausibles como criterio de arquitectura para decidir dónde corre un modelo o si el patrón depende de datos propios, pero enunciarlos no es validarlos. Cualquier uso en una decisión de proyecto exige contrastarlos contra fuentes primarias (coste de serving, gobernanza de datos, latencia y fiabilidad) antes de adoptarlos.

Se relaciona con la nota existente sobre la taxonomía sin contenido del mismo documento. Deriva de la pregunta sobre elegir el patrón de LLM por tipo de problema como criterio de secuenciación, no como herramienta validada.

## Links
- relates_to → [[how-to-match-llm-patterns-taxonomia-sin-contenido]]
- derived_from → [[taxonomia-por-tipo-de-problema-como-criterio-de-secuenciacion]]
