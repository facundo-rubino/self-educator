---
id: identificar-no-es-reconocer-en-la-fuente
title: «Identificar» en la fuente significa «no rechazar», no «reconocer»
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- 19cb8032958cd964
tags:
- llm
- ambiguedad-lexica
- claims
base_confidence: 0.12
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
En la fuente, «identificar» describe que el modelo no se niegue a nombrar a una persona; no mide si el modelo acierta ni con qué precisión reconoce. Leer «identifica» como «tiene la capacidad técnica» convierte una observación de política en un claim de capacidad por coincidencia léxica — source: 19cb8032958cd964.

## Evidence
- La fuente solo reporta que Gemini nombra figuras públicas y que ChatGPT y Claude se niegan — source: 19cb8032958cd964
- La fuente no mide exactitud, cobertura ni modos de fallo — source: 19cb8032958cd964

## Why it matters
Es un error de lectura reutilizable: claims que suenan técnicos pero que en realidad describen una decisión de producto. Quien compila o consume esta evidencia debe separar «el modelo se niega» de «el modelo puede».

Deriva de divergencia-de-rechazo-entre-proveedores, la observación que se malinterpreta. Se relaciona con relevancia-no-es-verdad: en ambos casos la utilidad o la plausibilidad se confunden con evidencia.

## Links
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[relevancia-no-es-verdad]]
