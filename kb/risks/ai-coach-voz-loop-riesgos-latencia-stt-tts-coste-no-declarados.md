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
updated: '2026-10-09'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- voz
- latencia
- coste
- riesgo
base_confidence: 0.04
half_life_days: 120
last_reinforced: '2026-10-09'
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
---

## What it is
Un coach por voz que ensambla STT, TTS, LLM y un número virtual arrastra riesgos de ingeniería evidentes —latencia del loop completo, calidad del STT y del TTS, coste por llamada— que el documento no reconoce [49140f9d5133d3c7]. Estos riesgos condicionan si el artefacto es usable como canal de interacción continuo.

## Evidence
- El documento enumera los cuatro componentes sin mencionar latencia, calidad ni coste — source: 49140f9d5133d3c7
- No hay métricas ni evaluación del flujo de voz — source: 49140f9d5133d3c7

## Why it matters
Citar el ensamblado como patrón funcional sería prematuro: sin reconocimiento de estos riesgos no hay evidencia de que el loop sea viable en uso real. Cualquier adopción en docencia o en flujos de equipo debería medir latencia y coste antes de comprometerse.

Deriva del stack enumerado. Se relaciona con los riesgos ya registrados de privacidad y coste en asistentes de voz continuos, y con el riesgo de asumir novedad en el simple ensamblado de STT, TTS, LLM y número virtual.

## Links
- derived_from → [[ai-coach-stack-stt-tts-llm-numero-virtual]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- relates_to → [[asumir-novedad-de-ensamblar-stt-tts-llm-numero-virtual]]
