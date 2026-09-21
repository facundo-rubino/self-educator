---
id: control-de-agente-como-composicion-de-secciones
title: 'Control del agente como composición de secciones: inferencia no demostrada'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- agentes
- claude-code
- control-de-agentes
- evidencia
- inferencia
- leak
- riesgo
- riesgo-epistemico
- system-prompt
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
---

## What it is
Que el control del agente consista en la composición de secciones condicionales del system prompt es una inferencia plausible, pero no está demostrada por la evidencia disponible. El cluster aporta una aserción de una línea sin fragmentos citados ni disparadores nombrados.

## Evidence
- La única evidencia del cluster es una aserción de una línea sobre ensamblado condicional, sin fragmentos de prompt citados ni disparadores condicionales nombrados — source: abf61eeec75462f9
- El ítem es un singleton RSS con engagement=0: no existe documento corroborante dentro de la señal — source: abf61eeec75462f9

## Why it matters
Presentar la composición condicional como el mecanismo de control del agente sería convertir un patrón plausible en un hecho verificado. Ese salto es el tipo de error que desorienta a estudiantes sobre qué está documentado y qué fue inferido. La decisión operativa debería apoyarse en el patrón, no en el framing de «fuente filtrada».

Cuelga directamente del concepto sobre el ensamblado condicional del prompt de Claude Code y refuerza el riesgo de sobre-generalizar el diseño de Claude Code a agentes propios. Se relaciona también con el riesgo general de que un leak sin autenticidad establecida no confirme lo que dice, y con el de que la modularidad de prompts sea plausible pero no verificable.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
