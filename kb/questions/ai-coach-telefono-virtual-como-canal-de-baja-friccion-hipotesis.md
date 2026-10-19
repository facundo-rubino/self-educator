---
id: ai-coach-telefono-virtual-como-canal-de-baja-friccion-hipotesis
title: 'El número virtual como canal de baja fricción para un coach: hipótesis sin
  medir'
type: question
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
- telefonia
- canal
- hipotesis
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: ai-coach-telefono-como-canal-asincrono-baja-friccion-hipotesis
  type: contradicts
- to: ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados
  type: relates_to
---

## What it is
La elección de un número de teléfono virtual frente a una app sugiere la hipótesis de que llamar es menos fricción que abrir una interfaz. El documento no la argumenta ni la mide. Queda como pregunta: ¿el canal de voz telefónica reduce el coste de iniciar una sesión de foco o de repaso?

## Evidence
- El stack incluye un número virtual además de STT, TTS y LLM — source: 49140f9d5133d3c7
- El documento no compara el canal telefónico con alternativas ni reporta uso — source: 49140f9d5133d3c7

## Why it matters
Si la hipótesis fuera cierta, un docente podría montar un canal de repaso por voz para estudiantes con un coste mínimo. Si es falsa, el número virtual es la pieza más cara y menos justificada del stack. Sin datos, ninguna de las dos ramas se puede recomendar.

`contradicts` la nota previa que ya registraba la misma hipótesis sin evidencia nueva: dos formulaciones de la misma conjetura no la refuerzan. `relates_to` los riesgos de latencia y coste por llamada del loop de voz, que condicionan cualquier adopción.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- contradicts → [[ai-coach-telefono-como-canal-asincrono-baja-friccion-hipotesis]]
- relates_to → [[ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados]]
