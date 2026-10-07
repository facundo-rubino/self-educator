---
id: concepto-precedente-identificacion-de-figuras-publicas
title: La identificación de figuras públicas por modelos multimodales no es nueva
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- 19cb8032958cd964
tags:
- estado-del-arte
- multimodal
- figuras-publicas
base_confidence: 0.75
half_life_days: 180
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
---

## What it is
La capacidad de identificar figuras públicas en imágenes — reconocimiento facial por embeddings, enlazado de entidades nombradas, grounding de descripciones — ha sido demostrada por modelos visión-lenguaje desde hace años. Lo que el documento reporta no es una capacidad nueva: es una diferencia de política entre asistentes desplegados.

## Evidence
- La puntuación de novelty del clúster es 0.00, lo que concede explícitamente que la capacidad subyacente no es nueva — source: 19cb8032958cd964

## Why it matters
Separar «capacidad presente» de «capacidad nueva» evita sobrevalorar la señal. Para enseñar o para decidir arquitectura, el eje relevante es el cumplimiento por proveedor, no la novedad de la capacidad.

Es la línea base frente a la que se lee `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`. Comparte el diagnóstico con `afirmacion-de-novedad-sin-linea-base` y con `llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia`.

## Links
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
