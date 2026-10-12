---
id: task-specific-llm-evals-do-dont-work-titulo-sin-contenido-ingerido
title: '«Task-Specific LLM Evals that Do & Don''t Work»: título y alcance declarado
  sin contenido ingerido (variante)'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-12'
sources:
- 93963a5f93e58d05
tags:
- corpus-truncado
- evals
- ingesta
- ingesta-truncada
- llm
- matching-por-titulo
- modo-de-fallo
- riesgo
- rss
- ruido
- titulo-sin-cuerpo
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: relates_to
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: mecanica-de-evals-afirmada-desde-solo-titulo-rss
  type: supports
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable
  type: derived_from
---

## What it is
Variante de registro del mismo hecho: el clúster de título y alcance declarado carece de cuerpo ingerido. Se mantiene como nodo separado solo para no romper los `contradicts`/`relates_to` que ya apuntan a él desde el grafo existente.

## Evidence
- Único contenido sustantivo: la lista de categorías de tarea — source: 93963a5f93e58d05
- Sin metodología, sin resultados, sin modos de fallo — source: 93963a5f93e58d05

## Why it matters
Es duplicado y debe fusionarse con el nodo principal en la próxima pasada de reconciliación. Se deja explícito como riesgo de inflación de conteo: dos nodos describiendo el mismo clúster de un solo documento hacen parecer que hay más señal de la que hay.

`relates_to` con el nodo principal, que es su equivalente. `derived_from` la nota sobre las familias declaradas como único contenido verificable, porque ambos describen el mismo material de origen sin añadir evidencia nueva.

## Links
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[mecanica-de-evals-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- derived_from → [[task-specific-llm-evals-familias-de-tarea-declaradas-como-unico-contenido-verificable]]
