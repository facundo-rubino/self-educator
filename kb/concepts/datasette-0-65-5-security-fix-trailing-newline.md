---
id: datasette-0-65-5-security-fix-trailing-newline
title: 'Datasette 0.65.5: bypass de permisos de tabla por salto de línea final'
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
- e083e6ac132e7884
tags:
- datasette
- seguridad
- release-notes
base_confidence: 0.6
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
La release 0.65.5 de Datasette corrige un fallo de seguridad por el cual un salto de línea final en el nombre de tabla solicitado podía saltarse los permisos de tabla y exponer filas privadas [e083e6ac132e7884]. Se reporta como GHSA-h547-rmjf-5m2m.

## Evidence
- 0.65.5 corrige un bypass de permisos donde un salto de línea final en el nombre de tabla solicitado podía exponer filas privadas — source: e083e6ac132e7884
- Reportado como GHSA-h547-rmjf-5m2m — source: e083e6ac132e7884

## Why it matters
Es un ejemplo de mantenimiento de una línea estable (0.65.x) en paralelo a una línea alpha. Es un parche de seguridad, no evidencia de práctica de equipo o de agentes de IA.

Se relaciona con la 1.0a40 [7ab4e0a5b839ac3f], que según esa fuente lleva el mismo security fix. La evidencia disponible no demuestra si es el mismo camino de código o dos parches separados para un mismo CVE; tratarlo como «un mismo fix» sería una inferencia no verificada.

## Links
- relates_to → [[datasette-1-0a40-cambios]]
- derived_from → [[datasette-cluster-mezcla-alpha-patch-y-plugin]]
