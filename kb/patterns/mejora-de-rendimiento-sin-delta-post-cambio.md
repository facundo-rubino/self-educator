---
id: mejora-de-rendimiento-sin-delta-post-cambio
title: Una afirmación de mejora de rendimiento sin «after» cuantificado no es un resultado
  establecido
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 481d2653708680a1
tags:
- benchmarking
- evidencia
- infraestructura
- metodología
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: vulkan-int8-coopmat1-matmul-rdna3-rdna4
  type: derived_from
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
---

## What it is
Cuando un documento publica un baseline «before» medido y una afirmación verbal de mejora («massive performance improvement») pero el estado «after» está truncado o ausente, no existe delta cuantificado. El resultado no es un hallazgo: es una promesa de mejora con evidencia unilateral.

## Evidence
- El documento afirma mejora masiva de rendimiento, pero la tabla solo contiene valores «before» y se corta tras pp512 — source: 481d2653708680a1
- El único valor completo visible es pp512 = 3410.53 ± 22.72 t/s (baseline), sin contraparte «after» — source: 481d2653708680a1

## Why it matters
El formato before/after es el patrón correcto para justificar una optimización; publicar solo el before convierte la afirmación en no verificable. Aplicado al oficio: una descripción de PR escrita por el proponente del cambio no es medición independiente.

Se deriva del caso `vulkan-int8-coopmat1-matmul-rdna3-rdna4`. Es pariente del modo de fallo ya registrado en `afirmacion-de-capacidad-desde-fragmento-de-una-linea` y de `afirmacion-de-novedad-sin-linea-base`: en los tres casos la afirmación excede lo que el cuerpo ingerido sostiene.

## Links
- derived_from → [[vulkan-int8-coopmat1-matmul-rdna3-rdna4]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
