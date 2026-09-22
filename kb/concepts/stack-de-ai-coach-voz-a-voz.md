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
updated: '2026-09-22'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-agents
- ai-coach
- arquitectura
- composicion-de-apis
- integration
- llm
- personal-productivity
- prototipado
- stack
- telefonia
- voice
- voz
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-22'
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
- to: hipotesis-de-coach-de-voz-como-accountability-de-equipo
  type: supports
- to: composicion-condicional-de-prompts-ensenable-a-principiantes
  type: relates_to
---

## What it is
Un AI coach personal se construye componiendo APIs ya existentes: speech-to-text para entrada, text-to-speech para salida, un LLM como motor de diálogo y un número de teléfono virtual como canal. No requiere entrenar modelos; el trabajo es de integración y encadenamiento de servicios.

## Evidence
- El documento describe construir un AI coach usando speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El propósito declarado de la construcción es ayudar a gestionar la propia «monkey mind» del autor — source: 49140f9d5133d3c7

## Why it matters
Muestra que un ingeniero individual puede prototipar un agente de voz sin infraestructura de modelos propia: el coste de entrada es de composición, no de entrenamiento. Es un punto de partida para scaffolding de voz reutilizable, aunque este documento no aporta detalle de implementación, coste, fiabilidad ni manejo de privacidad del número virtual.

Se relaciona con «monkey mind como encuadre de productividad personal» porque comparte el marco de autogestión de la atención. Es evidencia de apoyo débil a la hipótesis del coach de voz como accountability. Conecta con los riesgos de privacidad y coste de asistentes de voz continuos. Para el ángulo de composición de APIs, enlaza con la composición condicional de prompts como abstracción enseñable.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[hipotesis-de-coach-de-voz-como-accountability-de-equipo]]
- relates_to → [[composicion-condicional-de-prompts-ensenable-a-principiantes]]
