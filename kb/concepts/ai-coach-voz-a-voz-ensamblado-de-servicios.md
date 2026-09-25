---
id: ai-coach-voz-a-voz-ensamblado-de-servicios
title: AI coach por voz ensamblado con STT + TTS + LLM + número virtual
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-25'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- integration
- prototyping
- proyecto-personal
- stack
- voice
- voz
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: relates_to
- to: efectividad-de-ai-coach-no-demostrada
  type: supports
- to: privacidad-y-costo-en-asistentes-de-voz-continuos
  type: supports
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: supports
- to: monkey-mind-como-encuadre-de-productividad-personal
  type: relates_to
---

## What it is
Un AI coach personal construido ensamblando cuatro componentes existentes: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. El documento solo describe el stack, no decisiones de diseño, evaluación ni resultados.

## Evidence
- El documento describe la construcción de un AI coach con speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El documento es un ítem RSS con engagement=0 y no discute agentes de código, liderazgo de equipos, estimación, secuenciamiento, alcance, organización personal, oficio de software engineering ni técnicas de estudio — source: 49140f9d5133d3c7

## Why it matters
El único contenido técnico verificable es la lista de cuatro componentes. Eso la vuelve reutilizable como boceto de arquitectura para un asistente de voz, pero no como evidencia de práctica ni de eficacia: no hay decisiones de diseño, ni evaluación, ni resultados reportados.

Se relaciona con `stack-de-ai-coach-voz-a-voz`, la nota que ya registraba el mismo ensamblado. Apoya a `prototipado-por-composicion-de-apis-sin-entrenamiento`: es un caso de prototipado por composición de servicios existentes, sin entrenar modelos. Se relaciona con `monkey-mind-como-encuadre-de-productividad-personal` porque ese es el encuadre declarado del proyecto.

## Links
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- supports → [[efectividad-de-ai-coach-no-demostrada]]
- supports → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
