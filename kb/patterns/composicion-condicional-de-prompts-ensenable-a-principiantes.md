---
id: composicion-condicional-de-prompts-ensenable-a-principiantes
title: La composición condicional de prompts como abstracción enseñable
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-29'
sources:
- abf61eeec75462f9
tags:
- abstraccion
- agentes
- agents
- docencia
- prompt
- prompt-engineering
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: corregir-un-error-propio-en-publico-como-artefacto-pedagogico
  type: relates_to
---

## What it is
La idea, enunciada en las implicaciones del informe y no en el documento fuente, de que mostrar a estudiantes que un agente real ensambla su prompt de fragmentos condicionales es una lección más honesta sobre ingeniería de LLM que presentar el prompt como un texto monolítico.

## Evidence
- El documento fuente solo afirma el ensamblado condicional; el uso pedagógico es inferencia del analista, no contenido ingerido — source: abf61eeec75462f9
- El propio informe declara que toda inferencia aguas abajo es especulativa dada la ausencia de corroboración — source: abf61eeec75462f9

## Why it matters
Sería un buen encuadre didáctico si el artefacto fuera real y verificable; hoy es una hipótesis de enseñanza construida sobre un claim débil. Vale como candidato a preparar, no como material de clase.

Deriva de `claude-code-system-prompt-conditional-composition` y comparte tema con `ensamblado-condicional-de-prompts`. Se apoya en la idea, ya presente en el grafo, de que corregir o mostrar el mecanismo real es mejor artefacto pedagógico que presentar la versión limpia.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[corregir-un-error-propio-en-publico-como-artefacto-pedagogico]]
