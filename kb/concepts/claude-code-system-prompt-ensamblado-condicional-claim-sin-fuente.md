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
updated: '2026-10-13'
sources:
- abf61eeec75462f9
tags:
- claude-code
- ensamblado-condicional
- fuente-no-verificada
- prompt-composition
- prompt-engineering
- prompts
- single-source
- system-prompt
- unverified
base_confidence: 0.1
half_life_days: 180
last_reinforced: '2026-10-13'
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
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: afirmar-internals-de-claude-code-como-hecho-seria-especulacion
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: contradicts
- to: claude-code-system-prompt-sin-datos-de-eficacia
  type: contradicts
---

## What it is
Un ítem RSS [abf61eeec75462f9] afirma que el código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales, en lugar de un bloque monolítico. El único contenido verificable del clúster es esa aserción; no trae fragmentos, condiciones, versión ni artefacto primario.

## Evidence
- El código fuente filtrado de Claude Code mostraría un system prompt ensamblado a partir de docenas de partes condicionales — source: abf61eeec75462f9
- El clúster es de un solo documento con engagement=0 y novelty=0.00; el score de corroboración 0.50 no está respaldado por ningún segundo documento — source: abf61eeec75462f9 (crítico)

## Why it matters
Si fuera verificable, describiría al system prompt de un agente frontera como artefacto de ingeniería compuesto, no como texto único. Como claim sin fuente primaria ni detalle, no mueve ninguna decisión sobre estimación, secuenciamiento, liderazgo ni docencia.

Se relaciona con las notas existentes sobre el mismo claim (`claude-code-ensamblado-condicional-de-system-prompt`, `claude-code-system-prompt-conditional-composition`), que registran la misma fuente filtrada. Contradice a `claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion` y a `claude-code-system-prompt-sin-datos-de-eficacia` en el sentido de que no existen artefacto primario ni datos de eficacia que sostengan la afirmación. Deriva de `ensamblado-condicional-de-prompts` como patrón genérico ya conocido.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- contradicts → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
- derived_from → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- supports → [[afirmar-internals-de-claude-code-como-hecho-seria-especulacion]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- contradicts → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- contradicts → [[claude-code-system-prompt-sin-datos-de-eficacia]]
