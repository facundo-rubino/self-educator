---
id: ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados
title: Riesgos de latencia, calidad STT/TTS y coste por llamada en un coach de voz
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-14'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- cost
- coste
- latencia
- latency
- riesgo
- risk
- stt
- tts
- voice-pipeline
- voz
base_confidence: 0.04
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: ai-coach-stack-stt-tts-llm-numero-virtual
  type: derived_from
- to: privacidad-y-costo-en-asistentes-de-voz-continuos
  type: relates_to
- to: asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual
  type: relates_to
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: relates_to
- to: ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica
  type: relates_to
---

## What it is
Un pipeline de voz bidireccional (STT → LLM → TTS sobre telefonía) acumula latencias en cadena y coste por llamada minuto a minuto. El documento [49140f9d5133d3c7] describe el stack pero no reporta latencias, tasas de error STT/TTS ni coste operativo.

## Evidence
- El documento describe la composición STT + TTS + LLM + número virtual pero no reporta métricas de latencia, precisión ni coste — source: 49140f9d5133d3c7

## Why it matters
Sin estas cifras no puede evaluarse si el artefacto es viable más allá de la demo del autor. Un plan de adopción del mismo pipeline en gestión personal o en feedback conversacional exige esos números antes de comprometerse.

Cuantifica las condiciones prácticas del artefacto descrito en `ai-coach-voz-a-voz-ensamblado-de-servicios`. Los costes recurrentes y la privacidad de una grabación continua de voz se enlazan con `privacidad-y-costo-en-asistentes-de-voz-continuos`. La falta de evaluación sistemática es parte de `ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica`.

## Links
- derived_from → [[ai-coach-stack-stt-tts-llm-numero-virtual]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- relates_to → [[asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual]]
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- relates_to → [[ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica]]
