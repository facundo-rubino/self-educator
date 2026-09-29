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
updated: '2026-09-29'
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
last_reinforced: '2026-09-29'
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
---

## What it is
Observación de un documento RSS: ante una imagen con una figura pública, ChatGPT y Claude se niegan a identificarla y Gemini sí lo hace [19cb8032958cd964]. El comportamiento de rechazo es dependiente del proveedor para el mismo insumo. Es una asimetría de política de contenido, no una diferencia de capacidad demostrada.

## Evidence
- El documento distingue por proveedor: ChatGPT y Claude no lo hacen, pero Gemini sí — source: 19cb8032958cd964
- El proveedor se atribuye por nombre de producto; no se cita versión, cuenta, región ni prompt — source: 19cb8032958cd964

## Why it matters
Si un dev o educador integra modelos multimodales, la elección de proveedor incorpora una decisión de política de contenido, no solo técnica. La asimetría, si se replicara, permitiría usar la negativa/permisión como sonda barata de un proveedor frente a otro. Con una sola fuente sin metodología, es un dato a verificar, no una caracterización estable de los tres productos.

`supports` `divergencia-de-rechazo-entre-proveedores`, que ya recoge el mismo objeto en un caso distinto. Se lee con `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`: lo que diverge es la política observable. `probe-de-rechazo-por-identidad-en-produccion` propone cómo usarlo como sonda, precisamente por no estar establecido.

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
