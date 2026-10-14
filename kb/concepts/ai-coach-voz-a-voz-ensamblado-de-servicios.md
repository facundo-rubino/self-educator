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
updated: '2026-10-14'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-coach
- composicion-de-apis
- ensamblado-de-servicios
- integration
- llm
- monkey-mind
- personal-productivity
- prototipado
- prototyping
- proyecto-personal
- stack
- stt
- stt-tts
- telefonia
- telephony
- tts
- voice
- voz
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-10-14'
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
- to: ai-coach-como-herramienta-de-foco-no-de-liderazgo
  type: relates_to
- to: post-unico-como-plantilla-de-demostracion-end-to-end
  type: relates_to
- to: asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual
  type: contradicts
- to: stack-de-ai-coach-voz-a-voz-ensamblado
  type: relates_to
- to: privacidad-y-costo-en-asistentes-de-voz-continuos
  type: relates_to
- to: protoitipado-por-composicion-de-apis-sin-entrenamiento
  type: relates_to
- to: ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados
  type: relates_to
- to: ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica
  type: relates_to
---

## What it is
Un AI coach se construye ensamblando componentes existentes: speech-to-text para entrada, text-to-speech para salida, un LLM como motor de conversación y un número telefónico virtual como canal. El artefacto es un pipeline de servicios, no un modelo entrenado. El documento [49140f9d5133d3c7] describe únicamente esta composición, sin métricas de uso ni evaluación.

## Evidence
- El documento describe la construcción de un AI coach combinando speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El título indica que su propósito es lidiar con la propia «monkey mind» (autorregulación y atención personal) — source: 49140f9d5133d3c7

## Why it matters
Confirma como patrón accesible para un dev individual la composición de una interfaz conversacional completa (voz bidireccional + LLM + telefonía) sin entrenar nada propio. Exportable a gestión personal del dev-líder o a feedback conversacional, pero el documento no lo afirma: la inferencia queda fuera de la fuente.

`protoitipado-por-composicion-de-apis-sin-entrenamiento` describe la misma mecánica general (componer APIs en vez de entrenar). El loop de latencia/coste STT→LLM→TTS conecta con `ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados`. La aplicación al liderazgo técnico es exactamente el puente que `ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica` marca como no sostenido.

## Links
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- supports → [[efectividad-de-ai-coach-no-demostrada]]
- supports → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[ai-coach-como-herramienta-de-foco-no-de-liderazgo]]
- relates_to → [[post-unico-como-plantilla-de-demostracion-end-to-end]]
- contradicts → [[asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual]]
- relates_to → [[stack-de-ai-coach-voz-a-voz-ensamblado]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- relates_to → [[protoitipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados]]
- relates_to → [[ai-coach-anuncio-de-proyecto-personal-no-es-evidencia-de-practica]]
