---
id: identificar-no-es-reconocer-en-la-fuente
title: «Identificar» en la fuente significa «no rechazar», no «reconocer»
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-28'
sources:
- 19cb8032958cd964
tags:
- ambiguedad-lexica
- claims
- definiciones
- llm
- metodologia
- multimodal
- rechazo
- semantica
- vision
base_confidence: 0.12
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: M
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: contradicts
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: identificacion-de-figuras-publicas-ya-existia
  type: derived_from
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: identificacion-de-figuras-publicas-ya-existia
  type: supports
- to: nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria
  type: relates_to
---

## What it is
En el documento, que un modelo «identifique» una figura pública significa que no emitió un rechazo ante la petición, no que haya verificado o reconocido correctamente a la persona. La conducta observable es la ausencia de bloqueo; la identidad correcta es una inferencia que la fuente no comprueba.

## Evidence
- La descripción disponible es de comportamiento de rechazo (ChatGPT y Claude no identifican; Gemini sí), sin verificación de que la identidad atribuida sea correcta — source: 19cb8032958cd964

## Why it matters
Leer «no rechazó» como «acertó» infla la afirmación y la vuelve inútil para decidir si un flujo de identificación es fiable. Para evaluar esa fiabilidad haría falta exactitud medida, no ausencia de bloqueo.

Se relaciona con `confundir-rechazo-por-politica-con-capacidad-de-modelo`, porque la ambigüedad del verbo es parte de la misma confusión. Apoya a `identificacion-de-figuras-publicas-ya-existia`, ya que solo se puede discutir la novedad de la capacidad si se distingue de la tolerancia del filtro. Se relaciona con `nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria`, que niega el valor de práctica de esta observación.

## Links
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[relevancia-no-es-verdad]]
- contradicts → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- derived_from → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- supports → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria]]
