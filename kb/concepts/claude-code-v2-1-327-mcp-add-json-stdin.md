---
id: claude-code-v2-1-327-mcp-add-json-stdin
title: 'Claude Code v2.1.327: `claude mcp add-json <name> -` lee JSON por stdin para
  mantener tokens fuera de la línea de comandos'
type: concept
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
- claude-code
- mcp
- secretos
- seguridad
- release-notes
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-11-19'
provenance:
  scale: S
  query: null
links:
- to: claude-code-v2-1-327-confirmacion-install-github-app
  type: relates_to
- to: claude-code-v2-1-327-status-lista-agentes-skills-roto
  type: relates_to
---

## What it is
v2.1.327 añade `claude mcp add-json <name> -`, que lee el JSON de configuración de un server MCP desde stdin. Permite mantener tokens fuera de la línea de comandos. La opción no está disponible dentro de una sesión de Claude Code.

## Evidence
- v2.1.327 añadió `claude mcp add-json <name> -` para leer el JSON de un server por stdin y mantener tokens fuera de la línea de comandos; no disponible dentro de una sesión de Claude Code — source: 4f414908e605fee4

## Why it matters
Es un cambio guiado por modelo de amenaza para flujos con MCP: los secretos dejan de quedar en el historial de shell. La restricción de no funcionar dentro de una sesión acota su adopción real.

Comparte release con la confirmación de /install-github-app y con la lista de diagnósticos de /status; las tres apuntan a hardening y observabilidad del tooling de agentes, no a resultados medidos.

## Links
- relates_to → [[claude-code-v2-1-327-confirmacion-install-github-app]]
- relates_to → [[claude-code-v2-1-327-status-lista-agentes-skills-roto]]
