---
id: datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes
title: 'datasette-apps 0.4a0: enlace por fragmentos de URL y reporte de schemes al
  agente'
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
- release-notes
- alpha
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-11-16'
provenance:
  scale: S
  query: null
links:
- to: datasette-apps-sandbox-html-js-con-sql-analogo-a-artifacts
  type: relates_to
- to: datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage
  type: relates_to
- to: datasette-apps-0-4a0-alpha-inestable-sin-evidencia-de-uso
  type: relates_to
---

## What it is
datasette-apps 0.4a0 añade soporte de enlace: una app puede enlazarse con `#fragments` en la URL, leer y usar esos fragmentos, y reportar los schemes de URL soportados de vuelta a Datasette Agent.

## Evidence
- 0.4a0 añade linking: una app se enlaza con `#fragments`, los lee y los usa, y reporta los schemes de URL soportados a Datasette Agent — source: 34ebd7c4756f64e9

## Why it matters
Es la plomería mínima para que un agente genere o haga deep-link a una app con estado preservado. Superficie pequeña, cambio concreto de release, no una tesis.

Se relaciona con la definición de datasette-apps como sandbox HTML/JS con SQL (misma fuente) y con el release paralelo de datasette-agent 0.6a0, que expone el prompt del agente en la homepage. La conexión entre ambos es de vocabulario (`hash`/`fragment`) y de namespace (`datasette`), no de mecanismo compartido demostrado.

## Links
- relates_to → [[datasette-apps-sandbox-html-js-con-sql-analogo-a-artifacts]]
- relates_to → [[datasette-agent-0-6a0-fixes-acumulados-y-prompt-en-homepage]]
- relates_to → [[datasette-apps-0-4a0-alpha-inestable-sin-evidencia-de-uso]]
