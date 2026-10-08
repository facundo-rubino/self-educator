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
updated: '2026-10-08'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- cost
- coste
- costo
- llm
- llm-pipeline
- privacidad
- privacy
- telefonia
- telephony
- voice
- voz
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-10-08'
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
Grabar la propia voz hacia un pipeline de LLM de terceros y operar un número de teléfono virtual plantea preguntas de manejo de datos y de costo recurrente que la fuente no aborda.

## Evidence
- El clúster no contiene detalles de implementación: ni latencia, ni costo, ni privacidad de los datos de voz — source: 49140f9d5133d3c7

## Why it matters
Antes de reutilizar la forma para retro de sprint, postmortems de estimación o triaje de preguntas de estudiantes, hay que resolver explícitamente el tratamiento de la voz y el costo del número y del LLM.

Riesgo asociado al AI coach por voz ensamblado con servicios, del que hereda la superficie de entrada telefónica y el paso de audio a un tercero.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- derived_from → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
