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
updated: '2026-09-21'
sources:
- 19cb8032958cd964
tags:
- identificacion-facial
- multimodal
- politica-de-modelos
- politica-de-proveedor
- politicas-de-proveedor
- rechazo
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-21'
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
---

## What it is
Ante la misma consulta sobre una imagen con una figura pública, los proveedores no responden igual: Gemini la nombra y ChatGPT y Claude se niegan. Es una diferencia de guardrail, no de facultad: el modelo que se niega probablemente también podría nombrarla, pero su política de producto lo impide.

## Evidence
- «Los vendedores divergen al identificar figuras públicas en imágenes: ChatGPT y Claude no lo harán, pero Gemini sí» — source: 19cb8032958cd964
- «El documento enmarca el hecho como una afirmación de capacidad ("LLMs can now identify public figures in images")» — source: 19cb8032958cd964

## Why it matters
El mismo prompt produce éxito en un proveedor y rechazo en otro. Para quien delega tareas de manejo de imágenes a un agente, elegir proveedor es elegir política. La evidencia es de un solo ítem RSS sin metodología, versión, tamaño de muestra ni corroboración, así que el hallazgo se sostiene como cautela operativa, no como resultado.

Es una instancia concreta de `divergencia-de-rechazo-entre-proveedores` y evidencia para `gemini-no-rechaza-nombrar-figuras-publicas`. Refuerza la distinción de `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`, sobre `identificacion-de-figuras-publicas-ya-existia`. Se deriva de tratar la política de reconocimiento facial como variable de producto (`politica-de-face-recognition-como-variable-de-producto`).

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
