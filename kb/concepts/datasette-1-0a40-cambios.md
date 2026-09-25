---
id: datasette-1-0a40-cambios
title: 'Datasette 1.0a40: parche de seguridad, add_background_task() y migración a
  httpx2'
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
- 7ab4e0a5b839ac3f
tags:
- datasette
- release-notes
- changelog
base_confidence: 0.55
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: datasette-1-0a41-cambios
  type: relates_to
- to: datasette-0-65-5-security-fix-trailing-newline
  type: relates_to
- to: datasette-cluster-mezcla-alpha-patch-y-plugin
  type: derived_from
---

## What it is
La release 1.0a40 de Datasette incluye el mismo parche de seguridad que la 0.65.5, añade el método `datasette.add_background_task()` para que los plugins lancen y gestionen tareas en segundo plano, y migra el trabajo HTTP interno (p. ej. `datasette.client.get()`) a httpx2 [7ab4e0a5b839ac3f].

## Evidence
- La 1.0a40 incluye el mismo security fix que la 0.65.5 — source: 7ab4e0a5b839ac3f
- Añade `datasette.add_background_task()` para que los plugins lancen y gestionen tareas en segundo plano — source: 7ab4e0a5b839ac3f
- Migra Datasette a httpx2 para trabajo HTTP interno como `datasette.client.get()` — source: 7ab4e0a5b839ac3f

## Why it matters
Una API de tareas en segundo plano y la migración de la capa HTTP interna convierten una release de mantenimiento en un punto de extensión para plugins. No hay evidencia en el clúster de que estas features hayan sido adoptadas o probadas más allá de la nota de release.

Se relaciona con la 1.0a41 [a1cbd7d446e3f49c] por ser la release inmediatamente posterior en la misma línea alpha. Comparte el parche de seguridad con la 0.65.5 [e083e6ac132e7884], aunque la evidencia no demuestra que sean el mismo camino de código o dos parches separados para un mismo CVE.

## Links
- relates_to → [[datasette-1-0a41-cambios]]
- relates_to → [[datasette-0-65-5-security-fix-trailing-newline]]
- derived_from → [[datasette-cluster-mezcla-alpha-patch-y-plugin]]
