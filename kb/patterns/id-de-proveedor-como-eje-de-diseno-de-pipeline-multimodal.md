---
id: id-de-proveedor-como-eje-de-diseno-de-pipeline-multimodal
title: El proveedor como eje de diseño del pipeline multimodal, no como detalle de
  swapping
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-15'
updated: '2026-10-15'
sources:
- sig-237cc97a9794
tags:
- multimodal
- pipelines-de-agentes
- politica-de-proveedor
base_confidence: 0.4
half_life_days: 365
last_reinforced: '2026-10-15'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
---

## What it is
Si un comportamiento relevante de procesamiento de imágenes de personas está presente en un proveedor y ausente en otros, el mismo pipeline se comporta distinto según qué proveedor esté cableado. El proveedor deja de ser un detalle de swapping y pasa a ser un parámetro de diseño del flujo.

## Evidence
- El clúster reporta que la identificación de figuras públicas en imágenes difiere entre Gemini, ChatGPT y Claude — source: sig-237cc97a9794
- No hay corroboración adicional: corroboración 0.50 y novelty 0.00 sobre un único documento — source: sig-237cc97a9794

## Why it matters
Para quien triagea capturas, slides o fotos de stakeholders con un agente, la elección de asistente es una decisión relevante para compliance. No se debe arquitectar una feature asumiendo portabilidad entre proveedores: trátese como comportamiento detrás de un flag.

Derivado de `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`. Relacionado con `spike-por-proveedor-para-comportamiento-de-rechazo`: mismo movimiento de adaptar el diseño a la divergencia entre proveedores.

## Links
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
