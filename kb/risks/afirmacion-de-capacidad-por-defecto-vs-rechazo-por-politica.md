---
id: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
title: '«Puede» frente a «no rechaza»: capacidad de modelo confundida con política
  por defecto'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- politica-vs-capacidad
- guardrails
- multimodal
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: supports
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
---

## What it is
La diferencia observada (Gemini identifica figuras públicas, ChatGPT y Claude no) puede reflejar políticas de producto o guardrails activados por defecto, no una diferencia de capacidad técnica. Leer «Gemini puede y los demás no» como ranking de capacidad sería un error de categoría: sería una restricción configurable/contractual, no una limitación del modelo.

## Evidence
- El reporte lo enumera explícitamente como implicación: «la diferencia observada podría reflejar políticas de producto (guardrails distintos) más que diferencias de capacidad técnica» — source: sig-237cc97a9794
- El riesgo correspondiente: la distinción «puede/no puede» puede deberse a filtros de políticas por defecto — source: sig-237cc97a9794
- El documento fuente solo enuncia la asimetría sin experimento que separe capacidad de política — source: 19cb8032958cd964

## Why it matters
Cambia por completo la estrategia de adopción: si es política, hay margen de configuración o negociación de proveedor; si es capacidad, la única salida es cambiar de motor. Trabajar sobre la hipótesis equivocada lleva a descartar proveedores por una razón que no aplica.

Se apoya en las notas ya existentes `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo` y `confundir-rechazo-por-politica-con-capacidad-de-modelo`, y las usa como marco para el caso concreto del clúster multimodal.

## Links
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
