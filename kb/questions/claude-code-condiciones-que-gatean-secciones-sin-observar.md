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
updated: '2026-09-28'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia-debil
- hipotesis
- prompt-engineering
- prompting
- prompts
- system-prompt
- verificacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-28'
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
---

## What it is
El único dato disponible es el número aproximado («docenas») y la palabra «condicionales» [abf61eeec75462f9]. No hay enumeración de condiciones, ni orden de ensamblado, ni ejemplo de una sección que se active o se omita. La estructura interna del prompt no es observable desde este documento.

## Evidence
- «dozens of conditional parts», sin listado ni mecanismo — source: abf61eeec75462f9

## Why it matters
Sin condiciones identificables no se puede replicar el ensamblado, ni escribir tests de regresión por rama habilitada, ni depurar un comportamiento inesperado atribuyéndolo a una sección concreta. La pregunta es el prerrequisito técnico de cualquier uso práctico de la afirmación.

Deriva directamente de `claude-code-system-prompt-conditional-composition`. `reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria` explica por qué la carencia bloquea el uso práctico, y `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes` sería la herramienta que solo funciona una vez resuelta esta pregunta.

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
