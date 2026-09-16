---
id: system-prompt-como-artefacto-de-ingenieria
title: 'El system prompt como artefacto de ingeniería: versionado, revisado, testeado'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- agentic-coding
- engineering-practice
- prompt-architecture
- team-leadership
base_confidence: 0.35
half_life_days: 365
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: supports
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
---

## What it is
Práctica de tratar el system prompt de un agente como código: versionado, revisado y testeado en lugar de editado a mano como texto libre. Se propone como práctica transferible al resto del stack de agentes internos de un equipo.

## Evidence
- Documentar el 'prompt como artefacto de ingeniería' (versionado, revisado, testeado) es una práctica transferible al resto del stack de agentes internos — source: abf61eeec75462f9
- El diseño de prompts en herramientas serias de agentes es un problema de ingeniería de software (composición, condiciones, mantenibilidad) — source: abf61eeec75462f9

## Why it matters
Para un dev que lidera equipos chicos, convierte el prompt en algo que entra al mismo ciclo que el resto del código: revisión en PR, tests de regresión, historial de cambios. Sin eso, cada ajuste de prompt es irreversible y no auditable.

Se apoya en `claude-code-system-prompt-conditional-composition` como caso observado (aunque débilmente evidenciado) y sostiene a `ensamblado-condicional-de-prompts`: versionar y testear es requisito previo para componer bloques condicionales sin que el sistema se vuelva inmantenible.

## Links
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
