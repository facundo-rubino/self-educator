---
id: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
title: Un criterio de accesibilidad se verifica con lector de pantalla, no con la
  presencia del atributo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- oficio
- verificacion
base_confidence: 0.15
half_life_days: 365
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: derived_from
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: relates_to
---

## What it is
Patrón sugerido por la evidencia: la corrección de un error de accesibilidad se enuncia como premisa («aria-describedby isn't always enough») y no como procedimiento, lo que obliga a que el criterio de aceptación se valide en el comportamiento observable (lector de pantalla) y no en la presencia del atributo en el markup.

## Evidence
- El documento declara su premisa como lección tras corregir un error propio de tooltip — source: ded7560510c137bc
- No se recupera la alternativa concreta ni el método de verificación — source: ded7560510c137bc

## Why it matters
Es un criterio operativo de oficio: en revisión de accesibilidad, contar un atributo ARIA como prueba de cumplimiento es el mismo tipo de error que contar líneas como prueba de corrección.

Es la lectura transferible del caso de tooltip. Se apoya en `tooltip-accesible-no-basta-con-aria-describedby` y comparte forma con `validacion-de-senal-por-contenido-no-por-titulo`: en ambos, la etiqueta superficial se confunde con el efecto real.

## Links
- derived_from → [[tooltip-accesible-no-basta-con-aria-describedby]]
- relates_to → [[validacion-de-senal-por-contenido-no-por-titulo]]
