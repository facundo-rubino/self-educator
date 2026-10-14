---
id: politica-de-face-recognition-como-variable-de-producto
title: La política de reconocimiento facial como variable de producto, no de modelo
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-14'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- cumplimiento
- face-recognition
- gobernanza
- multimodal
- politica-de-producto
- proveedores
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: relates_to
- to: asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas
  type: derived_from
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: supports
---

## What it is
La decisión de identificar o rechazar la identificación de una persona en una imagen es una variable de política de producto de cada proveedor, no una propiedad derivable del modelo. Dos sistemas con capacidad visual comparable pueden diferir solo en esa política.

## Evidence
- Gemini identificará figuras públicas; ChatGPT y Claude no — diferencia de política entre productos, según el ítem RSS [19cb8032958cd964] — fuente: sig-237cc97a9794
- El comportamiento puede diferir por UI, región, versión de política o por el juicio del modelo sobre qué es una «figura pública» — fuente: sig-237cc97a9794

## Why it matters
Para un equipo que construye features multimodales, la política es una dependencia externa que puede cambiar sin aviso. Los criterios de aceptación deben fijarse por proveedor, no por supuesta capacidad genérica de «LLMs».

Deriva de la asimetría de rechazo entre proveedores; se relaciona con los criterios de aceptación dependientes de proveedor en features multimodales.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
