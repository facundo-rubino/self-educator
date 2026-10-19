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
updated: '2026-10-19'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-agents
- ai-coach
- arquitectura
- composicion
- composicion-de-apis
- composicion-de-servicios
- infraestructura
- integration
- llm
- personal-productivity
- prototipado
- stack
- stt
- telefonia
- tts
- voice
- voz
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-10-19'
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
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: supports
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: relates_to
- to: asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual
  type: relates_to
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: relates_to
- to: ai-coach-stt-tts-llm-loop-como-primitiva-no-demostrada-para-docencia
  type: relates_to
- to: api-coach-telefono-virtual-como-canal-asincrono-hipotesis
  type: relates_to
- to: ai-coach-como-herramienta-de-foco-personal
  type: relates_to
---

## What it is
Un «AI coach» personal se puede ensamblar con cuatro piezas de catálogo: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. El documento describe ese ensamblaje como el proyecto completo; no da arquitectura, flujo de integración ni evaluación. Es composición de servicios, no un sistema novedoso.

## Evidence
- El AI coach combina speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El proyecto se enmarca como forma de gestionar el «monkey mind» del autor — source: 49140f9d5133d3c7

## Why it matters
Fija el coste mínimo de un coach de voz: cuatro APIs y un número. Cualquier dev puede replicar el ensamblaje, pero el documento no muestra que el resultado sirva para organizarse ni para estudiar; el valor está en la composición, no en la evidencia.

`relates_to` el loop STT/TTS/LLM como primitiva no demostrada: es la misma idea vista como mecanismo. `relates_to` el canal telefónico como hipótesis de baja fricción: el número virtual es la única pieza que justifica el «voz a voz» frente a un chat.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[hipotesis-de-coach-de-voz-como-accountability-de-equipo]]
- relates_to → [[composicion-condicional-de-prompts-ensenable-a-principiantes]]
- supports → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- relates_to → [[asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-stt-tts-llm-loop-como-primitiva-no-demostrada-para-docencia]]
- relates_to → [[api-coach-telefono-virtual-como-canal-asincrono-hipotesis]]
- relates_to → [[ai-coach-como-herramienta-de-foco-personal]]
