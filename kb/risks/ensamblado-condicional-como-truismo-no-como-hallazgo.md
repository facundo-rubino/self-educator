---
id: ensamblado-condicional-como-truismo-no-como-hallazgo
title: «El contexto da forma al comportamiento del agente» es un truismo, no un hallazgo
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-08'
updated: '2026-10-08'
sources:
- abf61eeec75462f9
tags:
- system-prompt
- novelty
- brief
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: composicion-condicional-de-instrucciones-como-hallazgo-ya-conocido
  type: supports
- to: claude-code-system-prompt-novelty-cero-ya-conocido
  type: supports
- to: restatement-de-titulo-no-es-hallazgo
  type: relates_to
---

## What it is
La conclusión que sobrevive al escrutinio —«el contexto inyectado da forma al comportamiento del agente»— es una verdad general de los harness LLM, no una información sobre cómo Claude Code construye su system prompt. Con novelty=0.00 y engagement=0, no aporta material nuevo.

## Evidence
- El documento solo describe el ensamblado condicional del prompt — source: abf61eeec75462f9
- El hallazgo declarado coincide con el conocimiento ya asentado sobre composición condicional de instrucciones — source: abf61eeec75462f9 (comparación con corpus)

## Why it matters
Registrar truismos como hallazgos infla el grafo y erosiona la confianza en el resto. Marcar novelty=0.00 como señal de «no compilar» protege el valor del KB.

Se apoya en las notas existentes sobre composición condicional ya conocida y sobre novelty cero en Claude Code. Se relaciona con el patrón de restatement de título que no es hallazgo.

## Links
- supports → [[composicion-condicional-de-instrucciones-como-hallazgo-ya-conocido]]
- supports → [[claude-code-system-prompt-novelty-cero-ya-conocido]]
- relates_to → [[restatement-de-titulo-no-es-hallazgo]]
