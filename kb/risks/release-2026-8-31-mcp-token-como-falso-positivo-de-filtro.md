---
id: release-2026-8-31-mcp-token-como-falso-positivo-de-filtro
title: El token «MCP server» como falso positivo del filtro frente al brief de agentes
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-07'
sources:
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
- ffbd76916d1dfdc5
- sig-d0acf338c3a6
tags:
- brief-agentes
- falso-positivo
- falsos-positivos
- filtrado
- filtro-determinista
- matching-lexico
- mcp
- pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: supports
- to: titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters
  type: supports
- to: mcp-como-infraestructura-de-agentes-senal-indirecta-al-brief
  type: relates_to
- to: mcp-release-stubs-como-artefacto-de-feed
  type: relates_to
- to: release-2026-8-31-stub-sin-changelog
  type: supports
- to: mcp-cluster-2026-8-31-sin-relacion-con-el-brief
  type: supports
- to: mcp-release-2026-8-31-bumps
  type: relates_to
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades
  type: supports
---

## What it is
El clúster fue retenido con relevance=0.33, novelty=0.00 y corroboration=0.50, y todos sus ítems tienen engagement cero. El patrón que mejor explica su presencia en el brief es el solapamiento léxico superficial en «agents»/«AI»/«server» de un feed de releases, no una afinidad temática.

## Evidence
- El analista atribuye la retención a solapamiento superficial de keywords sobre «agents»/«AI», no a contenido — source: sig-d0acf338c3a6
- relevance=0.33 con novelty=0.00 y corroboration=0.50 acompañan a ítems de engagement cero — source: sig-d0acf338c3a6

## Why it matters
Un feed de changelog versionado por fecha puede reingresar en este topic en cada fecha futura mientras la regla de matching siga mirando tokens de superficie. Es un candidato directo a regla determinista de exclusión («aviso de release / digest de versiones de paquete») o a reasignarse a un stream dedicado de ecosistema/tooling.

Se relaciona con el release 2026.8.31 como el caso concreto que dispara esta regla, y con el riesgo general de que un clúster con relevance muy baja sobreviva al filtrado determinista. `supports` la nota sobre por qué un feed de releases MCP sin changelog no permite afirmar capacidades.

## Links
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- supports → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- supports → [[titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters]]
- relates_to → [[mcp-como-infraestructura-de-agentes-senal-indirecta-al-brief]]
- relates_to → [[mcp-release-stubs-como-artefacto-de-feed]]
- supports → [[release-2026-8-31-stub-sin-changelog]]
- supports → [[mcp-cluster-2026-8-31-sin-relacion-con-el-brief]]
- relates_to → [[mcp-release-2026-8-31-bumps]]
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- supports → [[mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades]]
