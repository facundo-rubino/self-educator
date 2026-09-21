---
id: js-como-lenguaje-general-ya-presente-en-el-runtime
title: Un lenguaje de propósito general ya presente en el runtime reduce el coste
  de evitar una herramienta especializada
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- 1bfe45ede61ee575
tags:
- seleccion-de-tecnologia
- dependencias
- javascript
- oficio
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: complejidad-esencial-vs-accidental-brooks
  type: relates_to
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
---

## What it is
La única idea extraíble del fragmento es débil: si el runtime ya trae un lenguaje de propósito general (JavaScript en navegador o Node), añadir un lenguaje de transformación especializado como XSLT implica una dependencia y una superficie de mantenimiento adicionales. La fuente solo enuncia esto de forma tácita con «JavaScript is right there».

## Evidence
- «JavaScript is right there» como toda la justificación de evitar XSLT — source: 1bfe45ede61ee575
- El analista infiere que la afirmación, de sostenerse, permitiría evitar añadir un toolchain XSLT y transformar con JavaScript ya presente — source: 1bfe45ede61ee575

## Why it matters
Es un criterio plausible de selección tecnológica, pero con base_confidence baja a propósito: la fuente no distingue coste de dependencia de coste de código, y XSLT es declarativo para exactamente este caso. Se registra para que quede rastreable, no como regla.

Se relaciona con `complejidad-esencial-vs-accidental-brooks` (evitar accidentalidad añadida) y con `agentes-abatatan-ports-mantener-sigue-costoso` (el coste que sobrevive no es el port inicial sino el mantenimiento).

## Links
- relates_to → [[complejidad-esencial-vs-accidental-brooks]]
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
