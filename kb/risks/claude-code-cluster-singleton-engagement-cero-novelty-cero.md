---
id: claude-code-cluster-singleton-engagement-cero-novelty-cero
title: 'El clúster de Claude Code: singleton con engagement cero y novelty 0.00'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia-debil
- singleton
- scoring
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: relates_to
- to: cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion
  type: relates_to
- to: corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso
  type: supports
---

## What it is
El clúster se sostiene en un único documento RSS con engagement cero y novelty 0.00; la corroboración moderada es un valor por defecto del scorer, no consenso entre fuentes [abf61eeec75462f9].

## Evidence
- Un solo documento de RSS constituye todo el clúster, con engagement nulo y novelty 0.00 — source: abf61eeec75462f9
- La corrobación reportada es «moderada» pese a no existir segunda fuente — source: abf61eeec75462f9

## Why it matters
Cualquier afirmación sobre arquitectura de prompts de producto extraída de este clúster es autodescripción del pipeline, no evidencia verificada. No debe citarse ante un equipo ni en una clase.

Es la cara de riesgo de `claude-code-system-prompt-conditional-composition`: descarta leer el claim como hallazgo. Coincide con el patrón general de singletons RSS sin engagement y con la regla de que corroboración 0.50 en un clúster de un documento no es consenso.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- relates_to → [[cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion]]
- supports → [[corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso]]
