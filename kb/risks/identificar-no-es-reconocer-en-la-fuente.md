---
id: identificar-no-es-reconocer-en-la-fuente
title: «Identificar» en la fuente significa «no rechazar», no «reconocer»
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-25'
sources:
- 19cb8032958cd964
tags:
- ambiguedad-lexica
- claims
- definiciones
- llm
- metodologia
- multimodal
- rechazo
base_confidence: 0.12
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: M
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: contradicts
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: identificacion-de-figuras-publicas-ya-existia
  type: derived_from
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
---

## What it is
«Identificar una figura pública en una imagen» es ambiguo y admite al menos tres lecturas distintas: poner el nombre exacto, producir una coincidencia facial contra una base, o dar una descripción reconocible. El documento fuente no elige ninguna, y sin esa definición la afirmación no es evaluable: no se sabe si se observó reconocimiento correcto o simplemente la ausencia de un rechazo.

## Evidence
- El documento no especifica qué se entiende por «identificar» ni en qué condiciones [19cb8032958cd964].
- Tampoco publica tasa de acierto, conjunto de prueba ni tasa de falsos positivos [19cb8032958cd964].
- El riesgo registrado en el pipeline señala explícitamente esa indefinición como impedimento para evaluar el alcance real [19cb8032958cd964].

## Why it matters
Sin operacionalizar el verbo, cualquier medición que se haga encima mide otra cosa. Antes de probar el comportamiento hay que decidir qué se contará como éxito: un nombre exacto, una coincidencia con tolerancia, o la mera no-negativa del modelo. Las tres dan números distintos para el mismo sistema.

Es consecuencia directa de `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`: como el único dato verificable es sí-rechaza / no-rechaza, la palabra «identificar» del titular solo puede sostenerse como «no rechazó». Depende de `identificacion-de-figuras-publicas-ya-existia` para el contexto de la afirmación. La autoliga registra que la ambigüedad terminológica se aplica a cualquier futura observación de este tipo, no solo a esta.

## Links
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[relevancia-no-es-verdad]]
- contradicts → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- derived_from → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
