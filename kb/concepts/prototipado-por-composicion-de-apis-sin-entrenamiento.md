---
id: prototipado-por-composicion-de-apis-sin-entrenamiento
title: Prototipado de agentes por composición de APIs, sin entrenamiento de modelos
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-24'
sources:
- 49140f9d5133d3c7
tags:
- agentes
- apis
- composicion
- composicion-de-apis
- prototipado
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: stack-de-ai-coach-voz-a-voz
  type: derived_from
- to: agent-based-stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: stack-de-ai-coach-voz-a-voz
  type: relates_to
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
---

## What it is
Ensamblar servicios existentes (STT, TTS, LLM, telefonía) en un asistente pequeño es una forma rápida de probar una hipótesis de flujo personal con código propio mínimo. El valor es como hipótesis a medir, no como técnica de productividad probada.

## Evidence
- El coach descrito se construye combinando speech-to-text, text-to-speech, un LLM y un número virtual — source: 49140f9d5133d3c7
- El clúster no incluye artefacto, código ni métricas que demuestren el resultado de la composición — source: 49140f9d5133d3c7

## Why it matters
Reconoce la actividad como práctica de ingeniería legítima — combinar componentes off-the-shelf — sin confundirla con evidencia de mejora. El coste real está en el mantenimiento posterior, no en el ensamblado inicial.

Se relaciona con `stack-de-ai-coach-voz-a-voz`, que es su instancia concreta. Conecta con `agentes-abatatan-ports-mantener-sigue-costoso` por el contraste entre coste de construcción y coste de mantenimiento.

## Links
- derived_from → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agent-based-stack-de-ai-coach-voz-a-voz]]
- relates_to → [[stack-de-ai-coach-voz-a-voz]]
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
