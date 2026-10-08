---
id: animating-zooming-css-singleton-engagement-cero-y-ausencia-de-linea-base
title: '«Animating zooming using CSS»: singleton con engagement=0 y sin línea base
  de navegador'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-08'
updated: '2026-10-08'
sources:
- b0df1f50a76ba564
tags:
- pipeline
- engagement-cero
- singleton
- css
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: animating-zooming-css-singleton-engagement-cero
  type: relates_to
- to: animating-zooming-css-singleton-sin-engagement
  type: relates_to
- to: animating-zooming-css-titulo-con-documento-unico-engagement-cero
  type: relates_to
- to: cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion
  type: supports
---

## What it is
El clúster se sostiene en un único documento con engagement=0, sin corroboración independiente y sin fecha ni detalles de compatibilidad de navegador [b0df1f50a76ba564]. Cualquier regla sobre el orden de `transform` derivada de aquí sería condicional y requeriría verificación empírica en el navegador objetivo antes de adoptarla [b0df1f50a76ba564].

## Evidence
- El documento es la única fuente del clúster y entró por RSS con engagement=0 — fuente: b0df1f50a76ba564
- Corroboration=0.50 y velocity=0.50: valores neutros sin señal de propagación — fuente: b0df1f50a76ba564
- No hay fecha, versión de navegador ni detalles de compatibilidad en el material disponible — fuente: b0df1f50a76ba564

## Why it matters
Un detalle de implementación de CSS extraído de un singleton sin cuerpo no es base suficiente para fijar una regla de equipo ni para citarlo en docencia. El riesgo concreto es aplicar «scale antes o después de translate» como regla fija cuando el propio título la condiciona con «sometimes» [b0df1f50a76ba564].

Refuerza el patrón general ya registrado en `cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion` y las notas de engagement cero de otros clústeres de un solo documento. No contradice la nota principal del clúster: la complementa señalando por qué la afirmación no se puede elevar a regla.

## Links
- relates_to → [[animating-zooming-css-singleton-engagement-cero]]
- relates_to → [[animating-zooming-css-singleton-sin-engagement]]
- relates_to → [[animating-zooming-css-titulo-con-documento-unico-engagement-cero]]
- supports → [[cluster-de-un-documento-sin-engagement-no-sostiene-generalizacion]]
