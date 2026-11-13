---
id: naming-auto-eval-tool-no-implica-sistema-autonomo
title: '«Auto eval tool» como etiqueta: `build_eval` y `hill-climb` son comandos de
  ayuda, no un sistema autónomo'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-13'
updated: '2026-11-13'
sources:
- 541b1e7161ae8f43
tags:
- evals
- naming
- titular
- capacidad
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-11-13'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: contradicts
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
---

## What it is
El titular «Claude's new auto eval tool» usa «auto» como modificador que la evidencia no respalda: `build_eval` y `hill-climb` se describen como comandos que ayudan a construir evals, verificar graders e iterar contra ellos. Un conjunto de helpers en un plugin no es un sistema de evaluación autónomo. La etiqueta «auto» puede ser una coincidencia de naming más que una capacidad verificada.

## Evidence
- `build_eval` y `hill-climb` se describen como ayudas para construir evals, chequear graders y mejorar iterando — source: 541b1e7161ae8f43
- No hay en la evidencia descripción de automatización autónoma del ciclo de evaluación — source: 541b1e7161ae8f43

## Why it matters
Comprar la etiqueta «auto» sin el mecanismo es la forma clásica de confundir naming con capacidad. Cualquier recomendación de equipo debería describir la herramienta como «comandos de construcción e iteración de evals» y no como «evaluación automática».

Contradice la formulación del concepto principal, que adopta el encuadre del titular. Comparte estructura con `afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion`: titular que afirma más de lo que el cuerpo sostiene.

## Links
- contradicts → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
