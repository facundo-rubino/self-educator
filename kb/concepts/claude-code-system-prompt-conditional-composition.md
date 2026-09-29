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
updated: '2026-09-29'
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
- fuente-unica
- ingenieria-inversa
- leak
- prompt-architecture
- prompt-engineering
- prompting
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-29'
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
---

## What it is
Un documento RSS afirma que el código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales, en lugar de un bloque monolítico de instrucciones. Es la única afirmación sustantiva del clúster. No viene con fragmento, autor, repositorio ni número de versión.

## Evidence
- Claude Code ensamblaría su system prompt a partir de docenas de partes condicionales, según una fuente secundaria que cita un leak — source: abf61eeec75462f9
- El clúster contiene un único documento; no hay corroboración independiente (corroboration 0.50, novelty 0.00) — source: abf61eeec75462f9

## Why it matters
Si fuera cierto, el modelo mental correcto para configurar agentes propios no sería «un prompt grande» sino «un conjunto de bloques pequeños seleccionados por contexto». Eso desplaza el esfuerzo de ingeniería hacia la estructura y la selección de bloques, no solo hacia la elección de modelo. Como claim, sin embargo, no autoriza ninguna prescripción: describe un artefacto ajeno, no una práctica validada.

Se relaciona con `ensamblado-condicional-de-prompts` como instancia concreta del patrón general, y con `claude-code-condiciones-que-gatean-secciones-sin-observar` porque las condiciones que gobiernan cada parte no están especificadas. Conecta con `system-prompt-como-artefacto-de-ingenieria` por el encuadre del prompt como artefacto versionable y con `claude-code-source-leak-condiciones-parts-unspecified` y `leak-de-claude-code-sin-fragmentos-citados` por lo mismo: la fuente no aporta el detalle que haría utilizable la afirmación.

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
