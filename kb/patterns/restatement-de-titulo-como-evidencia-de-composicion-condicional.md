---
id: restatement-de-titulo-como-evidencia-de-composicion-condicional
title: '«Docenas de partes condicionales» no es hallazgo: es la descripción genérica
  del ensamblado de prompts'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-10-12'
sources:
- 93963a5f93e58d05
- abf61eeec75462f9
tags:
- circularidad
- ensamblado-condicional
- evidence-quality
- evidencia
- evidencia-circular
- evidencia-debil
- generic-claim
- metodo
- patron
- prompt-composition
- prompt-engineering
- restatement
base_confidence: 0.5
half_life_days: 365
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: restatement-de-titulo-no-es-hallazgo
  type: derived_from
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: supports
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: supports
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: derived_from
- to: composicion-condicional-de-instrucciones-como-hallazgo-ya-conocido
  type: supports
- to: restatement-de-titulo-no-es-hallazgo
  type: supports
- to: task-specific-llm-evals-titulo-sin-contenido-ingerido
  type: supports
---

## What it is
Reformular el título de un documento como si fuera su hallazgo es circularidad, no evidencia. En este caso, describir que un documento «distingue evals que funcionan de las que no» porque su título lo dice repite la observación en lugar de inferirla de evidencia independiente.

## Evidence
- La evidencia del documento de evals se sostiene solo citando repetidamente la misma etiqueta de fuente, sin material adicional — source: 93963a5f93e58d05
- No se aportan criterios, métodos, ejemplos ni resultados que sustenten la distinción del título — source: 93963a5f93e58d05

## Why it matters
Aplicado al reporte: la única evidencia listada del documento es un restatement de su título. El crítico lo identifica como circularidad y baja la confianza a 0.05. La regla operativa es que un título reformulado no eleva el estatus epistémico de un claim.

`supports` la nota de riesgo sobre el mismo documento: la circularidad es la razón concreta por la que ese título no puede sostener un hallazgo. Se relaciona con la nota existente sobre restatement de título como no-hallazgo, de la que este caso es una confirmación más.

## Links
- derived_from → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- supports → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- supports → [[composicion-condicional-de-instrucciones-como-hallazgo-ya-conocido]]
- supports → [[restatement-de-titulo-no-es-hallazgo]]
- supports → [[task-specific-llm-evals-titulo-sin-contenido-ingerido]]
