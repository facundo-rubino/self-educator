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
updated: '2026-09-23'
sources:
- 19cb8032958cd964
tags:
- figuras-publicas
- identificacion-facial
- multimodal
- politica-de-modelos
- politica-de-proveedor
- politicas-de-proveedor
- rechazo
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-23'
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
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: contradicts
---

## What it is
Un único ítem RSS [19cb8032958cd964] afirma que los LLM frontera divergen al procesar imágenes de figuras públicas: Gemini las nombraría, ChatGPT y Claude no. La evidencia es solo el titular y una frase de cuerpo; no hay prueba fechada, benchmark, captura, versión de modelo ni prompt reproducido.

## Evidence
- El documento afirma que los LLM ya pueden identificar figuras públicas en imágenes, con el contraste parentético «ChatGPT and Claude won't, but Gemini will.» — source: 19cb8032958cd964
- La única evidencia ofrecida es el titular y una frase de cuerpo; no se aporta procedimiento de prueba, imágenes de muestra, versiones de modelo ni fechas. — source: 19cb8032958cd964
- El ítem ingerido es una entrada RSS con engagement=0, sin discusión ni corroboración observada en el pipeline. — source: 19cb8032958cd964

## Why it matters
Si fuera cierto, apuntaría a divergencia de política de producto a nivel de proveedor, no a una brecha de capacidad: la misma habilidad de reconocimiento podría estar deliberadamente bloqueada por ChatGPT y Claude. Para quien construye pipelines agénticos con imágenes, el reconocimiento de personas no sería portable entre proveedores; elegir proveedor podría determinar si la función existe siquiera. La relevancia para el brief (agentes de coding, liderazgo técnico, docencia, oficio) es marginal.

Se relaciona con `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo` y con `divergencia-de-rechazo-entre-proveedores`: el caso ilustra que un «no» del modelo no prueba incapacidad. `gemini-no-rechaza-nombrar-figuras-publicas` es el actor concreto al que apunta la afirmación. Se apoya en `identificacion-de-figuras-publicas-ya-existia` para descartar que la identificación por modelos multimodales sea nueva. Contradice `afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion`, que es justo el modo de fallo que este ítem ejemplifica.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- contradicts → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
