---
id: vista-filtrada-de-codigo-no-confirma-composicion-condicional
title: Una vista filtrada de código no confirma la composición condicional del prompt
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
- claude-code
- evidence-quality
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
---

## What it is
Aun disponiendo de una vista parcial del código, esta no bastaría para confirmar cómo se ensambla el prompt en runtime: la composición efectiva depende de la ejecución, no solo de la presencia de fragmentos en el código.

## Evidence
- El material disponible no incluye código ni extracto, solo la afirmación de que el leak lo muestra — source: abf61eeec75462f9
- La distinción entre lo que el código contiene y lo que efectivamente se ensambla no está establecida — source: abf61eeec75462f9

## Why it matters
Bloquea el salto de «hay fragmentos condicionales en el código» a «el prompt se ensambla condicionalmente en producción». Es una cautela de verificación, no una refutación.

Contradice la lectura directa de `claude-code-system-prompt-conditional-composition` y coincide con `vista-filtrada-del-codigo-no-confirma-composicion-condicional`.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
