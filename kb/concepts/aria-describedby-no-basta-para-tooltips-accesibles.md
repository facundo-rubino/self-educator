---
id: aria-describedby-no-basta-para-tooltips-accesibles
title: Un tooltip no queda accesible solo con aria-describedby
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-17'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- frontend
- tooltip
- tooltips
base_confidence: 0.05
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: M
  query: null
links:
- to: relevancia-no-es-verdad
  type: relates_to
- to: aria-describedby-tooltip-sin-detalle-de-mecanismo
  type: relates_to
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
---

## What it is
El patrón común de asociar un tooltip a su disparador mediante `aria-describedby` no basta por sí solo para que el tooltip sea accesible. El documento de origen lo enuncia como un error propio que el autor está corrigiendo, es decir, una implementación que se creía correcta y no lo era.

## Evidence
- «aria-describedby isn't always enough»: el título y la única frase de cuerpo afirman que `aria-describedby` no siempre es suficiente para tooltips — source: ded7560510c137bc
- El ítem se autopresenta como corrección de un mistake de accesibilidad propio del autor — source: ded7560510c137bc

## Why it matters
Rompe la equivalencia implícita entre «cablear el atributo ARIA» y «accesibilidad verificada». Un tech lead que revisa front-end no puede aceptar un tooltip como accesible solo porque declara `aria-describedby`; la accesibilidad necesita su propio paso de revisión y prueba.

Se relaciona con `aria-describedby-tooltip-sin-detalle-de-mecanismo`: esa nota cubre exactamente lo que este documento *no* dice (qué casos, qué combinaciones AT/navegador, qué fix). También se relaciona con `afirmacion-de-capacidad-desde-fragmento-de-una-linea`, porque el enunciado «no basta» proviene de una sola frase sin método reportado.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
