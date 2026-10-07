---
id: adoptar-composicion-condicional-sin-inspeccionar-perdida-de-depurabilidad
title: 'Adoptar composición condicional sin inspección de lo ensamblado: pérdida de
  depurabilidad'
type: risk
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
- depurabilidad
- agentes
- observabilidad
- composicion
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: archivos-de-instruccion-de-proyecto-como-modulos-con-condiciones-de-activacion
  type: supports
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria
  type: supports
---

## What it is
Si la conducta del agente depende de muchas condiciones y no hay forma de ver qué se ensambló en una ejecución concreta, se pierde la depurabilidad — el mismo problema que un sistema de build opaco. La adopción del patrón exige instrumentación del ensamblado.

## Evidence
- Riesgo enunciado en el reporte. — source: abf61eeec75462f9
- El documento fuente no muestra mecanismo de inspección, porque no muestra el ensamblador. — source: abf61eeec75462f9

## Why it matters
Es la condición práctica para que el patrón sea operable: sin observabilidad, «el modelo ignoró mis instrucciones» se vuelve indepurable y la maquinaria de módulos se vuelve deuda. También es el argumento para instrumentar antes de multiplicar módulos.

Refuerza `archivos-de-instruccion-de-proyecto-como-modulos-con-condiciones-de-activacion`. Se relaciona con `claude-code-condiciones-que-gatean-secciones-sin-observar` (ya existe la pregunta abierta sobre qué condiciones gatean qué secciones). Coincide con `reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria`.

## Links
- supports → [[archivos-de-instruccion-de-proyecto-como-modulos-con-condiciones-de-activacion]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- supports → [[reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria]]
