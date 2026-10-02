---
id: clusters-de-buzzword-compartido-no-indican-tendencia
title: Un buzzword compartido entre títulos no es una tendencia técnica
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-02'
sources:
- b5c67fa626902034
- 652b2c77b4efeb67
- 6f57359e13260d1f
- 2739eac7c4f07798
tags:
- clustering
- buzzword
- falsos-positivos
- verificacion
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: derived_from
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
---

## What it is
Cuando varios ítems de un agregador comparten una frase de titular («decision model»), el agrupamiento puede producir una «tendencia» que ningún documento sostiene por separado. La coincidencia es léxica, no semántica.

## Evidence
- Los tres ítems de «decision model» del clúster existen solo como títulos de submission, sin spec ni commit — fuentes: b5c67fa626902034, 652b2c77b4efeb67, 6f57359e13260d1f.
- Todos los ítems tienen engagement=0 y son títulos RSS sin commit, benchmark o design docs — fuente: 2739eac7c4f07798.

## Why it matters
Es un modo de fallo reusable: antes de compilar una tendencia, validar por solapamiento de contenido, no por título. Evita propagar categorías inventadas a materiales de equipo o docencia.

Se apoya en el patrón ya presente sobre validación de señal por contenido y deriva del de falsos positivos por embedding; el clúster es un caso concreto de ambos.

## Links
- derived_from → [[clustering-por-embedding-produce-falsos-positivos]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
