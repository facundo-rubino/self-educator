---
id: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
title: El matching por vocabulario genérico de infraestructura admite ítems fuera
  del tema
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- 0419fada62f5f071
tags:
- retrieval
- clustering
- filtrado
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
---

## What it is
Un clúster con relevance=0.00 respecto del tema, admitido con un único ítem RSS cuyo título contiene vocabulario de infraestructura («static», «server»), apunta a que la recuperación está matcheando por léxico genérico y no por tópico. Es una hipótesis del análisis, no un hallazgo demostrado [0419fada62f5f071].

## Evidence
- El clúster fue puntuado con relevance=0.00 frente al tema declarado — source: 0419fada62f5f071
- El análisis sugiere que si la señal se surfaced por una query en torno a «static» o «server», el pipeline probablemente está matcheando vocabulario genérico de infraestructura antes que el tópico previsto — source: 0419fada62f5f071
- El feed RSS con engagement=0 indica que el ítem nunca fue leído ni interactuado, lo que reduce su valor probatorio — source: 0419fada62f5f071

## Why it matters
Si la admisión de ítems así continúa, diluye la calidad de recuperación del brief de liderazgo técnico y agentes. Marca un lugar donde vale revisar el filtro de admisión (query-to-topic), pero la evidencia es un solo caso y no permite cuantificar la frecuencia del fallo.

Es una instancia concreta de `clustering-por-embedding-produce-falsos-positivos`. Contradice parcialmente `relevancia-tematica-baja-no-es-ruido`: aquí el ítem con relevancia 0.00 no aporta señal al brief, aunque la contradicción es débil porque aquella nota habla de relevancia baja, no nula.

## Links
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
