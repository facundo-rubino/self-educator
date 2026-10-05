---
id: task-specific-llm-evals-relevancia-lexica-no-tematica
title: '«Task-Specific LLM Evals»: relevance=0.67 por coincidencia léxica en «evals»,
  no por conexión temática'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- 93963a5f93e58d05
tags:
- evals
- relevance-scoring
- lexical-match
- pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
  type: supports
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: relates_to
- to: how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief
  type: relates_to
---

## What it is
La relevance=0.67 asignada al clúster «Task-Specific LLM Evals» no proviene de una conexión argumental con el brief, sino del solapamiento del término genérico «evals»/«LLM» en el título. El documento no contiene ninguna afirmación sustantiva sobre agentes de IA aplicados a programar, gestionar, enseñar, liderazgo técnico, estimación, secuenciamiento, alcance u organización personal.

## Evidence
- La relevancia reportada (0.67) parece provenir del término genérico «evals», no de una conexión argumental con el tema del brief — source: 93963a5f93e58d05
- El único documento del clúster enumera tareas de evaluación (clasificación, resumen, traducción, regurgitación de copyright, toxicidad) sin afirmaciones sobre programación, gestión ni docencia — source: 93963a5f93e58d05

## Why it matters
Un score de relevancia léxico puede inducir a asignar cupo de compilación a un ítem sin contenido temático, desplazando documentos con señal real. Es el mismo modo de fallo que en otros matches léxicos del corpus.

Refuerza `task-specific-llm-evals-adyacencia-al-brief-no-demostrada`, que ya formulaba la carencia de vínculo con el brief. Es análogo al falso positivo léxico de `matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief` y de `how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief`. Relacionado con `task-specific-llm-evals-titulo-sin-contenido-ingerido`, que documenta la ausencia del cuerpo.

## Links
- supports → [[task-specific-llm-evals-adyacencia-al-brief-no-demostrada]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- relates_to → [[how-to-match-llm-patterns-titulo-como-match-lexico-sin-ejes-del-brief]]
