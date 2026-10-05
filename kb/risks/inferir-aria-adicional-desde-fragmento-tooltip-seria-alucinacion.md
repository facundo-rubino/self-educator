---
id: inferir-aria-adicional-desde-fragmento-tooltip-seria-alucinacion
title: Inferir la mecánica ARIA del caso de tooltip desde un fragmento sería alucinación
type: risk
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
- sobreinterpretacion
- accesibilidad
- evidencia-insuficiente
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: tooltip-accessibility-aria-describedby-insuficiente-sin-detalle
  type: derived_from
- to: inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion
  type: relates_to
- to: aria-describedby-tooltip-sin-detalle-de-mecanismo
  type: supports
---

## What it is
Solo se dispone de una frase del documento [ded7560510c137bc]. Cualquier detalle sobre la implementación correcta de tooltips (combinación de `role="tooltip"`, `aria-labelledby`, gestión de visibilidad, relación nombre/descripción accesible) sería una reconstrucción desde conocimiento general, no evidencia del clúster.

## Evidence
- El único contenido recuperado es la frase «aria-describedby isn't always enough» — source: ded7560510c137bc
- No hay cuerpo, ejemplos de código ni explicación del caso — source: ded7560510c137bc

## Why it matters
Inferir que la entrada discute ARIA más ampliamente, o que establece una regla general de accesibilidad, excede lo que el texto recuperado sostiene. Escribir esa reconstrucción en el KB propagaría un claim sin fuente.

Depende de la nota que registra el fragmento original. Coincide con el riesgo ya inventariado en `inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion` y respalda el hueco registrado en `aria-describedby-tooltip-sin-detalle-de-mecanismo`.

## Links
- derived_from → [[tooltip-accessibility-aria-describedby-insuficiente-sin-detalle]]
- relates_to → [[inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion]]
- supports → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
