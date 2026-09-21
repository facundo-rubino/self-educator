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
updated: '2026-09-21'
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
last_reinforced: '2026-09-21'
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
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: relates_to
---

## What it is
Un tooltip no queda accesible solo por asignarle `aria-describedby`. El único contenido ingerido que sostiene esto es la frase del propio post: «aria-describedby isn't always enough» — source: ded7560510c137bc. No hay en el corpus mecanismo, caso reproducible ni alcance declarado.

## Evidence
- El documento «Fixing my tooltip accessibility mistake» afirma que «aria-describedby isn't always enough» — source: ded7560510c137bc
- El clúster consta de un único documento RSS con engagement=0 — source: ded7560510c137bc

## Why it matters
Si la afirmación se sostiene, cualquier checklist que dé por resuelta la accesibilidad de un tooltip tras añadir `aria-describedby` está incompleta. Pero con una sola frase sin desarrollo no se puede decidir qué falta (foco, teclado, anuncio del rol, relación con el disparador): la nota marca la duda, no la resuelve.

Se relaciona con [[tooltip-accesible-no-basta-con-aria-describedby]], que registra la misma afirmación desde otro ángulo, y con [[aria-describedby-tooltip-sin-detalle-de-mecanismo]], que ya señalaba la ausencia de mecanismo y alcance en esta misma evidencia.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
