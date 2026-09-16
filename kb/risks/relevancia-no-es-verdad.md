---
id: relevancia-no-es-verdad
title: 'Utilidad no es evidencia: el argumento de relevancia no valida una afirmación'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- evidence-quality
- epistemics
- risk
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
---

## What it is
Que una afirmación sea útil para el brief no la vuelve verdadera. El argumento de que el patrón es replicable para devs y educadores es una afirmación de utilidad, no de verdad, y no sostiene la afirmación técnica que dice respaldar.

## Evidence
- El argumento de 'relevancia' (este patrón es replicable para devs/educadores) es una afirmación de utilidad, no de verdad — source: abf61eeec75462f9
- La plausibilidad de la afirmación se apoya en el meme comunitario de prompts modulares/condicionales: el documento confirma lo ya asumido en vez de introducir evidencia nueva — source: abf61eeec75462f9

## Why it matters
Es un modo de falla recurrente en la compilación de conocimiento: entran afirmaciones al grafo porque encajan con el tema del brief, y quedan con la misma apariencia que afirmaciones sostenidas por evidencia. Separar utilidad de verdad es requisito para que `base_confidence` signifique algo.

Contradice el salto inferencial de `claude-code-system-prompt-conditional-composition` hacia recomendaciones prácticas. Se relaciona con `prompt-modular-sin-mecanica-verificable` como el mismo problema visto desde el lado de la mecánica faltante: aquí falta el nexo entre utilidad y verdad, allí falta el detalle técnico.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
