---
id: vista-filtrada-del-codigo-no-confirma-composicion-condicional
title: Una vista filtrada de código no confirma la composición condicional del prompt
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-28'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia
- fuentes
- leak
- verificabilidad
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: leak-sin-autenticidad-establecida
  type: derived_from
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: relates_to
- to: leak-de-claude-code-sin-fragmentos-citados
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: documento-unico-como-base-de-afirmacion-de-estandar
  type: relates_to
---

## What it is
Aun si existiera un fragmento real de código filtrado, una vista parcial no basta para afirmar que el prompt se ensambla condicionalmente: haría falta la ruta completa de construcción, el orden de composición y al menos una condición activándose. El documento [abf61eeec75462f9] no aporta nada de eso y, además, no establece la autenticidad del material citado.

## Evidence
- Afirmación «leaked source shows» sin extracto ni ruta de ensamblado — source: abf61eeec75462f9

## Why it matters
Distingue dos fallos independientes: material no auténtico y material auténtico pero insuficiente. Ambos impiden elevar la confianza por encima del suelo de 0.05 que puso el crítico.

Soporta `leak-de-claude-code-sin-fragmentos-citados` y comparte mecanismo con `leak-sin-autenticidad-establecida`. Se relaciona asimismo con `documento-unico-como-base-de-afirmacion-de-estandar`: un solo documento no sostiene una afirmación general.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[leak-sin-autenticidad-establecida]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[mcp-fechas-2026-sinteticas-no-corroborables]]
- supports → [[leak-de-claude-code-sin-fragmentos-citados]]
- supports → [[leak-sin-autenticidad-establecida]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[documento-unico-como-base-de-afirmacion-de-estandar]]
