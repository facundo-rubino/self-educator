---
id: legibilidad-de-la-afirmacion-sin-fuente-primaria
title: Una afirmación sobre un artefacto ajeno no es evidencia de práctica propia
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- abf61eeec75462f9
tags:
- evidencia
- agentes-de-codigo
- prompting
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: supports
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: overfitting-tematico-desde-mecanica-ajena
  type: relates_to
---

## What it is
El documento describe un artefacto de un producto (el system prompt de Claude Code) y no una práctica del desarrollador ni su efecto medido [abf61eeec75462f9]. Para el brief —agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico, oficio— un leak sin fragmentos no autoriza ninguna lección sobre cómo trabajar mejor. La conexión con productividad, estimación o docencia sería invención del analista.

## Evidence
- El clúster es un documento único de RSS sin corroboración — source: abf61eeec75462f9
- No se mide impacto en productividad, estimación ni liderazgo técnico — source: abf61eeec75462f9

## Why it matters
Marca el modo de fallo de convertir la descripción de un producto en consejo de práctica. El uso legítimo de la nota es como ejemplo débil del patrón de composición condicional, con confianza baja, nunca como recomendación operativa.

Soporta `afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases`, el mismo modo de fallo aplicado a releases. Se relaciona con `sobre-generalizacion-desde-claude-code` y `overfitting-tematico-desde-mecanica-ajena`: inferir tu propio diseño desde la mecánica de un sistema ajeno sin datos de transferibilidad.

## Links
- supports → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[overfitting-tematico-desde-mecanica-ajena]]
