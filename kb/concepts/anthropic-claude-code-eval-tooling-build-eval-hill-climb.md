---
id: anthropic-claude-code-eval-tooling-build-eval-hill-climb
title: 'Tooling de evaluación de Anthropic para Claude Code: `build_eval` y `hill-climb`
  en el plugin `claude-api`'
type: concept
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
- agentes
- anthropic
- claude-code
- evals
- single-source
- tooling
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-11-08'
provenance:
  scale: S
  query: null
links:
- to: evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas
  type: relates_to
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
  type: supports
- to: anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia
  type: supports
- to: anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial
  type: derived_from
- to: anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia
  type: derived_from
- to: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
  type: derived_from
---

## What it is
Anthropic publicó tooling de evaluación de primera parte para Claude Code dentro de su plugin `claude-api`. El plugin añade los comandos `build_eval` y `hill-climb`: construir evals, verificar los graders e iterar la aplicación contra ellos [541b1e7161ae8f43]. El mecanismo descrito es un loop «construir eval → escalar contra la eval» integrado en el flujo de trabajo de un ingeniero que usa agentes [541b1e7161ae8f43].

## Evidence
- Anthropic publicó tooling de evaluación para Claude Code vía el plugin `claude-api` — source: 541b1e7161ae8f43
- El plugin añade `build_eval` y `hill-climb`, que ayudan a construir evals, comprobar los graders y mejorar una aplicación contra ellos — source: 541b1e7161ae8f43
- El autor normalmente evita reseñar herramientas de eval por la corta vida útil de esas reseñas, pero hace una excepción con el tooling de primera parte de Anthropic por su probable influencia en la práctica — source: 541b1e7161ae8f43

## Why it matters
Un loop de evaluación (`build_eval` → `hill-climb`) vuelve accesible por defecto la medición del trabajo asistido por IA dentro de un flujo agéntico, en lugar de inspeccionar salidas a ojo. El respaldo es una sola fuente (un documento RSS de anuncio de vendor): la utilidad práctica y el impacto están afirmados, no demostrados [541b1e7161ae8f43].

Se relaciona con la evaluación específica por tarea como infraestructura de fiabilidad: ambos describen medir salidas de modelo contra criterios explícitos. Las notas de riesgo derivadas registran que la evidencia es de fuente única, que el tooling no cubre liderazgo/docencia, y que el propio autor advierte vida útil corta.

## Links
- relates_to → [[evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- supports → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- supports → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- derived_from → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
