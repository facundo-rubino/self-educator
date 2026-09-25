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
updated: '2026-09-25'
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
last_reinforced: '2026-09-25'
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
---

## What it is
Un asistente de voz ensamblado con STT, TTS, un LLM y un número virtual implica audio continuo hacia servicios de terceros y un canal telefónico facturado por uso. El documento no aborda ninguno de los dos.

## Evidence
- El stack descrito incluye STT, TTS, un LLM y un número de teléfono virtual — source: 49140f9d5133d3c7
- El documento no discute implicaciones de privacidad ni de costo — source: 49140f9d5133d3c7

## Why it matters
Son dos restricciones que condicionan la viabilidad de reutilizar este boceto en un contexto de equipo: dónde vive el audio y quién paga el canal. El documento no las trata, así que quedan como preguntas abiertas del diseño, no como hallazgos.

Se deriva de `ai-coach-voz-a-voz-ensamblado-de-servicios`: la composición del stack es lo que genera ambos riesgos. Se relaciona con `prototipado-por-composicion-de-apis-sin-entrenamiento`, donde el costo y la dependencia de terceros son inherentes al patrón.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- derived_from → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
