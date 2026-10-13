---
id: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
title: Capacidad técnica y política de rechazo no son lo mismo
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-13'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- capacidad
- capacidad-vs-politica
- evaluacion
- multimodal
- politica
- politicas-de-modelo
- rechazo
base_confidence: 0.65
half_life_days: 180
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: derived_from
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
---

## What it is
Un modelo puede ser plenamente capaz de identificar a una figura pública y a la vez estar instruido o restringido por política para negarse. Inversamente, un modelo permisivo puede alucinar un nombre plausible. Por tanto, observar una negativa o una respuesta no establece capacidad del modelo.

## Evidence
- El documento se limita a registrar negativa/no-negativa, sin verificación contra verdad de referencia — source: 19cb8032958cd964
- «Gemini identifica figuras públicas» podría ser igual de bien «Gemini confabula un nombre para una cara» — source: sig-237cc97a9794
- El claim confunde cumplimiento de política con capacidad de modelo — source: sig-237cc97a9794

## Why it matters
Cualquier decisión de producto o de evaluación que dependa del rechazo de un modelo debe probar la política por tarea, no inferirla de la capacidad nominal. Es un error de razonamiento con consecuencias operativas: elegir un proveedor por lo que «no rechaza» es elegir por política vigente, no por músculo técnico.

Se deriva de `confundir-rechazo-por-politica-con-capacidad-de-modelo` y refuerza `afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica`. Se relaciona con `identificar-no-es-reconocer-en-la-fuente`: la palabra «identificar» en la fuente significa «no rechazar», no «reconocer».

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- derived_from → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
