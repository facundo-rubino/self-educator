---
id: confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido
title: 'Confianza de 0.88 sobre una tagline: miscalibración al puntuar hallazgos por
  ausencia'
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
- metodologia
- calibracion
- evals
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: garantizar-relevancia-no-es-verdad
  type: relates_to
- to: documento-unico-como-base-de-afirmacion-de-estandar
  type: relates_to
---

## What it is
El análisis inicial asignó confianza 0.88 a la afirmación de que el clúster es un «null signal», apoyándose en un único ítem cuya tagline es todo el contenido. El crítico la ajustó a 0.05 por miscalibración radical. Una afirmación sobre ausencia de contenido no puede llevar alta confianza cuando la evidencia es un solo documento sin cuerpo.

## Evidence
- El análisis declaró confianza inicial 0.88 — source: 0419fada62f5f071
- El crítico emitió veredicto WEAK y ajustó la confianza a 0.05, señalando que la confianza de 0.88 es radicalmente miscalibrada para un claim que descansa en una sola tagline con relevance=0.00 — source: 0419fada62f5f071
- La confianza final registrada del pipeline es 0.05 — source: 0419fada62f5f071

## Why it matters
Documenta un modo de fallo recurrente: la caracterización de un clúster por lo que su único miembro no dice se presenta con confianza alta porque es trivialmente cierta, pero como hallazgo de investigación no aporta nada. El ajuste del crítico es lo que preserva la calibración del grafo.

Se relaciona con `garantizar-relevancia-no-es-verdad` en el sentido de que un artefacto del pipeline (un clúster) no por existir valida una afirmación. También con `documento-unico-como-base-de-afirmacion-de-estandar`: un solo documento no sostiene afirmaciones fuertes.

## Links
- relates_to → [[garantizar-relevancia-no-es-verdad]]
- relates_to → [[documento-unico-como-base-de-afirmacion-de-estandar]]
