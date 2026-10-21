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
updated: '2026-10-21'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- agentes
- cumplimiento
- face-recognition
- gobernanza
- multimodal
- politica-de-producto
- proveedores
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-10-21'
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
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes
  type: supports
---

## What it is
La respuesta de un proveedor ante una imagen con personas es una decisión de producto configurable, no una propiedad estable del modelo. Cambia por proveedor, por versión, por cuenta y por región, y puede cambiar sin aviso. Tratarla como constante de diseño rompe flujos que hoy funcionan.

## Evidence
- ChatGPT y Claude rechazan identificar figuras públicas mientras Gemini no lo hace, en el mismo tipo de tarea — source: 19cb8032958cd964

## Why it matters
Para un equipo chico que integra agentes en revisión de screenshots o material de clase: documentar qué modelo se usa con imágenes, y prever fallback, es más barato que descubrir el cambio en producción o en medio de una clase.

Se deriva de la observación de `gemini-no-rechaza-nombrar-figuras-publicas`. Es una instancia concreta de `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo` y alimenta el riesgo `riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes`.

**Caveat de evidencia:** la afirmación de esta nota descansa en un único documento RSS sin engagement (19cb8032958cd964). La generalización a «variable de producto» es plausible pero no está medida.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[riesgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes]]
