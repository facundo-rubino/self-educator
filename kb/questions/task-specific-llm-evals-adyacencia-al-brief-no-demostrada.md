---
id: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
title: '«Task-Specific LLM Evals»: la adyacencia al brief es léxica, no demostrada'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-23'
sources:
- 93963a5f93e58d05
tags:
- evals
- llm
- brief
- relevancia
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
La conexión del documento con el brief (agentes LLM aplicados a programar, gestionar y enseñar; liderazgo técnico; oficio; productividad) descansa en la palabra «evals», no en un mecanismo compartido demostrado. Relevance=0.67 es la única dimensión por encima del punto medio.

## Evidence
- El clúster tiene relevance=0.67 y el resto de dimensiones en o por debajo de 0.50 — source: 93963a5f93e58d05
- El documento no se recuperó con cuerpo que conecte sus categorías con agentes de coding, gestión o docencia — source: 93963a5f93e58d05

## Why it matters
Señala una pregunta abierta: ¿basta la coincidencia de vocabulario («evals») para que un documento entre en este brief? Si no se responde con contenido, el criterio de admisión del pipeline queda sin justificar.

Apoya a `task-specific-llm-evals-titulo-sin-contenido-ingerido` porque ambas describen la falta de cuerpo. Se relaciona con `relevancia-tematica-baja-no-es-ruido` y `relevancia-no-es-verdad` y refuerza `mismatch-query-tema-por-vocabulario-generico-de-infraestructura`, que ya documenta el mismo modo de fallo.

## Links
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-no-es-verdad]]
