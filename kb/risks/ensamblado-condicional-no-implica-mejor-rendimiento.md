---
id: ensamblado-condicional-no-implica-mejor-rendimiento
title: Ensamblado condicional del prompt no implica mejor rendimiento del agente
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
- abf61eeec75462f9
tags:
- claude-code
- system-prompt
- medicion
- inferencia
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: prompt-modular-sin-mecanica-verificable
  type: supports
- to: claude-code-system-prompt-sin-datos-de-eficacia
  type: supports
- to: sobre-abstraer-la-composicion-condicional
  type: relates_to
---

## What it is
Que un system prompt esté compuesto de partes condicionales es una descripción estructural, no un resultado de rendimiento. El documento no mide si esa arquitectura produce mejores respuestas que un prompt monolítico, ni en qué tareas.

## Evidence
- El código fuente filtrado muestra un system prompt ensamblado de partes condicionales — source: abf61eeec75462f9
- No hay ninguna medición de resultados asociada al ensamblado condicional — source: abf61eeec75462f9 (ausencia)

## Why it matters
Impedir la inferencia «condicional ⇒ mejor» evita que un equipo copie la estructura por prestigio de la fuente. Sin datos de eficacia, adoptarla añade complejidad sin beneficio demostrado.

Extiende la nota sobre prompts modulares sin mecánica verificable y la que señala la ausencia de datos de eficacia en el caso Claude Code. Se relaciona con el riesgo de sobre-abstraer la composición condicional.

## Links
- supports → [[prompt-modular-sin-mecanica-verificable]]
- supports → [[claude-code-system-prompt-sin-datos-de-eficacia]]
- relates_to → [[sobre-abstraer-la-composicion-condicional]]
