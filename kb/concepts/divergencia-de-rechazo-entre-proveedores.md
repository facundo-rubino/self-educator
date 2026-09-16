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
updated: '2026-09-16'
sources:
- 19cb8032958cd964
tags:
- comportamiento-de-modelos
- llm
- modelos
- multimodal
- politica-de-proveedor
- refusal
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: supports
---

## What it is
Distintos asistentes frontera pueden diferir en si se niegan a ejecutar la misma tarea, no solo en cuán bien la ejecutan. El caso reportado: ante la tarea de nombrar figuras públicas en imágenes, ChatGPT y Claude se niegan mientras Gemini no [19cb8032958cd964]. Es una diferencia de política de proveedor, no una diferencia de capacidad demostrada.

## Evidence
- Ante identificación de figuras públicas en imágenes, ChatGPT y Claude rechazan y Gemini no — source: 19cb8032958cd964
- No hay metodología, imágenes de ejemplo, fecha de test ni benchmark — source: 19cb8032958cd964

## Why it matters
El rechazo es parte observable de la interfaz de un proveedor: dos modelos pueden compartir capacidad y diferir en si la exponen. Para quien construye features multimodales, esto convierte la elección de proveedor en una decisión de producto (qué va a rechazar el modelo) y no solo de capacidad técnica [19cb8032958cd964].

Refuerza [[afirmacion-poblacional-desde-un-solo-proveedor]]: aquí la asimetría se reporta desde un único ítem RSS sin corroboración independiente. Se relaciona con la práctica de testear prompt y guardrails por proveedor, no asumir portabilidad.

## Links
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[afirmacion-poblacional-desde-un-solo-proveedor]]
