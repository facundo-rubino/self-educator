---
id: claude-code-source-leak-condiciones-parts-unspecified
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-08'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- evidencia-debil
- evidencia-faltante
- inferencia
- leak
- prompt-engineering
- system-prompt
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: supports
- to: claude-code-system-prompt-conditional-composition
  type: supports
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: claude-code-source-leak-sin-artefacto-primario
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria-claude-code
  type: relates_to
---

## What it is
El leak del código fuente de Claude Code se invoca como evidencia de un system prompt ensamblado de partes condicionales, pero no especifica qué condiciones activan qué secciones, cómo se ordenan ni con qué granularidad se componen. Sin esos detalles, «docenas de partes condicionales» es una descripción de forma, no de mecanismo.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales — source: abf61eeec75462f9
- No hay especificación de condiciones, partes ni secuenciación más allá de esa afirmación — source: abf61eeec75462f9 (ausencia)

## Why it matters
Cualquier lectura operativa («así se depura un prompt de agente», «así se estructura contexto para un equipo») requeriría los detalles que el documento no trae. Queda como pregunta abierta, no como base para diseño.

Refuerza la nota sobre la vista filtrada de código que no confirma composición condicional y la que pide un artefacto primario verificable. Se conecta temáticamente con el patrón general del system prompt como artefacto de ingeniería, sin aportarle evidencia nueva.

## Links
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- supports → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- supports → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria-claude-code]]
