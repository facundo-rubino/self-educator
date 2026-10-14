---
id: redesigning-source-control-ausencia-de-evidencia-no-es-evidencia-de-ausencia
title: «La recuperación está rota» desde una muestra de ~30 documentos es un sobrealcance
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-14'
updated: '2026-10-14'
sources:
- sig-7ffae862f68c
tags:
- retrieval
- inferencia
- corpus-muestreado
- pipeline
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: argumento-ex-silentio-en-corpus-truncado
  type: supports
- to: ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo
  type: supports
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: relates_to
---

## What it is
La conclusión de que «el retriever o el etiquetado están fallando» no se sigue de una muestra delgada de ~30 documentos de un feed RSS heterogéneo y no curado. La ausencia de material sobre source control en el clúster no demuestra que no exista en el corpus mayor.

## Evidence
- El crítico sostiene que la muestra es delgada, ruidosa y no curada, y que inferir «retrieval is broken» es un sobrealcance — source: sig-7ffae862f68c.
- El propio analista describe el clúster como «generic RSS firehose» con ~30 documentos, sin afirmar que sea exhaustivo — source: sig-7ffae862f68c.

## Why it matters
Evita que el diagnóstico de pipeline se compile como hallazgo firme. El paso correcto es verificar contra el corpus completo, no concluir desde este clúster. Afecta a cómo se cita este caso en cualquier nota sobre calidad de la ingesta.

Es una instancia directa de `argumento-ex-silentio-en-corpus-truncado`. Coincide con `ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo`: la falta de conexión observada es del muestreo, no del mundo. Y se relaciona con `pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss`, que describe el modo de fallo hermano.

## Links
- supports → [[argumento-ex-silentio-en-corpus-truncado]]
- supports → [[ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo]]
- relates_to → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
