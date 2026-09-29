---
id: arquitectura-de-prompt-de-producto-no-generaliza-a-practica-recomendada
title: La arquitectura de prompt de un producto no generaliza a práctica recomendada
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
- prompt-engineering
- evidence-quality
- agents
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
---

## What it is
Riesgo metodológico: aunque el artefacto existiera, probaría lo que hizo un proveedor en un momento dado, no lo que es práctica común ni lo que funciona. La inferencia de «los agentes de producción estructuran así sus prompts» generaliza desde n=1 no verificado.

## Evidence
- El material del clúster no contiene código, extracto, autor, repositorio, release note ni replicación independiente — source: abf61eeec75462f9
- La formulación «docenas de partes condicionales» no es falsable con la evidencia suministrada — source: abf61eeec75462f9
- El informe admite explícitamente que la extrapolación a prácticas generales puede sobrepasarse — source: abf61eeec75462f9

## Why it matters
Evita reclutar un claim atractivo para confirmar la creencia previa de que los prompts modulares son mejor práctica. La conclusión correcta con esta evidencia es «hipótesis interesante», no «mental model de industria».

Contradice el salto de `claude-code-system-prompt-conditional-composition` a prescripción general, y coincide con `sobre-generalizacion-desde-claude-code`: el diseño interno de un producto no es la práctica recomendada para agentes propios.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
