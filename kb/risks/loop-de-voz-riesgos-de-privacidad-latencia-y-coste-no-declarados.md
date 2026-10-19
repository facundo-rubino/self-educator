---
id: loop-de-voz-riesgos-de-privacidad-latencia-y-coste-no-declarados
title: 'Privacidad, latencia y coste por llamada: riesgos no declarados del coach
  de voz'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-19'
updated: '2026-10-19'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- privacidad
- latencia
- coste
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: privacidad-y-costo-en-asistentes-de-voz-continuos
  type: relates_to
- to: ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados
  type: supports
---

## What it is
Un coach de voz que corre sobre APIs de terceros expone audio personal a STT y TTS, depende de la latencia combinada de tres servicios y paga por turno de conversación. El documento no menciona ninguno de esos tres costes. Son riesgos estructurales del ensamblaje, independientes de si el coach funciona.

## Evidence
- El stack es STT + TTS + LLM + número virtual, sin mención a tratamiento de datos ni coste — source: 49140f9d5133d3c7
- No hay información sobre fiabilidad del LLM ni sobre resultados de uso — source: 49140f9d5133d3c7

## Why it matters
Antes de proponer un asistente de voz a un equipo o a estudiantes, hay que resolver privacidad del audio y modelar el coste por sesión. Sin eso, el prototipo barato se convierte en un compromiso caro y difícil de retirar.

`derived_from` el stack de cuatro servicios: cada pieza añade dependencia. `supports` la nota existente sobre riesgos del loop de voz, que esta compilación confirma sin añadir medición.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados]]
