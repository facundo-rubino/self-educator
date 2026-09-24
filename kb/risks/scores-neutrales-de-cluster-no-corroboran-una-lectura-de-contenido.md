---
id: scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido
title: Scores en línea base neutra (novelty 0.00, corroboration 0.50) no corroboran
  ninguna lectura del contenido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 0248fdb60811e91e
tags:
- miscalibracion-de-scores
- novelty
- corroboracion
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: scoring-novelty-cero-corroboration-uno-contradictorio
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: afirmar-contenido-de-bof-desde-titulo-de-signal
  type: relates_to
- to: garantizar-relevancia-no-es-verdad
  type: supports
---

## What it is
Los scores del clúster [0248fdb60811e91e] — novelty=0.00, corroboration=0.50, velocity=0.50, surprise=0.50 — son indistinguibles de una línea base nula. Un 0.50 de corroboración en esa escala no es evidencia de corroboración: es el valor por defecto, y presentarlo como respaldo de cualquier afirmación sobre el documento sería leer un artefacto del scorer como confirmación.

## Evidence
- Los scores del clúster reportan novelty=0.00, corroboration=0.50, velocity=0.50 y surprise=0.50, indistinguibles de una línea base nula/neutra aparte de una relevancia de 0.33 por debajo del punto medio — source: 0248fdb60811e91e
- El documento tenía engagement=0, sin señal de lectura, compartición o discusión — source: 0248fdb60811e91e

## Why it matters
Si los valores neutros pueden citarse como corroboración, cualquier clúster vacío parece respaldado. La regla operativa es que novelty 0.00 y corroboration 0.50 no sostienen ninguna lectura positiva del contenido: son ausencia de señal, no confirmación.

Es el mismo problema que `scoring-novelty-cero-corroboration-uno-contradictorio` documenta con otro par de valores internamente inconsistentes. Apoya a `corroboracion-y-velocidad-como-artefactos-del-scorer` y a `garantizar-relevancia-no-es-verdad`: la relevancia o los scores del pipeline no validan una afirmación sobre el mundo. Se relaciona con `afirmar-contenido-de-bof-desde-titulo-de-signal` por compartir el patrón de construir contenido desde una señal sin cuerpo.

## Links
- relates_to → [[scoring-novelty-cero-corroboration-uno-contradictorio]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[afirmar-contenido-de-bof-desde-titulo-de-signal]]
- supports → [[garantizar-relevancia-no-es-verdad]]
