---
id: relevance-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
title: 'relevance=0.67 sin evidencia extraíble: artefacto del scorer, no acuerdo topical'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-09'
sources:
- d2a0c86ca8027978
tags:
- artefacto-de-pipeline
- falsos-positivos
- ingesta
- relevance
- relevancia
- scorer
- scoring
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: wandb-llm-as-a-judge-hackathon-sin-corroboracion
  type: supports
- to: relevancia-no-es-verdad
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
- to: matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief
  type: relates_to
- to: juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
---

## What it is
El scorer asigna relevance=0.67 al ítem «Weights & Biases LLM-Evaluator Hackathon - Hackathon Judge» [d2a0c86ca8027978] pese a que el documento no contiene ningún eje extraíble del brief. La cifra parece medir solapamiento léxico con «LLM» y «evaluación», no conexión temática con agentes de programación, liderazgo técnico o docencia.

## Evidence
- El documento solo contiene una descripción de rol de juez humano — source: d2a0c86ca8027978
- No hay en él ningún claim sustantivo sobre programación, gestión, docencia, estimación o craft — source: d2a0c86ca8027978

## Why it matters
Una relevance alta sobre un documento vacío sesga hacia abajo los resúmenes que leen esa métrica como aval temático y puede fabricar corroboración con otros clústeres que solo comparten vocabulario. Donde no hay ejes del brief, la relevance debería reflejarlo.

Es el mismo fenómeno que ya documentan las notas de relevancia léxica frente al brief en ítems con «LLM» en el título. Refuerza la nota sobre corroboración y velocidad como artefactos del scorer, extendiéndola a la dimensión de relevance.

## Links
- supports → [[wandb-llm-as-a-judge-hackathon-sin-corroboracion]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[matching-llm-as-a-judge-relevancia-lexica-sin-ejes-del-brief]]
- relates_to → [[juez-humano-we-and-b-llm-evaluator-hackathon-relevancia-lexica]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
