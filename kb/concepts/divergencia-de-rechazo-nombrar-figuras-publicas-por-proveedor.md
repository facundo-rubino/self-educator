---
id: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
title: 'Divergencia de rechazo al nombrar figuras públicas en imágenes: Gemini sí,
  ChatGPT y Claude no'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-14'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- chatgpt
- claude
- figuras-publicas
- gemini
- guardrails
- identificacion-facial
- imagenes
- multimodal
- politica-de-modelo
- politica-de-modelos
- politica-de-proveedor
- politicas-de-proveedor
- proveedores
- rechazo
- refusal
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: supports
- to: identificacion-de-figuras-publicas-ya-existia
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: politica-de-face-recognition-como-variable-de-producto
  type: derived_from
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: contradicts
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: contradicts
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
- to: privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: relates_to
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
- to: asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas
  type: relates_to
---

## What it is
El mismo tipo de tarea —nombrar una figura pública en una imagen— recibe respuestas divergentes según el proveedor: Gemini lo hace, ChatGPT y Claude no. Es conducta observable de producto, no una propiedad general de «los LLMs».

## Evidence
- Gemini sí, ChatGPT y Claude no, según el único ítem RSS [19cb8032958cd964] — fuente: sig-237cc97a9794
- Sin repetición, versiones ni condiciones de prueba en el documento — fuente: sig-237cc97a9794

## Why it matters
Obliga a tratar el rechazo como comportamiento por producto, con resultados verificados por proveedor y por tarea, no como una capacidad del modelo genérico.

Se relaciona con la asimetría de rechazo; sostiene la nota general de divergencia de rechazo entre proveedores. Contradice la lectura poblacional: una observación de un proveedor no autoriza un claim sobre «los LLMs».

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- contradicts → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- contradicts → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas]]
- relates_to → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- relates_to → [[asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas]]
