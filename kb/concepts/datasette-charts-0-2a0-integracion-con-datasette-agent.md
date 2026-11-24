---
id: datasette-charts-0-2a0-integracion-con-datasette-agent
title: datasette-charts 0.2a0 integra charting con Datasette Agent reusando las mismas
  herramientas
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
- 27878e595eaaf299
tags:
- datasette
- plugins
- agentes-de-codigo
- willison
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-11-24'
provenance:
  scale: S
  query: null
links:
- to: datasette-charts-0-2a0-prototipo-con-agente-a-plugin
  type: derived_from
---

## What it is
Al día siguiente del lanzamiento del plugin, datasette-charts 0.2a0 ganó integración con Datasette Agent: se le puede pedir un gráfico al chat y el agente lo genera usando las mismas herramientas subyacentes de sugerencia y generación de charts. Hay un demo grabado en agent.datasette.io con login vía GitHub.

## Evidence
- datasette-charts 0.2a0 añade integración con Datasette Agent: pedir un gráfico en el chat lo genera con las mismas herramientas de sugerencia y generación — source: 27878e595eaaf299
- Demo grabado en agent.datasette.io con login por GitHub — source: 27878e595eaaf299

## Why it matters
El claim implícito es que la integración no reescribió el charting: reutilizó las mismas herramientas de generación, cambiando solo la superficie de invocación (UI vs chat). Eso apunta a que el criterio humano se desplaza hacia el diseño de APIs/herramientas compartidas, no hacia el código de la feature. Es una observación de release note, no una medición.

Deriva del prototipo (datasette-charts-0-2a0-prototipo-con-agente-a-plugin): sin plugin base no hay herramientas reutilizables para el agente. Refuerza la idea de que la ventaja se juega en la interfaz entre componentes, no en el código inicial.

## Links
- derived_from → [[datasette-charts-0-2a0-prototipo-con-agente-a-plugin]]
