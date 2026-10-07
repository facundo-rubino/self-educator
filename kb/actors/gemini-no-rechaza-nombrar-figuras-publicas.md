---
id: gemini-no-rechaza-nombrar-figuras-publicas
title: Gemini no rechaza nombrar figuras públicas en imágenes, según un ítem RSS
type: actor
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-10-07'
sources:
- 19cb8032958cd964
tags:
- gemini
- guardrails
- imagenes
- multimodal
- politica-de-proveedor
- rechazo
- refusal-policy
- vision
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: supports
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: contradicts
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: prueba-con-proveedores-y-cuentas-especificas
  type: relates_to
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
---

## What it is
Un único ítem RSS reporta que Gemini no se niega a nombrar figuras públicas presentes en una imagen, en contraste con ChatGPT y Claude. Es un dato de política observada de un proveedor, sin metodología, versión ni fecha publicadas en la evidencia disponible.

## Evidence
- Gemini identifica figuras públicas en imágenes donde ChatGPT y Claude rechazan hacerlo — source: 19cb8032958cd964

## Why it matters
El dato es directamente relevante para elegir proveedor en cualquier demo docente o herramienta que procese imágenes: si el flujo asume uniformidad entre asistentes, el comportamiento de Gemini lo rompe. Al mismo tiempo, una observación de un solo proveedor en un solo documento no sostiene ninguna afirmación poblacional sobre «los LLM».

Es el actor concreto del caso descrito en `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor` y evidencia del patrón general de divergencia entre proveedores. Queda condicionada por `afirmacion-poblacional-desde-un-solo-proveedor` y por `afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion`: la fuente no es una medición, es una anécdota de feed.

## Links
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- supports → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- contradicts → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[prueba-con-proveedores-y-cuentas-especificas]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
