---
id: release-2026-8-31-cluster-falso-positivo-del-filtro
title: El clúster del release 2026.8.31 entró al brief por boilerplate compartido,
  no por relevancia semántica
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- 30a26335a9988ba2
- 9750590bbfe6b285
- 5a4df6bef0a4905f
- ffbd76916d1dfdc5
- 748f8b0a02cd7524
- b9106690f5dfd849
tags:
- mcp
- clustering
- falso-positivo
- pipeline
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: release-2026-8-31-bumps-mcp-sin-changelog
  type: derived_from
- to: release-2026-8-31-falso-positivo-por-vocabulario-mcp-agentes
  type: supports
- to: release-2026-8-31-relevance-baja-novelty-cero
  type: supports
- to: mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo
  type: supports
---

## What it is
Los títulos y listas de paquetes comparten vocabulario y plantilla, lo que basta para agrupar los seis ítems como clúster. Los propios scores del pipeline (novelty=0.00, relevance=0.33) indican ausencia de novedad y relevancia baja, pero usarlos como validación independiente es circular: son salida del mismo filtro que dejó pasar el ruido.

## Evidence
- Los seis documentos comparten plantilla de release con versión de calendario y lista de paquetes — source: 30a26335a9988ba2, 9750590bbfe6b285, 5a4df6bef0a4905f, ffbd76916d1dfdc5, 748f8b0a02cd7524, b9106690f5dfd849

## Why it matters
Un clúster de release notes templadas no debe presentarse como señal sobre el brief. El filtro determinista debería descartar o infravalorar feeds de bumps de versión antes de agrupar, no surfacingarlos como tema.

Es la cara de pipeline del mismo hecho descrito en la nota de bumps. Refuerza riesgos ya registrados sobre falsos positivos por vocabulario y sobre novelty/relevance como artefactos del scorer.

## Links
- derived_from → [[release-2026-8-31-bumps-mcp-sin-changelog]]
- supports → [[release-2026-8-31-falso-positivo-por-vocabulario-mcp-agentes]]
- supports → [[release-2026-8-31-relevance-baja-novelty-cero]]
- supports → [[mcp-feed-releases-ruido-para-brief-de-agentes-y-liderazgo]]
