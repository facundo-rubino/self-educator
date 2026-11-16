---
id: datasette-apps-sandbox-html-js-con-sql-analogo-a-artifacts
title: 'datasette-apps: apps HTML/JS en sandbox dentro de Datasette, análogas a Artifacts
  pero con SQL'
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
- 34ebd7c4756f64e9
tags:
- datasette
- datasette-apps
- sandbox
- artifacts
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-11-16'
provenance:
  scale: S
  query: null
links:
- to: datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes
  type: relates_to
- to: datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage
  type: relates_to
---

## What it is
Las datasette-apps son apps HTML/JS en sandbox que viven dentro de Datasette. Se describen como análogas a Claude Artifacts, pero capaces de ejecutar consultas SQL contra los datos del usuario.

## Evidence
- datasette-apps son apps HTML/JS en sandbox dentro de Datasette, análogas a Claude Artifacts pero capaces de correr consultas SQL sobre los datos del usuario — source: 34ebd7c4756f64e9

## Why it matters
Es el modelo de superficie sobre el que opera el cambio 0.4a0 (enlace por fragmentos, reporting de schemes al agente). Sin esta definición, el release no significa nada.

Es el sustrato del cambio 0.4a0 de la misma fuente, y el contrapunto de datasette-agent, que es quien recibe los schemes reportados.

## Links
- relates_to → [[datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes]]
- relates_to → [[datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage]]
