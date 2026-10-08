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
updated: '2026-10-08'
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
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-08'
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
---

## What it is
Un ítem RSS [19cb8032958cd964] reporta que ChatGPT y Claude no identifican figuras públicas en imágenes, mientras que Gemini sí lo permite. La observación es una frase sin prompts, versiones, cuentas ni región: no se sabe qué se probó, con qué modelo, ni en qué fecha. Es un snapshot de política de producto, no un resultado de capacidad.

## Evidence
- ChatGPT y Claude no identifican figuras públicas en imágenes; Gemini sí lo hace — source: 19cb8032958cd964
- Sin cuerpo argumental, prompts, imágenes de prueba, métricas ni condiciones de evaluación — source: 19cb8032958cd964
- Clúster de un solo documento con engagement=0 y novelty=0.00 — source: sig-237cc97a9794

## Why it matters
La observación agrupa dos cosas que conviene mantener separadas: que un modelo *pueda* nombrar a alguien en una imagen (capacidad) y que el proveedor *permita* hacerlo (política). Una asimetría de política puede cambiar de un día para otro y no se extiende a otros modelos del mismo proveedor ni a otras cuentas o regiones. Como sonda de proveedores es interesante; como hallazgo estable, no.

Es una instancia concreta de `divergencia-de-rechazo-entre-proveedores` —mismo tipo de prompt, distinta respuesta—, y refuerza `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo` y `afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica`: «Gemini sí lo hace» describe una política por defecto, no una capacidad exclusiva. Se solapa con la nota de actor `gemini-no-rechaza-nombrar-figuras-publicas`, que registra el mismo ítem desde el lado del proveedor.

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
