---
id: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
title: 'Un clúster con relevance=0.00 sobrevive al filtrado determinista: fallo de
  precisión del pipeline'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 17812b444cd34df2
tags:
- pipeline
- filtrado
- precision
- ingesta
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: black-and-white-archive-photos-cluster-sin-senal
  type: derived_from
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
---

## What it is
Un clúster con `relevance` puntuada en 0.00 y todas las demás dimensiones (novelty, corroboration, velocity, surprise) en o cerca de 0.50 llegó a la fase de análisis sin ser descartado. Un filtrado determinista cuyo propósito es suprimir ruido dejó pasar un caso con la métrica de relevancia en su mínimo y el resto indistinguible del azar, lo que apunta a un problema de precisión en el pipeline de ingesta o de clustering, no a un hallazgo de contenido.

## Evidence
- El clúster reporta relevance=0.00, novelty=0.48, corroboration=0.50, velocity=0.50, surprise=0.50 y aun así fue procesado hasta el estadio de análisis — source: 17812b444cd34df2
- El documento único es un ítem RSS con engagement=0 y contenido de una sola frase sin relación con el tema declarado del clúster — source: 17812b444cd34df2

## Why it matters
Si esto es puntual, el coste es un clúster desperdiciado. Si es sistémico, diluye el brief y consume capacidad de análisis en documentos sin relación con el tema. La acción correctiva no es reclasificar este ítem concreto sino auditar el umbral de relevancia del filtrado determinista y su interacción con el clustering.

Deriva directamente de `black-and-white-archive-photos-cluster-sin-senal`, que es el caso concreto. Refuerza `clustering-por-embedding-produce-falsos-positivos`. Contradice parcialmente `relevancia-tematica-baja-no-es-ruido`: si bien relevancia baja puede coexistir con señal, aquí relevance=0.00 con todas las demás dimensiones en el azar indica que el descarte habría sido correcto y no perdió señal alguna.

## Links
- derived_from → [[black-and-white-archive-photos-cluster-sin-senal]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
