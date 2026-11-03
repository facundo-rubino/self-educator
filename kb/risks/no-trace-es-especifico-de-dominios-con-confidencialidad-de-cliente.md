---
id: no-trace-es-especifico-de-dominios-con-confidencialidad-de-cliente
title: El régimen sin trazas es específico de dominios regulados con confidencialidad
  de cliente
type: risk
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
- generalizacion
- confidencialidad
- dominio
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-11-03'
provenance:
  scale: S
  query: null
links:
- to: constraint-de-evaluacion-sin-trazas-legora
  type: contradicts
- to: legora-cto-jacob-lauritzen-legal-ai
  type: relates_to
---

## What it is
El constraint de no ver trazas proviene de que los datos pertenecen a los clientes de la firma legal. En la mayor parte del trabajo de software las trazas completas están disponibles, así que el insight central puede no aplicar de forma general.

## Evidence
- Legora no puede leer trazas porque los datos pertenecen a los clientes de la firma — source: b8aebacaf4660f6c

## Why it matters
Antes de importar la práctica de evals sin trazas a un equipo de producto genérico, hay que preguntar si el constraint existe. Si las trazas son accesibles, sustituirlas por proxies es coste sin motivo.

Contradice la generalización del constraint sin trazas. Se relaciona con Legora como actor, que define las condiciones del dominio.

## Links
- contradicts → [[constraint-de-evaluacion-sin-trazas-legora]]
- relates_to → [[legora-cto-jacob-lauritzen-legal-ai]]
