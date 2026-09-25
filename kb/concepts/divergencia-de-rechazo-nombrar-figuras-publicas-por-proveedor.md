---
id: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
title: 'Divergencia de rechazo al nombrar figuras públicas: Gemini sí, ChatGPT y Claude
  no'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-25'
sources:
- 19cb8032958cd964
tags:
- chatgpt
- claude
- figuras-publicas
- gemini
- identificacion-facial
- multimodal
- politica-de-modelos
- politica-de-proveedor
- politicas-de-proveedor
- rechazo
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-25'
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
---

## What it is
Ante la misma petición de nombrar una figura pública en una imagen, tres proveedores principales responden de forma distinta: Gemini la nombra, ChatGPT y Claude la rechazan. La divergencia es de política de producto y de filtros de seguridad aplicados, no una diferencia demostrada de capacidad de reconocimiento entre los modelos.

## Evidence
- El documento afirma que ChatGPT y Claude no identifican figuras públicas en imágenes, pero Gemini sí [19cb8032958cd964].
- No se declara metodología, fecha, versión de modelo, cuenta ni región para ninguna de las tres observaciones [19cb8032958cd964].
- La corroboración del pipeline es de 0.50, es decir, parcial [19cb8032958cd964].

## Why it matters
Convierte «¿puede el modelo hacer X?» en «¿qué proveedor, en qué versión y bajo qué cuenta deja hacer X?». Para cualquier flujo que dependa del comportamiento de rechazo, la decisión de compra es una decisión de política, y la sonda de compatibilidad debe hacerse por proveedor antes de comprometer una feature.

Es la instancia multimodal de `divergencia-de-rechazo-entre-proveedores`, y su lectura correcta pasa por `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`. Sustenta operativamente `spike-por-proveedor-para-comportamiento-de-rechazo`: si tres proveedores divergen en una frase, el spike es obligatorio. Se apoya en la observación registrada en `gemini-no-rechaza-nombrar-figuras-publicas`. La nota `identificacion-de-figuras-publicas-ya-existia` contiene el encuadre general del que esta es el caso concreto. Contradice a `afirmacion-poblacional-desde-un-solo-proveedor` en el sentido de que el reporte fuente sí generaliza desde un solo proveedor; el enlace registra esa tensión sin resolverla.

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
