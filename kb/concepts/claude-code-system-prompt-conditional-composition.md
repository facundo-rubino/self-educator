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
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- agentic-coding
- system-prompt
- claude-code
- prompt-architecture
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-09-16'
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
---

## What it is
El system prompt de Claude Code no sería un texto monolítico sino una composición dinámica ensamblada a partir de docenas de partes condicionales. La afirmación proviene de una lectura del supuesto código fuente filtrado de la herramienta, reportada a nivel de titular.

## Evidence
- El system prompt de Claude Code se ensambla a partir de "docenas de partes condicionales", no es un texto monolítico — source: abf61eeec75462f9
- Fuente única, tipo rss, engagement=0, sin corroboración independiente ni código o fragmentos citados — source: abf61eeec75462f9

## Why it matters
Si el diseño es real, el prompt deja de ser un artefacto de redacción y pasa a ser un artefacto de composición: el problema se desplaza a qué bloques activar, cuándo y en qué orden. Bajo ese encuadre, construir agentes propios deja de ser "escribir bien el prompt" y se vuelve diseñar un ensamblador.

Se apoya en `system-prompt-como-artefacto-de-ingenieria` porque es un caso concreto de tratar el prompt como software construido, no como texto. Contradice parcialmente `prompt-modular-sin-mecanica-verificable`: la afirmación es plausible pero no verificable en el estado actual, y el rol de esa nota es sostener la duda hasta que exista evidencia mecánica. `sobre-generalizacion-desde-claude-code` acota el alcance de cualquier conclusión tomada de aquí.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
