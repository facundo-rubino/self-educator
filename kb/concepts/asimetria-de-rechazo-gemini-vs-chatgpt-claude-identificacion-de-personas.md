---
id: asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas
title: Asimetría entre Gemini (identifica) y ChatGPT/Claude (no) al nombrar figuras
  públicas en imágenes
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-14'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- chatgpt
- claude
- gemini
- multimodal
- politica-de-modelo
- politica-de-rechazo
- reconocimiento-de-personas
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: supports
- to: divergencia-de-rechazo-al-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: relates_to
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: derived_from
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
---

## What it is
Según un único ítem RSS, Gemini identificará figuras públicas en imágenes mientras ChatGPT y Claude no lo harán. La asimetría es una divergencia de política de producto entre proveedores, no evidencia de una diferencia de capacidad técnica subyacente.

## Evidence
- Gemini identificará figuras públicas en imágenes mientras ChatGPT y Claude no, según el ítem RSS [19cb8032958cd964] — fuente: sig-237cc97a9794
- El claim se apoya en un solo documento, sin verificación independiente — fuente: sig-237cc97a9794

## Why it matters
Si se confirma, la elección de proveedor para features multimodales depende de la política de identificación de personas, variable por producto, región y versión. No de la «capacidad» del modelo.

Se relaciona con la nota de Gemini que no rechaza nombrar figuras públicas y con la de divergencia de rechazo entre proveedores; deriva de la distinción entre capacidad técnica y política de rechazo.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[divergencia-de-rechazo-al-nombrar-figuras-publicas-por-proveedor]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- derived_from → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[divergencia-de-rechazo-entre-proveedores]]
