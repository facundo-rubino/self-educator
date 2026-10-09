---
id: fixing-my-tooltip-accessibility-mistake-falso-positivo-filtro
title: '«Fixing my tooltip accessibility mistake» como falso positivo del filtro determinista:
  novelty 0.00, relevance 0.33'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-09'
sources:
- ded7560510c137bc
tags:
- filtro-determinista
- falso-positivo
- accesibilidad
- brief
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: accesibilidad-tooltip-como-falso-positivo-del-filtro-determinista
  type: relates_to
- to: corroboration-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: supports
---

## What it is
El ítem sobrevive al filtrado con novelty=0.00 y relevance=0.33: no aporta información nueva y su relevancia para el brief es marginal. La corroboración media (0.50) no proviene de este documento, sino de que «aria-describedby isn't always enough» es una idea conocida en la práctica de accesibilidad web.

## Evidence
- novelty=0.00 y relevance=0.33 para el clúster — source: ded7560510c137bc
- La corroboración media se hereda de un truismo de la comunidad de accesibilidad, no de demostración alguna en el documento — source: ded7560510c137bc
- El engagement reportado es 0 — source: ded7560510c137bc

## Why it matters
El caso confirma un patrón recurrente del pipeline: un token léxico del título («tooltip», «accessibility») activa el filtro y un prior externo suple la ausencia de contenido. El resultado no es una señal débil, es la ausencia de señal revestida de hallazgo: no debe retenerse como afirmación ni reetiquetarse, porque reetiquetar asume un contenido que no tenemos.

Extiende la nota ya existente sobre el mismo falso positivo de categoría y aporta un segundo ejemplo al riesgo general de matching degenerado entre relevancia y corroboración.

## Links
- relates_to → [[accesibilidad-tooltip-como-falso-positivo-del-filtro-determinista]]
- supports → [[corroboration-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
