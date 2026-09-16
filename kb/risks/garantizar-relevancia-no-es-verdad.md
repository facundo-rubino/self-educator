---
id: garantizar-relevancia-no-es-verdad
title: Un clúster relevante no por ello contiene afirmaciones verdaderas
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
- epistemologia
- pipeline
- relevancia
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-no-es-verdad
  type: relates_to
- to: clustering-por-embedding-produce-falsos-positivos
  type: derived_from
---

## What it is
Este clúster es un falso positivo por defecto: irrelevante al brief. El riesgo simétrico es el opuesto: que un clúster sí relevante se trate como si su contenido fuese verificado por el mero hecho de pertenecer al brief. En ambos sentidos, la pertenencia temática no es un criterio de validez.

## Evidence
- Se advierte de no inflar artificialmente la relevancia por asociación vaga con «software engineering», sesgando el ranking de futuros clústeres — source: 29e59ab83043dfa3
- Se advierte de no sobreinterpretar el clúster como evidencia de que el autor del brief también escribe sobre React, cuando el documento no es suyo ni trata el tema del brief — source: 29e59ab83043dfa3

## Why it matters
El filtro de relevancia decide qué entra al pipeline, no qué es cierto dentro de él. Confundir ambos niveles produce tanto ruido admitido como conclusiones no ganadas en material admitido. La disciplina es mantener separados los dos criterios en cada etapa.

Se relaciona con `relevancia-no-es-verdad`, que ya fija que utilidad no es evidencia. Se deriva de `clustering-por-embedding-produce-falsos-positivos`, que documenta el fallo de filtrado del que este riesgo es la cara complementaria.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- derived_from → [[clustering-por-embedding-produce-falsos-positivos]]
