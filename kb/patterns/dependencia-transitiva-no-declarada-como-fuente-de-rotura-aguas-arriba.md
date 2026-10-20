---
id: dependencia-transitiva-no-declarada-como-fuente-de-rotura-aguas-arriba
title: Una dependencia transitiva no declarada puede romperse por un cambio aguas
  arriba
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 22e0e79c5f31252d
tags:
- dependencias
- mantenimiento
- compatibilidad
- oficio
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: llm-tools-datasette-0-1-1-fix-dependencia-transitiva-httpx2
  type: derived_from
- to: agent-feed-de-dependencias-no-es-evidencia-de-practica-profesional
  type: relates_to
---

## What it is
Cuando un plugin consume una librería solo de forma transitiva (aquí httpx vía LLM), un cambio de esa librería en una versión aguas arriba (LLM 0.33 → httpx2) puede romperlo sin que el plugin lo haya declarado. Declarar las dependencias propias explícitamente reduce ese modo de fallo.

## Evidence
- Plugins que usaban httpx sin depender de él directamente se rompieron al pasar LLM 0.33 a httpx2 — source: 22e0e79c5f31252d
- llm-tools-datasette 0.1.1 es el parche que corrige ese caso — source: 22e0e79c5f31252d

## Why it matters
Es una heurística de mantenimiento de dependencias, no de gestión de equipos ni de docencia. Su valor para el brief es anecdótico: un caso documentado, no una práctica medida.

Se deriva del caso concreto de llm-tools-datasette 0.1.1. Se relaciona con la nota de que un feed de dependencias no es evidencia de práctica profesional: aquí la evidencia es un solo changelog autodeclarado.

## Links
- derived_from → [[llm-tools-datasette-0-1-1-fix-dependencia-transitiva-httpx2]]
- relates_to → [[agent-feed-de-dependencias-no-es-evidencia-de-practica-profesional]]
