---
id: muse-wonder-admision-de-anuncios-de-modelo-sin-benchmarks
title: 'Regla de admisión: los anuncios de modelo sin benchmarks ni fuentes secundarias
  no deberían competir por cupo'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-19'
updated: '2026-10-19'
sources:
- 4004eb9d4bbe0e76
tags:
- pipeline
- admission-rule
- modelos-frontera
- brief
base_confidence: 0.55
half_life_days: 365
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: muse-wonder-singleton-rss-engagement-cero-no-sostiene-hallazgo
  type: derived_from
- to: umbral-de-contenido-minimo-antes-de-clustering
  type: relates_to
- to: ranking-openrouter-mide-consumo-no-calidad
  type: supports
---

## What it is
Un anuncio de modelo sin benchmarks, sin artefacto primario y sin fuente secundaria dentro del clúster produce una señal de mercado, no un hallazgo de práctica. Para un brief orientado a ingeniería y docencia, ese tipo de ítem debería quedar fuera del cupo operativo y registrarse como rumor de baja prioridad.

## Evidence
- El clúster de un solo documento de feed, engagement=0, novelty 0.00 y corroboración 0.50 es consistente con un anuncio no verificado por terceros — source: 4004eb9d4bbe0e76
- El propio corpus del clúster no documenta capacidades, precios, contexto ni resultados reproducibles — source: 4004eb9d4bbe0e76

## Why it matters
Fija una regla de admisión reutilizable: sin evidencia primaria ni triangulación, el anuncio no debe alimentar recomendaciones sobre agentes, estimación ni enseñanza. Evita contaminar el brief con capacidades no verificadas.

Se deriva del riesgo de singleton sin engagement. Conecta con el patrón de umbral de contenido mínimo antes de clustering y con la observación de que un ranking mide consumo, no calidad.

## Links
- derived_from → [[muse-wonder-singleton-rss-engagement-cero-no-sostiene-hallazgo]]
- relates_to → [[umbral-de-contenido-minimo-antes-de-clustering]]
- supports → [[ranking-openrouter-mide-consumo-no-calidad]]
