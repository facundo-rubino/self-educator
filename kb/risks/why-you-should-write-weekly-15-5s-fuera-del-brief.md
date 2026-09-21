---
id: why-you-should-write-weekly-15-5s-fuera-del-brief
title: '«Why You Should Write Weekly 15-5s»: relevance=0.00 frente al brief'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- f301b379af549017
tags:
- pipeline
- filtrado
- relevancia
- muestreo
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-no-es-verdad
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo
  type: contradicts
---

## What it is
El clúster puntúa 0.00 de relevancia contra el topic declarado (agentes de IA para programar/gestionar/enseñar, liderazgo técnico, oficio de ingeniería, productividad y técnicas de estudio). El único vínculo plausible es léxico: el topic lista «productividad» y «organización personal», y el documento trata un hábito semanal de documentación personal. Ese puente es vocabulario compartido, no sustancia compartida.

## Evidence
- El clúster tiene un único documento y puntúa relevance=0.00 contra el topic — source: f301b379af549017
- El documento es un post corto sobre un hábito de documentación personal, no sobre agentes de IA, liderazgo técnico ni oficio de ingeniería — source: f301b379af549017

## Why it matters
Una palabra de productividad en la lista del topic no vuelve relevante cualquier post arbitrario de productividad: si lo hiciera, el topic absorbería desde higiene del sueño hasta bullet journaling. Este caso sugiere que la etapa de ingesta/filtrado admite ítems off-brief vía vocabulario genérico de productividad. Tratarlo como hallazgo contaminaría el brief con contenido ajeno.

Se apoya en `mismatch-query-tema-por-vocabulario-generico-de-infraestructura`: el matching por vocabulario genérico admite ítems fuera del tema. Se relaciona con `relevancia-no-es-verdad`: la relevancia temática no valida afirmaciones. A la vez, contradice parcialmente a `ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo`, porque aquí la desconexión no parece artefacto de muestreo sino coincidencia léxica en la consulta del topic.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- contradicts → [[ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo]]
