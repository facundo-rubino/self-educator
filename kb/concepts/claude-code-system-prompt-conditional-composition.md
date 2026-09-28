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
updated: '2026-09-28'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentes-de-codigo
- agentic-coding
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
last_reinforced: '2026-09-28'
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
El código fuente filtrado de Claude Code mostraría que su system prompt no es un bloque monolítico, sino un ensamblado de docenas de partes condicionales. La afirmación proviene de un único post de RSS [abf61eeec75462f9], sin cita de código, archivo, función ni mecanismo de activación. No se especifica qué condiciones gatean qué secciones, ni la versión observada.

## Evidence
- «Claude Code's leaked source shows a system prompt assembled from dozens of conditional parts.» — source: abf61eeec75462f9

## Why it matters
Si el ensamblado condicional fuera real, sería una instancia del patrón general de composición condicional de prompts, no un hallazgo nuevo sobre él: la descripción es la esperada de cualquier pipeline de prompt grande. La afirmación no aporta detalle implementable, no mide efecto alguno sobre el trabajo del desarrollador, y no tiene corroboración en el clúster. Confianza 0.05.

Soporta el patrón `ensamblado-condicional-de-prompts` y la tesis de `system-prompt-como-artefacto-de-ingenieria`, pero solo como una instancia no verificada. La pregunta `claude-code-source-leak-condiciones-parts-unspecified` registra exactamente lo que este documento deja sin decir, y `leak-de-claude-code-sin-fragmentos-citados` es la misma carencia de evidencia.

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
