---
id: scoring-novelty-cero-corroboration-uno-contradictorio
title: 'novelty=0.00 con corroboration=1.00: score interno contradictorio'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- sig-49787d554595
tags:
- scoring
- pipeline
- metricas
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
---

## What it is
El score del clúster «Gemini 3.8 TTS Playground» es internamente contradictorio: novelty=0.00 junto a corroboration=1.00 y relevance=0.20 [sig-49787d554595]. El crítico lo marca como no probativo: una corroboración perfecta con novedad nula señala solapamiento de fuente (duplicación), no confirmación independiente.

## Evidence
- El informe reporta novelty=0.00, relevance=0.20, corroboration=1.00 para el clúster — source: sig-49787d554595
- El informe advierte que corroboration=1.00 con novelty=0.00 es red flag de feed-source overlap, no confirmación independiente — source: sig-49787d554595
- El crítico califica el scoring de contradictorio y no probativo — source: sig-49787d554595

## Why it matters
Un score así no puede usarse como evidencia de calidad ni de consenso: la corroboración alta proviene de la duplicación de ítems del mismo feed, no de fuentes independientes. Tratar corroboration=1.00 como señal positiva amplificaría ruido de agregación.

Refuerza la nota previa sobre corroboración por repetición de serie como no-validación independiente. Confirma el patrón de corroboración y velocidad como artefactos del scorer.

## Links
- supports → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
