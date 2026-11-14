---
id: harness-agentico-de-seis-pasos-para-asegurar-codigo
title: Harness agéntico de seis pasos para asegurar código con LLMs
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-14'
updated: '2026-11-14'
sources:
- b8a2ffe60796b1b8
- 48abbf91d3309b20
tags:
- seguridad
- agentes
- llm
- harness
- source-code
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-14'
provenance:
  scale: S
  query: null
links:
- to: agentes-ia-aceleran-trabajo-acotado-y-verificable
  type: relates_to
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
---

## What it is
Un workflow de seis pasos propuesto para usar LLMs en el aseguramiento de código fuente: construir un threat model, descubrir vulnerabilidades, verificar hallazgos, triage y parchear. El material del clúster llega solo como dos ítems RSS casi duplicados que describen la misma charla/artículo, sin cuerpo ingerido ni ejemplo trabajado.

## Evidence
- El clúster propone un harness agéntico de seis pasos para trabajo de seguridad: threat model, descubrir vulnerabilidades, verificar, triage y parchear — source: b8a2ffe60796b1b8
- El mismo harness se enmarca con una rationale de «why now» más cuellos de botella organizacionales posteriores a la adopción — source: 48abbf91d3309b20

## Why it matters
Es un marcador de tópico («agentic security harness»), no un hallazgo validado: novelty=0.08, corroboración=0.50, engagement cero en ambos ítems. Su único valor utilizable es como puntero para seguir la fuente de forma independiente.

Se relaciona con el patrón de trabajo acotado y verificable de los agentes, y con la disciplina de evals por tarea, porque los pasos de verificación y triage son los que deciden si un hallazgo del LLM es accionable. Ninguna de esas conexiones está demostrada por la fuente.

## Links
- relates_to → [[agentes-ia-aceleran-trabajo-acotado-y-verificable]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
