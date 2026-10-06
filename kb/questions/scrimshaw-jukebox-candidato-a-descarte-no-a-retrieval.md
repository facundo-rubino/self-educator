---
id: scrimshaw-jukebox-candidato-a-descarte-no-a-retrieval
title: 'Clúster «Scrimshaw Jukebox»: candidato a descarte, no a retrieval'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-06'
sources:
- sig-47b9ce860e32
tags:
- descarte
- pipeline
- retrieval
- priorizacion
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-candidato-a-retrieval-o-descarte
  type: relates_to
- to: umbral-de-contenido-minimo-antes-de-clustering
  type: relates_to
- to: scrimshaw-jukebox-veredicto-weak-por-descripcion-tautologica
  type: derived_from
---

## What it is
Con confianza 0.10, relevance 0.20 y novelty 0.00, la pregunta abierta es si este clúster debe descartarse antes de clustering o enviarse a retrieval de texto completo. El análisis no responde si los documentos individuales contienen señal recuperable, solo que el clúster como unidad no la contiene.

## Evidence
- La confianza final del análisis es 0.10 y el crítico lo marca WEAK — source: sig-47b9ce860e32
- El analista propone no priorizar el clúster en el pipeline de investigación — source: sig-47b9ce860e32
- El analista advierte sesgo de selección: el filtro puede no haber capturado la relevancia real — source: sig-47b9ce860e32

## Why it matters
Decidir entre descartar y recuperar por documento individual es una decisión de diseño del pipeline que este caso deja abierta. Si los documentos tienen valor individual pero el clustering los mezcla, el fallo está en el agrupamiento, no en el contenido.

Se relaciona con la pregunta ya registrada sobre si un clúster es candidato a retrieval o descarte, y con el patrón de umbral de contenido mínimo antes de clustering. Deriva del veredicto WEAK: una vez reconocido el no-hallazgo, la pregunta útil es qué hacer con los documentos.

## Links
- relates_to → [[how-to-match-llm-patterns-candidato-a-retrieval-o-descarte]]
- relates_to → [[umbral-de-contenido-minimo-antes-de-clustering]]
- derived_from → [[scrimshaw-jukebox-veredicto-weak-por-descripcion-tautologica]]
