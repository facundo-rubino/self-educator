---
id: release-2026-8-31-falso-positivo-por-vocabulario-mcp-agentes
title: El cluster del release 2026.8.31 sobrevivió al filtro por vocabulario compartido
  MCP/agentes, no por contenido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-09'
sources:
- 30a26335a9988ba2
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
- ffbd76916d1dfdc5
tags:
- mcp
- filtrado
- falso-positivo
- pipeline
- agentes
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: release-2026-8-31-mcp-token-como-falso-positivo-de-filtro
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: supports
- to: mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades
  type: supports
- to: mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo
  type: relates_to
---

## What it is
Los ocho documentos del clúster son notas de release con formato 'Release: vFECHA' y listas de paquetes MCP: server-filesystem, server-everything, server-sequential-thinking, server-memory, mcp-server-git, mcp-server-time y mcp-server-fetch. Su único vínculo con el topic del brief es léxico: 'MCP' y 'agentes' comparten vocabulario con el vocabulario del brief, sin que ningún documento describa uso, aplicación, metodología ni resultado.

## Evidence
- Release 2025.11.25 lista server-sequential-thinking, server-everything, server-filesystem, server-memory y mcp-server-git — source: 16a4e3995d6c827e.
- Release 2025.12.18 repite el mismo patrón de bumps de paquetes MCP — source: 2221814efbefaa3b.
- Release 2026.8.31 incluye server-filesystem, server-memory, server-sequential-thinking y server-everything — source: 30a26335a9988ba2.
- Release 2026.7.10 introduce mcp-server-time y mcp-server-fetch junto a server-filesystem y mcp-server-git — source: 5a4df6bef0a4905f.
- Release 2026.1.14 lista server-everything, server-filesystem y mcp-server-git — source: 748f8b0a02cd7524.
- Release 2026.8.18 lista server-everything, mcp-server-time, mcp-server-fetch y mcp-server-git — source: 9750590bbfe6b285.
- Release 2026.1.26 lista server-everything, server-memory y mcp-server-time — source: b9106690f5dfd849.
- Release 2026.7.4 lista server-everything, server-filesystem, server-sequential-thinking y server-memory — source: ffbd76916d1dfdc5.

## Why it matters
El corte léxico por 'MCP' y 'agentes' deja pasar infraestructura como si fuese práctica documentada. Si el brief busca cómo aplicar agentes a programar, gestionar o enseñar, el pipeline necesita distinguir 'la herramienta existe / se actualizó' de 'práctica documentada'. Sin esa distinción, futuros briefs se contaminan con ruido de infraestructura.

Refuerza la nota previa sobre el token 'MCP server' como falso positivo de filtro y el análisis de solapamiento léxico 'agents'/'servers'. Contradice implícitamente cualquier lectura del clúster como evidencia de uso de agentes para organizar trabajo o estudio, lo que las notas de riesgo sobre el feed MCP ya señalaban.

## Links
- supports → [[release-2026-8-31-mcp-token-como-falso-positivo-de-filtro]]
- supports → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- supports → [[mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades]]
- relates_to → [[mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo]]
