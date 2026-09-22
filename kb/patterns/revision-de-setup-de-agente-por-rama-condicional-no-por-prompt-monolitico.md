---
id: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
title: Revisar el setup de un agente por rama condicional, no por prompt monolítico
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- abf61eeec75462f9
tags:
- agentes
- code-review
- liderazgo-técnico
- prompts
base_confidence: 0.1
half_life_days: 365
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
---

## What it is
Propuesta: si la conducta del agente se compone de ramas condicionales, la unidad revisable del setup de un agente es la rama (qué contexto activa qué conducta) y no el prompt como texto único. Bajo esa unidad, el code review de un rules file o skill apunta a condiciones, no a longitud ni estilo del texto. La propuesta está motivada por una sola observación sobre Claude Code (doc:abf61eeec75462f9) y no ha sido validada en ningún equipo ni herramienta.

## Evidence
- El system prompt de Claude Code se reporta como ensamblado de docenas de partes condicionales, lo que haría de la condición la unidad efectiva de conducta — source: abf61eeec75462f9
- La fuente es un reporte secundario sobre un leak, con engagement 0, sin segunda fuente que lo corrobore — source: abf61eeec75462f9
- El documento no describe ninguna práctica de revisión ni caso de equipo; la propuesta de revisión por rama es inferencia — source: abf61eeec75462f9

## Why it matters
Si se adopta sin evidencia, un lead reorganizaría su revisión de agentes alrededor de condiciones que su propia herramienta puede no tener. Tratada como hipótesis de bajo coste, la propuesta es barata de probar: al escribir un rules file, nombrar explícitamente cada condición que activa una regla; al revisar, verificar cobertura de condiciones. Su valor no está demostrado por la fuente, y su confianza es 0.10.

`derived_from` → `claude-code-system-prompt-conditional-composition`: la propuesta depende enteramente de esa observación. `relates_to` → `system-prompt-como-artefacto-de-ingenieria`: encaja como una unidad de revisión concreta dentro de ese patrón ya registrado. `relates_to` → `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes`: comparten la tesis de que las condiciones, no el texto completo, son lo testeable.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
