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
updated: '2026-09-23'
sources:
- 19cb8032958cd964
tags:
- estimacion
- multimodal
- proveedores
- rechazo
- spike
- verificacion
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-23'
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
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: supports
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
---

## What it is
Cuando una feature depende de que el modelo acepte o rechace un tipo de contenido, el comportamiento es una propiedad del proveedor y de su política vigente, no del modelo en abstracto. La decisión de diseño correcta es un spike por proveedor con casos fechados antes de comprometer la feature.

## Evidence
- Un único ítem sin fecha ni metodología afirma divergencia de rechazo entre Gemini, ChatGPT y Claude frente a imágenes de figuras públicas. — source: 19cb8032958cd964
- El documento no aporta versión de modelo, prompt reproducido, ni fechas, de modo que la conducta no es verificable ni estable como propiedad del vendor. — source: 19cb8032958cd964

## Why it matters
Fija un criterio operativo: cualquier feature multimodales que dependa de la política de rechazo debe probarse por proveedor y fecharse, y validarse en build time en vez de asumirse como propiedad estable. También implica que los criterios de aceptación de la feature deben formularse por proveedor, no una vez para todos.

Deriva de `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`, que es el caso concreto que muestra la divergencia. Refuerza `criterios-de-aceptacion-dependientes-de-proveedor` y su variante multimodal `aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales`: ambas prescriben exactamente la prueba por proveedor que aquí se formaliza.

## Links
- derived_from → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
