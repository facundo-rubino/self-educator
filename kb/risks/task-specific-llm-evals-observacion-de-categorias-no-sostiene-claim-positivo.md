---
id: task-specific-llm-evals-observacion-de-categorias-no-sostiene-claim-positivo
title: Una observación de categorías de eval no sostiene un claim positivo sobre evaluación
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-14'
updated: '2026-10-14'
sources:
- 93963a5f93e58d05
tags:
- evals
- circularidad
- claim
- metodologia
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: derived_from
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
- to: afirmar-aptitud-de-modelo-o-agente-desde-categorias-de-eval-sin-mecanismo
  type: relates_to
---

## What it is
Registro del modo de fallo específico de este clúster: la «señal» es el propio documento descrito como una mención de categorías de tarea. Convertir esa mención en un claim metodológico («los siguientes tipos de eval funcionan y estos no») es circular y no soportado por la evidencia.

## Evidence
- La única evidencia aportada es la enumeración de categorías de tarea del propio documento — source: 93963a5f93e58d05
- No hay del documento métodos, resultados ni recomendaciones que respalden un veredicto — source: 93963a5f93e58d05

## Why it matters
Evita que un revisor cite «Task-Specific LLM Evals that Do & Don't Work» como fuente de criterios de aceptación o de validación de agentes: la fuente no entrega esos criterios. Cualquier afirmación sobre aptitud de agentes para código o docencia inferida de un listado de categorías es invención.

Deriva del registro de insuficiencia de cuerpo. Reutiliza el patrón `restatement-de-titulo-no-es-hallazgo` (reformular un título no es un hallazgo) y la advertencia `afirmar-aptitud-de-modelo-o-agente-desde-categorias-de-eval-sin-mecanismo`.

## Links
- derived_from → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[afirmar-aptitud-de-modelo-o-agente-desde-categorias-de-eval-sin-mecanismo]]
