---
id: claude-code-condiciones-que-gatean-secciones-sin-observar
title: 'Qué condiciones gatean qué secciones en Claude Code: sin observación directa'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-10-08'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia-debil
- hipotesis
- observacion
- prompt-engineering
- prompting
- prompts
- system-prompt
- verificacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: control-de-agente-como-composicion-de-secciones
  type: relates_to
- to: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: supports
---

## What it is
No hay observación directa de qué condiciones (tipo de tarea, repo, herramienta, turno de conversación) activan qué secciones del system prompt de Claude Code. La pregunta queda abierta y no puede resolverse desde este documento.

## Evidence
- El documento afirma el ensamblado condicional sin detallar condiciones ni secciones — source: abf61eeec75462f9
- No hay observación directa del mecanismo más allá de la afirmación — source: abf61eeec75462f9 (ausencia)

## Why it matters
Sin observar las condiciones, no se puede transferir el diseño a agentes propios ni evaluar si merece la pena replicarlo. Cualquier réplica hoy sería un experimento, no una adopción informada.

Es variante específica de la nota sobre el leak sin especificar condiciones, partes ni secuenciación. Se relaciona con control del agente como composición de secciones y con el problema de reproducibilidad/depuración de prompts.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[control-de-agente-como-composicion-de-secciones]]
- relates_to → [[revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- supports → [[claude-code-source-leak-condiciones-parts-unspecified]]
