---
id: post-css-sin-engagement-y-relevancia-tangencial-al-brief
title: Un singleton de CSS con engagement=0 y relevance=0.33 es ruido para el brief
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
- b0df1f50a76ba564
tags:
- pipeline
- filtrado
- relevancia
- brief
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
- to: single-document-cluster-engagement-cero-no-generaliza
  type: supports
- to: mecanica-css-afirmada-desde-solo-titulo-rss
  type: supports
---

## What it is
El clúster de la señal está formado por un único documento de feed RSS con engagement=0, novelty=0.00 y relevance=0.33 respecto de un brief centrado en liderazgo técnico, agentes de IA aplicados a programar y oficio de software engineering. La nota técnica de CSS es tangencial al brief y no tiene corroboración.

## Evidence
- Documento único con engagement=0 — source: b0df1f50a76ba564
- relevance=0.33, novelty=0.00, corroboration=0.50 en la señal — source: b0df1f50a76ba564

## Why it matters
Si el pipeline conservó este ítem, conviene revisar la regla de filtrado: un post de CSS sobre `transform order` difícilmente mapea a los ejes del brief más allá de la vaga etiqueta de «oficio de software engineering». Tratarlo como hallazgo relevante sesga el reporte hacia ruido.

Se apoya en el riesgo de generalizar desde un clúster de un solo documento sin engagement. Se relaciona con la idea de que la baja relevancia temática no equivale automáticamente a ausencia de señal, pero aquí la falta de corroboración sí limita el valor.

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- supports → [[single-document-cluster-engagement-cero-no-generaliza]]
- supports → [[mecanica-css-afirmada-desde-solo-titulo-rss]]
