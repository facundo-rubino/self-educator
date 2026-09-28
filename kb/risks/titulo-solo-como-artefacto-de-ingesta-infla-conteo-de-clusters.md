---
id: titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters
title: 'Un título-solo es artefacto de ingesta: infla el conteo de clústeres sin sumar
  señal'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- d2a0c86ca8027978
tags:
- ingesta
- pipeline
- rss-stub
- calidad-de-corpus
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: input-truncado-como-riesgo-sistemico-de-cobertura
  type: relates_to
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: clustering-por-embedding-produce-falsos-positivos
  type: relates_to
- to: wandb-llm-as-a-judge-hackathon-stub-sin-cuerpo
  type: derived_from
---

## What it is
Los ítems RSS cuyo cuerpo no resuelve en la ingesta entran al corpus como títulos solos: pasan el filtro determinista por relevancia léxica, pero aportan novelty=0.00 y engagement=0. Repetidos, inflan el recuento de clústeres sin añadir información al brief.

## Evidence
- Un documento con relevance=0.67, novelty=0.00 y engagement=0 consiste solo en un título/fragmento, sin cuerpo — source: d2a0c86ca8027978
- Se atribuye a una fuente RSS con engagement=0, sin interacción observada — source: d2a0c86ca8027978

## Why it matters
Los ítems título-solo recurrentes son candidatos a poda y obligan a re-ingerir la página fuente antes de que puedan informar cualquier conclusión. Un relevance alto sobre un stub no es relevancia sustantiva.

`supports` la nota que señala que el pipeline no recupera el cuerpo antes de evaluar clústeres RSS. `relates_to` los riesgos de ingesta truncada, de supervivencia al filtro determinista con relevancia alta y de falsos positivos por clustering sobre vocabulario genérico.

## Links
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- relates_to → [[input-truncado-como-riesgo-sistemico-de-cobertura]]
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- relates_to → [[clustering-por-embedding-produce-falsos-positivos]]
- derived_from → [[wandb-llm-as-a-judge-hackathon-stub-sin-cuerpo]]
