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
updated: '2026-09-24'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- cost
- coste
- privacidad
- privacy
- telephony
- voice
- voz
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-24'
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
---

## What it is
Un coach de voz que combina número virtual telefónico con servicios de speech-to-text y LLM de terceros implica riesgos de privacidad (audio y transcripciones hacia terceros) y de coste operativo por minuto de telefonía y tokens. El documento no aborda ninguno de los dos.

## Evidence
- El stack incluye un número virtual de telefonía además de STT, TTS y LLM — source: 49140f9d5133d3c7
- El documento no menciona tratamiento de datos, consentimiento, retención de audio ni costes operativos — source: 49140f9d5133d3c7

## Why it matters
Operar un asistente de voz continuo convierte un prototipo personal en un flujo con datos sensibles y coste recurrente. Antes de adoptarlo como herramienta de foco conviene instrumentar privacidad y coste, no solo la ganancia percibida.

Deriva de `stack-de-ai-coach-voz-a-voz`, que identifica los componentes que crean los riesgos. Se relaciona con `efectividad-de-ai-coach-no-demostrada` porque ambos limitan la adopción acrítica del asistente.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
