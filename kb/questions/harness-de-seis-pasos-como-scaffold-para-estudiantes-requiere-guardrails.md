---
id: harness-de-seis-pasos-como-scaffold-para-estudiantes-requiere-guardrails
title: Un harness ordenado como scaffold para estudiantes exige guardrails en verificación
  y triage
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
- docencia
- seguridad
- guardrails
- scaffold
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-11-14'
provenance:
  scale: S
  query: null
links:
- to: harness-agentico-de-seis-pasos-para-asegurar-codigo
  type: derived_from
- to: agentes-no-sustituyen-especificacion-experta
  type: relates_to
---

## What it is
Un harness con pasos nombrados y ordenados es un scaffold listo para estudiantes, pero el material del clúster no discute docencia ni aporta mecanismo para hacer obligatorios los pasos de verificación y triage. La conexión con enseñanza la genera el analista, no la fuente.

## Evidence
- El harness está enunciado como pasos ordenados (threat model, discover, verify, triage, patch) — source: b8a2ffe60796b1b8
- No hay en el clúster benchmarks, ejemplos trabajados ni datos de uso en docencia — source: b8a2ffe60796b1b8

## Why it matters
Si la hipótesis se sostuviera, enseñar el harness equivaldría a enseñar cuándo un hallazgo del LLM no es accionable. Sin fuente que lo respalde, es una extrapolación plausible que un docente debería verificar antes de llevarla al aula.

Se deriva del harness de seis pasos. Se conecta con la idea de que los agentes no sustituyen al experto que enmarca la especificación: el paso de verificación sería justamente el juicio que el estudiante debe aprender.

## Links
- derived_from → [[harness-agentico-de-seis-pasos-para-asegurar-codigo]]
- relates_to → [[agentes-no-sustituyen-especificacion-experta]]
