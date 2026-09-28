---
id: how-to-match-llm-patterns-candidato-a-retrieval-o-descarte
title: '«How to Match LLM Patterns to Problems»: candidato a retrieval de texto completo
  o a descarte, no a insight corroborado'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-28'
sources:
- 0248fdb60811e91e
tags:
- descarte
- ingesta
- llm-patterns
- pipeline
- retrieval
- stub
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido
  type: derived_from
- to: pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques
  type: relates_to
- to: argumento-ex-silentio-en-corpus-truncado
  type: contradicts
- to: how-to-match-llm-patterns-titulo-sin-contenido-ingerido
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
---

## What it is
Pregunta abierta: dado que solo se ingirió título y subtítulo, ¿debe este documento recuperarse en texto completo para evaluar sus claims, o descartarse del brief? Hasta que se recupere el cuerpo, no hay base para acreditar ningún hallazgo.

## Evidence
- El clúster contiene un único documento RSS-ingestado del que solo hay título y snippet de una línea — source: 0248fdb60811e91e
- El titular promete un mapeo problema-patrón (externo/interno, datos/no-datos) sin cuerpo que lo desarrolle — source: 0248fdb60811e91e

## Why it matters
Si el documento completo argumentase que la elección de patrón LLM depende de restricciones externo/interno y datos/no-datos, podría dar una heurística ligera para un dev líder. Sin cuerpo, esa posibilidad no es una hipótesis sostenida por evidencia, solo un candidato de retrieval.

Deriva de la nota sobre título sin contenido ingerido. Refuerza la nota sobre el pipeline que evalúa clústeres RSS sin recuperar antes el cuerpo.

## Links
- derived_from → [[how-to-match-llm-patterns-to-problems-titulo-sin-contenido-ingerido]]
- relates_to → [[pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques]]
- contradicts → [[argumento-ex-silentio-en-corpus-truncado]]
- derived_from → [[how-to-match-llm-patterns-titulo-sin-contenido-ingerido]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
