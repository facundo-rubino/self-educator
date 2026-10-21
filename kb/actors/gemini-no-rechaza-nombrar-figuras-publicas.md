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
updated: '2026-10-21'
sources:
- 19cb8032958cd964
tags:
- chatgpt
- claude
- gemini
- guardrails
- imagenes
- multimodal
- politica-de-proveedor
- politica-de-rechazo
- rechazo
- refusal-policy
- rss
- vision
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-10-21'
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
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: supports
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
---

## What it is
Un único documento RSS afirma que ChatGPT y Claude se niegan a identificar figuras públicas en imágenes mientras Gemini sí lo hace. El documento llega con engagement=0 y sin cuerpo metodológico: la afirmación es un titular más una frase de caracterización. No hay benchmark, versión de modelo, región ni tasa de error declarada.

## Evidence
- ChatGPT y Claude no identifican figuras públicas en imágenes; Gemini sí — source: 19cb8032958cd964
- El ítem es un post RSS con engagement=0, sin tracción ni discusión verificable — source: 19cb8032958cd964

## Why it matters
Es un dato de comportamiento de proveedor, no de capacidad de modelo. Para un dev que integra agentes con imágenes (screenshots para revisión, material de clase) importa como recordatorio de que la política de rechazo es una variable de producto, cambiable sin aviso.

Evidencia a favor de `divergencia-de-rechazo-entre-proveedores` (mismo patrón: mismo insumo, distinta respuesta por proveedor) y de `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`. Alimenta el riesgo `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion`.

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
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
