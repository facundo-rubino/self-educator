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
updated: '2026-09-23'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentic-coding
- claude-code
- composicion-condicional
- composición-condicional
- filtracion
- fuente-unica
- leak
- prompt-architecture
- prompt-engineering
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-23'
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
---

## What it is
El system prompt de Claude Code no es un bloque monolítico: se ensambla a partir de docenas de partes condicionales. La afirmación proviene de un artículo que se presenta como basado en «leaked source» de Claude Code. Es la única afirmación sostenible del clúster: no hay detalle de implementación, medición, autoría ni verificación independiente.

## Evidence
- El system prompt de Claude Code está ensamblado a partir de docenas de partes condicionales — source: abf61eeec75462f9
- El artículo se presenta como basado en «leaked source» de Claude Code — source: abf61eeec75462f9

## Why it matters
Si la arquitectura es real, describe un patrón de diseño transferible: bloques activables según contexto (herramientas disponibles, estado de sesión, tipo de tarea) en lugar de un prompt único. Eso alinearía con separar instrucciones de dominio (p. ej. un profile `teaching`) de las de coding. Pero el registro es de titular, no de artefacto: engagement 0, corroboración 0.50, novelty 0.00. No debería desplazar fuentes con evidencia más fuerte sobre liderazgo, estimación o docencia.

`supports` las notas sobre ensamblado condicional de prompts y sobre el system prompt como artefacto de ingeniería: la composición por bloques es justamente lo que hace versionable y testeable un prompt. `relates_to` las notas sobre el leak de Claude Code y la vista filtrada del código: comparten fuente y la misma laguna (condiciones, partes y secuenciación sin especificar). También `relates_to` el riesgo de sobre-generalizar desde Claude Code y la nota sobre prompt condicional como patrón conocido en productos LLM.

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
