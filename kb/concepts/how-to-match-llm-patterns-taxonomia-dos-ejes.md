---
id: how-to-match-llm-patterns-taxonomia-dos-ejes
title: 'La taxonomía de dos ejes para elegir patrones de LLM: externo/interno y datos/no-datos'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 0248fdb60811e91e
tags:
- llm
- taxonomia
- arquitectura
- secuenciacion
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-problema-patron
  type: derived_from
---

## What it is
El marco propone clasificar problemas por dos ejes antes de elegir un patrón: si el LLM es externo o interno al sistema, y si el patrón está basado en datos o no. La decisión de arquitectura se desplaza del catálogo de patrones a la ubicación del modelo y a la dependencia de datos.

## Evidence
- El documento plantea distinguir problemas según se resuelvan con LLMs externos vs. internos y con patrones basados en datos vs. no basados en datos — source: 0248fdb60811e91e

## Why it matters
Si el eje se sostiene, cambia el orden de las decisiones de un equipo: primero dónde vive el modelo y si el problema requiere datos, después qué patrón. Ese orden tiene consecuencias para costo, sobre-ingeniería y estimación, aunque el documento no cuantifica ninguna.

Es la sustancia concreta de la nota sobre el emparejamiento patrón-problema del mismo documento. Queda condicionada por la nota sobre los bordes no validados de la dicotomía externo/interno y datos/no-datos.

## Links
- derived_from → [[how-to-match-llm-patterns-problema-patron]]
