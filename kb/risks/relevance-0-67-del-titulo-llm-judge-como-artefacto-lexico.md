---
id: relevance-0-67-del-titulo-llm-judge-como-artefacto-lexico
title: 'relevance=0.67 en el clúster del hackathon W&B: artefacto léxico del título
  «LLM»+«judge»'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- d2a0c86ca8027978
tags:
- matching-lexico
- relevance
- falso-positivo
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: juez-humano-en-hackathon-llm-as-a-judge-de-wandb
  type: derived_from
- to: how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro
  type: relates_to
- to: clusters-de-buzzword-compartido-no-indican-tendencia
  type: supports
---

## What it is
La relevance=0.67 del clúster proviene de que el título contiene «LLM» y «judge», no de un vínculo topical demostrado con construcción de agentes, docencia o liderazgo técnico. Es una coincidencia léxica de superficie. — source: d2a0c86ca8027978

## Evidence
- El título del ítem menciona «LLM» y «judge»; no hay cuerpo que establezca la conexión con los ejes del brief. — source: d2a0c86ca8027978
- La relevancia reportada es 0.67 junto a novelty 0.00. — source: d2a0c86ca8027978

## Why it matters
Sobrestimar este score llevaría a asignar cupo del brief a un documento vacío. El score mide solapamiento de superficie, no afinidad temática verificada.

Se deriva del clúster (`juez-humano-en-hackathon-llm-as-a-judge-de-wandb`). Es el mismo patrón que el falso positivo léxico del filtro en `how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro` y refuerza que un buzzword compartido no es tendencia (`clusters-de-buzzword-compartido-no-indican-tendencia`).

## Links
- derived_from → [[juez-humano-en-hackathon-llm-as-a-judge-de-wandb]]
- relates_to → [[how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro]]
- supports → [[clusters-de-buzzword-compartido-no-indican-tendencia]]
