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
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- docencia
- agentes
- prompt
- abstraccion
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-09-21'
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
---

## What it is
Modelar el system prompt como una composición de secciones gateadas por features, en lugar de un bloque monolítico, es una abstracción enseñable para agentes de código: separa qué texto se incluye de cuándo se incluye. La evidencia del cluster es la aserción sobre Claude Code, no una demostración didáctica.

## Evidence
- El prompt descrito como ensamblado de docenas de partes condicionales es la base de la abstracción propuesta — source: abf61eeec75462f9
- La única fuente es un ítem RSS con engagement=0; el report no aporta material didáctico ni medición de aprendizaje — source: abf61eeec75462f9

## Why it matters
Si se adopta como unidad de enseñanza, el objetico es que el estudiante vea el prompt como configuración con partes y condiciones, no como texto a editar. La evidencia disponible sostiene el ejemplo, no la efectividad de la secuencia didáctica, que requeriría su propia validación en el KB de docencia.

Deriva del patrón general de ensamblado condicional de prompts y lo proyecta al aula. Se alinea con el system prompt entendido como artefacto de ingeniería (versionado, revisado, testeado) y con la observación de que el prompt modular y condicional ya es conocido en productos LLM.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
