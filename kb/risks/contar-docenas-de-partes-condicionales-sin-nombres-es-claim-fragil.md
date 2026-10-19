---
id: contar-docenas-de-partes-condicionales-sin-nombres-es-claim-fragil
title: «Docenas de partes condicionales» sin condiciones nombradas es un claim frágil
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-19'
updated: '2026-10-19'
sources:
- abf61eeec75462f9
tags:
- calidad-de-evidencia
- claim-de-conteo
- descripcion-generica
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: restatement-de-titulo-no-es-hallazgo
  type: derived_from
- to: docenas-de-partes-condicionales-claim-de-conteo-inverificable
  type: relates_to
- to: ensamblado-condicional-como-truismo-no-como-hallazgo
  type: relates_to
---

## What it is
"Docenas de partes condicionales" es una descripción arquitectónica atractiva léxicamente pero genérica: los prompts condicionales por herramienta y contexto son un patrón conocido en harnesses de agentes. El claim de conteo no viene con nombres ni mecanismo, así que lo que parece un hallazgo específico sobre Claude Code es una reformulación de una generalidad de ingeniería.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado de docenas de partes condicionales — source: abf61eeec75462f9
- La novelty declarada del documento es 0.00, señal de que el pipeline no lo trata como información nueva — source: abf61eeec75462f9

## Why it matters
El claim se autolimita en ambos extremos: novelty 0.00 lo declara no-nuevo y la falta de mecanismo lo hace inverificable. Sobrevive solo "el ensamblado condicional es un patrón", que es conocimiento de fondo.

`contradicts` la nota de contenido en su parte específica (nombra docenas, no las identifica). `derived_from` la regla general de que reformular un título no es hallazgo; familia con las notas de claim-de-conteo inverificable y de ensamblado condicional como truismo.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[docenas-de-partes-condicionales-claim-de-conteo-inverificable]]
- relates_to → [[ensamblado-condicional-como-truismo-no-como-hallazgo]]
