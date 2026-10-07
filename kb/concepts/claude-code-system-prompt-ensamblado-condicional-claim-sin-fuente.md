---
id: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
title: El system prompt de Claude Code se ensambla de partes condicionales (claim
  de fuente filtrada, no verificada)
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- abf61eeec75462f9
tags:
- claude-code
- prompts
- fuente-no-verificada
- ensamblado-condicional
base_confidence: 0.1
half_life_days: 180
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-sin-artefacto-primario
  type: supports
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: contradicts
- to: ensamblado-condicional-de-prompts
  type: derived_from
---

## What it is
Un único documento RSS [abf61eeec75462f9] afirma que el system prompt de Claude Code se ensambla dinámicamente a partir de docenas de partes condicionales. El documento enmarca el claim como proveniente de «leaked source» sin mostrar el artefacto. No hay segundo documento, código, prompt observado ni test dentro del clúster.

## Evidence
- «Claude Code's system prompt is assembled from dozens of conditional parts rather than being a single static block». El autor lo atribuye a «leaked source». — source: abf61eeec75462f9
- El documento es un ítem RSS con engagement=0 en el pipeline de ingesta: circuló sin discusión medida que lo corrobore. — source: abf61eeec75462f9

## Why it matters
Es la afirmación concreta sobre internals de Claude Code que sostiene el resto del clúster. Su confianza real es baja: novelty 0.00, una sola fuente, sin artefacto primario. Cualquier nota derivada debe heredar ese techo, no elevarlo citando plausibilidad como confirmación.

Se relaciona con el patrón genérico de composición condicional (`claude-code-system-prompt-conditional-composition`, `ensamblado-condicional-de-prompts`), pero sin aportar evidencia nueva: el patrón ya era conocido. Contradice `restatement-de-titulo-como-evidencia-de-composicion-condicional` en la medida en que una reformulación del titular no constituye hallazgo. La ausencia de artefacto primario está registrada en `claude-code-source-leak-sin-artefacto-primario`.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- contradicts → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
- derived_from → [[ensamblado-condicional-de-prompts]]
