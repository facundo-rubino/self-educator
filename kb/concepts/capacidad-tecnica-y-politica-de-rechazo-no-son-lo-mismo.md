---
id: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
title: Capacidad técnica y política de rechazo no son lo mismo (caso multimodal)
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- capacidad
- capacidad-de-modelo
- capacidad-vs-politica
- error-de-categoria
- evaluacion
- marco-conceptual
- multimodal
- politica
- politica-de-producto
- politica-de-rechazo
- politica-vs-capacidad
- politicas-de-modelo
- rechazo
- refusal
base_confidence: 0.65
half_life_days: 180
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: derived_from
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
- to: politica-de-face-recognition-como-variable-de-producto
  type: supports
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: supports
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: llms-identifican-figuras-publicas-sin-metodologia
  type: derived_from
---

## What it is
Que un modelo se niegue a nombrar a una figura pública en una imagen no demuestra que no pueda hacerlo: el rechazo puede ser política de producto, no límite técnico. La distinción «el modelo puede» vs «el producto lo expone» es la que el caso multimodal hace visible.

## Evidence
- El documento atribuye la diferencia a la conducta del producto («won't… but Gemini will») y no a una diferencia de capacidad del modelo — source: 19cb8032958cd964

## Why it matters
Para quien construye sobre varios proveedores, la conducta de identificación debe tratarse como variable de producto por proveedor, no como constante del modelo. La misma inferencia es especulativa en ambos sentidos: el gating puede reflejar capacidad presente o tolerancia al riesgo, y la fuente única no distingue.

Generaliza la nota sobre confundir rechazo por política con capacidad; sostiene la nota sobre divergencia de rechazo entre proveedores y deriva del ítem de identificación de figuras públicas.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- derived_from → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- supports → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- supports → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- derived_from → [[llms-identifican-figuras-publicas-sin-metodologia]]
