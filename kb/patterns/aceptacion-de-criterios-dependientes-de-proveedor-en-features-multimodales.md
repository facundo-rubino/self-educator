---
id: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
title: Los criterios de aceptación en features multimodales deben ser dependientes
  del proveedor
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
- multimodal
- criterios-de-aceptacion
- estimacion
- proveedores
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
---

## What it is
Cuando una feature depende de una acción del modelo cuyo permiso varía por proveedor, el criterio de aceptación no puede ser «el modelo identifica X», sino «el proveedor P en la interfaz I en la versión V identifica X». El comportamiento observado y el contrato de producto se separan en una matriz de proveedor.

## Evidence
- El caso de figuras públicas muestra tres proveedores con respuestas distintas ante la misma clase de tarea — source: 19cb8032958cd964
- El crítico advierte que el comportamiento de rechazo cambia con versión de modelo, system prompt, región, tier de cuenta y actualizaciones de política — source: 19cb8032958cd964

## Why it matters
Introduce una tarea oculta de descubrimiento y verificación en estimación y alcance: toda feature que dependa de identificación facial exige un spike por proveedor y un plan de fallback. Asumir paridad entre APIs infla el alcance no reconocido.

Deriva de la observación de divergencia entre proveedores: si el comportamiento difiere, el criterio de aceptación debe diferir. Se relaciona con la divergencia de rechazo entre proveedores ya registrada y con la sonda de rechazo por identidad como mecanismo operativo para producir esa matriz.

## Links
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
