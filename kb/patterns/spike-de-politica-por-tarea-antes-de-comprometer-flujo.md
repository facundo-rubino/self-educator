---
id: spike-de-politica-por-tarea-antes-de-comprometer-flujo
title: Probar la política por tarea antes de comprometer un flujo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- sig-237cc97a9794
tags:
- spike
- politica-de-proveedor
- agentes
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: derived_from
---

## What it is
Cuando una feature depende de que un modelo acepte una tarea (nombrar personas en imágenes, por ejemplo), el comportamiento de rechazo es variable por proveedor y por configuración. Corresponde un spike de política por tarea y por proveedor antes de comprometer el diseño, no asumir paridad ni extrapolar de una observación anecdótica.

## Evidence
- Si la asimetría entre proveedores es real y estable, el dev tendría que elegir proveedor según la tarea y no asumir paridad de capacidades — source: sig-237cc97a9794
- La observación de referencia proviene de una sola sesión sin versiones ni fecha: no es base suficiente para fijar el proveedor — source: 19cb8032958cd964

## Why it matters
Convierte un claim no verificable en una acción de bajo costo: medir el comportamiento de rechazo del proveedor en la tarea concreta, antes de que la política se convierta en dependencia arquitectónica.

Instancia concreta de `spike-por-proveedor-para-comportamiento-de-rechazo` y de `aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales` en el dominio de imágenes con personas. Depende de `afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica` para saber qué se está midiendo.

## Links
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
