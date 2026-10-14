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
updated: '2026-10-14'
sources:
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
- ffbd76916d1dfdc5
tags:
- agentes
- clustering
- falso-positivo
- filtrado
- mcp
- pipeline
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-14'
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
- to: release-2026-8-31-mcp-token-como-falso-positivo-de-filtro
  type: relates_to
- to: mcp-release-stubs-como-artefacto-de-feed
  type: supports
- to: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
  type: relates_to
- to: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
  type: relates_to
---

## What it is
Los siete documentos del cluster (2025.12.18, 2026.1.14, 2026.1.26, 2026.7.4, 2026.7.10, 2026.8.18, 2026.8.31) comparten un mismo template: «Release : v<fecha>» seguido de «Updated packages» y una lista de package@date — sources: 30a26335a9988ba2, 2221814efbefaa3b, 5a4df6bef0a4905f, 748f8b0a02cd7524, 9750590bbfe6b285, b9106690f5dfd849, ffbd76916d1dfdc5. Ninguno contiene prosa, argumento ni guía sobre productividad, estimación, secuenciamiento, alcance o docencia. La coincidencia léxica «MCP/servers/agents/update» con el vocabulario del brief de agentes es el mecanismo probable de un falso positivo de clustering.

## Evidence
- Los siete documentos comparten el template «Release : v<fecha>» + «Updated packages» + lista de package@date — sources: 2221814efbefaa3b, 748f8b0a02cd7524, b9106690f5dfd849, ffbd76916d1dfdc5, 5a4df6bef0a4905f, 9750590bbfe6b285, 30a26335a9988ba2
- Los scores reportados son novelty=0.00 y relevance=0.33 — source: sig-806e0d2a2326
- Ningún documento contiene prosa sobre práctica de desarrollo ni docencia — sources: 30a26335a9988ba2, 2221814efbefaa3b, 5a4df6bef0a4905f, 748f8b0a02cd7524, 9750590bbfe6b285, b9106690f5dfd849, ffbd76916d1dfdc5

## Why it matters
El cluster llegó al análisis como resultado del filtro determinista, no como hallazgo temático. Tratarlo como evidencia sobre práctica de ingeniería o liderazgo sería fabricación. El modo de fallo es reutilizable: el vocabulario genérico de infraestructura (agents, servers, packages, update) admite ítems fuera del tema declarado del brief.

`release-2026-8-31-mcp-token-como-falso-positivo-de-filtro` describe la misma mecánica desde el ángulo del token «MCP server». `mcp-release-stubs-como-artefacto-de-feed` generaliza el patrón de que los stubs de release son artefacto de feed, no señal de tema. Los falsos positivos por keyword del filtro ya están documentados en otros clusters (`xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro`, `matching-llm-patterns-relevancia-lexica-al-brief-de-agentes`).

## Links
- supports → [[release-2026-8-31-mcp-token-como-falso-positivo-de-filtro]]
- supports → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- supports → [[mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades]]
- relates_to → [[mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo]]
- relates_to → [[release-2026-8-31-mcp-token-como-falso-positivo-de-filtro]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
- relates_to → [[xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro]]
- relates_to → [[matching-llm-patterns-relevancia-lexica-al-brief-de-agentes]]
