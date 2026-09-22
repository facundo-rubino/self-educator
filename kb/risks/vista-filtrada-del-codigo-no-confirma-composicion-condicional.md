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
updated: '2026-09-22'
sources:
- abf61eeec75462f9
tags:
- leak
- verificabilidad
- claude-code
- fuentes
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-22'
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
---

## What it is
La afirmación de que el system prompt de Claude Code se ensambla de docenas de partes condicionales proviene de una vista filtrada del código, reportada de segunda mano en un ítem RSS (doc:abf61eeec75462f9). Un leak puede ser parcial, estar desactualizado o estar mal leído, y no admite verificación contra documentación oficial. Por tanto, el contenido de la nota correspondiente debe tratarse como reportado, no como establecido.

## Evidence
- La fuente del claim es una vista filtrada del código, es decir, un reporte secundario sobre material filtrado y no documentación de primera parte — source: abf61eeec75462f9
- El clúster consta de un solo documento, sin segunda fuente independiente que corrobore el ensamblado condicional — source: abf61eeec75462f9
- No se citan fragmentos de código, condiciones ni versión del material filtrado — source: abf61eeec75462f9

## Why it matters
Cualquier práctica derivada —revisar por ramas condicionales, tratar prompts como configuración— queda condicionada a que el leak sea auténtico y a que una release posterior no cambie la arquitectura del prompt, lo que invalidaría la práctica recomendada. El coste de equivocarse no es alto si las prácticas se adoptan como hipótesis; sí lo es si se presentan como hechos verificados.

`contradicts` → `claude-code-system-prompt-conditional-composition`: tensión directa entre el claim sobre composición condicional y la imposibilidad de confirmarlo desde un leak. `derived_from` → `leak-sin-autenticidad-establecida`: principio general del que este caso es instancia. `relates_to` → `leak-de-claude-code-sin-fragmentos-citados`: refuerza que no hay fragmentos, disparadores ni versión que permitan auditar el leak. `relates_to` → `claude-code-source-leak-conditions-parts-unspecified`: mismo límite de detalle, condiciones y partes sin especificar. `relates_to` → `mcp-fechas-2026-sinteticas-no-corroborables`: comparte el modo de fallo de material no corroborable citado como fuente.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[leak-sin-autenticidad-establecida]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[mcp-fechas-2026-sinteticas-no-corroborables]]
