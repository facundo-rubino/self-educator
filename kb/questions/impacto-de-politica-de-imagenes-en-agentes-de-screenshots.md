---
id: impacto-de-politica-de-imagenes-en-agentes-de-screenshots
title: La política de imágenes condiciona agentes que procesan screenshots
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 19cb8032958cd964
tags:
- agentes
- multimodal
- screenshots
- politica-de-rechazo
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: politica-de-face-recognition-como-variable-de-producto
  type: derived_from
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: relates_to
- to: impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia
  type: relates_to
---

## What it is
Si un agente de codificación procesa screenshots de UI o capturas de app, cualquiera con caras (avatares, fotos de perfil en una demo) puede disparar rechazos dependientes del proveedor. El documento no lo mide; la pregunta queda abierta.

## Evidence
- La conducta de rechazo ante personas en imágenes diverge entre ChatGPT/Claude y Gemini — source: 19cb8032958cd964

## Why it matters
Determina si el equipo necesita una política explícita de «qué se envía en una imagen» o un modelo con rechazo más laxo para los flujos con capturas. Sin medición, es un riesgo a testear antes de comprometer un flujo.

Deriva de `politica-de-face-recognition-como-variable-de-producto` y se hermana con `impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia`: ambos son riesgos de dependencia de proveedor no medidos en el clúster.

## Links
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
