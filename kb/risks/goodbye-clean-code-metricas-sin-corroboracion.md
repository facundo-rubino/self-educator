---
id: goodbye-clean-code-metricas-sin-corroboracion
title: Las métricas de «Goodbye, Clean Code» son autodescripción del pipeline
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-22'
sources:
- bc47e7115f9ba8d0
tags:
- autodescripcion
- corroboracion
- evidencia
- meta-evidencia
- metricas
- pipeline
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: a-chain-reaction-metricas-no-son-evidencia-independiente
  type: relates_to
- to: goodbye-clean-code-titulo-sin-contenido-ingerido
  type: supports
- to: goodbye-clean-code-titulo-sin-contenido-ingerido
  type: relates_to
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: relates_to
---

## What it is
Los números del clúster (novelty 0.00, corroboration 0.50, engagement 0) no son evidencia independiente sobre el tema: son la descripción del propio pipeline sobre un único ítem RSS. Una corroboración de 0.50 dentro de un clúster de un solo documento no corrobora nada, porque no hay contra qué corroborar.

## Evidence
- El documento aparece como ítem RSS con engagement=0, sin señal de lectura ni discusión — source: bc47e7115f9ba8d0
- El clúster contiene un solo documento y novelty 0.00, de modo que no está corroborado independientemente dentro de este conjunto — source: bc47e7115f9ba8d0

## Why it matters
Cualquier lectura cuantitativa de este clúster como «validado al 50%» o «con engagement medido» sería un artefacto del scorer, no un hallazgo. El único uso legítimo del clúster es como hook temático candidato a corroborar contra otras fuentes, o a descartar.

Se relaciona con `goodbye-clean-code-titulo-sin-contenido-ingerido` porque la ausencia de cuerpo es la razón de fondo. Se relaciona con `a-chain-reaction-metricas-no-son-evidencia-independiente` y con `corroboracion-y-velocidad-como-artefactos-del-scorer`, que documentan el mismo modo de fallo del pipeline.

## Links
- relates_to → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
- supports → [[goodbye-clean-code-titulo-sin-contenido-ingerido]]
- relates_to → [[goodbye-clean-code-titulo-sin-contenido-ingerido]]
- relates_to → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
