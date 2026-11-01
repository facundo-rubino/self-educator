---
id: finedna-receta-tres-etapas-midtraining-sft-rl
title: 'Receta de tres etapas: midtraining de dominio, SFT y RL con recompensa verificable'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-01'
updated: '2026-11-01'
sources:
- 5f7f86aa64f4ba64
tags:
- fine-tuning
- curriculum
- reproducibility
- handoff
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-11-01'
provenance:
  scale: S
  query: null
links:
- to: finedna-dataset-announcement-single-source
  type: derived_from
- to: finedna-receta-abierta-como-patron-de-handoff-reproducible
  type: relates_to
---

## What it is
FineDNA estructura el entrenamiento de competencia de dominio en tres etapas: midtraining sobre exposición amplia al dominio (300B+ tokens), SFT sobre conversaciones (~200K) y RL sobre prompts con recompensa verificable (~98K). La etapa de prompts verificables es una restricción de ingeniería: exige construir tareas comprobables, no solo datos.

## Evidence
- Tres etapas declaradas: midtraining con 300B+ tokens de genomas y texto rico en DNA, ~200K conversaciones SFT y ~98K prompts RL verificables — source: 5f7f86aa64f4ba64.
- El release se enmarca como reutilizable: código y receta abiertos para aplicar los datos a otros LLMs — source: 5f7f86aa64f4ba64.

## Why it matters
El crítico señala que la receta midtraining→SFT→RL es práctica estándar, no un hallazgo novedoso. La analogía con un curriculum de programación (contexto amplio → práctica guiada → ejercicios comprobables) es estructural y laxa, no evidencia de valor pedagógico transferible.

Deriva del anuncio de FineDNA. Su valor de transferencia —si lo hay— es la disciplina de construir tareas verificables, no la secuencia en sí.

## Links
- derived_from → [[finedna-dataset-announcement-single-source]]
- relates_to → [[finedna-receta-abierta-como-patron-de-handoff-reproducible]]
