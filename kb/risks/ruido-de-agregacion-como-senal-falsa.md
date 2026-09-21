---
id: ruido-de-agregacion-como-senal-falsa
title: El ruido de agregación puede presentarse como señal
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- sig-9f3c75dfc038
tags:
- pipeline
- senal
- agregacion
- rss
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: cluster-precios-suben-incoherente-sin-cuerpo
  type: derived_from
- to: garantizar-relevancia-no-es-verdad
  type: relates_to
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
El caso «How it feels watching prices go up» muestra que una coincidencia léxica entre títulos de un feed puede promoverse a «señal» sin ningún hallazgo semántico detrás. La etiqueta se infiere de los títulos y luego se usa para caracterizar el clúster, lo que hace el argumento circular.

## Evidence
- Confianza inicial del analista 0.05 y ajustada a 0.02 por el crítico — source: sig-9f3c75dfc038
- El crítico califica el caso como ruido de agregación disfrazado de insight, con evidencia circular y delgada — source: sig-9f3c75dfc038

## Why it matters
Un mecanismo de promoción que no exige solapamiento sustantivo inyecta ruido en la base de conocimiento con contenido ajeno a los temas del brief. La mitigación concreta es imponer un mínimo de términos compartidos antes de promover un clúster.

Deriva del caso concreto del clúster de precios. Se relaciona con las notas que separan utilidad de verdad y con la que advierte que un clúster relevante no por ello contiene afirmaciones verdaderas.

## Links
- derived_from → [[cluster-precios-suben-incoherente-sin-cuerpo]]
- relates_to → [[garantizar-relevancia-no-es-verdad]]
- relates_to → [[relevancia-no-es-verdad]]
