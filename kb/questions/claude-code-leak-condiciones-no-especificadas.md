---
id: claude-code-leak-condiciones-no-especificadas
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- abf61eeec75462f9
tags:
- claude-code
- open-question
- prompt-assembly
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: derived_from
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
---

## What it is
Pregunta abierta: ¿qué condiciones gatean qué secciones del system prompt, en qué orden se ensamblan y con qué granularidad? El documento no responde ninguna de las tres cosas.

## Evidence
- El ítem solo menciona «conditional parts» sin nombrar condiciones ni secciones. — source: abf61eeec75462f9
- No hay fragmentos citados del prompt filtrado en el clúster. — source: abf61eeec75462f9

## Why it matters
Sin esta información, el claim no es transferible a un agente propio ni enseñable como patrón concreto. Solo justifica recuperar la fuente primaria.

`derived_from` la nota del claim principal. `relates_to` la pregunta existente sobre qué condiciones gatean qué secciones: la nueva evidencia confirma que sigue sin observación directa.

## Links
- derived_from → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
