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
updated: '2026-10-07'
sources:
- 19cb8032958cd964
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
last_reinforced: '2026-10-07'
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
---

## What it is
Un único documento RSS reporta que, ante una imagen con figuras públicas, ChatGPT y Claude se niegan a identificarlas mientras Gemini sí lo hace. El documento presenta esta asimetría como el comportamiento distintivo del caso. Es una observación de política de producto sobre asistentes desplegados, no un resultado de investigación ni una medición de capacidad.

## Evidence
- ChatGPT y Claude no identifican figuras públicas en imágenes; Gemini sí lo hace, y el documento lo enmarca como el comportamiento que los distingue — source: 19cb8032958cd964

## Why it matters
La selección de modelo para una demo docente o para cualquier pipeline que procese imágenes suministradas por usuarios no puede apoyarse solo en la calidad de benchmark: prompts idénticos producen rechazos distintos según el proveedor. Una feature multimodal construida sobre una abstracción multi-proveedor puede regresar en silencio cuando un proveedor endurece o relaja su política de identificación. Para docencia, la divergencia sirve como ejemplo en vivo de política frente a capacidad, siempre que no se lea como prueba de lo segundo.

Se apoya en la distinción entre capacidad técnica y política de rechazo (`capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`, `confundir-rechazo-por-politica-con-capacidad-de-modelo`): el rechazo es una decisión de producto, no un límite técnico. Es un caso concreto dentro del patrón general de divergencia de rechazo entre proveedores. Refuerza la nota sobre Gemini (`gemini-no-rechaza-nombrar-figuras-publicas`) y comparte el eje de la afirmación de capacidad sin metodología (`llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia`, `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion`). Conecta con `identificar-no-es-reconocer-en-la-fuente` por la ambigüedad del verbo y con `privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas` por el riesgo que el documento no aborda.

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
