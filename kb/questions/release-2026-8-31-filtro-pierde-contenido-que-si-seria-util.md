---
id: release-2026-8-31-filtro-pierde-contenido-que-si-seria-util
title: 'Pregunta abierta: ¿qué contenido sustantivo de la serie MCP quedó fuera del
  feed y no llegó al clúster?'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- 30a26335a9988ba2
- 9750590bbfe6b285
- 5a4df6bef0a4905f
- ffbd76916d1dfdc5
- 748f8b0a02cd7524
- b9106690f5dfd849
tags:
- mcp
- cobertura
- pipeline
base_confidence: 0.4
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: release-2026-8-31-cluster-falso-positivo-del-filtro
  type: derived_from
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
---

## What it is
El clúster captura únicamente el formato de release. No responde si existen notas de changelog, discusiones o PRs asociados a estas versiones que sí describan cambios de comportamiento. La cobertura del corpus no permite saberlo.

## Evidence
- Los seis documentos son stubs de release sin prosa, changelog ni discusión — source: 30a26335a9988ba2, 9750590bbfe6b285, 5a4df6bef0a4905f, ffbd76916d1dfdc5, 748f8b0a02cd7524, b9106690f5dfd849

## Why it matters
Antes de descartar la serie como ruido conviene registrar qué quedó fuera. Si el pipeline solo ingiere feeds de bumps, la ausencia de changelog es artefacto de ingesta, no propiedad de los releases.

Deriva del diagnóstico de falso positivo del filtro y se relaciona con el riesgo sistémico de ingesta truncada.

## Links
- derived_from → [[release-2026-8-31-cluster-falso-positivo-del-filtro]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
