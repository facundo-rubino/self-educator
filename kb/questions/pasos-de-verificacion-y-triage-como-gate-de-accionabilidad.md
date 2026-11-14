---
id: pasos-de-verificacion-y-triage-como-gate-de-accionabilidad
title: Verificación y triage como gate de accionabilidad en el harness de seguridad
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-14'
updated: '2026-11-14'
sources:
- b8a2ffe60796b1b8
tags:
- seguridad
- revision
- triage
- agentes
base_confidence: 0.08
half_life_days: 120
last_reinforced: '2026-11-14'
provenance:
  scale: S
  query: null
links:
- to: harness-agentico-de-seis-pasos-para-asegurar-codigo
  type: derived_from
- to: agentes-ia-aceleran-trabajo-acotado-y-verificable
  type: relates_to
---

## What it is
El harness descrito sitúa la habilidad escasa en verificación y triage, no en el descubrimiento de bugs. Es una implicación derivada del resumen del analista, no una afirmación del documento, y el clúster no trae tasas de falsos positivos ni ejemplos de hallazgos descartados.

## Evidence
- Los pasos de verificar y triage gatean si un hallazgo del LLM es accionable — source: b8a2ffe60796b1b8
- El clúster no incluye benchmarks, tasas de fallo ni datos de falsos positivos sobre descubrimiento de vulnerabilidades por LLM — source: b8a2ffe60796b1b8

## Why it matters
Sin datos de falsos positivos no puede saberse si verificación y triage son el cuello real o si el volumen de hallazgos es manejable. Queda como pregunta a resolver con fuente primaria.

Depende del harness de seis pasos como su premisa. Se conecta con el patrón de que los agentes aceleran trabajo acotado y verificable: aquí la verificación sería justamente la parte no automatizable.

## Links
- derived_from → [[harness-agentico-de-seis-pasos-para-asegurar-codigo]]
- relates_to → [[agentes-ia-aceleran-trabajo-acotado-y-verificable]]
