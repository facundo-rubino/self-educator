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
updated: '2026-09-24'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- ai-agents
- ai-coach
- arquitectura
- composicion
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
last_reinforced: '2026-09-24'
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
---

## What it is
Un AI coach por voz se arma combinando cuatro servicios de terceros: speech-to-text, text-to-speech, un LLM y un número virtual de telefonía. Es una lista de componentes declarada por el autor, no una arquitectura observada ni un resultado medido.

## Evidence
- El coach descrito se compone de speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El ítem es un RSS con engagement=0: registra una afirmación, no un método revisado ni adoptado — source: 49140f9d5133d3c7

## Why it matters
El valor transferible es el patrón: ensamblar servicios existentes para probar una hipótesis de flujo personal con código propio mínimo. No acredita mejora de productividad, foco ni calidad de trabajo, y no hay artefacto, métricas ni retroalimentación de usuarios en el clúster.

Sostiene `prototipado-por-composicion-de-apis-sin-entrenamiento` como instancia concreta de ese patrón. Se relaciona con `ai-coach-voz-a-voz-ensamblado-de-servicios`, que describe el mismo ensamblado; esta nota es la variante específica de stack.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[monkey-mind-como-encuadre-de-productividad-personal]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
- relates_to → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
- supports → [[hipotesis-de-coach-de-voz-como-accountability-de-equipo]]
- relates_to → [[composicion-condicional-de-prompts-ensenable-a-principiantes]]
- supports → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- relates_to → [[ai-coach-voz-a-voz-ensamblado-de-servicios]]
