---
id: build-eval-y-hill-climb-como-ciclo-de-mejora-iterativa-contra-graders
title: '`build_eval` y `hill-climb` como ciclo de mejora iterativa contra graders'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-13'
updated: '2026-11-23'
sources:
- 541b1e7161ae8f43
tags:
- agentes
- agentes-de-codigo
- ciclo-de-mejora
- claude-code
- evals
- graders
- hill-climb
- iteracion
base_confidence: 0.25
half_life_days: 180
last_reinforced: '2026-11-23'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: eval-discipline-como-capa-de-medicion-del-trabajo-con-agentes
  type: relates_to
- to: naming-auto-eval-tool-no-implica-sistema-autonomo
  type: contradicts
- to: hackathon-wandb-llm-as-a-judge-tangencial-por-definicion-de-llm-evaluation
  type: relates_to
---

## What it is
La descripción del anuncio presenta `build_eval` y `hill-climb` como dos pasos encadenados: construir la eval y luego mejorar la aplicación contra los graders. Se lee como un ciclo de refinamiento iterativo, no como una sola herramienta. El nombre `hill-climb` es una etiqueta de marketing sugerente; el documento no describe el algoritmo ni lo que realmente optimiza.

## Evidence
- `build_eval` ayuda a construir evals — source: 541b1e7161ae8f43
- `hill-climb` ayuda a revisar graders y mejorar una aplicación contra ellos — source: 541b1e7161ae8f43

## Why it matters
Si el ciclo funciona como se describe, materializa la secuencia «escribir evals, iterar contra graders, luego enviar» como ergonomía por defecto. Para docencia, ofrece un modelo observable de refinamiento iterativo demostrable sin depender del resultado concreto de la herramienta.

`derived_from` la nota del tooling de Anthropic. `contradicts` el riesgo de que el nombre de la herramienta se confunda con un sistema autónomo: el documento no pasa de nombrar comandos. `relates_to` con la disciplina de evals y con la noción de evaluación de LLMs, de la que este ciclo es una instancia concreta aunque no verificada.

## Links
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- relates_to → [[eval-discipline-como-capa-de-medicion-del-trabajo-con-agentes]]
- contradicts → [[naming-auto-eval-tool-no-implica-sistema-autonomo]]
- relates_to → [[hackathon-wandb-llm-as-a-judge-tangencial-por-definicion-de-llm-evaluation]]
