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
updated: '2026-09-17'
sources:
- abf61eeec75462f9
tags:
- control-de-agentes
- inferencia
- leak
- riesgo-epistemico
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-09-17'
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
---

## What it is
El reporte extrae de un detalle interno de implementación («prompt ensamblado de partes condicionales») una conclusión sobre affordances del desarrollador: que el control sobre el agente también sería composicional. Es un salto inferencial: la evidencia describe cómo se construye el prompt dentro del producto, no qué control expone el producto al usuario.

## Evidence
- La evidencia disponible es un único documento con un único claim sobre estructura interna del prompt — source: abf61eeec75462f9.
- El propio crítico del pipeline señala que la conclusión sobre control composicional está «smuggled in from the premise rather than derived» — source: transcript del signal sig-979a04e33a30 (confianza ajustada 0.12).

## Why it matters
Tratar un detalle interno como capacidad del desarrollador infla la utilidad práctica del hallazgo: un lead que elige tooling de agentes no puede decidir sobre la base de una estructura de prompt que el proveedor no expone ni documenta. La lección transferible al brief es que «cómo está construido por dentro» y «qué puedo controlar desde fuera» son claims distintos y requieren evidencia distinta.

Deriva de `claude-code-system-prompt-conditional-composition`, cuyo único soporte es la fuente filtrada. Es la misma familia de riesgo que `prompt-modular-sin-mecanica-verificable` (modularidad plausible pero no verificable) y `sobre-generalizacion-desde-claude-code` (extrapolar el diseño de un producto a los propios agentes).

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
