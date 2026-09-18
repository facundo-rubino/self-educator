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
updated: '2026-09-18'
sources:
- 19cb8032958cd964
tags:
- identificacion-facial
- multimodal
- politica-de-proveedor
- politicas-de-proveedor
- rechazo
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-18'
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
---

## What it is
Un único ítem RSS afirma que ChatGPT y Claude se niegan a identificar figuras públicas en imágenes mientras que Gemini sí lo hace. El documento solo contiene la aserción: no aporta metodología, benchmark, cita de documentación ni fecha. Engagement=0.

## Evidence
- El documento afirma que los LLM ya pueden identificar figuras públicas en imágenes — source: 19cb8032958cd964
- El documento afirma la divergencia conductual: ChatGPT y Claude no identifican, Gemini sí — source: 19cb8032958cd964
- El clúster contiene un solo ítem RSS con engagement=0, sin corroboración independiente dentro de la señal — source: 19cb8032958cd964

## Why it matters
Si la divergencia fuese real, implicaría diferencias de política a nivel de proveedor en visión, no necesariamente de capacidad subyacente — relevante para quien construye agentes multimodales que procesan caras o figuras públicas. Sin metodología verificable, cualquier acción práctica (adoptar Gemini para identificación de caras) sería prematura: el veredicto honesto es «no verificado, no actuar».

Es una instancia concreta del patrón general de divergencia de rechazo entre proveedores, y refuerza la distinción entre capacidad técnica y política de rechazo: el titular «los LLM ya pueden identificar» puede estar conflacionando gating de política con capacidad del modelo. Corrobora el ítem existente sobre Gemini.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
