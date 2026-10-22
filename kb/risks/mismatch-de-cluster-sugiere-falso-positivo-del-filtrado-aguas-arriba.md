---
id: mismatch-de-cluster-sugiere-falso-positivo-del-filtrado-aguas-arriba
title: El mismatch de clúster apunta a un falso positivo del filtrado aguas arriba
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- sig-b90d2e50ef10
tags:
- pipeline
- filtro-lexico
- falso-positivo
base_confidence: 0.45
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: mismatch-de-topico-no-es-hallazgo-empirico
  type: supports
- to: cluster-php-security-heterogeneo-mismatch-de-topico
  type: derived_from
- to: clusters-de-buzzword-compartido-no-indican-tendencia
  type: relates_to
---

## What it is
El desajuste sugiere que el filtrado/keyword mapping aguas arriba está produciendo clústeres falsos positivos respecto al brief: el título anuncia un tema y los documentos no lo contienen. El riego asociado es leer documentos no relacionados como evidencia tópica y producir síntesis fabricada.

## Evidence
- La implicación del análisis es que el filtrado aguas arriba produce falsos positivos relativos al brief — source: sig-b90d2e50ef10
- Riesgo de sobre-leer documentos no relacionados como evidencia tópica y fabricar síntesis — source: sig-b90d2e50ef10
- Riesgo de que el clúster esté estancado o mal unido (título ausente) — source: sig-b90d2e50ef10

## Why it matters
Es la parte del reporte con valor operativo: señala un fallo de pipeline, no un hallazgo sobre el tema. Justifica re-agrupar o descartar.

Se apoya en la observación de que el mismatch no es un hallazgo empírico. Se relaciona con el patrón de que un buzzword compartido no indica tendencia.

## Links
- supports → [[mismatch-de-topico-no-es-hallazgo-empirico]]
- derived_from → [[cluster-php-security-heterogeneo-mismatch-de-topico]]
- relates_to → [[clusters-de-buzzword-compartido-no-indican-tendencia]]
