---
id: animating-zooming-css-titulo-sin-contenido-ingerido
title: '«Animating zooming using CSS»: título sin contenido ingerido'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-30'
sources:
- b0df1f50a76ba564
tags:
- css
- extraccion
- ingesta
- ingesta-truncada
- pipeline
- titulo-solo
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: animating-zooming-css-singleton-sin-engagement
  type: supports
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
- to: animating-zooming-css-titulo-con-documento-unico-engagement-cero
  type: supports
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: transform-order-en-css-afecta-el-zoom
  type: relates_to
---

## What it is

El clúster del signal `sig-173dfdbcdcc9` contiene un único documento cuyo contenido sustantivo no está disponible: solo se expone el título y el subtítulo del post. Cualquier lectura del contenido sería reconstrucción, no compilación.

## Evidence

- El único documento del clúster es un post RSS con engagement=0 titulado «Animating zooming using CSS: transform order is important… sometimes». — source: b0df1f50a76ba564
- El subtítulo disponible es «How to get the right transform animation.», sin más material. — source: b0df1f50a76ba564
- Métricas del signal: relevance=0.33, novelty=0.00, corroboration=0.50. — source: b0df1f50a76ba564

## Why it matters

El condicional «sometimes» del propio título sugiere que el autor matiza la regla, y sin el texto que la justifica no se puede distinguir un hallazgo técnico de una repetición de conocimiento común (novelty=0.00). Incorporar este documento como evidencia de práctica llevaría a citas vacías.

Comparte patrón con las notas que registran clústeres de un solo documento sin engagement y con el riesgo sistémico de evaluar clústeres RSS cuyo cuerpo el pipeline no recuperó. Es la nota madre de la lectura crítica de este signal.

## Links
- supports → [[animating-zooming-css-singleton-sin-engagement]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
- supports → [[animating-zooming-css-titulo-con-documento-unico-engagement-cero]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- relates_to → [[transform-order-en-css-afecta-el-zoom]]
