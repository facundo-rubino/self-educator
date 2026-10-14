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
updated: '2026-10-14'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
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
last_reinforced: '2026-10-14'
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
- to: politica-de-face-recognition-como-variable-de-producto
  type: derived_from
- to: riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes
  type: relates_to
---

## What it is
Si el comportamiento de identificación de personas depende de la política del proveedor, ese comportamiento puede cambiar sin aviso y romper un flujo —un agente, una demo de docencia, un pipeline de evaluación— que hoy funciona.

## Evidence
- La conducta difiere por proveedor y puede variar por UI, región y versión de política — fuente: sig-237cc97a9794
- El anuncio original es de producto, sujeto a cambio, no una garantía contractual — fuente: sig-237cc97a9794

## Why it matters
Los flujos que dependen de una decisión de política necesitan una sonda por proveedor antes de comprometerse, no una suposición de estabilidad.

Deriva de la nota sobre la política de reconocimiento facial como variable de producto; sostiene la práctica de hacer spike por proveedor para el comportamiento de rechazo.

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
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes]]
