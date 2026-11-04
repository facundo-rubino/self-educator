---
id: coste-de-mantener-memoria-persistente-y-harness-propio-en-equipos-chicos
title: Coste de mantener memoria persistente y harness propio en equipos chicos
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-04'
updated: '2026-11-04'
sources:
- 5e81338675ea4d09
tags:
- coste
- mantenimiento
- equipos-chicos
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-11-04'
provenance:
  scale: S
  query: null
links:
- to: harness-propio-frente-a-framework-generico-caso-arca
  type: contradicts
- to: generacion-barata-no-elimina-coste-de-mantenimiento
  type: supports
- to: agentes-abaratan-el-ensamblaje-no-la-integracion-con-el-flujo
  type: relates_to
---

## What it is
Construir y mantener un harness propio y memoria persistente exige inversión inicial y mantenimiento continuo. En equipos chicos o en docencia entry-level —donde la rotación de alumnos y la simplicidad pesan— ese coste puede superar el beneficio.

## Evidence
- Se defiende el beneficio de construir un harness propio en lugar de depender solo de tooling genérico — fuente: 5e81338675ea4d09
- Se describen flujos agénticos que abarcan varios días, no solo tareas puntuales — fuente: 5e81338675ea4d09

## Why it matters
El harness propio no elimina el coste de mantenimiento; lo traslada al equipo. Es la misma asimetría generación-barata/mantenimiento-caro aplicada al tooling de agentes.

Contradice la preferencia de harness propio del caso Arca al señalar su coste. Se apoya en la nota existente de que la generación barata no elimina el mantenimiento.

## Links
- contradicts → [[harness-propio-frente-a-framework-generico-caso-arca]]
- supports → [[generacion-barata-no-elimina-coste-de-mantenimiento]]
- relates_to → [[agentes-abaratan-el-ensamblaje-no-la-integracion-con-el-flujo]]
