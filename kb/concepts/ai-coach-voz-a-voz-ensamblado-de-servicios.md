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
updated: '2026-10-08'
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
last_reinforced: '2026-10-08'
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
---

## What it is
Un coach de IA personal construido ensamblando cuatro servicios preexistentes: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. El número virtual implica una interfaz de telefonía entrante, de modo que la interacción se dispara con una llamada y no con una ventana de chat. Todos los componentes son servicios componibles ya existentes, no modelos nuevos.

## Evidence
- El coach se construyó como herramienta personal, enmarcada explícitamente como respuesta al «monkey mind» del propio autor — source: 49140f9d5133d3c7
- El stack consiste en speech-to-text, text-to-speech, un LLM y un número virtual, es decir componentes preexistentes y componibles en lugar de modelos novedosos — source: 49140f9d5133d3c7
- El número virtual sugiere una interfaz de telefonía entrante: la interacción se dispara por llamada, no por chat — source: 49140f9d5133d3c7

## Why it matters
Es un caso de ensamblado de servicios, no de entrenamiento: el valor está en la composición y en el diseño del prompt, no en el modelo. La telefonía como superficie de entrada mantiene al coach ambiente en lugar de atado a una app. No hay en la fuente ningún detalle de implementación, elección de LLM, manejo de latencia, costo ni privacidad de la voz.

Instancia concreta del patrón general de prototipado por composición de APIs sin entrenamiento (supports). Se relaciona con la lectura del AI coach como herramienta de foco personal y no de liderazgo técnico, y con las preguntas abiertas sobre privacidad y costo de asistentes de voz continuos.

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
