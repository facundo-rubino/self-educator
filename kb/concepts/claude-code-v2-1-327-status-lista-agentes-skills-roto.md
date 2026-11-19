---
id: claude-code-v2-1-327-status-lista-agentes-skills-roto
title: Claude Code v2.1.327 añade lista en /status de agentes, skills, comandos y
  output rotos
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
- diagnostico
- agentes
- release-notes
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-11-19'
provenance:
  scale: S
  query: null
links:
- to: claude-code-v2-1-327-aviso-sesion-reanudada
  type: relates_to
- to: claude-code-v2-1-327-mcp-add-json-stdin
  type: relates_to
---

## What it is
v2.1.327 añade en `/status` una lista de agentes, skills, comandos y output que están rotos. Mejora la diagnosticabilidad de la configuración del agente.

## Evidence
- v2.1.327 añadió una lista en /status de agentes, skills, comandos y output rotos — source: 4f414908e605fee4

## Why it matters
Cuando la conducta del agente depende de muchas piezas de configuración, saber cuáles están rotas es prerrequisito para depurar. Es observabilidad de tooling; no mide mejora de productividad ni de estimación.

Es la pieza más directamente ligada a la depurabilidad de un setup de agente; se relaciona con el aviso de sesión reanudada y con el resto de la release.

## Links
- relates_to → [[claude-code-v2-1-327-aviso-sesion-reanudada]]
- relates_to → [[claude-code-v2-1-327-mcp-add-json-stdin]]
