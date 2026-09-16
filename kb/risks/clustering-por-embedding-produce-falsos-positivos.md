---
id: clustering-por-embedding-produce-falsos-positivos
title: El clustering por embeddings puede producir falsos positivos temáticos
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
- 29e59ab83043dfa3
tags:
- pipeline
- clustering
- embeddings
- falsos-positivos
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: why-do-react-hooks-titulo-sin-mencion-al-brief
  type: derived_from
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: relates_to
---

## What it is
El caso del clúster [29e59ab83043dfa3] sugiere que el agrupamiento por similitud de embeddings puede hacer competir material temáticamente ajeno con el brief. Si un artículo de React entra en el mismo proceso que material de liderazgo, docencia e IA, el umbral de clustering o las señales de filtrado están mal calibrados.

## Evidence
- Si el pipeline agrupa por similitud de embeddings, este caso sugiere revisar el umbral de clustering o las señales de filtrado, porque un artículo de React no debería competir con material de liderazgo/docencia/IA — source: 29e59ab83043dfa3
- El clúster se clasifica como falso positivo respecto al brief y se recomienda que no consuma cupo analítico — source: 29e59ab83043dfa3

## Why it matters
Los falsos positivos desplazan clústeres con señal real y sesgan el ranking si se les asigna relevancia por asociación vaga. El costo no es solo el análisis desperdiciado: es la oportunidad perdida de procesar material que sí importa.

Se deriva de `why-do-react-hooks-titulo-sin-mencion-al-brief`, que establece la ausencia de mención temática. Se relaciona con `generalizacion-desde-cluster-de-un-solo-documento`: el otro eje del mismo fallo de pipeline —clúster de uno que se lee como señal consolidada.

## Links
- derived_from → [[why-do-react-hooks-titulo-sin-mencion-al-brief]]
- relates_to → [[generalizacion-desde-cluster-de-un-solo-documento]]
