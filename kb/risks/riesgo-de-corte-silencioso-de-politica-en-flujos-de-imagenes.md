---
id: riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes
title: 'Riesgo: la política de imágenes puede cambiar sin aviso y romper un flujo
  de agente que hoy funciona'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-28'
sources:
- 19cb8032958cd964
tags:
- agentes
- drift-temporal
- fiabilidad
- fragilidad
- multimodal
- politica
- politica-de-modelos
- politica-de-proveedor
- riesgo-de-integracion
- versionado
- vision
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
- to: impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: relates_to
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: derived_from
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: supports
---

## What it is
Una afirmación del tipo «Gemini will» sobre identificación de personas en imágenes caduca sin aviso: la conducta de rechazo varía por región, nivel de cuenta y UI, y cambia con actualizaciones de modelo o de política. Un flujo construido sobre esa conducta se rompe en silencio, sin cambio de versión que lo señale.

## Evidence
- La afirmación descansa en un único ítem RSS sin verificación independiente, por lo que puede estar desactualizada, ser marketing o ser directamente falsa — source: 19cb8032958cd964
- La conducta de rechazo en LLMs de consumo cambia con frecuencia y varía por región, cuenta y UI, de modo que una afirmación estática puede expirar en silencio — source: 19cb8032958cd964

## Why it matters
El coste no es la pérdida de la función, es la pérdida silenciosa: un pipeline de materiales o de herramientas que dependa de identificar personas en imágenes fallará en producción sin que ningún número de versión lo anticipe. La mitigación es tratar el rechazo como criterio dependiente de proveedor y mantener un spike que se revalide.

Se deriva de `confundir-rechazo-por-politica-con-capacidad-de-modelo`, porque solo se puede vigilar el drift si se sabe que se está observando política y no capacidad. Apoya a `criterios-de-aceptacion-dependientes-de-proveedor` y a `spike-por-proveedor-para-comportamiento-de-rechazo`, que son las respuestas prácticas a este riesgo.

## Links
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
