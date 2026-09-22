---
id: claude-code-system-prompt-conditional-composition
title: El system prompt de Claude Code se ensambla de partes condicionales
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-22'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentic-coding
- claude-code
- composicion-condicional
- composición-condicional
- filtracion
- leak
- prompt-architecture
- prompt-engineering
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-22'
provenance:
  scale: M
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: supports
- to: prompt-modular-sin-mecanica-verificable
  type: contradicts
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
- to: sobre-generalizacion-desde-claude-code
  type: contradicts
- to: leak-sin-autenticidad-establecida
  type: derived_from
---

## What it is
Según un ítem RSS que reporta una vista filtrada del código de Claude Code, su system prompt no es un bloque monolítico sino que se ensambla en runtime a partir de docenas de partes condicionales (doc:abf61eeec75462f9). La fuente es un reporte secundario sobre material filtrado, no documentación de primera parte (doc:abf61eeec75462f9). El ítem no especifica qué condiciones activan qué partes, ni la secuencia de ensamblado.

## Evidence
- El system prompt se ensambla de docenas de partes condicionales en lugar de ser un texto fijo — source: abf61eeec75462f9
- La afirmación proviene de una vista filtrada del código, es decir, un reporte secundario sobre material filtrado y no documentación de primera parte — source: abf61eeec75462f9
- El documento es un ítem RSS con engagement 0, sin lectores ni discusión demostrados en el momento de la ingesta — source: abf61eeec75462f9

## Why it matters
Si la conducta del agente se configura en gran medida por condicionales en runtime, los prompts, archivos de reglas y skills escritos para un agente no son portables literalmente a otro: son configuración que debe re-derivarse por herramienta. Para un lead, la unidad revisable del setup de un agente sería la rama condicional (qué contexto dispara qué conducta), no el prompt monolítico. Para docencia, «el prompt» como artefacto enseñable es engañoso: lo enseñable es la lógica de ensamblado. Nada de esto está sostenido por el documento — es inferencia — y la confianza es 0.10 por fuente única, engagement nulo y procedencia no verificable.

`supports` → `ensamblado-condicional-de-prompts`: es una instancia concreta del patrón general ya registrado, aunque el documento no nombre el patrón. `relates_to` → `claude-code-source-leak-conditions-parts-unspecified`: el mismo corpus de leak del que este ítem es la única pieza que describe composición condicional. `contradicts` → `sobre-generalizacion-desde-claude-code`: ese riesgo advierte contra generalizar el diseño de Claude Code a agentes propios, mientras este ítem invita justamente a extraer conclusiones de práctica desde el leak. `derived_from` → `leak-sin-autenticidad-establecida`: la afirmación hereda la fragilidad de un leak cuya autenticidad no está establecida.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- contradicts → [[sobre-generalizacion-desde-claude-code]]
- derived_from → [[leak-sin-autenticidad-establecida]]
