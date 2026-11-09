---
id: afirmacion-de-una-pasada-de-agentes-no-medida
title: '«Los agentes resuelven los deberes en un prompt»: condición afirmada, no medida'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-09'
updated: '2026-11-09'
sources:
- 537f26930a76d7e3
- 14d26da33645360c
tags:
- medicion
- agentes-de-codigo
- docencia
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-11-09'
provenance:
  scale: S
  query: null
links:
- to: cs146s-rediseno-de-deberes-por-agentes-que-hacen-una-pasada
  type: contradicts
- to: mejora-de-rendimiento-sin-delta-post-cambio
  type: relates_to
---

## What it is
La condición que dispara el rediseño —que un agente completa los deberes del año anterior en una pasada— se afirma en los documentos, no se mide. No hay enunciado de tarea, modelo, número de intentos ni tasa de éxito reportada.

## Evidence
- El rediseño se justifica por el hecho de que un agente puede terminar los deberes del año anterior en un prompt, sin datos de la prueba. — source: 537f26930a76d7e3
- El encuadre del curso es la pregunta por esa posibilidad, no la medición de su frecuencia o alcance. — source: 14d26da33645360c

## Why it matters
Si la premisa es solo narrativa, el rediseño puede responder a una anécdota memorable y no a una propiedad estable de los agentes. Antes de reescribir una asignación por esta razón, conviene medirlo: qué tarea, qué agente, cuántos intentos, qué tasa.

Contradice la nota que registra el rediseño como respuesta a una condición establecida. Se relaciona con el patrón existente de que una afirmación de mejora sin «después» cuantificado no es un resultado establecido.

## Links
- contradicts → [[cs146s-rediseno-de-deberes-por-agentes-que-hacen-una-pasada]]
- relates_to → [[mejora-de-rendimiento-sin-delta-post-cambio]]
