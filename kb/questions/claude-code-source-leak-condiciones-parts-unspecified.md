---
id: claude-code-source-leak-condiciones-parts-unspecified
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-29'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- evidencia-debil
- prompt-engineering
- system-prompt
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: supports
- to: claude-code-system-prompt-conditional-composition
  type: supports
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
---

## What it is
Pregunta abierta: ¿qué condiciones activan qué secciones del prompt, en qué orden y con qué granularidad? El documento afirma «docenas de partes condicionales» sin enumerar ninguna condición, ninguna parte ni la secuencia de ensamblado.

## Evidence
- La única caracterización disponible es «docenas de partes condicionales», una formulación que no se puede confirmar ni refutar con el material del clúster — source: abf61eeec75462f9

## Why it matters
Sin las condiciones no se puede extraer ninguna regla de diseño trasladable a agentes propios. La pregunta marca exactamente qué evidencia faltaría para convertir el claim en algo operable.

Es la laguna concreta de `claude-code-system-prompt-conditional-composition` y solapa con `claude-code-condiciones-que-gatean-secciones-sin-observar` y `leak-de-claude-code-sin-fragmentos-citados`, que registran la misma ausencia desde otros ángulos.

## Links
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- supports → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- supports → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
