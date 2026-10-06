---
id: claude-code-source-leak-sin-artefacto-primario
title: '«Leaked source» de Claude Code: fuente sin artefacto primario verificable'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-06'
sources:
- abf61eeec75462f9
tags:
- claude-code
- verificabilidad
- fuente-filtrada
- rss
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: supports
- to: leak-sin-autenticidad-establecida-claude-code
  type: supports
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: supports
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
---

## What it is
La afirmación sobre el system prompt de Claude Code se apoya en «leaked source code», un género de procedencia no verificable y sin artefacto primario presentado: no hay volcado del prompt, repositorio ni diff [abf61eeec75462f9]. Una fuente filtrada sin autenticidad establecida no confirma lo que dice el leak.

## Evidence
- La evidencia del documento rss es la frase «Claude Code's leaked source shows…», sin material primario adjunto — source: abf61eeec75462f9
- El material suministrado no ofrece contenido sustantivo más allá del titular y un resumen de una línea — source: abf61eeec75462f9

## Why it matters
Introduce una fecha de caducidad y un riesgo de integridad: si Anthropic cambia la implementación, la afirmación queda obsoleta de inmediato, y sin artefacto reproducible no hay forma de comprobarla antes de citarla. Cualquier uso en docencia, configuración o diseño de agentes propios debe verificar contra upstream primero.

Refuerza las notas previas sobre leaks sin autenticidad establecida y sobre el system prompt de Claude Code como artefacto de ingesta sin API de verificación. Se relaciona con la nota principal del clúster como su condición de validez.

## Links
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[leak-sin-autenticidad-establecida-claude-code]]
- supports → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
