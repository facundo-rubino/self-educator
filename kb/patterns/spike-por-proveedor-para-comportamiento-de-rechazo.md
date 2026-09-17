---
id: spike-por-proveedor-para-comportamiento-de-rechazo
title: Spike por proveedor antes de comprometer features que dependen del rechazo
  del modelo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 19cb8032958cd964
tags:
- estimacion
- spike
- verificacion
- proveedores
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: derived_from
- to: impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
---

## What it is
Antes de comprometer una feature cuyo valor depende de si el modelo acepta o rechaza una acción, se ejecuta un spike acotado contra cada proveedor candidato, con la interfaz real (API o app), y se registra el resultado con versión y fecha. El spike es el artefacto que convierte una aserción en un dato.

## Evidence
- La afirmación original sobre figuras públicas no cita test, fecha, versión de modelo ni método; es exactamente el artefacto que un spike habría producido — source: 19cb8032958cd964

## Why it matters
Convierte un riesgo de descubrimiento tardío en una tarea acotada y presupuestable en la estimación. También produce el fallback plan exigido cuando el proveedor principal cambia de política o de comportamiento.

Deriva del patrón de criterios dependientes de proveedor; sin esta tarea, esos criterios no se pueden escribir. Se relaciona con el impacto de un corte de proveedor en flujos de coding con IA: ambos tratan la dependencia de proveedor como variable de diseño, no como constante de entorno.

## Links
- derived_from → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
