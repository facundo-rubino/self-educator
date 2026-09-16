---
id: argumento-ex-silentio-en-corpus-truncado
title: 'Argumento ex silentio sobre un corpus truncado: ausencia de evidencia no es
  evidencia de ausencia'
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
- 43e006f4538b71dd
tags:
- metodologia
- inferencia
- ingestion
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: the-two-reacts-titulo-sin-contenido-ingerido
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
Inferir «no hay evidencia que conecte este contenido con el tema del brief» a partir del texto ingerido es un argumento ex silentio sobre un corpus presumiblemente truncado. No prueba ausencia de relación temática; solo prueba ausencia en el texto recuperado, lo cual es un artefacto de recuperación, no un hecho sobre el tema.

## Evidence
- La conclusión «aporta poco» se deriva tautológicamente del propio acto de ingestión defectuoso, no de un análisis del material — source: 43e006f4538b71dd
- La fórmula `UI = f(data)(state)` pertenece al ámbito de la ingeniería de software, pero esa coincidencia es léxica de dominio, no un hallazgo — source: 43e006f4538b71dd
- El veredicto registrado es WEAK con confianza ajustada de 0.05 — source: 43e006f4538b71dd

## Why it matters
Cualquier análisis que use este documento debe distinguir entre «no está en el texto ingerido» y «no es cierto». Confundir ambas cosas convierte un fallo de recuperación en una conclusión no falsable.

Se deriva de `the-two-reacts-titulo-sin-contenido-ingerido`: si el título no tiene contenido ingerido, la afirmación negativa sobre su relevancia no puede establecerse desde ese mismo material. Se relaciona con `relevancia-no-es-verdad` porque en ambos casos una propiedad aparente (relevancia temática o ausencia de ella) se confunde con la verdad de una afirmación.

## Links
- derived_from → [[the-two-reacts-titulo-sin-contenido-ingerido]]
- relates_to → [[relevancia-no-es-verdad]]
