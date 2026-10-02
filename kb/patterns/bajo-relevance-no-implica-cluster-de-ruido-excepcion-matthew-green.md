---
id: bajo-relevance-no-implica-cluster-de-ruido-excepcion-matthew-green
title: 'Bajo relevance no siempre implica clúster de ruido: el caso «Quoting Matthew
  Green» es la excepción confirmada'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-02'
sources:
- sig-60c5604761f7
tags:
- relevance
- clustering
- calibracion
base_confidence: 0.7
half_life_days: 365
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: bajo-relevance-pero-al-menos-cinco-docs-on-topic
  type: relates_to
- to: quoting-matthew-green-cluster-sin-documento-de-matthew-green
  type: derived_from
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
---

## What it is
La nota existente sostiene que bajo relevance no implica clúster de ruido cuando hay al menos cinco documentos on-topic. Este clúster es el caso opuesto: relevance=0.20 y, verificado el contenido, ningún documento on-topic. La distinción se decide por inspección de contenido, no por el score.

## Evidence
- El clúster «Quoting Matthew Green» tiene relevance=0.20 y novelty=0.00, y ninguno de sus documentos aborda el tema declarado del brief — source: sig-60c5604761f7
- Existen al menos cinco documentos on-topic en el clúster citado como contraejemplo previo, según la nota existente — source: bajo-relevance-pero-al-menos-cinco-docs-on-topic

## Why it matters
El score de relevance por sí solo no decide si un clúster es ruido: hay que verificar el contenido. Este caso fija un extremo de la escala y evita que la heurística «bajo relevance ≠ ruido» se aplique sin inspección.

Se relaciona con `bajo-relevance-pero-al-menos-cinco-docs-on-topic` como caso complementario. Contradice la lectura general de `relevancia-tematica-baja-no-es-ruido` en su forma fuerte: aquí sí es ruido, verificado por contenido.

## Links
- relates_to → [[bajo-relevance-pero-al-menos-cinco-docs-on-topic]]
- derived_from → [[quoting-matthew-green-cluster-sin-documento-de-matthew-green]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
