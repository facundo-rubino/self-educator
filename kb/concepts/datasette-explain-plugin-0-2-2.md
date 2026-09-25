---
id: datasette-explain-plugin-0-2-2
title: 'datasette-explain 0.2.2: explain plans en páginas de stored query de solo
  lectura'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- 2265b46813a2dd66
tags:
- datasette
- plugin
- release-notes
base_confidence: 0.55
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: datasette-1-0a40-cambios
  type: relates_to
- to: datasette-cluster-mezcla-alpha-patch-y-plugin
  type: derived_from
---

## What it is
El plugin de terceros datasette-explain 0.2.2 añade soporte de explain plans en páginas de stored query de solo lectura [2265b46813a2dd66]. La motivación declarada es que el autor actualizó datasette.simonwillison.net a Datasette 1.0a40.

## Evidence
- datasette-explain 0.2.2 hace funcionar los explain plans en páginas de stored query de solo lectura — source: 2265b46813a2dd66
- La release fue motivada por la actualización del autor de datasette.simonwillison.net a Datasette 1.0a40 — source: 2265b46813a2dd66

## Why it matters
Es un artefacto de un mantenedor gestionando un proyecto aguas abajo de un núcleo alpha en movimiento. Es una release de plugin, no evidencia de práctica de ingeniería más allá del propio changelog.

Se relaciona con la 1.0a40 [7ab4e0a5b839ac3f] porque la actualización de la instancia autoalojada a esa versión disparó la release del plugin. Es un vínculo léxico y de cadencia, no un hilo causal demostrado.

## Links
- relates_to → [[datasette-1-0a40-cambios]]
- derived_from → [[datasette-cluster-mezcla-alpha-patch-y-plugin]]
