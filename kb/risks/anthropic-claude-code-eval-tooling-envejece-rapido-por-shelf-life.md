---
id: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
title: 'El tooling de evals envejece rápido: el propio autor advierte vida útil corta
  de las reseñas'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-07'
updated: '2026-11-23'
sources:
- 541b1e7161ae8f43
tags:
- churn
- claude-code
- evals
- mantenimiento
- obsolescencia
- shelf-life
- tooling
- vida-util
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-11-23'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: relates_to
- to: arquitectura-de-prompt-cambia-sin-aviso
  type: relates_to
- to: datasette-alpha-features-no-son-settled
  type: relates_to
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
- to: jev-herramientas-de-tooling-open-source-envejecen-rapido-conclusiones-fragiles
  type: relates_to
- to: arquitectura-de-prompt-cambia-sin-aviso
  type: supports
- to: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
  type: relates_to
---

## What it is
El autor declara que normalmente evita reseñar tooling de evaluación porque el software cambia rápido y las reseñas tienen vida útil corta. El propio documento es, por tanto, un artefacto perecedero: sus detalles pueden estar ya obsoletos o cambiar en poco tiempo.

## Evidence
- El autor evita revisiones de tooling de eval porque el software cambia rápido y las reseñas envejecen pronto — source: 541b1e7161ae8f43

## Why it matters
Cualquier convención de equipo que dependa de estos comandos debe planificar el churn: verificar contra upstream antes de fijarlos en configuración o en material de docencia.

`relates_to` la nota del anuncio y la de fuente única. `supports` el riesgo conocido de que la arquitectura de un producto comercial cambia sin aviso: aquí el propio autor lo concede por adelantado.

## Links
- relates_to → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[arquitectura-de-prompt-cambia-sin-aviso]]
- relates_to → [[datasette-alpha-features-no-son-settled]]
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[jev-herramientas-de-tooling-open-source-envejecen-rapido-conclusiones-fragiles]]
- supports → [[arquitectura-de-prompt-cambia-sin-aviso]]
- relates_to → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
