---
id: corroboracion-y-velocidad-como-artefactos-del-scorer
title: Corroboración y velocidad como artefactos del scorer, no evidencia
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- sig-450e39a1cef2
tags:
- pipeline
- metricas
- scoring
- falsos-positivos
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: senal-jev-system-one-sin-documento-de-soporte
  type: supports
- to: ruido-de-agregacion-como-senal-falsa
  type: relates_to
- to: a-chain-reaction-metricas-no-son-evidencia-independiente
  type: relates_to
---

## What it is
En este clúster, corroboration=1.00 y velocity=0.50 se generan determinantemente sin anclaje a ningún documento, mientras novelty=0.00 admite explícitamente que no se encontró nada nuevo. Las dos primeras parecen confirmación; la tercera desmiente la lectura.

## Evidence
- El analyst afirma que «corroboration=1.00 and velocity=0.50 appear to be artifacts of the deterministic scorer, not evidence» — source: sig-450e39a1cef2
- El critic coincide: son «deterministic scorer outputs unmoored from any document» — source: sig-450e39a1cef2
- novelty=0.00 se declara explícitamente en la propia salida del scorer — source: sig-450e39a1cef2

## Why it matters
Si un consumidor downstream usa corroboración como filtro de admisión, este clúster lo pasa con 1.00 pese a tener cero soporte documental. La corroboración alta puede estar midiendo repetición de ítems RSS no relacionados entre sí, no confirmación mutua. Un score de novedad en 0 debería invalidar la lectura de corroboración alta, no convivir con ella.

Soporta directamente el riesgo de señal sin soporte: explica por qué la señal «Jev / System One» superó un umbral sin tener documento detrás. Es la variante de pipeline de «ruido-de-agregacion-como-senal-falsa» y comparte con «a-chain-reaction-metricas-no-son-evidencia-independiente» la idea de que las métricas del propio pipeline no cuentan como corroboración externa.

## Links
- supports → [[senal-jev-system-one-sin-documento-de-soporte]]
- relates_to → [[ruido-de-agregacion-como-senal-falsa]]
- relates_to → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
