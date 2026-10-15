---
id: ensamblado-condicional-de-prompt-como-heuristica-debil-sobre-conocimiento-previo
title: 'Ensamblado condicional de prompts: heurística débil sobre conocimiento pre-existente'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-15'
updated: '2026-10-15'
sources:
- abf61eeec75462f9
- sig-979a04e33a30
tags:
- system-prompt
- composicion-condicional
- novelty-cero
base_confidence: 0.75
half_life_days: 180
last_reinforced: '2026-10-15'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: system-prompt-modular-como-ejemplo-ensenable-de-separacion-de-concerns
  type: relates_to
- to: claude-code-system-prompt-novelty-cero-ya-conocido
  type: derived_from
---

## What it is
Lo único que sobrevive al escrutinio del clúster es una heurística débil: los prompts de agentes pueden diseñarse como sistemas modulares activados por contexto. Es una idea pre-existente en ingeniería de LLM, no un descubrimiento derivado del clúster.

## Evidence
- El crítico del reporte afirma que, eliminada la apelación a la autoridad del leak, solo queda una heurística débil — fuente: sig-979a04e33a30.
- El reporte registra novedad 0.00 para este material — fuente: sig-979a04e33a30.

## Why it matters
Aceptar que el valor aquí es heurístico y no verificable evita tratarlo como hallazgo en notas, docencia o decisiones de arquitectura de agentes. La heurística puede mantenerse como punto de partida mental, no como resultado.

Se relaciona con `claude-code-system-prompt-conditional-composition` (misma idea, distinta base de evidencia) y con `system-prompt-modular-como-ejemplo-ensenable-de-separacion-de-concerns`. Se deriva de `claude-code-system-prompt-novelty-cero-ya-conocido`.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[system-prompt-modular-como-ejemplo-ensenable-de-separacion-de-concerns]]
- derived_from → [[claude-code-system-prompt-novelty-cero-ya-conocido]]
