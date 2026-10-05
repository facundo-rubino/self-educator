---
id: claude-code-system-prompt-novelty-cero-ya-conocido
title: 'Novelty 0.00: el ensamblado condicional de prompts ya es conocido por la audiencia'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-10-05'
sources:
- abf61eeec75462f9
tags:
- claude-code
- novelty
- patron-conocido
- prompt-engineering
- signal-quality
- system-prompt
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: ensamblado-condicional-de-prompts
  type: supports
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: relates_to
---

## What it is
El scorer marca el clúster con novelty=0.00. La arquitectura de system prompts modulares/condicionales y el ensamblado dinámico de contexto en agentes de codificación era ya un patrón documentado y ampliamente asumido antes del leak. La supuesta revelación es una re-descripción de un patrón conocido, no un descubrimiento.

## Evidence
- novelty=0.00 indica que el clúster no aporta información nueva respecto a lo ya conocido en el pipeline — source: abf61eeec75462f9

## Why it matters
Impedir que un novelty bajo pase por hallazgo depende de que exista una nota donde el patrón conocido esté anclado. Sin ella, cada leak que reformula el patrón se leería como avance. Esta nota cumple esa función de anclaje.

No contradice el hecho del leak, sino su valor informativo: por eso enlaza a la nota de concepto con antecedente negativo. Refuerza la nota existente sobre ensamblado condicional de prompts, que ya recogía el patrón general.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
- relates_to → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
