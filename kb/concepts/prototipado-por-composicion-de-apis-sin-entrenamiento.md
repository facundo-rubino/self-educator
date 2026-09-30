---
id: prototipado-por-composicion-de-apis-sin-entrenamiento
title: Prototipado de agentes por composición de APIs, sin entrenamiento de modelos
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-30'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- apis
- composicion
- composicion-de-apis
- prototipado
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: agent-based-stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: supports
---

## What it is
El proyecto descrito se construye ensamblando servicios existentes (STT, TTS, LLM, número virtual) en lugar de entrenar un modelo propio [49140f9d5133d3c7]. Es la construcción de un agente por composición de APIs, un patrón que no requiere datos de entrenamiento ni ajuste fino [49140f9d5133d3c7].

## Evidence
- La lista de componentes del proyecto sugiere ensamblado de APIs existentes, sin mención de entrenamiento — source: 49140f9d5133d3c7

## Why it matters
Componer APIs existentes abarata prototipar, pero no dice nada sobre si el prototipo resuelve el problema que declara resolver. La composición es condición de posibilidad, no evidencia de eficacia [49140f9d5133d3c7].

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agent-based-stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- supports → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
