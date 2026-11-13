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
updated: '2026-11-13'
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
last_reinforced: '2026-11-13'
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
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life
  type: supports
---

## What it is
Un documento reporta que el plugin `claude-api` de Claude Code incluye los comandos `build_eval` y `hill-climb`, descritos como ayudas para construir evals, verificar los graders y mejorar la aplicación iterando contra ellos. El reporte no describe la mecánica interna de los comandos ni si están publicados y estables. La etiqueta «auto eval tool» del titular no está respaldada por la evidencia: `build_eval` y `hill-climb` se presentan como comandos de ayuda, no como un sistema autónomo de evaluación.

## Evidence
- Anthropic lanzó nuevo tooling de evaluación para Claude Code — source: 541b1e7161ae8f43
- El plugin `claude-api` incluye `build_eval` y `hill-climb` para construir evals, chequear los graders y mejorar la aplicación contra ellos — source: 541b1e7161ae8f43

## Why it matters
Si el tooling existe y es estable, el ciclo de desarrollo con Claude Code incorporaría evals como práctica de primera clase en lugar de confianza ciega en el output del agente. La consecuencia práctica sería definir criterios de aceptación y graders antes de iterar. Nada de esto está demostrado por la evidencia disponible: un solo documento, sin detalle técnico de los comandos.

Se relaciona con `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad` por compartir la idea de evals por tarea como capa de verificación. Es evidencia (débil) para las tres notas de riesgo sobre este mismo tooling: vida útil corta, fuente única sin documentación oficial, y ausencia de conexión con liderazgo/docencia.

## Links
- relates_to → [[evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- supports → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- supports → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-single-source-sin-documentacion-oficial]]
- derived_from → [[anthropic-claude-code-eval-tooling-no-cubre-ejes-de-liderazgo-docencia]]
- derived_from → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- supports → [[anthropic-claude-code-eval-tooling-envejece-rapido-por-shelf-life]]
