---
id: datasette-apis-internas-como-puntos-de-extension
title: 'Diseñar mejoras internas como puntos de extensión: add_background_task() y
  un Web Component documentado'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- a1cbd7d446e3f49c
- 7ab4e0a5b839ac3f
tags:
- datasette
- diseño-de-apis
- plugins
base_confidence: 0.45
half_life_days: 365
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: datasette-1-0a41-cambios
  type: derived_from
- to: datasette-1-0a40-cambios
  type: derived_from
- to: datasette-explain-upgrade-como-forcing-function
  type: relates_to
---

## What it is
Dos cambios del clúster convierten mejoras internas en extensiones para terceros: el método `datasette.add_background_task()` para que los plugins gestionen tareas [7ab4e0a5b839ac3f] y un Web Component único documentado para que los plugins reutilicen los diálogos modales [a1cbd7d446e3f49c].

## Evidence
- `datasette.add_background_task()` permite a los plugins lanzar y gestionar tareas en segundo plano — source: 7ab4e0a5b839ac3f
- Los diálogos modales se refactorizan en un Web Component compartido y documentado para otros plugins — source: a1cbd7d446e3f49c

## Why it matters
Formularlo como patrón de diseño de APIs con el ecosistema de plugins como consumidor es lo más cercano a un movimiento de liderazgo técnico en el clúster, pero la evidencia son dos features de una nota de release, no una práctica observada con resultados.

Se deriva de las notas de la 1.0a40 y la 1.0a41. Se relaciona con la práctica de acoplar uso propio y releases [datasette-explain-upgrade-como-forcing-function] porque ambas describen el ecosistema de plugins como consumidor de decisiones del núcleo.

## Links
- derived_from → [[datasette-1-0a41-cambios]]
- derived_from → [[datasette-1-0a40-cambios]]
- relates_to → [[datasette-explain-upgrade-como-forcing-function]]
