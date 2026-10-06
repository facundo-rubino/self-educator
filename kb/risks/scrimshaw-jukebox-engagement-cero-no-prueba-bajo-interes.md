---
id: scrimshaw-jukebox-engagement-cero-no-prueba-bajo-interes
title: Engagement cero en un clúster RSS no prueba bajo interés
type: risk
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
- engagement
- inferencia
- ausencia-de-evidencia
- rss
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo
  type: supports
- to: ausencia-de-datos-temporales-y-engagement-limita-inferencia
  type: supports
- to: scrimshaw-jukebox-cluster-heterogeneo-rss-sin-hilo-conductor
  type: relates_to
---

## What it is
El análisis del clúster «Scrimshaw Jukebox» infiere bajo interés de los documentos a partir de que su engagement es 0. Esa inferencia es un argumento ex silentio: la ausencia de interacción registrada no es evidencia de que el contenido sea de bajo interés ni de baja calidad.

## Evidence
- El clúster declara documentos etiquetados `rss` sin interacción (engagement=0) — source: sig-47b9ce860e32
- El crítico señala que se infiere bajo interés desde cero engagement, lo cual es ausencia de evidencia — source: sig-47b9ce860e32

## Why it matters
Usar engagement como proxy de interés convierte un dato de plataforma en un juicio de valor sobre el contenido. Si el pipeline descarta clústeres por engagement cero, puede estar descartando señal real por un artefacto de medición.

Conecta con el patrón de que la ausencia de conexión con el brief es artefacto de muestreo y con el riesgo ya registrado de que engagement en cero y ausencia de fechas impiden inferir impacto. Ambos apuntan a la misma dirección: no leer ausencia como evidencia.

## Links
- supports → [[ausencia-de-conexion-con-el-brief-es-artefacto-de-muestreo]]
- supports → [[ausencia-de-datos-temporales-y-engagement-limita-inferencia]]
- relates_to → [[scrimshaw-jukebox-cluster-heterogeneo-rss-sin-hilo-conductor]]
