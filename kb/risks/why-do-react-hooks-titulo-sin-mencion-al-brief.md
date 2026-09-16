---
id: why-do-react-hooks-titulo-sin-mencion-al-brief
title: El artículo sobre call order de Hooks no menciona ningún eje del brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- 29e59ab83043dfa3
tags:
- react
- brief
- filtrado
- falsos-positivos
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: why-do-react-hooks-rely-on-call-order-titulo-sin-contenido-ingerido
  type: derived_from
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
---

## What it is
El documento de [29e59ab83043dfa3] no menciona agentes de IA aplicados a programar, gestionar o enseñar; tampoco liderazgo técnico de equipos chicos, estimación, secuenciamiento, alcance, organización personal, docencia entry-level, productividad ni técnicas de estudio. Su conexión con el brief es tangencial, vía «oficio de software engineering» entendido como fundamentos de un framework.

## Evidence
- El documento no menciona agentes de IA aplicados a programar, gestionar o enseñar — source: 29e59ab83043dfa3
- No aborda liderazgo técnico de equipos chicos, estimación, secuenciamiento, alcance ni organización personal — source: 29e59ab83043dfa3
- No trata docencia de programación entry-level, productividad ni técnicas de estudio — source: 29e59ab83043dfa3

## Why it matters
Si el pipeline agrupa por similitud de embeddings, este caso sugiere revisar el umbral de clustering o las señales de filtrado: un artículo de React no debería competir por cupo analítico con material de liderazgo, docencia e IA. La consecuencia operativa es evitar que falsos positivos así desplacen a clústeres con señal real.

Se deriva de `why-do-react-hooks-rely-on-call-order-titulo-sin-contenido-ingerido`: sin cuerpo, lo único evaluable es la ausencia de mención temática. Contradice matizadamente a `relevancia-tematica-baja-no-es-ruido`, que advierte que baja relevancia no equivale automáticamente a descarte; aquí la ausencia de mención de cualquier eje del brief sí justifica no consumir cupo.

## Links
- derived_from → [[why-do-react-hooks-rely-on-call-order-titulo-sin-contenido-ingerido]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
