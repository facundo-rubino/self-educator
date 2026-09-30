---
id: relevancia-1-00-no-es-validacion-del-cluster
title: relevancia=1.00 no es validación del clúster cuando novelty=0.00 y corroboración=0.50
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- 31820ad25e39a34b
tags:
- scoring
- pipeline
- metrica-degenerada
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: llm-anthropic-0-29-topic-match-espurio-por-vocabulario
  type: derived_from
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: scores-neutrales-de-cluster-no-corroban-una-lectura-de-contenido
  type: supports
---

## What it is
Un score de relevancia=1.00 convive aquí con novelty=0.00 y corroboración=0.50 [31820ad25e39a34b]. Tomar el máximo de relevancia como validación del clúster ignora que las otras dos dimensiones indican ausencia de señal temática novedosa y de triangulación.

## Evidence
- Con novelty=0.00 y corroboración=0.50, el clúster no aporta señal temática nueva ni triangulada — source: 31820ad25e39a34b
- El score de relevancia=1.00 del pipeline parece un falso positivo por contenido — source: 31820ad25e39a34b

## Why it matters
La relevancia es una medida de solapamiento con el tema, no de verdad ni de novedad. Un clúster puede puntuar 1.00 en relevancia y seguir sin contener ningún hallazgo compilable.

Deriva de la lectura del match léxico (`llm-anthropic-0-29-topic-match-espurio-por-vocabulario`). Refuerza el patrón `corroboracion-y-velocidad-como-artefactos-del-scorer` y se relaciona con `scores-neutrales-de-cluster-no-corroban-una-lectura-de-contenido`.

## Links
- derived_from → [[llm-anthropic-0-29-topic-match-espurio-por-vocabulario]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- supports → [[scores-neutrales-de-cluster-no-corroban-una-lectura-de-contenido]]
