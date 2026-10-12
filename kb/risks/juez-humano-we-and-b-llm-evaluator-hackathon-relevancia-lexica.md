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
updated: '2026-10-12'
sources:
- d2a0c86ca8027978
tags:
- falso-positivo
- llm
- llm-as-a-judge
- pipeline
- relevance
- relevancia-lexica
- scoring
base_confidence: 0.04
half_life_days: 120
last_reinforced: '2026-10-12'
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
- to: juez-humano-we-and-b-llm-as-a-judge-hackathon-sin-contenido-ingerido
  type: derived_from
- to: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
  type: supports
---

## What it is
La relevance=0.67 del clúster es la única señal positiva, y es probable que provenga de coincidencia de superficie en keywords como «LLM», «judge» y «hackathon». Con novelty=0.00 y corroboration=0.50, esa relevancia no se apoya en ningún eje del brief.

## Evidence
- La relevancia del clúster es 0.67 mientras novelty=0.00 y corroboration=0.50 — source: d2a0c86ca8027978
- El documento subyacente es una entrada RSS con engagement=0 y sin afirmaciones sustantivas sobre el tema del brief — source: d2a0c86ca8027978

## Why it matters
Usar esta nota como evidencia de práctica en evaluación de LLM sería leer el scorer como si midiera afinidad temática. El riesgo es que un ítem con vocabulario adyacente al brief se propague como supuesto hallazgo.

Deriva de la nota principal del clúster. Refuerza `matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief` y `relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer`, que documentan el mismo patrón de falsa señal.

## Links
- derived_from → [[juez-humano-we-and-b-llm-evaluator-hackathon]]
- supports → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- supports → [[falso-match-llm-as-a-judge-evaluacion-vs-brief-de-agentes-y-liderazgo]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss-2]]
- derived_from → [[juez-humano-we-and-b-llm-as-a-judge-hackathon-sin-contenido-ingerido]]
- supports → [[relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer]]
