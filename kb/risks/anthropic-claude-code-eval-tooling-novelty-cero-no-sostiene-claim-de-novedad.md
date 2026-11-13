---
id: anthropic-claude-code-eval-tooling-novelty-cero-no-sostiene-claim-de-novedad
title: 'Novelty 0.00 en el tooling de evals de Claude Code: el pipeline no encontró
  nada nuevo'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-13'
updated: '2026-11-13'
sources:
- 541b1e7161ae8f43
tags:
- evals
- novedad
- pipeline
- senal
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-11-13'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
- to: claude-code-system-prompt-novelty-cero-conocimiento-ya-disponible
  type: relates_to
---

## What it is
La novedad reportada del clúster es 0.00 y la corroboración 0.50, con un solo documento de feed RSS sin engagement. Es decir: el pipeline no encontró ninguna novedad, y la corroboración «media» no viene de fuentes independientes sino de la posición por defecto del scorer en un clúster de un solo documento. Afirmar que la herramienta es «nueva» apoya el titular en una palabra que la propia puntuación contradice.

## Evidence
- Novedad reportada de 0.00 en el clúster — source: 541b1e7161ae8f43
- Un solo documento de fuente RSS sin engagement — source: 541b1e7161ae8f43

## Why it matters
Una señal de novedad cero con un solo documento es un candidato a retrieval de texto completo, no a insight corroborado. El valor del KB está en registrar el puntero («existen build_eval y hill-climb en claude-api»), no en compilar afirmaciones sobre tendencia o adopción.

Deriva del concepto del tooling. Repite el patrón documentado en `claude-code-system-prompt-novelty-cero-conocimiento-ya-disponible`: novelty 0.00 significa que la audiencia del brief ya conoce el marco, no que el ítem sea falso.

## Links
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- relates_to → [[claude-code-system-prompt-novelty-cero-conocimiento-ya-disponible]]
