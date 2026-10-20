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
updated: '2026-10-20'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- capacidad
- capacidad-vs-politica
- error-de-categoria
- evaluacion
- marco-conceptual
- multimodal
- politica
- politica-de-rechazo
- politica-vs-capacidad
- politicas-de-modelo
- rechazo
- refusal
base_confidence: 0.65
half_life_days: 180
last_reinforced: '2026-10-20'
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
Que un modelo se niegue a nombrar a una persona no implica que no pueda reconocerla. El caso reportado contrapone ChatGPT/Claude (rechazan) con Gemini (nombra), y esa diferencia es más plausiblemente un umbral de política distinto entre proveedores que una brecha de capacidad de visión. Tratar el rechazo como evidencia de capacidad es un error de categoría.

## Evidence
- ChatGPT y Claude declinan identificar figuras públicas, Gemini no — source: 19cb8032958cd964
- El informe no mide precisión de reconocimiento, tasas de error ni cobertura, solo qué proveedor emite un nombre — source: 19cb8032958cd964

## Why it matters
Si un practitioner construye tooling agéntico, los guardrails del proveedor son superficie de runtime: prompts idénticos producen rechazo duro en un proveedor y respuesta en otro. Cualquier diseño de agente debe tratar la conducta de rechazo como variable a probar y abstraer.

Es una instancia concreta de `confundir-rechazo-por-politica-con-capacidad-de-modelo` («won't» no es «can now»). Apoya a `divergencia-de-rechazo-entre-proveedores` como evidencia del patrón y deriva del claim crudo en `llms-identifican-figuras-publicas-sin-metodologia`.

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
