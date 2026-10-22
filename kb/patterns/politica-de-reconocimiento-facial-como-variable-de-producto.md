---
id: politica-de-reconocimiento-facial-como-variable-de-producto
title: La política de reconocimiento facial como variable de producto, no de modelo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
tags:
- multimodal
- feature-flag
- proveedores
- privacidad
base_confidence: 0.15
half_life_days: 365
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
---

## What it is
En pipelines que ingieren imágenes de personas, la identificación de figuras públicas debe modelarse como capacidad por proveedor sujeta a política, no como propiedad estable del modelo. Implica capa de abstracción o feature-flag alrededor de las features de identidad visual.

## Evidence
- El contraste ChatGPT/Claude vs Gemini muestra que la misma tarea produce distinta conducta según proveedor — source: 19cb8032958cd964

## Why it matters
Un swap de proveedor puede cambiar sin aviso lo que el producto hace con fotos de personas, con consecuencias de privacidad, consentimiento y derechos de imagen que deben ser checkpoint de diseño y review. La evidencia es de una sola fuente titular, así que el patrón es plausible, no establecido.

Se relaciona con la nota sobre criterios de aceptación dependientes de proveedor en features multimodales; deriva de la divergencia de rechazo y respalda el spike por proveedor antes de comprometer el flujo.

## Links
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
