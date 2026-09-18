---
id: privacidad-y-costo-en-asistentes-de-voz-continuos
title: Riesgos de privacidad y costo de un asistente de voz basado en LLM y telefonía
type: risk
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
- cost
- privacy
- telephony
- voice
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: efectividad-de-ai-coach-no-demostrada
  type: relates_to
---

## What it is
Un coach por voz que corre sobre un número telefónico virtual y un LLM implica (a) que el audio personal pasa por STT y por un proveedor de modelo, y (b) que hay un costo variable por minuto o por token en un canal que se pretende siempre disponible. Ninguna de las dos está discutida en el documento.

## Evidence
- El documento describe un AI coach compuesto por speech-to-text, text-to-speech, un LLM y un número virtual, sin tratar implicaciones de privacidad ni de costo — source: 49140f9d5133d3c7

## Why it matters
Un asistente de voz continuo es un canal de captura de pensamiento sin filtro; ese material es exactamente el que un dev no querría enviar a un proveedor externo sin control. Y una interfaz «siempre disponible» tiende a usarse más de lo previsto, lo que convierte el costo variable en una decisión de diseño, no en un detalle de factura.

Deriva de `stack-de-ai-coach-voz-a-voz`: es consecuencia directa de las piezas elegidas. Se relaciona con `efectividad-de-ai-coach-no-demostrada`: sin evaluación de resultado, el costo y la exposición se asumen sin retorno verificado.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[efectividad-de-ai-coach-no-demostrada]]
