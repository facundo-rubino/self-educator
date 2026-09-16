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
- llm
- politica-de-proveedor
- comportamiento-de-modelos
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
---

## What it is
Ante un mismo prompt, distintos proveedores de LLM pueden responder de forma distinta por política, no por capacidad. El caso reportado: ChatGPT y Claude se niegan a identificar figuras públicas en imágenes, mientras que Gemini sí las identifica — source: 19cb8032958cd964.

## Evidence
- ChatGPT y Claude no identifican figuras públicas en imágenes; Gemini sí — source: 19cb8032958cd964
- La fuente es un único ítem RSS de bajo engagement, sin metodología, set de prueba ni fecha descritos — source: 19cb8032958cd964

## Why it matters
Para quien elige entre proveedores, el rechazo es una variable de diseño: la misma función puede funcionar con un proveedor y fallar con otro, y cambiar de modelo puede alterar el comportamiento de forma silenciosa. La evidencia es demasiado débil para tratarlo como hecho establecido.

Se relaciona con sobre-generalizacion-desde-claude-code: ambos son observaciones sobre el comportamiento de un proveedor que se leen como propiedades generales de los LLM.

## Links
- relates_to → [[sobre-generalizacion-desde-claude-code]]
