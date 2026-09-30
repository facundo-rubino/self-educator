---
id: mecanica-de-evals-afirmada-desde-solo-titulo-rss
title: Afirmar una mecánica de evaluación desde un título RSS sin cuerpo
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-30'
sources:
- 93963a5f93e58d05
- d2a0c86ca8027978
tags:
- evals
- inferencia-desde-titular
- ingesta
- llm-eval
- rss
- sobreinterpretacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: task-families-evaluadas-en-el-documento-evals
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: supports
- to: mecanica-css-afirmada-desde-solo-titulo-rss
  type: relates_to
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: relates_to
---

## What it is
Modo de fallo recurrente del pipeline: un ítem que llega solo como título o marcador de rol, sin cuerpo, se lee como si describiera la mecánica de lo que nombra. En este caso, «LLM-as-a-Judge» se trataría como si el documento describiera cómo se juzga con LLM, cuando solo dice que alguien fue juez.

## Evidence
- El clúster del hackathon W&B contiene un único documento que es marcador de rol/título, sin cuerpo — source: d2a0c86ca8027978

## Why it matters
Generaliza un patrón ya registrado para CSS y para constraints de diseño: cuando el pipeline no recupera cuerpo, el título es la única señal y confundirlo con contenido envenena el grafo.

Replica la forma del riesgo «mecánica CSS afirmada desde un título RSS» y del riesgo sobre constraints de diseño desde títulos RSS.

## Links
- relates_to → [[task-families-evaluadas-en-el-documento-evals]]
- supports → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- relates_to → [[mecanica-css-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
