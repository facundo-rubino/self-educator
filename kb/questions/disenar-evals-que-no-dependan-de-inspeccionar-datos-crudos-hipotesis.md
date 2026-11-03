---
id: disenar-evals-que-no-dependan-de-inspeccionar-datos-crudos-hipotesis
title: 'Hipótesis: diseñar evaluaciones de agente que no requieran inspeccionar datos
  crudos del cliente'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-03'
updated: '2026-11-03'
sources:
- b8aebacaf4660f6c
- 2a3fe06e209d30d8
tags:
- evals
- observabilidad
- proxy-signals
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-11-03'
provenance:
  scale: S
  query: null
links:
- to: constraint-de-evaluacion-sin-trazas-legora
  type: derived_from
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
---

## What it is
El reporte propone señales proxy, métricas agregadas, harness en el lado del cliente o resúmenes sanitizados de trazas como formas de evaluar sin inspeccionar datos crudos del cliente. Ninguna de esas técnicas se describe ni se mide en el material; son implicaciones del analista, no prácticas documentadas.

## Evidence
- Legora no puede leer trazas del agente porque los datos son del cliente — source: b8aebacaf4660f6c
- El episodio cubre evals sin trazas — source: 2a3fe06e209d30d8

## Why it matters
Si el constraint es real, la evaluación tiene que rediseñarse. Qué técnica concreta funciona queda abierto: el clúster no trae mecanismo, ni métrica, ni comparación.

Deriva del constraint sin trazas. Se relaciona con la evaluación específica por tarea como infraestructura de fiabilidad, pero no la evidencia: es una pregunta, no un resultado.

## Links
- derived_from → [[constraint-de-evaluacion-sin-trazas-legora]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
