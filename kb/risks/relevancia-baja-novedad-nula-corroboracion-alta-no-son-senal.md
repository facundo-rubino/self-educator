---
id: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
title: Relevancia baja, novedad nula y corroboración alta no constituyen señal
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
- sig-1287cec35a25
tags:
- metricas
- senal
- ruido
- auditoria
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: ruido-de-agregacion-como-senal-falsa
  type: supports
- to: cluster-heterogeneo-sin-tesis-sostenible-sobre-el-brief
  type: relates_to
---

## What it is
La combinación de relevancia muy baja (0.20), novedad nula (0.00) y corroboración alta (1.00) no implica señal: la corroboración alta puede deberse a que los documentos comparten una única fuente RSS, no a validación independiente. La novedad cero indica ausencia de información nueva.

## Evidence
- La señal tiene relevancia muy baja (0.20), novedad nula (0.00) y corroboración alta (1.00) — source: sig-1287cec35a25
- El alto valor de corroboración podría deberse a que los documentos provienen de una misma fuente RSS, no a una validación independiente del contenido — source: sig-1287cec35a25

## Why it matters
Alertar contra leer la corroboración alta como consenso. Es un modo de fallo conocido del pipeline: la métrica mide homogeneidad de fuente, no verificación. Aplicable a cualquier señal de este tipo.

Se relaciona con el riesgo ya catalogado de que el ruido de agregación se presente como señal. Complementa la auditoría del cluster heterogéneo.

## Links
- supports → [[ruido-de-agregacion-como-senal-falsa]]
- relates_to → [[cluster-heterogeneo-sin-tesis-sostenible-sobre-el-brief]]
