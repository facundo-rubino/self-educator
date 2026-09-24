---
id: benchmark-pp512-no-informa-generacion-interactiva
title: pp512 (prefill) no informa la generación token a token que define la experiencia
  interactiva
type: pattern
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
- benchmarking
- inferencia
- latencia
- agentes
base_confidence: 0.65
half_life_days: 365
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: vulkan-int8-coopmat1-matmul-rdna3-rdna4
  type: relates_to
---

## What it is
pp512 mide throughput de prefill; no mide tg (generación token a token), que es lo que determina la latencia percibida en uso interactivo y en bucles de agente. Un benchmark limitado a pp512 no permite inferir mejora en la experiencia de uso.

## Evidence
- El único valor completo de la tabla es pp512; la fila posterior queda truncada — source: 481d2653708680a1

## Why it matters
Para evaluar si un backend abarata agentes o asistentes locales, la métrica relevante es la generación, no solo el prefill. Un reporte de pp512 puede mostrar ganancia y no traducirse en mejor experiencia interactiva.

Se relaciona con `vulkan-int8-coopmat1-matmul-rdna3-rdna4` como límite interpretativo del benchmark publicado.

## Links
- relates_to → [[vulkan-int8-coopmat1-matmul-rdna3-rdna4]]
