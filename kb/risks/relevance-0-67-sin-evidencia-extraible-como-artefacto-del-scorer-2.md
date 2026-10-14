---
id: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer-2
title: 'relevance=0.67 con un solo claim etiquetado: artefacto del scorer en el clúster
  de Claude Code'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-14'
updated: '2026-10-14'
sources:
- abf61eeec75462f9
tags:
- scoring
- clusters
- precision
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
  type: relates_to
- to: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
  type: supports
---

## What it is
La relevance de 0.67 del clúster [abf61eeec75462f9] no descansa en cobertura de los ejes del brief, sino en una intersección léxica: «modularidad de prompts» se etiqueta como transferible a agentes de IA, cosa cierta de casi cualquier técnica de prompt engineering. El propio crítico llama a esto coincidencia léxica, no relación sustantiva.

## Evidence
- El reporte declara relevance 0.67 con novedad 0.00 y corroboración 0.50 para un único documento [abf61eeec75462f9].
- El crítico afirma que la relevancia está «inflada por una intersección temática vaga» y que no se establece conexión con estimación, secuenciamiento, liderazgo ni docencia.

## Why it matters
Un score de relevancia alto sin cobertura de ejes hace pasar al grafo ítems que solo comparten vocabulario. Para el pipeline, la consecuencia es que el umbral de relevance no discrimina por sí solo entre señal temática y falso positivo léxico.

Es la variante concreta del patrón ya registrado en `relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer`, y la misma mecánica que documenta `matching-llm-patterns-relevancia-lexica-al-brief-de-agentes`.

## Links
- relates_to → [[relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer]]
- supports → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
