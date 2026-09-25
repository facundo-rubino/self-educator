---
id: ingesta-truncada-como-riesgo-sistemico-de-cobertura
title: 'Riesgo de ingesta truncada: clústeres evaluados sobre cuerpos vacíos'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-25'
sources:
- 43e006f4538b71dd
- 93963a5f93e58d05
tags:
- cobertura
- ingesta
- pipeline
- riesgo-sistemico
- senal
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: argumento-ex-silentio-en-corpus-truncado
  type: supports
- to: task-specific-llm-evals-singleton-rss-engagement-cero-novelty-cero
  type: relates_to
---

## What it is
Riesgo estructural del pipeline: los metadatos pueden estar incompletos o el ítem RSS puede ser un stub. Si el cuerpo completo se ingiere después, podría reforzar o invalidar cualquier interpretación hecha solo a partir del título.

## Evidence
- El resumen del pipeline advierte que el metadato por sí solo puede ser incompleto y que el ítem RSS podría ser un stub — source: 93963a5f93e58d05
- Las conclusiones derivadas solo del título son frágiles según el propio informe del pipeline — source: 93963a5f93e58d05

## Why it matters
Justifica no cerrar el caso de este ítem como «evaluado y descartado»: lo correcto es registrarlo como cobertura incompleta hasta que exista cuerpo. Afecta a cualquier evaluación de clúster hecha sin texto.

`supports` la nota existente de que el pipeline evalúa clústeres RSS cuyo cuerpo no recuperó. Se relaciona con el riesgo de singleton sin engagement porque ambos nacen del mismo tramo del pipeline.

## Links
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- supports → [[argumento-ex-silentio-en-corpus-truncado]]
- relates_to → [[task-specific-llm-evals-singleton-rss-engagement-cero-novelty-cero]]
