---
id: task-specific-llm-evals-singleton-rss-engagement-cero-novelty-cero
title: '«Task-Specific LLM Evals»: singleton RSS con engagement cero y novelty 0.00'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-30'
sources:
- 93963a5f93e58d05
tags:
- corpus
- corroboracion
- engagement
- evals
- ingesta
- llm
- rss
- rss-stub
- senal-debil
- singleton
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-singleton-engagement-cero
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: supports
- to: pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques
  type: relates_to
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
- to: single-document-cluster-engagement-cero-no-generaliza
  type: derived_from
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: supports
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: relates_to
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
---

## What it is
Un clúster de un único documento RSS con engagement=0 y novelty=0.00 no sostiene ninguna afirmación sustantiva. El crítico degrada la confianza a 0.05: no hay evidencia textual, ni datos, ni método, ni resultados sobre los que razonar.

## Evidence
- Documento único procedente de un feed RSS con engagement=0 — source: 93963a5f93e58d05
- novelty=0.00 y corroboration=0.50 en el clúster — source: 93963a5f93e58d05
- El crítico califica el veredicto como WEAK con confianza ajustada a 0.05 — source: 93963a5f93e58d05

## Why it matters
Cualquier afirmación sobre qué evals funcionan o no, extraída de este clúster, sería especulativa. La única acción defendible es registrar el ítem como candidato a retrieval de texto completo y no priorizarlo.

Se deriva de la nota sobre el alcance declarado y refuerza el patrón más amplio ya registrado sobre afirmar práctica desde feeds sin contenido. También complementa la nota existente sobre el título sin cuerpo ingerido.

## Links
- relates_to → [[task-specific-llm-evals-singleton-engagement-cero]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[generalizacion-desde-cluster-de-un-solo-documento]]
- relates_to → [[pipeline-sin-fuente-primaria-para-verificar-senal-de-ataques]]
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
- derived_from → [[single-document-cluster-engagement-cero-no-generaliza]]
- supports → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
