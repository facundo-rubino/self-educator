---
id: how-to-match-llm-patterns-relevancia-lexica-sin-ejes-del-brief-3
title: «LLM patterns» solapa léxicamente con «agentes de IA» sin cubrir un eje del
  brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-06'
sources:
- 0248fdb60811e91e
tags:
- falso-positivo-lexico
- matching
- brief
- agentes
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido-3
  type: relates_to
- to: corroboration-1-00-con-relevance-0-20-metrica-degenerada
  type: relates_to
- to: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
  type: relates_to
---

## What it is
El título de este clúster sobrevive al filtro determinista por coincidencia de tokens («LLM», «patterns», «problems») con el vocabulario del brief (agentes de IA, patrones, problemas de ingeniería). Pero el clúster no contiene ninguna afirmación sobre programar, liderar o enseñar: la conexión es de superficie, no temática.

## Evidence
- engagement=0, novelty=0.00, corroboration=0.50 en el único documento — source: 0248fdb60811e91e
- El crítico identifica la interpretación de «adyacencia a la toma de decisiones arquitectónicas» como descansando en solapamiento léxico, no en aserciones verificadas de la fuente — source: 0248fdb60811e91e
- No hay declaraciones explícitas sobre agentes aplicados a programar, gestionar o enseñar — source: 0248fdb60811e91e

## Why it matters
Tratar este signal como evidencia de práctica o como base para una decisión de tooling sería sobreinterpretar una coincidencia de tokens. El registro correcto es que el clúster no cubre ningún eje del topic declarado, más allá del léxico compartido.

Es el caso concreto de la observación general en `corroboration-1-00-con-relevance-0-20-metrica-degenerada`: un score alto en una métrica de superficie no es señal temática. Se solapa con `matching-llm-patterns-relevancia-lexica-al-brief-de-agentes` como instancia adicional del mismo falso positivo. Y se apoya en la nota de ausencia de cuerpo `how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido-3`: sin cuerpo, el solapamiento léxico es lo único que sostiene la relevancia.

## Links
- relates_to → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido-3]]
- relates_to → [[corroboration-1-00-con-relevance-0-20-metrica-degenerada]]
- relates_to → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
