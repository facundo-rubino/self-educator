---
id: novelty-cero-y-relevance-alta-no-son-mediciones-independientes
title: 'novelty=0.00 con relevance=1.00: la «ausencia de señal» está en el encuadre,
  no medida'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-31'
updated: '2026-10-31'
sources:
- 127f90d84154dcf5
- b647bfde274dd2a1
- ee7d97417bb16595
tags:
- circularity
- scoring
- cluster-diagnosis
base_confidence: 0.65
half_life_days: 120
last_reinforced: '2026-10-31'
provenance:
  scale: S
  query: null
links:
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
- to: relevance-1-00-por-keyword-matching-no-por-ajuste-tematico
  type: relates_to
---

## What it is
El reporte presenta novelty=0.00 y relevance=1.00 como mediciones independientes, pero un clúster de topic-drift trivialmente tiene cero contenido novel para cualquier brief: «no señal» está incorporado al encuadre, no demostrado. El crítico del reporte señala esta circularidad.

## Evidence
- El crítico argumenta que novelty=0.00 y relevance=1.00 son la misma observación reformulada: un clúster de topic-drift tiene trivialmente cero contenido novel para cualquier brief — fuente: 127f90d84154dcf5, b647bfde274dd2a1, ee7d97417bb16595

## Why it matters
Diagnósticos como «artefacto de topic-drift» o «no informativo» se apoyan en scores que no son evidencia independiente. Lo honesto es registrar un resultado nulo, no una afirmación negativa fuerte.

Se relaciona con el patrón de que corroboración y velocidad son artefactos del scorer. Depende de la nota sobre relevance alta por keyword matching.

## Links
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[relevance-1-00-por-keyword-matching-no-por-ajuste-tematico]]
