---
id: divergencia-de-rechazo-entre-proveedores
title: 'Divergencia de rechazo entre proveedores: mismo prompt, distinta respuesta'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
tags:
- comportamiento-de-modelos
- llm
- modelos
- multimodal
- politica-de-producto
- politica-de-proveedor
- politica-de-rechazo
- proveedores
- rechazo
- refusal
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-10-22'
provenance:
  scale: M
  query: null
links:
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: supports
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
---

## What it is
Ante la misma tarea de identificar figuras públicas en imágenes, ChatGPT y Claude rechazan y Gemini no, según un único ítem RSS. La divergencia se enuncia como conducta observada de producto, sin metodología, versión, cuenta ni región.

## Evidence
- «ChatGPT and Claude won't, but Gemini will» — source: 19cb8032958cd964

## Why it matters
Si la conducta difiere por proveedor, un agente que procesa imágenes de usuarios no puede asumir uniformidad: la identificación de personas debe ser un toggle por proveedor, con feature-flag o capa de abstracción para que un swap no cambie silenciosamente lo que el producto hace con imágenes ajenas.

Se relaciona con la separación capacidad/política y respalda el patrón de spike por proveedor antes de comprometer features que dependen del rechazo del modelo.

## Links
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
