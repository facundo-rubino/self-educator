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
updated: '2026-09-18'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-agents
- arquitectura
- integration
- personal-productivity
- stack
- telefonia
- voice
- voz
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-18'
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
Un AI coach personal se compone de cuatro piezas: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. El documento lo describe como un build propio, sin detallar arquitectura, integración entre piezas ni elección de proveedores.

## Evidence
- El documento describe la construcción de un AI coach compuesto por speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7

## Why it matters
El stack es la superficie de integración mínima para un asistente por voz: telefonía como canal de entrada/salida y STT/TTS/LLM como procesamiento. Lo aprovechable aquí es el ejercicio de integración (aprender los límites de cada API y su encadenamiento), no un producto reutilizable ni una metodología. Un dev que lidera y enseña puede tratar este tipo de build como práctica de oficio acotada.

Se relaciona con `monkey-mind-como-encuadre-de-productividad-personal`: el stack es el medio, el encuadre es el fin declarado. Se relaciona con `efectividad-de-ai-coach-no-demostrada`: el stack no viene acompañado de evaluación. Se relaciona con `privacidad-y-costo-en-asistentes-de-voz-continuos`: un canal telefónico permanente abre esas preguntas incluso en un build personal.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
