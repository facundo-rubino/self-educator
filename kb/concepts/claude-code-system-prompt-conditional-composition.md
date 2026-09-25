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
updated: '2026-09-25'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentes-de-codigo
- agentic-coding
- claude-code
- composicion-condicional
- composición-condicional
- filtracion
- fuente-unica
- ingenieria-inversa
- leak
- prompt-architecture
- prompt-engineering
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-25'
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
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
---

## What it is
El documento abf61eeec75462f9 reporta que el código fuente filtrado de Claude Code muestra que su system prompt se ensambla a partir de docenas de partes condicionales, en lugar de un bloque monolítico. Es una afirmación de ingeniería inversa sobre las tripas de una herramienta de agentes aplicada a programar: la instrucción al modelo sería el resultado de componer secciones activadas por condiciones.

## Evidence
- El system prompt de Claude Code se construye ensamblando docenas de partes condicionales, según el código fuente filtrado que cita el documento — source: abf61eeec75462f9

## Why it matters
Marca una arquitectura de prompts componible (bloques activados por contexto de entorno, herramientas o modo de tarea) frente al prompt monolítico, y sitúa el prompt del agente como artefacto auditable y testeable por bloque. También desmitifica la IA como caja negra para quien enseña a programar con agentes: la instrucción al modelo es configuración y composición, no magia.

`system-prompt-como-artefacto-de-ingenieria` es la tesis general que este caso instancia. `prompt-condicional-conocimiento-comun-en-productos-llm` y `ensamblado-condicional-de-prompts` ya establecen que el ensamblado condicional es un patrón conocido en productos LLM, no una exclusiva de Claude Code. `leak-de-claude-code-sin-fragmentos-citados` recoge la ausencia de fragmentos, disparadores y versión. `sobre-generalizacion-desde-claude-code` advierte contra extrapolar este diseño a agentes propios.

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
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
