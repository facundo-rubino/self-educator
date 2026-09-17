---
id: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
title: El pipeline evalúa clústeres RSS cuyo cuerpo no recuperó
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- sig-fade19e1d50a
- dec9f3cc9a87f904
tags:
- pipeline
- rss
- ingesta
- evaluacion
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: react-for-two-computers-titulo-sin-contenido-ingerido
  type: derived_from
- to: mcp-release-stubs-como-artefacto-de-feed
  type: relates_to
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
---

## What it is
El caso sugiere que la etapa de evaluación puntúa clústeres construidos sobre ítems RSS cuyo contenido no fue capturado: el sistema asigna relevance 0.33, novelty 0.00, corroboration 0.50 y engagement 0 a un documento del que solo tiene el título y una frase. Puntuar así produce métricas sobre la forma del feed, no sobre el tema.

## Evidence
- El clúster contiene un documento sin contenido sustantivo recuperado más allá del título y «Two things, one origin», y aun así recibe relevance/novedad/corroboración numéricas — source: sig-fade19e1d50a / dec9f3cc9a87f904
- El analista atribuye el artefacto a que «probablemente un post o episodio […] cuyo cuerpo no fue capturado» — source: sig-fade19e1d50a

## Why it matters
Si el cuerpo no se recuperó, ninguna puntuación aguas abajo es interpretable: novelty 0.00 puede significar «sin contenido», no «sin novedad». Antes de descartar la fuente completa conviene arreglar la captura; de lo contrario el mismo título volverá a aparecer con métricas igualmente vacías.

Deriva directamente de `react-for-two-computers-titulo-sin-contenido-ingerido`. Es el mismo mecanismo de `mcp-release-stubs-como-artefacto-de-feed`: los metadatos del feed se leen como si fueran el contenido. Se relaciona con `afirmacion-de-novedad-sin-linea-base`, porque un novelty calculado sobre texto ausente no tiene línea base que lo sostenga.

## Links
- derived_from → [[react-for-two-computers-titulo-sin-contenido-ingerido]]
- relates_to → [[mcp-release-stubs-como-artefacto-de-feed]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
