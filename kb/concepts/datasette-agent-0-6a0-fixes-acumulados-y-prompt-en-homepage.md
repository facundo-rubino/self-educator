---
id: datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage
title: 'datasette-agent 0.6a0: fixes acumulados y prompt del agente en la homepage
  con hash-mentions'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-16'
updated: '2026-11-16'
sources:
- 783baeb398598850
tags:
- datasette
- datasette-agent
- release-notes
- alpha
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-11-16'
provenance:
  scale: S
  query: null
links:
- to: datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes
  type: relates_to
- to: datasette-apps-sandbox-html-js-con-sql-analogo-a-artifacts
  type: relates_to
---

## What it is
datasette-agent es un plugin de agente para Datasette que permite hacer preguntas sobre los datos. La 0.6a0 es un lote de fixes pequeños acumulados; el cambio más notable es un prompt del agente colocado en la homepage de Datasette, con soporte para hash-mentions de tablas y queries.

## Evidence
- datasette-agent es un plugin de agente para Datasette que permite preguntar cosas sobre los datos — source: 783baeb398598850
- 0.6a0 es fixes pequeños acumulados; el cambio más notable es un prompt del agente en la homepage con soporte para hash-mentions de tablas y queries — source: 783baeb398598850

## Why it matters
Superficie de invocación del agente en la propia homepage, no en un panel aparte. Es un cambio de UX de release, no un hallazgo sobre práctica de ingeniería.

Se relaciona con datasette-apps 0.4a0 por el reporte de schemes hacia Datasette Agent y por compartir namespace `datasette`. La coincidencia de vocabulario (`hash`/`fragment`) no demuestra una tesis de «ecosistema agente/app» coherente.

## Links
- relates_to → [[datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes]]
- relates_to → [[datasette-apps-sandbox-html-js-con-sql-analogo-a-artifacts]]
