---
id: ausencia-de-datos-temporales-y-engagement-limita-inferencia
title: Engagement en cero y ausencia de fechas impiden inferencia de impacto
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
- ingesta
- metricas
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: senal-jev-system-one-sin-documento-de-soporte
  type: relates_to
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
- to: hy3-fuente-primaria-y-metodologia-ausentes
  type: relates_to
---

## What it is
Todos los documentos del clúster tienen engagement=0 y ninguno trae fechas, lo que anula cualquier inferencia temporal o de impacto. Es un artefacto de ingesta, no una propiedad del tema.

## Evidence
- «Ingestion-time artifacts (engagement=0 across all docs, no dates) limit any temporal or impact inference» — source: sig-450e39a1cef2
- Los riesgos listados incluyen «no dates» como limitación explícita de la inferencia — source: sig-450e39a1cef2

## Why it matters
Sin fechas no hay velocidad, orden de aparición ni relación causal entre ítems; sin engagement no hay jerarquía de relevancia dentro del clúster. Cualquier puntuación de velocity calculada sobre este corpus es sospechosa por construcción.

Refuerza el caso «Jev / System One»: explica por qué metrics como velocity=0.50 no pueden tomarse al pie de la letra en este corpus. Comparte con «ingesta-truncada-como-riesgo-sistemico-de-cobertura» la idea de que los límites de la ingesta se leen como propiedades del tema, y con «hy3-fuente-primaria-y-metodologia-ausentes» la ausencia de metadatos que permitirían verificar.

## Links
- relates_to → [[senal-jev-system-one-sin-documento-de-soporte]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
