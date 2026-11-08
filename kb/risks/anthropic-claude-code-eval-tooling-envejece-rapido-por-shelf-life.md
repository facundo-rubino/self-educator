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
updated: '2026-11-08'
sources:
- 541b1e7161ae8f43
tags:
- evals
- mantenimiento
- obsolescencia
- shelf-life
- tooling
- vida-util
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-11-08'
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
---

## What it is
El autor declara que normalmente evita reseñar herramientas de evaluación porque el software cambia rápido y las reseñas tienen vida útil corta; hace una excepción con el tooling de primera parte de Anthropic [541b1e7161ae8f43]. Cualquier detalle sobre `build_eval` o `hill-climb` registrado hoy puede quedar obsoleto o cambiar pronto.

## Evidence
- El autor evita reseñar herramientas de eval por el ritmo de cambio del software y la corta vida útil de las reseñas — source: 541b1e7161ae8f43

## Why it matters
Un claim sobre este tooling es perecedero por diseño: no debe citarse como estado estable de la práctica sin re-verificación contra upstream antes de usarse en configuración o docencia.

Se relaciona con la nota del tooling como condición de vigencia de su contenido, y con la nota sobre features de alpha no asentadas: en ambos casos lo documentado puede cambiar antes de estabilizarse.

## Links
- relates_to → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[arquitectura-de-prompt-cambia-sin-aviso]]
- relates_to → [[datasette-alpha-features-no-son-settled]]
