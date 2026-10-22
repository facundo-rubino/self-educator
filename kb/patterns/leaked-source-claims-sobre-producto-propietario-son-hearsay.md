---
id: leaked-source-claims-sobre-producto-propietario-son-hearsay
title: Los claims de «fuente filtrada» sobre productos propietarios son hearsay no
  verificable
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- abf61eeec75462f9
tags:
- leak
- verificacion
- evidencia-debil
- propietario
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-source-leak-sin-artefacto-primario
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: relates_to
---

## What it is
Un claim de producto propietario basado en un leak no inspeccionado es hearsay de segunda mano. Los leaks sobre productos cerrados suelen ser parciales, obsoletos o distorsionados, y la plausibilidad de la arquitectura no constituye evidencia.

## Evidence
- El crítico califica la cadena como «hearsay-of-hearsay»: fuente secundaria citando un leak no revisado — source: abf61eeec75462f9
- Afirma que los claims de leak sobre productos cerrados son «especially prone to being partial, stale, or fabricated» — source: abf61eeec75462f9

## Why it matters
Antes de citar cualquier «el código filtrado muestra X» sobre un producto propietario, hay que exigir el artefacto primario. Sin él, lo único compilable es la dirección cualitativa, no el hecho.

Generaliza el caso de Claude Code a una regla de admisión de evidencia; se apoya en las notas previas sobre leaks sin artefacto primario y autenticidad no establecida.

## Links
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- supports → [[leak-sin-autenticidad-establecida]]
- relates_to → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
