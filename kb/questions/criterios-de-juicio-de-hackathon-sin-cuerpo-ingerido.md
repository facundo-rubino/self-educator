---
id: criterios-de-juicio-de-hackathon-sin-cuerpo-ingerido
title: Los criterios de juicio del hackathon de W&B no vienen con cuerpo ingerido
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- d2a0c86ca8027978
tags:
- hackathon
- wandb
- ingesta-truncada
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: juez-humano-en-hackathon-llm-as-a-judge-de-wandb
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
---

## What it is
El clúster declara que no hay descripción de criterios de juicio, cuenta de lo construido ni conclusiones extraíbles. No puede determinarse si esa ausencia refleja el estado real de la fuente o un fallo de ingesta del pipeline.

## Evidence
- El clúster afirma que no hay contenido sustantivo: ni descripción de criterios de juicio, ni cuenta de lo construido, ni conclusiones — source: d2a0c86ca8027978
- El documento muestra novelty=0.00 y corroboration=0.50, sin documentos corroborantes — source: d2a0c86ca8027978

## Why it matters
Si el snippet solo no fue recuperado o parseado, declarar «sin evidencia utilizable» sería un artefacto de procesamiento disfrazado de juicio sustantivo. Queda abierto si el documento es un stub, un error de feed o un anuncio, y si su tema declarado se desarrolla en algún lugar del corpus.

Depende de `juez-humano-en-hackathon-llm-as-a-judge-de-wandb` para el hecho de la ingesta. Refuerza `pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss`: la evaluación del clúster ocurrió sobre un cuerpo que el pipeline no recuperó.

## Links
- derived_from → [[juez-humano-en-hackathon-llm-as-a-judge-de-wandb]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
