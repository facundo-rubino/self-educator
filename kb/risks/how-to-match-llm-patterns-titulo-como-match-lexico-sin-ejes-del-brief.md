---
id: how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief
title: «LLM patterns» solapa léxicamente con «agentes de IA» sin cubrir ningún eje
  del brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-10-02'
sources:
- 0248fdb60811e91e
tags:
- brief
- falso-positivo-lexico
- match-lexico
- relevance
- relevancia-baja
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido
  type: derived_from
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido
  type: supports
- to: how-to-match-llm-patterns-taxonomia-sin-contenido
  type: derived_from
- to: how-to-match-llm-patterns-relevancia-baja-sin-ejes-del-topic
  type: supports
- to: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
  type: supports
---

## What it is
El ítem entró al brief por el solapamiento entre «LLM patterns» y «agentes de IA». Ninguno de los ejes del brief (agentes aplicados a programar, gestionar o enseñar; liderazgo técnico; estimación; secuenciamiento; oficio) queda cubierto por el título y el subtítulo disponibles.

## Evidence
- La señal tiene relevance=0.33 frente al brief de agentes, liderazgo y docencia, con un único documento y sin corroboración — source: 0248fdb60811e91e.

## Why it matters
Compilar esta señal como contribución temática introduciría ruido de recuperación en el grafo. Su único valor posible es como candidato a retrieval de texto completo si alguna vez se ingiere el cuerpo, no como insight corroborado.

Confirma el patrón de match léxico por vocabulario compartido. Se apoya en las notas de riesgo ya existentes sobre la baja relevancia de este ítem respecto al topic.

## Links
- derived_from → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
- supports → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido]]
- derived_from → [[how-to-match-llm-patterns-taxonomia-sin-contenido]]
- supports → [[how-to-match-llm-patterns-relevancia-baja-sin-ejes-del-topic]]
- supports → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
