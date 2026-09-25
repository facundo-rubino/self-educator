---
id: how-to-match-llm-patterns-taxonomia-sin-validar
title: La taxonomía externo/interno y datos/no-datos del clúster existe solo como
  descripción de ingest, no como claim validado
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- 0248fdb60811e91e
tags:
- llm-patterns
- taxonomy
- circularidad
- stub
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido
  type: derived_from
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: relates_to
- to: taxonomia-dos-ejes-llm-externo-interno-datos
  type: relates_to
---

## What it is
La única afirmación disponible sobre la taxonomía propuesta (LLMs externos vs. internos, patrones con datos vs. sin datos) proviene de la descripción de ingest del propio pipeline, no del texto del documento. Citarla como evidencia de que la taxonomía existe es circular: el metadato se usa para probar lo que el metadato dice.

## Evidence
- La caracterización «externo vs. interno y datos vs. no-datos» es la única descripción de contenido en la señal — source: 0248fdb60811e91e
- Esa descripción es metadato de ingest, no texto extraído del documento — source: 0248fdb60811e91e

## Why it matters
Cualquier afirmación de que existe un marco de decisión utilizable sería inventada; lo defendible es solo que un marco puede existir en un documento que no podemos leer.

Deriva del ítem sin cuerpo ingerido y ejemplifica el patrón de reformular el título o el metadato como si fuera hallazgo. Se relaciona con la pregunta abierta sobre una taxonomía de dos ejes externo/interno y datos/no-datos, que aquí no queda validada ni refutada.

## Links
- derived_from → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[validacion-de-senal-por-contenido-no-por-titulo]]
- relates_to → [[taxonomia-dos-ejes-llm-externo-interno-datos]]
