---
id: divergencia-de-rechazo-entre-proveedores
title: 'Divergencia de rechazo entre proveedores: mismo prompt, distinta respuesta'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-10-20'
sources:
- 19cb8032958cd964
tags:
- comportamiento-de-modelos
- llm
- modelos
- multimodal
- politica-de-producto
- politica-de-proveedor
- proveedores
- rechazo
- refusal
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-10-20'
provenance:
  scale: M
  query: null
links:
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: supports
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
---

## What it is
Un mismo prompt sobre identificación de figuras públicas en imágenes produce respuestas opuestas según el proveedor: ChatGPT y Claude se niegan, Gemini nombra. La diferencia observable es de umbral de política, no de capacidad de visión. El documento no aporta metodología ni fecha, así que el contraste queda como descripción de una divergencia de producto.

## Evidence
- ChatGPT y Claude declinan identificar figuras públicas; Gemini sí lo hace — source: 19cb8032958cd964

## Why it matters
Establece que la paridad entre proveedores no se puede asumir: la política de rechazo es una variable de producto y de runtime. Es la base empírica mínima para diseñar agentes que abstraigan el rechazo.

Complementa `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo` (por qué el rechazo no es capacidad) y sostiene la práctica de `spike-por-proveedor-para-comportamiento-de-rechazo`. Se deriva del caso concreto registrado en `gemini-no-rechaza-nombrar-figuras-publicas`.

## Links
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
