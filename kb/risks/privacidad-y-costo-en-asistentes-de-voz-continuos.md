---
id: privacidad-y-costo-en-asistentes-de-voz-continuos
title: Riesgos de privacidad y costo de un asistente de voz basado en LLM y telefonía
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-28'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- cost
- coste
- costo
- llm
- privacidad
- privacy
- telefonia
- telephony
- voice
- voz
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: efectividad-de-ai-coach-no-demostrada
  type: relates_to
- to: privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia
  type: relates_to
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: derived_from
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: relates_to
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: relates_to
---

## What it is
Un coach por voz que enruta audio por STT, un LLM remoto y TTS a través de un número telefónico virtual implica capturar voz continua, enviarla a servicios de terceros y mantener líneas y llamadas activas.

## Evidence
- El stack del coach incluye speech-to-text, un LLM y un número de teléfono virtual — source: 49140f9d5133d3c7

## Why it matters
Son los dos costos no técnicos del patrón: audio personal persistido o procesado por terceros, y el gasto recurrente de telefonía más inferencia. El documento no los aborda ni los cuantifica, así que quedan como riesgo a resolver antes de reutilizar el diseño.

Deriva de `stack-de-ai-coach-voz-a-voz` al señalar las consecuencias de cada pieza. Se relaciona con `ai-coach-voz-a-voz-ensamblado-de-servicios` como el artefacto que incurre en estos costos.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- derived_from → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
