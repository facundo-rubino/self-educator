---
id: tooltip-accessibility-aria-describedby-insuficiente-sin-detalle
title: '«aria-describedby isn''t always enough»: afirmación de tooltip sin cuerpo
  que la desarrolle'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-12'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- artefacto-de-ingesta
- documento-sin-cuerpo
- front-end
- frontend
- tooltip
- tooltips
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: relates_to
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: relates_to
- to: aria-describedby-no-basta-para-tooltips-accesibles-integracion
  type: relates_to
- to: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
  type: relates_to
- to: tooltip-accessibility-corregir-error-propio-como-ejemplo-de-oficio
  type: relates_to
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: supports
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: supports
- to: aria-describedby-no-basta-para-tooltips-accesibles-integracion
  type: supports
- to: tooltip-accessibility-aria-describedby-insuficiente-sin-detalle
  type: relates_to
- to: tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado
  type: derived_from
- to: inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion
  type: relates_to
---

## What it is
El único contenido verificable del documento `ded7560510c137bc` es una tesis técnica acotada: confiar en `aria-describedby` de forma aislada no garantiza la accesibilidad correcta de un tooltip. No hay cuerpo del artículo en el material proporcionado, por lo que el error concreto, el framework, la versión WAI-ARIA y la corrección aplicada no son reconstruibles.

## Evidence
- El documento afirma que «aria-describedby isn't always enough» — source: ded7560510c137bc
- El título indica que narra la corrección de un error propio de accesibilidad en tooltips («Fixing my tooltip accessibility mistake») — source: ded7560510c137bc
- El documento tiene engagement=0 — source: ded7560510c137bc

## Why it matters
La afirmación es una advertencia ARIA genérica y ampliamente conocida (gestión de foco, estados hover/focus, contenido accesible, relación trigger-tooltip) y no viene acompañada de experimento, diff ni fallo reproducible. Cualquier conclusión más específica —qué atributo alternativo, qué patrón, qué framework— sería inventada.

Refuerza (supports) las notas existentes que ya registran la misma afirmación desde otras entradas del mismo clúster: `aria-describedby-no-basta-para-tooltips-accesibles`, `tooltip-accesible-no-basta-con-aria-describedby` y `aria-describedby-no-basta-para-tooltips-accesibles-integracion`. Se deriva de `tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado`, que documenta el truncamiento del cuerpo. Se relaciona con `inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion`, que marca el límite: inferir la mecánica concreta desde el fragmento sería alucinación.

## Links
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles-integracion]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
- relates_to → [[tooltip-accessibility-corregir-error-propio-como-ejemplo-de-oficio]]
- supports → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- supports → [[tooltip-accesible-no-basta-con-aria-describedby]]
- supports → [[aria-describedby-no-basta-para-tooltips-accesibles-integracion]]
- relates_to → [[tooltip-accessibility-aria-describedby-insuficiente-sin-detalle]]
- derived_from → [[tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado]]
- relates_to → [[inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion]]
