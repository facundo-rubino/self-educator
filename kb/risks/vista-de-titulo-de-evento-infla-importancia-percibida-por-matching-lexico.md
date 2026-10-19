---
id: vista-de-titulo-de-evento-infla-importancia-percibida-por-matching-lexico
title: El matching léxico «LLM/evaluator» infla la importancia percibida de eventos
  sin contenido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-15'
updated: '2026-10-19'
sources:
- d2a0c86ca8027978
- sig-b2a3f5dd7004
tags:
- falso-positivo
- falsos-positivos
- hackathon
- matching-lexico
- pipeline
- scoring
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro
  type: supports
- to: juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica
  type: supports
- to: llm-anthropic-0-29-topic-match-espurio-por-vocabulario
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: riesgo-de-propagacion-de-falsos-positivos-por-titulo
  type: relates_to
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: supports
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss-2
  type: supports
- to: juez-humano-en-hackathon-llm-as-a-judge-de-wandb-rol-declarado
  type: derived_from
- to: como-el-titulo-de-un-evento-no-es-un-hallazgo
  type: relates_to
---

## What it is
El título «Hackathon Judge» es una etiqueta de evento, no un hallazgo. El scorer lo eleva por solapamiento de keywords con «LLM»/«evaluator», no porque el documento cubra ningún eje del brief.

## Evidence
- El documento es una entrada RSS cuyo contenido es únicamente el rol de juez humano declarado — source: d2a0c86ca8027978
- No hay contenido técnico, hallazgos ni evidencia que toque los ejes del brief — source: d2a0c86ca8027978

## Why it matters
Señala un modo de fallo del pipeline: un título de evento puede parecer señal temática por vocabulario compartido. El efecto es una inflación de relevancia sin sustancia, que contamina la compilación aguas abajo.

Converge con `juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica`, `matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief` y `mecanica-de-evals-afirmada-desde-solo-titulo-rss-2`. Se deriva de la nota factual del clúster. Nota: el id `como-el-titulo-de-un-evento-no-es-un-hallazgo` es un enlace previsto, no verificado en el índice; si no existe, es un candidato a crear.

## Links
- supports → [[how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro]]
- supports → [[juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica]]
- supports → [[llm-anthropic-0-29-topic-match-espurio-por-vocabulario]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- relates_to → [[riesgo-de-propagacion-de-falsos-positivos-por-titulo]]
- supports → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- supports → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss-2]]
- derived_from → [[juez-humano-en-hackathon-llm-as-a-judge-de-wandb-rol-declarado]]
- relates_to → [[como-el-titulo-de-un-evento-no-es-un-hallazgo]]
