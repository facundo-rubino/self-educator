---
id: corroboracion-de-serie-mcp-repeticion-de-boilerplate
title: La corroboración de la serie MCP es artefacto de boilerplate repetido, no confirmación
  independiente
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- 30a26335a9988ba2
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 5a4df6bef0a4905f
tags:
- mcp
- scoring
- corroboracion
- pipeline
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: supports
- to: mcp-release-stubs-como-artefacto-de-feed
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
---

## What it is
El clúster es homogéneo por construcción (mismo origen RSS, formato templado, engagement cercano a cero). Una aparente corroboración de 0.50 es plausiblemente artefacto de repetición de boilerplate, no confirmación cruzada entre fuentes.

## Evidence
- Los ocho documentos son stubs auto-generados con identificadores estables pero mismo origen y plantilla — source: 30a26335a9988ba2, 16a4e3995d6c827e, 2221814efbefaa3b, 5a4df6bef0a4905f
- El analista reporta relevance=0.33, novelty=0.00 y engagement cero en cada ítem — source: 30a26335a9988ba2

## Why it matters
Tomar repetición de plantilla como corroboración inflaría la confianza en un clúster que no tiene acuerdo independiente. Es un modo de fallo del scorer, no una propiedad del corpus.

Refuerza `corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente` y `corroboracion-y-velocidad-como-artefactos-del-scorer`. Se relaciona con `mcp-release-stubs-como-artefacto-de-feed` porque ambos describen el mismo origen homogéneo.

## Links
- supports → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- relates_to → [[mcp-release-stubs-como-artefacto-de-feed]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
