---
id: tooltip-aria-describedby-insuficiente-anecdota-sin-mecanismo
title: '«aria-describedby isn''t always enough»: anécdota de tooltip sin mecanismo
  ni alcance'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- tooltip
- arte-de-ingesta
- fuera-del-brief
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: relates_to
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: relates_to
- to: aria-describedby-tooltip-sin-detalle-de-mecanismo
  type: derived_from
- to: tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado
  type: supports
- to: inferir-aria-adicional-desde-fragmento-tooltip-seria-alucinacion
  type: supports
---

## What it is
El documento único del clúster afirma que `aria-describedby` no basta para hacer accesible un tooltip, y no aporta mecanismo, plataforma, código ni alcance de casos afectados. La afirmación llega solo como tesis de titular más narración de un fallo propio; queda sin especificar qué condición adicional exige el remedio. — source: ded7560510c137bc

## Evidence
- El documento trata sobre la corrección de un error propio en accesibilidad de tooltips, con la idea central «aria-describedby isn't always enough» — source: ded7560510c137bc
- El formato es RSS y no registra engagement — source: ded7560510c137bc

## Why it matters
Sin el código ni la plataforma, la afirmación no se puede generalizar a otros tooltips: es una anécdota contextual, no una regla accionable. Cualquier criterio de accesibilidad derivado de aquí habría que verificarlo con lector de pantalla en el caso propio, no por la presencia/ausencia del atributo.

Se relaciona con las notas existentes que registran la misma insuficiencia (tooltip-accesible-no-basta-con-aria-describedby, aria-describedby-no-basta-para-tooltips-accesibles). Se deriva de la nota sobre la falta de detalle de mecanismo. Refuerza la nota de cuerpo truncado y la que prohíbe inferir la mecánica ARIA desde un fragmento. Reafirma lo ya sabido: la insuficiencia de `aria-describedby` se enuncia, pero no se desarrolla.

## Links
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- derived_from → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- supports → [[tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado]]
- supports → [[inferir-aria-adicional-desde-fragmento-tooltip-seria-alucinacion]]
