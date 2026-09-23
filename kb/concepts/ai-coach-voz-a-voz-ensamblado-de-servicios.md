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
updated: '2026-09-23'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- voice
- integration
- prototyping
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-23'
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
---

## What it is
Un coach personal de voz se construye ensamblando cuatro servicios existentes: speech-to-text, text-to-speech, un LLM y un número de teléfono virtual. No hay entrenamiento de modelos propios; el valor está en la orquestación, no en la tecnología base.

## Evidence
- El documento describe un AI coach hecho con speech-to-text, text-to-speech, un LLM y un número de teléfono virtual, es decir, integración de servicios comerciales en vez de modelos propios — source: 49140f9d5133d3c7

## Why it matters
Es un precedente de «comprar/ensamblar antes que construir» para prototipar una herramienta interna: alcance reducido, coste de integración bajo, sin I+D de modelos. Fija el mínimo arquitectónico del género.

Se relaciona con `stack-de-ai-coach-voz-a-voz` (posible solapamiento de descripción de componentes: verificar si deben fusionarse). Es un caso de `prototipado-por-composicion-de-apis-sin-entrenamiento`. Soporta `efectividad-de-ai-coach-no-demostrada` y `privacidad-y-costo-en-asistentes-de-voz-continuos` al no reportar métricas ni tratamiento de datos.

## Links
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[prototipado-por-composicion-de-apis-sin-entrenamiento]]
- supports → [[efectividad-de-ai-coach-no-demostrada]]
- supports → [[privacidad-y-costo-en-asistentes-de-voz-continuos]]
