---
id: release-2026-8-31-relevance-baja-novelty-cero
title: 'Scoring del release 2026.8.31: novelty 0.00, relevance 0.33, corroboración
  plana 0.50'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-06'
sources:
- sig-d0acf338c3a6
tags:
- artefacto-de-ingesta
- falsos-positivos
- filtro-determinista
- mcp
- metricas
- scoring
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: cluster-rss-generico-bajo-relevance-novelty-cero
  type: supports
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: release-2026-8-31-stub-sin-changelog
  type: relates_to
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: relates_to
- to: release-2026-8-31-mcp-token-como-falso-positivo-de-filtro
  type: supports
---

## What it is
El scoring de esta señal (novelty 0.00, relevance 0.33) no es una señal débil sino una señal ausente disfrazada de puntuación baja. El crítico lo lee como corroboración independiente del resultado nulo, no como evidencia circular.

## Evidence
- El analista reporta novelty 0.00 y relevance 0.33 sobre el clúster, y el crítico acepta que estos scores corroboran el diagnóstico de ruido desde un mecanismo separado — source: sig-d0acf338c3a6
- El veredicto del crítico es «survives» con confianza ajustada 0.08, explícitamente etiquetado como null result bien soportado — source: sig-d0acf338c3a6
- La única debilidad reconocida es interpretativa: depende de juzgar que la etiqueta de tópico está «equivocada», lo que solo recorta confianza, no rescata el clúster — source: sig-d0acf338c3a6

## Why it matters
Fija un umbral operativo: novelty 0.00 con relevance baja no debe compilarse como hallazgo de práctica, aunque sobreviva al filtro determinista. Cualquier nota derivada arrastraría una confianza artificialmente inflada.

Se relaciona con `relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal` y sostiene el diagnóstico de `release-2026-8-31-mcp-token-como-falso-positivo-de-filtro`. Comparte con `corroboracion-y-velocidad-como-artefactos-del-scorer` la tesis de que las métricas internas describen el scorer, no el contenido.

## Links
- supports → [[cluster-rss-generico-bajo-relevance-novelty-cero]]
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[release-2026-8-31-stub-sin-changelog]]
- relates_to → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- supports → [[release-2026-8-31-mcp-token-como-falso-positivo-de-filtro]]
