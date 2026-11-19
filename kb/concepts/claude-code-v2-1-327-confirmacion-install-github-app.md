---
id: claude-code-v2-1-327-confirmacion-install-github-app
title: Claude Code v2.1.327 añade confirmación antes de /install-github-app
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
- guardrail
- github
- release-notes
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-11-19'
provenance:
  scale: S
  query: null
links:
- to: claude-code-v2-1-327-mcp-add-json-stdin
  type: relates_to
- to: claude-code-v2-1-327-aviso-sesion-reanudada
  type: relates_to
---

## What it is
v2.1.327 introduce un paso de confirmación antes de que `/install-github-app` modifique un repositorio. Es un guardrail pequeño contra cambios accidentales de repo disparados desde el agente.

## Evidence
- v2.1.327 añadió confirmación antes de que /install-github-app modifique un repositorio — source: 4f414908e605fee4

## Why it matters
Convierte una acción del agente con efecto lateral sobre un repo en una operación que exige asentimiento explícito. Es higiene de seguridad de tooling, no una medición de productividad.

Hermana de las otras tres entradas de la misma release (stdin para tokens MCP, aviso de sesión reanudada, /status de diagnósticos): todas son cambios de hardening y observabilidad incremental del mismo changelog.

## Links
- relates_to → [[claude-code-v2-1-327-mcp-add-json-stdin]]
- relates_to → [[claude-code-v2-1-327-aviso-sesion-reanudada]]
