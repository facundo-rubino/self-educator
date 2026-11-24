---
id: datasette-agent-0-7a1-panel-iframe-y-fragment-hashes
title: 'datasette-agent 0.7a1: panel lateral iframe y navegación por fragment hashes
  para otros plugins'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-24'
updated: '2026-11-24'
sources:
- 9091e8f0745b1341
tags:
- datasette
- plugins
- interfaces
- willison
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-11-24'
provenance:
  scale: S
  query: null
links:
- to: datasette-charts-0-2a0-integracion-con-datasette-agent
  type: relates_to
- to: datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes
  type: relates_to
---

## What it is
datasette-agent 0.7a1 mejora la navegación por fragment hashes y permite abrir un panel lateral iframe que navega a distintas páginas. El objetivo declarado es integrarse con otros plugins que actualizan fragment hashes al cambiar de estado.

## Evidence
- datasette-agent 0.7a1 mejora la navegación por fragment hashes y permite abrir un panel lateral iframe que navega a distintas páginas — source: 9091e8f0745b1341
- El propósito es integrarse con plugins que actualizan fragment hashes al cambiar de estado — source: 9091e8f0745b1341

## Why it matters
Es un caso de trabajo de integración entre plugins donde el coste real está en el estado compartido y la sincronización de URL, no en la generación de feature. No hay medida de que un agente haya hecho esto más rápido: es un release note de mejora menor.

Se relaciona con la integración de charts y con la nota sobre datasette-apps 0.4a0 que también usa fragmentos de URL (datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes). Juntas apuntan a un patrón de interfaces de estado en Datasette, pero sin evidencia de que sea hallazgo del clúster.

## Links
- relates_to → [[datasette-charts-0-2a0-integracion-con-datasette-agent]]
- relates_to → [[datasette-apps-0-4a0-enlace-por-fragmentos-y-schemes]]
