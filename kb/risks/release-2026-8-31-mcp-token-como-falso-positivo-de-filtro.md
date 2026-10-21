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
updated: '2026-10-21'
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
- brief
- brief-agentes
- falso-positivo
- falsos-positivos
- filtrado
- filtro
- filtro-determinista
- matching-lexico
- mcp
- pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-21'
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
- to: mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
---

## What it is
El clúster entra al brief por coincidencia de palabras clave del ecosistema MCP («server», «agents», «sequential-thinking», «memory»), no por contenido sobre la práctica de un dev que lidera y enseña. La relevancia medida (0.33) y la novedad (0.00) son coherentes con un match léxico, no semántico.

## Evidence
- La relevancia medida del clúster es 0.33 y la novedad 0.00 — source: 30a26335a9988ba2
- Los seis documentos son de tipo RSS con engagement=0 — source: 30a26335a9988ba2
- Las entradas solo listan bumps de versión sin descripción de funcionalidad ni uso — source: ffbd76916d1dfdc5

## Why it matters
Si el pipeline sigue ingiriendo estos release-feeds sin un gate de contenido, seguirán consumiendo cupo de briefs temáticos sin aportar señal. Etiquetarlos como maintenance/noise evita ese desgaste.

Es el mecanismo concreto del solapamiento léxico «agents/servers» ya documentado como falso positivo de clustering, y sostiene la lectura del clúster como ruido para el brief.

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
- supports → [[mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
