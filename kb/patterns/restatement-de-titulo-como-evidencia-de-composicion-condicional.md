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
updated: '2026-10-09'
sources:
- abf61eeec75462f9
tags:
- circularidad
- evidence-quality
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
last_reinforced: '2026-10-09'
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
---

## What it is
Patrón recurrente en este corpus: cuando un documento describe un system prompt como «compuesto de partes condicionales», no aporta un hallazgo nuevo sobre el sistema observado. Es la formulación genérica de cómo funcionan la mayoría de los system prompts de producto actuales.

## Evidence
- La frase «assembled from dozens of conditional parts» es una descripción genérica de bajo contenido informativo, aplicable a muchos system prompts modernos — source: abf61eeec75462f9
- El crítico de la señal la califica de coincidencia léxica, no de hallazgo distintivo — source: abf61eeec75462f9

## Why it matters
Evita inflar una nota o una clase con una «arquitectura descubierta» que en realidad es el estado del arte conocido. Para liderar o enseñar, la afirmación solo sería útil si viniera con las partes concretas, las condiciones que las activan y el efecto medido: nada de eso está en la evidencia.

Deriva directamente del claim sobre el prompt de Claude Code, que es su caso instancia. Refuerza el patrón ya registrado de que la composición condicional de instrucciones no es hallazgo nuevo y el más general de que reformular un título no es un hallazgo.

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
