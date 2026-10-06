---
id: react-for-two-computers-pasa-filtro-determinista-con-cuerpo-vacio
title: Un ítem con novelty 0.00 y cuerpo vacío pasa el filtro determinista
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-06'
sources:
- dec9f3cc9a87f904
tags:
- falso-positivo
- falsos-positivos
- filtrado
- filtro-determinista
- ingesta-truncada
- pipeline
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: relates_to
- to: react-for-two-computers-singleton-engagement-cero
  type: derived_from
- to: react-for-two-computers-titulo-sin-contenido-ingerido-2
  type: derived_from
- to: umbral-de-contenido-minimo-antes-de-clustering
  type: contradicts
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: supports
- to: titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters
  type: relates_to
---

## What it is
El clúster «React for Two Computers» llegó a la etapa de análisis con novelty=0.00, relevance=0.33 y un único documento sin cuerpo, lo que sugiere que los umbrales actuales del filtro determinista admiten registros casi vacíos.

## Evidence
- El clúster contiene un solo documento sin cuerpo ingerido, con novelty=0.00 — source: dec9f3cc9a87f904.
- El registro sobrevive al filtrado pese a tener un único documento y engagement=0 — source: dec9f3cc9a87f904.
- El analista y el crítico del propio informe señalan que el documento no habría pasado un filtro determinista más estricto — source: dec9f3cc9a87f904.

## Why it matters
Si el pipeline evalúa clústeres sin recuperar primero el cuerpo, consume cupo de análisis sobre artefactos vacíos. La consecuencia operativa es un umbral de contenido mínimo antes de agrupar, no después.

Deriva de `react-for-two-computers-titulo-sin-contenido-ingerido-2` (el registro vacío es la premisa). Contradice el patrón `umbral-de-contenido-minimo-antes-de-clustering`: este caso muestra que el umbral no se está aplicando o no existe en esta ruta. Refuerza `ingesta-truncada-como-riesgo-sistemico-de-cobertura` y se relaciona con `relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista` y `titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters`.

## Links
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- relates_to → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
- derived_from → [[react-for-two-computers-singleton-engagement-cero]]
- derived_from → [[react-for-two-computers-titulo-sin-contenido-ingerido-2]]
- contradicts → [[umbral-de-contenido-minimo-antes-de-clustering]]
- supports → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
- relates_to → [[titulo-solo-como-artefacto-de-ingesta-infla-conteo-de-clusters]]
