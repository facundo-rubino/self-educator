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
updated: '2026-10-02'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- frontend
- oficio
- tooltip
- tooltips
base_confidence: 0.05
half_life_days: 180
last_reinforced: '2026-10-02'
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
- to: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
  type: supports
---

## What it is
La afirmación central del post es que `aria-describedby` no basta para que un tooltip sea accesible. Es un heurístico desnudo: no viene acompañado de mecanismo, ejemplo, ni especificación del fallo concreto (ded7560510c137bc).

## Evidence
- El clúster consta de un único documento titulado «Fixing my tooltip accessibility mistake» — source: ded7560510c137bc
- La única aserción de cuerpo es `aria-describedby isn't always enough` para la accesibilidad de tooltips — source: ded7560510c137bc
- El documento no detalla cuál fue el error, qué fix se aplicó, ni en qué circunstancias surgió — source: ded7560510c137bc

## Why it matters
Refuerza un punto estrecho de oficio: los atributos ARIA como `aria-describedby` no son una solución completa para la accesibilidad de tooltips; puede requerirse trabajo adicional (gestión de foco, comportamiento de teclado, regiones vivas o patrones nativos). No hay evidencia en el clúster sobre agentes de IA, liderazgo técnico, estimación, docencia ni técnicas de estudio (ded7560510c137bc).

Sostiene el patrón de que un criterio de accesibilidad se verifica con lector de pantalla, no con la presencia del atributo (ded7560510c137bc). Se relaciona con la nota sobre el fallo de `aria-describedby` en tooltips sin detalle de mecanismo, de la que esta es la cara concreta.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- supports → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
