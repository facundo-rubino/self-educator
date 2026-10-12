---
id: agentes-abatatan-ports-mantener-sigue-costoso
title: Los agentes abaratan los ports nativos pero no el mantenimiento
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-10-12'
sources:
- 01910c0f29cb0570
tags:
- agentes
- costo
- electron
- mantenimiento
- ports
base_confidence: 0.5
half_life_days: 180
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: complejidad-esencial-vs-accidental-brooks
  type: supports
- to: mantenimiento-sigue-costoso-electron-app
  type: relates_to
- to: agentes-y-complejidad-esencial-limite-de-lo-abaratado
  type: supports
- to: complejidad-esencial-vs-accidental-brooks
  type: relates_to
- to: pluralidad-de-llm-en-software-adjacent-senal-debil-sin-convergencia
  type: supports
---

## What it is
Con agentes de código, un port nativo de una aplicación es barato de producir. Sin embargo, el mantenimiento posterior no se abarató en la misma medida, y ese coste explica decisiones de producto aparentemente contradictorias (por ejemplo, seguir enviando Claude como app Electron).

## Evidence
- «Coding agents make native ports cheap, yet Anthropic still ships Claude as an Electron app because 'code is cheap but maintenance isn't'.» — fuente: 01910c0f29cb0570

## Why it matters
Separa dos costes que las narrativas de productividad por IA suelen confundir: generación inicial y mantenimiento. Ofrece un criterio práctico para evaluar reescrituras: ¿qué se abarata, la creación o el sostenimiento?

Se relaciona con `complejidad-esencial-vs-accidental-brooks`: el mantenimiento recae del lado de lo esencial y por eso resiste la reducción. Sostiene a `pluralidad-de-llm-en-software-adjacent-senal-debil-sin-convergencia` como uno de sus cuatro ítems.

## Links
- supports → [[complejidad-esencial-vs-accidental-brooks]]
- relates_to → [[mantenimiento-sigue-costoso-electron-app]]
- supports → [[agentes-y-complejidad-esencial-limite-de-lo-abaratado]]
- relates_to → [[complejidad-esencial-vs-accidental-brooks]]
- supports → [[pluralidad-de-llm-en-software-adjacent-senal-debil-sin-convergencia]]
