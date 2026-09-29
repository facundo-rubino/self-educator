---
id: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
title: La evidencia sobre Claude Code es artefacto de ingesta, no fuente verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- abf61eeec75462f9
tags:
- signal-quality
- evidence-quality
base_confidence: 0.65
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: relates_to
---

## What it is
Lo que el clúster contiene es un documento RSS que reporta una afirmación secundaria; el cuerpo sustantivo del artefacto fuente no está ingerido. La validación por título daría una señal falsa; solo el solapamiento de contenido permitiría decidir.

## Evidence
- El clúster ofrece un único documento RSS sin código, extracto, autor ni release note — source: abf61eeec75462f9
- El título del documento coincide con el tema del clúster, lo que puede inflar el matching — source: abf61eeec75462f9

## Why it matters
Explica por qué este ítem pudo superar el filtro sin aportar contenido verificable, y qué haría falta para promoverlo: recuperar el artefacto fuente.

Contradice la materialidad de `claude-code-system-prompt-conditional-composition` y aplica la cautela de `validacion-de-senal-por-contenido-no-por-titulo`.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[validacion-de-senal-por-contenido-no-por-titulo]]
