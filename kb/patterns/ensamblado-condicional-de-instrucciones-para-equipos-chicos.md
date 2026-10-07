---
id: ensamblado-condicional-de-instrucciones-para-equipos-chicos
title: 'Ensamblado condicional de instrucciones aplicado a equipos chicos: base más
  módulos activados por contexto'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- abf61eeec75462f9
tags:
- liderazgo
- instrucciones
- composicion
- estimacion
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: composicion-condicional-de-prompts-ensenable-a-principiantes
  type: relates_to
- to: transferencia-de-patron-de-prompts-a-herramientas-internas
  type: supports
---

## What it is
Propuesta de trasladar el patrón de composición condicional al material de instrucciones de un equipo chico: mantener una capa base (estándares, definición de hecho, etiqueta de revisión) y activar módulos según contexto (heurísticas de estimación greenfield vs. legacy, reglas de secuenciación para trabajo con dependencias fuertes vs. paralelizable) en lugar de un documento único que nadie relee.

## Evidence
- El único respaldo empírico es la analogía con el claim de ensamblado condicional de Claude Code, documentado en un solo RSS. — source: abf61eeec75462f9

## Why it matters
Da vocabulario compartido para depurar fallos de proceso: «¿qué capa no se activó?» en vez de «¿quién lo hizo mal?». Aplicable a estimación y scope creep. Pero la evidencia no viene del clúster: es transferencia analógica del analista. Exige umbral de diversidad de contexto para compensar el coste de mantener la maquinaria de selección de módulos.

Se deriva de `ensamblado-condicional-de-prompts` (patrón base). Es pariente de `composicion-condicional-de-prompts-ensenable-a-principiantes` en tanto abstracción enseñable. Reforzaría `transferencia-de-patron-de-prompts-a-herramientas-internas`, que explícitamente exige evidencia del patrón antes de generalizar: aquí esa evidencia no está.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- relates_to → [[composicion-condicional-de-prompts-ensenable-a-principiantes]]
- supports → [[transferencia-de-patron-de-prompts-a-herramientas-internas]]
