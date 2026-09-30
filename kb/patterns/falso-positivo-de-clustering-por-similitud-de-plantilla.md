---
id: falso-positivo-de-clustering-por-similitud-de-plantilla
title: Falso positivo de clustering por similitud de plantilla de título
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- 30a26335a9988ba2
- 16a4e3995d6c827e
tags:
- clustering
- metodologia
- pipeline
- mcp
base_confidence: 0.75
half_life_days: 365
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: mcp-cluster-2026-8-31-sin-relacion-con-el-brief
  type: supports
- to: etiqueta-cluster-desde-titulo-de-un-documento
  type: relates_to
---

## What it is
Regularidad de pipeline: cuando el clustering agrupa por similitud de plantilla de título («Release vYYYY.MM.DD / Updated packages») en lugar de por tópico, produce clusters temáticamente vacíos. En este caso agrupó ocho notas de release de paquetes MCP bajo una etiqueta que no describe ningún eje del brief.

## Evidence
- El cluster contiene únicamente notas de release con formato idéntico y sin cuerpo argumental — source: 30a26335a9988ba2
- Las versiones son datadas y consecutivas, propias de un feed de publicación automática más que de contenido editorial — source: 16a4e3995d6c827e

## Why it matters
Si el clustering agrupa por formato, filtrará falsos positivos de forma sistemática y no puntual. Corregir la función de clustering evita que el mismo falso positivo reaparezca cada mes que el feed emita releases idénticas en formato.

Respalda el patrón existente de falsos positivos por embedding (clustering-por-embedding-produce-falsos-positivos) y la observación concreta sobre este cluster (mcp-cluster-2026-8-31-sin-relacion-con-el-brief). Se relaciona con cómo la etiqueta de un cluster puede venir de un solo documento (etiqueta-cluster-desde-titulo-de-un-documento).

## Links
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- supports → [[mcp-cluster-2026-8-31-sin-relacion-con-el-brief]]
- relates_to → [[etiqueta-cluster-desde-titulo-de-un-documento]]
