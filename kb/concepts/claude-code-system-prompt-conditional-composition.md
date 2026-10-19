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
updated: '2026-10-19'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentes-de-codigo
- agentic-coding
- agents
- claude-code
- claude-code-leak
- composicion-condicional
- composición-condicional
- filtracion
- fuente-filtrada
- fuente-unica
- ingenieria-inversa
- leak
- prompt-architecture
- prompt-arquitectura
- prompt-engineering
- prompting
- prompts-modulares
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-10-19'
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
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: entrega-de-prompt-monolitico-vs-condicional
  type: relates_to
- to: system-prompt-como-artefacto-de-ingenieria-claude-code
  type: relates_to
- to: claude-code-system-prompt-doc-sin-analisis-de-condiciones
  type: relates_to
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: claude-code-system-prompt-novelty-cero-ya-conocido
  type: supports
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: supports
- to: claude-code-system-prompt-condicional-composicion-condicional-claim-sin-fuente
  type: relates_to
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: contradicts
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
---

## What it is
Un documento RSS único [abf61eeec75462f9] afirma que el código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales. La afirmación describe arquitectura de prompts, no conducta medida del agente: no especifica qué condiciones gatean qué secciones, ni cómo se secuencian.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado de docenas de partes condicionales — source: abf61eeec75462f9

## Why it matters
Si el ensamblado condicional es real, refuerza la idea de configurar un agente por contexto (rol, herramienta, etapa) en lugar de un prompt monolítico. Para el brief, el valor es anecdótico: no hay medición de estimación, secuenciamiento, liderazgo ni docencia en la fuente.

Instancia específica del patrón general de `ensamblado-condicional-de-prompts`. Se relaciona con la nota existente `claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente` (misma afirmación, misma carencia) y con `claude-code-condiciones-que-gatean-secciones-sin-observar`, que registra precisamente lo que este documento no dice. `supports` es débil: aporta un caso al patrón, no evidencia de eficacia.

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
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[entrega-de-prompt-monolitico-vs-condicional]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria-claude-code]]
- relates_to → [[claude-code-system-prompt-doc-sin-analisis-de-condiciones]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[claude-code-system-prompt-novelty-cero-ya-conocido]]
- supports → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- relates_to → [[claude-code-system-prompt-condicional-composicion-condicional-claim-sin-fuente]]
- contradicts → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- relates_to → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
