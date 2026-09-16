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
updated: '2026-09-16'
sources:
- 19cb8032958cd964
tags:
- gemini
- multimodal
- rechazo
- politica-de-proveedor
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: leak-sin-autenticidad-establecida
  type: relates_to
---

## What it is
El único comportamiento concreto que el ítem reporta es que Gemini accede a la tarea de identificar figuras públicas en imágenes donde ChatGPT y Claude rechazan [19cb8032958cd964]. No es una afirmación sobre capacidad de identificación de Gemini, sino sobre su postura de rechazo relativa.

## Evidence
- Gemini no se niega a nombrar figuras públicas en imágenes, según la observación reportada — source: 19cb8032958cd964
- La observación es anecdótica y sin fecha de test — source: 19cb8032958cd964

## Why it matters
Si la asimetría es real y estable, sirve como sonda pequeña de cómo difieren los proveedores en comportamiento de rechazo ligado a identidad, algo relevante al evaluar comportamiento de modelos en producción [19cb8032958cd964]. Un dato de una sola observación no basta para tratarlo como propiedad estable del actor.

Es el soporte empírico concreto de [[divergencia-de-rechazo-entre-proveedores]]. Comparte con [[leak-sin-autenticidad-establecida]] el problema de escribir sobre un reporte cuya autenticidad y método no están establecidos.

## Links
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[leak-sin-autenticidad-establecida]]
