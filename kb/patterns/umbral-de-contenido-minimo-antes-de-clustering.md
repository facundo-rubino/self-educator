---
id: umbral-de-contenido-minimo-antes-de-clustering
title: 'Umbral de contenido mínimo: descartar antes de agrupar, no después'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- dec9f3cc9a87f904
tags:
- pipeline
- filtro-determinista
- ingesta
base_confidence: 0.55
half_life_days: 365
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: riesgo-de-propagacion-de-falsos-positivos-por-titulo
  type: derived_from
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
---

## What it is
Aplicar la criba por cuerpo sustantivo antes de la fase de agrupamiento evita que documentos sin texto real lleguen a competir por cupo en clusters temáticos. El scoring posterior penaliza, pero no impide la contaminación del conjunto de candidatos.

## Evidence
- El caso [dec9f3cc9a87f904] es un cluster de un solo documento con relevance=0.33 y novelty=0.00: el score lo penaliza después de haber sido agrupado — fuente: dec9f3cc9a87f904

## Why it matters
Desplaza el coste de la limpieza a la fase más barata. Es una decisión de ingeniería de pipeline con efecto directo sobre la precisión temática del KB.

Se deriva de `riesgo-de-propagacion-de-falsos-positivos-por-titulo`. Se relaciona con `relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista` e `ingesta-truncada-como-riesgo-sistemico-de-cobertura` como instancias del mismo problema de cribado.

## Links
- derived_from → [[riesgo-de-propagacion-de-falsos-positivos-por-titulo]]
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
