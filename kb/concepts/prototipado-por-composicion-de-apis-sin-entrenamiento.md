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
updated: '2026-10-08'
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
last_reinforced: '2026-10-08'
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
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: derived_from
---

## What it is
Construir un sistema de agentes encadenando servicios ya existentes —STT, TTS, un LLM, telefonía— en lugar de entrenar o ajustar un modelo. El caso del clúster es un coach de voz armado enteramente con componentes preexistentes y componibles.

## Evidence
- El stack del AI coach del clúster son cuatro servicios preexistentes y componibles, no modelos nuevos — source: 49140f9d5133d3c7

## Why it matters
Es un proyecto lateral de alcance bajo y aprendizaje alto: ejercita integración de sistemas y diseño de prompts sin requerir entrenamiento. La fuente no aporta detalle de implementación que permita evaluar la calidad del ensamblado.

El AI coach por voz es una instancia concreta de este patrón; la nota de composición se apoya en él como evidencia puntual (derived_from).

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agent-based-stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- supports → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- derived_from → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
