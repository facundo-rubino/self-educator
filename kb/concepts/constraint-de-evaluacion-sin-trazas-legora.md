---
id: constraint-de-evaluacion-sin-trazas-legora
title: 'Construir y testear agentes sin poder ver sus trazas: el constraint de Legora'
type: concept
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
tags:
- agentes
- evaluacion
- observabilidad
- confidencialidad
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-11-03'
provenance:
  scale: S
  query: null
links:
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: agentes-ia-aceleran-trabajo-acotado-y-verificable
  type: relates_to
---

## What it is
Legora no puede leer ninguna traza de lo que su agente hace para un abogado porque los datos pertenecen a los clientes de la firma legal. Eso obliga a construir, testear y enviar agentes bajo un régimen sin trazas: no hay inspección del trabajo del agente en producción. La pregunta central de la entrevista es exactamente esa: cómo construir y testear un agente cuando no puedes ver su trabajo.

## Evidence
- Legora no puede leer ninguna traza de lo que su agente hace para un abogado porque los datos pertenecen a los clientes de la firma — source: b8aebacaf4660f6c
- La pregunta central de la entrevista es cómo construir y testear un agente cuando no puedes ver su trabajo — source: b8aebacaf4660f6c

## Why it matters
Si no puedes observar la ejecución, la evaluación y la depuración dejan de ser actividades posteriores al build y pasan a ser restricciones de diseño. Cualquier flujo que asuma trazas accesibles falla por defecto en este contexto.

Conecta con la evaluación específica por tarea como infraestructura de fiabilidad: el constraint elimina una de las fuentes de evidencia (las trazas) y fuerza a sustituirla. También roza la tesis de que los agentes aceleran trabajo acotado y verificable, porque aquí lo verificable no es directamente observable.

## Links
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[agentes-ia-aceleran-trabajo-acotado-y-verificable]]
