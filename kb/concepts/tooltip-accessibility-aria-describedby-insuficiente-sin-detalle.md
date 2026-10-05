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
updated: '2026-10-05'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- tooltips
- aria
- artefacto-de-ingesta
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-05'
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
---

## What it is
La entrada «Fixing my tooltip accessibility mistake» afirma que `aria-describedby` no siempre basta para resolver la accesibilidad de un tooltip. El único contenido recuperado del documento es la frase «aria-describedby isn't always enough»; no hay cuerpo, ejemplo de código ni explicación del caso concreto [ded7560510c137bc].

## Evidence
- El autor publicó una entrada señalando que cometió un error de accesibilidad al implementar tooltips y que lo está corrigiendo — source: ded7560510c137bc
- El autor sostiene explícitamente que `aria-describedby` no siempre es suficiente para resolver la accesibilidad de un tooltip — source: ded7560510c137bc
- El único contenido disponible del documento es la frase «aria-describedby isn't always enough»; no hay ejemplos de código ni explicación del caso — source: ded7560510c137bc

## Why it matters
Del documento solo se extrae una afirmación negativa («el atributo X no basta») sin la parte constructiva que la haría reutilizable. Para un dev que lidera y enseña, una corrección de error propia podría ser material de estudio de caso breve, pero sin el cuerpo del artículo no hay lección operativa transferible ni mecanismo que verificar.

Se relaciona con las notas existentes que registran la misma frase sin desarrollo (`aria-describedby-no-basta-para-tooltips-accesibles`, `tooltip-accesible-no-basta-con-aria-describedby`) y con la variante que ya señala el hueco de integración (`aria-describedby-no-basta-para-tooltips-accesibles-integracion`). Todas comparten el mismo fragmento como único contenido verificable.

## Links
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles-integracion]]
