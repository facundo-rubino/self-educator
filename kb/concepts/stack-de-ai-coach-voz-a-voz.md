---
id: stack-de-ai-coach-voz-a-voz
title: 'Stack de un AI coach por voz: STT + TTS + LLM + número virtual'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-21'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-agents
- ai-coach
- arquitectura
- integration
- llm
- personal-productivity
- stack
- telefonia
- voice
- voz
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
- to: monkey-mind-como-encuadre-de-productividad-personal
  type: relates_to
- to: efectividad-de-ai-coach-no-demostrada
  type: relates_to
- to: privacidad-y-costo-en-asistentes-de-voz-continuos
  type: relates_to
---

## What it is
Un AI coach personal construido sobre cuatro piezas apiladas: speech-to-text para entrada de voz, un LLM como motor de conversación, text-to-speech para salida hablada, y un número de teléfono virtual como canal. Es un ensamblado de APIs, no un sistema de agentes con diseño propio.

## Evidence
- El documento describe un AI coach que usa speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7

## Why it matters
Muestra que el umbral para construir un asistente conversacional personal es hoy bajo: cuatro servicios encadenados bastan para un prototipo funcional. No dice nada sobre si funciona ni sobre arquitectura de agentes, así que sirve como punto de partida arquitectónico, no como recomendación.

Se relaciona con `monkey-mind-como-encuadre-de-productividad-personal` porque el stack existe para atacar ese pain point, y con `privacidad-y-costo-en-asistentes-de-voz-continuos` porque la fuente no discute ninguno de esos dos ejes.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
