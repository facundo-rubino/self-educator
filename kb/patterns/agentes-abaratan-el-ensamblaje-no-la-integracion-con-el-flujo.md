---
id: agentes-abaratan-el-ensamblaje-no-la-integracion-con-el-flujo
title: Los agentes abaratan el ensamblaje de servicios, no la integración con el flujo
  de trabajo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-19'
updated: '2026-10-19'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- composicion-de-servicios
- integracion
- estimacion
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
- to: agentes-y-complejidad-esencial-limite-de-lo-abaratado
  type: derived_from
- to: stack-de-ai-coach-voz-a-voz
  type: supports
---

## What it is
El caso del AI coach muestra el patrón: juntar STT, TTS, LLM y telefonía es barato porque cada pieza es una API de catálogo. Lo que el documento no muestra —y es lo caro— es la integración con el flujo real del usuario: cuándo se invoca, qué contexto recuerda, cómo se evalúa que ayuda. El patrón es composición barata con integración no resuelta.

## Evidence
- El AI coach se ensambla con cuatro servicios de catálogo — source: 49140f9d5133d3c7
- No hay descripción de integración con flujos de trabajo, evaluación ni resultados — source: 49140f9d5133d3c7

## Why it matters
Para estimar y secuenciar: el prototipo de un asistente se hace en un fin de semana; convertirlo en herramienta que un equipo o una clase use de verdad es otro proyecto. Presupuestar la integración y la evaluación como partidas separadas, no como detalle del ensamblaje.

`relates_to` la nota de que los agentes abaratan los ports pero no el mantenimiento: mismo eje coste-de-ensamblaje vs coste-de-sostener. `derived_from` el límite de Brooks a lo abaratado por agentes: la integración es complejidad esencial, no accidental.

## Links
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- derived_from → [[agentes-y-complejidad-esencial-limite-de-lo-abaratado]]
- supports → [[stack-de-ai-coach-voz-a-voz]]
