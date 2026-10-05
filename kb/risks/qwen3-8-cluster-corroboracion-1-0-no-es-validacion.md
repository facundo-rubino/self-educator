---
id: qwen3-8-cluster-corroboracion-1-0-no-es-validacion
title: 'corroboration=1.00 en el clúster «Qwen3.8 27B»: ingests casi duplicados, no
  confirmación independiente'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- sig-795d5eab7806
tags:
- metricas
- scorer
- corroboracion
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: corroboration-1-00-con-relevance-0-20-metrica-degenerada
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
---

## What it is
La corroboración de 1.00 declarada para este clúster es engañosa: probablemente refleja múltiples ingests de baja calidad casi duplicados, no confirmación independiente de una misma afirmación. relevance=0.20 y novelty=0.00 ya indican bajo valor.

## Evidence
- La corroboración de 1.00 probablemente refleja ingests casi duplicados, no confirmación independiente — fuente: sig-795d5eab7806
- relevance=0.20 y novelty=0.00 indican bajo valor de la señal — fuente: sig-795d5eab7806
- Tratar este clúster como señal real arriesga fabricar un hallazgo a partir de ruido — fuente: sig-795d5eab7806

## Why it matters
La métrica de corroboración no es usable como validación aquí. Cualquier scorer que la consuma debe cruzarla con relevance y novelty antes de tratar un clúster como confirmado.

Añade una instancia concreta al patrón de corroboración degenerada con relevance baja y al de métricas como artefactos del scorer, no como evidencia.

## Links
- supports → [[corroboration-1-00-con-relevance-0-20-metrica-degenerada]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
