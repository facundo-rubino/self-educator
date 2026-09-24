---
id: delta-de-rendimiento-triangulado-por-una-sola-maquina
title: ¿Generaliza la mejora de Vulkan int8 más allá de una RX 7900 XTX concreta?
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
- 481d2653708680a1
tags:
- vulkan
- amd-rdna
- benchmarking
- generalizacion
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: vulkan-int8-coopmat1-matmul-rdna3-rdna4
  type: derived_from
- to: single-document-cluster-engagement-cero-no-generaliza
  type: relates_to
---

## What it is
El reporte es n=1: una máquina (RX 7900 XTX), una configuración de batch y una versión de llama.cpp. Queda abierto si la mejora se replica en otras GPUs RDNA3/RDNA4, otros drivers o con otras cargas.

## Evidence
- El benchmark se tomó en una sola GPU (RX 7900 XTX) con ngl=-1, n_ubatch=1024, fa=1 — source: 481d2653708680a1
- Engagement 0 y ausencia de corroboración en el cluster — source: 481d2653708680a1

## Why it matters
Sin replicación independiente, no hay base para planificar sobre esa mejora. La pregunta es la accionable: qué haría falta para confirmar el delta.

Se deriva de `vulkan-int8-coopmat1-matmul-rdna3-rdna4`. Es la misma condición de no-generalización registrada en `single-document-cluster-engagement-cero-no-generaliza`.

## Links
- derived_from → [[vulkan-int8-coopmat1-matmul-rdna3-rdna4]]
- relates_to → [[single-document-cluster-engagement-cero-no-generaliza]]
