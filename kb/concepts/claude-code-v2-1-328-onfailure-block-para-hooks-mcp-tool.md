---
id: claude-code-v2-1-328-onfailure-block-para-hooks-mcp-tool
title: 'Claude Code v2.1.328: `"onFailure": "block"` en hooks de `mcp_tool`'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-20'
updated: '2026-11-20'
sources:
- f7420b2e33629c6e
tags:
- claude-code
- hooks
- mcp
- onfailure
base_confidence: 0.6
half_life_days: 180
last_reinforced: '2026-11-20'
provenance:
  scale: S
  query: null
links:
- to: claude-code-v2-1-328-modo-auto-por-defecto-en-proveedores-cloud
  type: relates_to
- to: mcp-como-infraestructura-de-agentes-relevancia-lateral-al-brief
  type: relates_to
---

## What it is
Claude Code v2.1.328 añade `"onFailure": "block"` para hooks de tipo `mcp_tool`, con la misma semántica que ya existía para hooks de comando y HTTP: si la llamada del hook falla, la acción queda bloqueada.

## Evidence
- Se añadió `"onFailure": "block"` para hooks `mcp_tool`, igual que para hooks de comando y HTTP: si la llamada del hook falla, bloquea la acción — source: f7420b2e33629c6e

## Why it matters
Convierte un fallo de hook MCP en un fallo cerrado (fail-closed) en vez de silencioso, para quien dependa de hooks MCP en automatizaciones. Es un cambio de semántica operativa del tooling, no un hallazgo sobre estimación, liderazgo ni docencia.

Relacionado con el otro cambio de la misma release (modo auto por defecto). Toca la capa MCP como infraestructura de agentes, cuya conexión al brief es lateral.

## Links
- relates_to → [[claude-code-v2-1-328-modo-auto-por-defecto-en-proveedores-cloud]]
- relates_to → [[mcp-como-infraestructura-de-agentes-relevancia-lateral-al-brief]]
