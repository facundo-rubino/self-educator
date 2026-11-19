---
id: changelog-de-release-como-senal-de-craft-y-tooling-no-de-practica-medida
title: Un changelog de release es señal de craft y calidad de tooling, no de práctica
  medida
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-19'
updated: '2026-11-19'
sources:
- 4f414908e605fee4
tags:
- release-notes
- evidencia
- craft
- tooling
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-11-19'
provenance:
  scale: S
  query: null
links:
- to: release-de-parche-no-revela-practica-de-ingenieria
  type: contradicts
- to: claude-code-v2-1-327-mcp-add-json-stdin
  type: derived_from
- to: claude-code-v2-1-327-status-lista-agentes-skills-roto
  type: derived_from
- to: feed-de-dependencias-no-es-evidencia-de-practica-profesional
  type: relates_to
---

## What it is
Las entradas de un changelog describen features enviadas, no resultados medidos. Contienen señal real de craft y de calidad de tooling —por ejemplo, un cambio de manejo de secretos guiado por modelo de amenaza o una mejora de diagnosability— pero no evidencian mejora de productividad, precisión de estimación ni efectividad docente.

## Evidence
- v2.1.327 añadió el paso de stdin para mantener tokens MCP fuera de la línea de comandos y una lista en /status de agentes/skills/comandos rotos — source: 4f414908e605fee4
- El documento es un changelog de una sola versión; ninguna entrada reporta outcome medido — source: 4f414908e605fee4

## Why it matters
Corrige el error simétrico a «el changelog no contiene nada»: sí contiene señal de craft, pero de un tipo que no sostiene claims de práctica ni de liderazgo. Leerlo como evidencia de resultados es fabricación; declararlo vacío es conclusión por reetiquetado.

Contradice la nota `release-de-parche-no-revela-practica-de-ingenieria`, que descarta el release de parche como fuente de cualquier señal; este caso muestra que hay señal de tooling, aunque no de práctica medida. Se apoya en las cuatro entradas concretas de v2.1.327.

## Links
- contradicts → [[release-de-parche-no-revela-practica-de-ingenieria]]
- derived_from → [[claude-code-v2-1-327-mcp-add-json-stdin]]
- derived_from → [[claude-code-v2-1-327-status-lista-agentes-skills-roto]]
- relates_to → [[feed-de-dependencias-no-es-evidencia-de-practica-profesional]]
