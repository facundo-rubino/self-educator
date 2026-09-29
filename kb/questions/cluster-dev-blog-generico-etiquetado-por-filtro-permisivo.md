---
id: cluster-dev-blog-generico-etiquetado-por-filtro-permisivo
title: Un clúster de RSS genérico sobrevive al filtro por relevancia baja y novedad
  nula
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- sig-c718e5611ff4
tags:
- pipeline
- ingesta
- relevance
- novelty
- rss
- falso-positivo
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
  type: relates_to
- to: cluster-heterogeneo-como-vertedero-de-firehose
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: relates_to
---

## What it is
Un clúster con relevance=0.20, novelty=0.00 y corroboration=1.00 agrupó 20 documentos sin campo semántico común, lo que sugiere que el filtro determinista los retuvo por palabras clave de «blog de desarrollo» y no por semántica del tema [sig-c718e5611ff4].

## Evidence
- relevance=0.20 y novelty=0.00 coinciden con ítems que matchean keywords amplias de blog de desarrollo en lugar de semántica del topic — source: sig-c718e5611ff4
- corroboration=1.00 reflejaría la representación amplia de contenido dev-blog en el feed, no confirmación entre fuentes independientes — source: sig-c718e5611ff4

## Why it matters
Si el filtro no se ajusta, las etapas aguas abajo consumirán capacidad de análisis en ítems de CSS y JSON ajenos al brief. ¿Qué umbral convierte relevance baja + novelty nula en descarte automático?

Es el mismo modo de fallo que documenta `corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching`; comparte con `cluster-heterogeneo-como-vertedero-de-firehose` el síntoma de agrupar sin campo semántico común; y con `mismatch-query-tema-por-vocabulario-generico-de-infraestructura` la causa de matching por vocabulario genérico.

## Links
- relates_to → [[corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching]]
- relates_to → [[cluster-heterogeneo-como-vertedero-de-firehose]]
- relates_to → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
