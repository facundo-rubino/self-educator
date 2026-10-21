---
id: claude-code-leak-detalle-condiciones-no-especificadas
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- abf61eeec75462f9
tags:
- claude-code
- leak
- metodologia
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: claude-code-leak-condiciones-no-especificadas
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
---

## What it is
La fuente afirma «docenas de partes condicionales» pero no enumera ninguna condición, parte ni orden de ensamblado [abf61eeec75462f9].

## Evidence
- No hay fragmentos citados del prompt ni descripción del gating — source: abf61eeec75462f9
- No se especifica versión de Claude Code a la que corresponde el supuesto código filtrado — source: abf61eeec75462f9

## Why it matters
Sin nombrar condiciones no se puede testear el claim ni distinguirlo de una descripción genérica de cualquier harness LLM. La pregunta queda abierta hasta recuperar el artefacto primario.

Extiende la nota existente sobre condiciones no especificadas en el leak. Se apoya en el riesgo de que un leak sin autenticidad establecida no confirma lo que afirma.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-leak-condiciones-no-especificadas]]
- relates_to → [[leak-sin-autenticidad-establecida]]
