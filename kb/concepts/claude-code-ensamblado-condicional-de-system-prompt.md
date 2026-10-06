---
id: claude-code-ensamblado-condicional-de-system-prompt
title: El system prompt de Claude Code se ensambla de partes condicionales (claim
  de fuente filtrada)
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-06'
sources:
- abf61eeec75462f9
tags:
- claude-code
- system-prompt
- agentes-de-codigo
- fuente-filtrada
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-system-prompt-doc-sin-analisis-de-condiciones
  type: supports
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria-claude-code
  type: supports
---

## What it is
El código fuente filtrado de Claude Code revelaría que su system prompt se ensambla a partir de «decenas de partes condicionales» [abf61eeec75462f9]. La afirmación es un titular de una pieza de tipo rss, sin artefacto primario citado (ni volcado del prompt, ni repositorio, ni diff) y sin método que explique cómo se seleccionan, activan u ordenan esos fragmentos [abf61eeec75462f9].

## Evidence
- «Claude Code's leaked source shows a system prompt assembled from dozens of conditional parts» — source: abf61eeec75462f9
- El documento es un ítem rss con engagement=0 — source: abf61eeec75462f9
- El clúster consta de un único documento, sin corroboración interna — source: abf61eeec75462f9

## Why it matters
Si fuera cierto, el comportamiento de un agente de codificación sería auditable y configurable por bloques en lugar de tratarse como monolito, lo que abriría la puerta a adaptar agentes por rol (programar, gestionar, enseñar) razonando sobre qué contexto activa qué sección. Pero con evidencia de una sola fuente sin artefacto primario, esto es un puntero a un rumor, no un hallazgo de arquitectura utilizable.

Relacionado con la nota preexistente «claude-code-system-prompt-conditional-composition», que registra la misma composición condicional. Refuerza las notas que documentan la laguna de condiciones y partes no especificadas, y apoya el encuadre del system prompt como artefacto de ingeniería. No se vincula con liderazgo, estimación ni docencia: la afirmación es de arquitectura interna de herramienta, no de método.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[claude-code-system-prompt-doc-sin-analisis-de-condiciones]]
- supports → [[claude-code-source-leak-condiciones-parts-unspecified]]
- supports → [[system-prompt-como-artefacto-de-ingenieria-claude-code]]
