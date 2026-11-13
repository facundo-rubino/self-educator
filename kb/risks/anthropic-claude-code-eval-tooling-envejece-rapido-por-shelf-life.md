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
updated: '2026-11-13'
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
last_reinforced: '2026-11-13'
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
---

## What it is
El autor del documento afirma que normalmente no revisa herramientas de evaluación por su corta vida útil. Ese juicio es en sí mismo evidencia de que cualquier nota o recomendación basada en el tooling de evals de Claude Code caduca rápido: los comandos, su interfaz y su comportamiento pueden cambiar o desaparecer sin correlato en un estándar estable.

## Evidence
- El autor declara que no suele reseñar herramientas de eval por su corta vida útil — source: 541b1e7161ae8f43

## Why it matters
Una nota del KB que documente `build_eval` y `hill-climb` como práctica recomendada debe fecharse y revisarse contra la versión del plugin. Para un equipo chico, invertir en un harness propio sobre evals estables es más duradero que adoptar comandos de un plugin que puede cambiar por release.

Deriva del concepto del tooling. Conecta con la discusión general sobre mantenimiento frente a generación: el coste de re-verificar tooling, no el de escribirlo, es lo que no baja.

## Links
- relates_to → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[arquitectura-de-prompt-cambia-sin-aviso]]
- relates_to → [[datasette-alpha-features-no-son-settled]]
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
