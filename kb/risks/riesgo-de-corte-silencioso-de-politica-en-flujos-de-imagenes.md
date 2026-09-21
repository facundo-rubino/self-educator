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
updated: '2026-09-21'
sources:
- 19cb8032958cd964
tags:
- riesgo-de-integracion
- agentes
- politica-de-modelos
- versionado
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-21'
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
---

## What it is
Un flujo de agente que hoy procesa imágenes de personas puede dejar de funcionar cuando el proveedor ajuste su política de rechazo. El rechazo no depende del prompt ni del código: depende de una configuración del proveedor que puede cambiar en silencio entre versiones de modelo.

## Evidence
- «Si construyes flujos de agente que tocan imágenes de personas, la elección de modelo es una elección de política tanto como de capacidad: prompts idénticos tendrán éxito en un proveedor y serán rechazados en otro» — source: 19cb8032958cd964
- «El comportamiento de rechazo es un riesgo de integración que debe probarse por proveedor y fijarse a versiones específicas de modelo, porque puede cambiar sin aviso» — source: 19cb8032958cd964

## Why it matters
Para quien estima y secuencia trabajo con agentes, este riesgo exige: spike de rechazo por proveedor antes de comprometer la feature, criterios de aceptación dependientes del proveedor, y pinning a versión. No es un riesgo de capacidad del modelo sino de superficie de política.

Se deriva de `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`. Refuerza `spike-por-proveedor-para-comportamiento-de-rechazo` y `aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales`. Es una instancia del problema general descrito en `impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia`: dependencia de un proveedor para una capacidad que puede desaparecer sin control propio.

## Links
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
