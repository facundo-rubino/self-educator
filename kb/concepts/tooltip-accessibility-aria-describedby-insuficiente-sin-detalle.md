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
updated: '2026-10-08'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- artefacto-de-ingesta
- front-end
- tooltips
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-08'
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
---

## What it is
El documento [ded7560510c137bc] sostiene que `aria-describedby` no basta para que un tooltip sea accesible. La afirmación llega solo como titular y una línea de tesis: no hay cuerpo, código, referencias WCAG ni resultados de pruebas con lector de pantalla.

## Evidence
- La aserción central del documento es que `aria-describedby` no es siempre una solución suficiente para la accesibilidad de tooltips — source: ded7560510c137bc
- El documento se enmarca como retrospectiva de un error propio del autor («Fixing my tooltip accessibility mistake»), no como estudio general — source: ded7560510c137bc
- El contenido ingerido se reduce a título más una línea; sin código, WCAG, pruebas de lector de pantalla ni remediación paso a paso — source: ded7560510c137bc

## Why it matters
La afirmación no es evaluable en su forma ingerida: sin mecanismo, alcance ni reproducción, no puede verificarse ni generalizarse. Solo registra que existe un pitfall de accesibilidad de tooltips conocido por su autor.

Se relaciona con `tooltip-accesible-no-basta-con-aria-describedby` (misma afirmación, otra ingesta). Se relaciona con `criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo`: la presencia del atributo no equivale a accesibilidad verificada. Se relaciona con `tooltip-accessibility-corregir-error-propio-como-ejemplo-de-oficio` por el encuadre retrospectivo del autor.

## Links
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles-integracion]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
- relates_to → [[tooltip-accessibility-corregir-error-propio-como-ejemplo-de-oficio]]
