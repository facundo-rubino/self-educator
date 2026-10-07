---
id: stack-de-ai-coach-voz-a-voz-ensamblado
title: 'Stack de un AI coach por voz: STT + TTS + LLM + número virtual'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- voice
- stack
- personal-productivity
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: ai-coach-voz-a-voz-ensamblado-de-servicios
  type: relates_to
- to: ai-coach-como-herramienta-de-foco-no-de-liderazgo
  type: derived_from
- to: prototipado-por-composicion-de-apis-sin-entrenamiento
  type: supports
- to: ai-coach-voz-a-voz-ensamblado-de-servicios-2024
  type: contradicts
---

## What it is
Un AI coach personal se construye ensamblando cuatro servicios existentes: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. No hay entrenamiento ni modelo propio; el valor está en la composición de APIs ya disponibles.

## Evidence
- El documento describe la construcción de un «AI coach» personal combinando speech-to-text, text-to-speech, un LLM y un número de teléfono virtual — source: 49140f9d5133d3c7
- El ensamblado se presenta como proyecto/hobby narrado, sin evaluación de eficacia — source: 49140f9d5133d3c7

## Why it matters
Muestra que el envoltorio de un LLM en canales de voz/telefonía para un asistente personal es alcanzable sin infraestructura propietaria. Lo que no aporta es evidencia de que el resultado funcione mejor que un chat de texto, ni de que la práctica transfiera a ingeniería o docencia.

Se relaciona con `ai-coach-voz-a-voz-ensamblado-de-servicios` (mismo stack descrito en el clúster previo); se apoya en `prototipado-por-composicion-de-apis-sin-entrenamiento` como caso adicional; y se deriva del encuadre `ai-coach-como-herramienta-de-foco-no-de-liderazgo`, que acota su alcance a productividad personal.

Se marca `contradicts` sobre `ai-coach-voz-a-voz-ensamblado-de-servicios-2024` si esa nota afirmara novedad del stack: este documento lo repite sin añadir nada.

## Links
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
- derived_from → [[ai-coach-como-herramienta-de-foco-no-de-liderazgo]]
- supports → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- contradicts → [[ai-coach-voz-a-voz-ensamblado-de-servicios-2024]]
