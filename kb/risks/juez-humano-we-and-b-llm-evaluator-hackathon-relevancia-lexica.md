---
id: juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica
title: La relevance 0.67 de este ítem es solapamiento de superficie con «LLM», no
  afinidad temática
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- d2a0c86ca8027978
tags:
- pipeline
- scoring
- falso-positivo
- relevance
- llm
base_confidence: 0.04
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: juez-humano-we-and-b-llm-evaluator-hackathon
  type: derived_from
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: supports
- to: falso-match-llm-as-a-judge-evaluacion-vs-brief-de-agentes-y-liderazgo
  type: supports
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss-2
  type: relates_to
---

## What it is
La relevance de 0.67 de este clúster frente a los temas del brief está impulsada por solapamiento de superficie con «LLM» y tooling para desarrolladores, no por contenido semántico [d2a0c86ca8027978]. Es la definición de libro de texto de una coincidencia léxica: `novelty` 0.00, `corroboration`/`velocity`/`surprise` en 0.50, es decir, el filtro determinista no aporta evidencia positiva sino su ausencia [d2a0c86ca8027978].

## Evidence
- `relevance` 0.67 atribuida explícitamente a solapamiento léxico con «LLM» y tooling para desarrolladores — source: d2a0c86ca8027978
- `novelty` 0.00 y `corroboration`/`velocity`/`surprise` en 0.50: todos en suelo o prior neutro — source: d2a0c86ca8027978
- El ítem superó el filtro siendo un único documento de peso cero con engagement=0 — source: d2a0c86ca8027978

## Why it matters
Es un candidato directo a endurecer los criterios de relevancia de ingesta para este brief: una relevance alta con novelty 0.00 y sin engagement no es corroboración, es su ausencia presentada como puntuación. Cualquier afirmación que conecte este ítem con las preguntas sustantivas del brief sería inferencia desde el título, no desde el contenido.

Deriva de la nota que registra el contenido real del clúster. `supports` las notas preexistentes sobre relevance léxica de «LLM-as-a-Judge» sin cubrir los ejes del brief y sobre el falso match de esa categoría frente al brief de agentes y liderazgo; se relaciona con el modo de fallo general de afirmar una mecánica de eval desde un solo título RSS.

## Links
- derived_from → [[juez-humano-we-and-b-llm-evaluator-hackathon]]
- supports → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- supports → [[falso-match-llm-as-a-judge-evaluacion-vs-brief-de-agentes-y-liderazgo]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss-2]]
