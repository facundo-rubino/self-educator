---
id: vista-filtrada-de-codigo-no-confirma-composicion-condicional
title: Una vista filtrada de código no confirma la composición condicional del prompt
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-10-14'
sources:
- 49140f9d5133d3c7
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- prompt-engineering
- system-prompt
- verificacion
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-14'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: claude-code-source-leak-sin-artefacto-primario
  type: supports
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: claude-code-system-prompt-condicional-singleton-sin-artefacto-primario
  type: relates_to
- to: afirmar-internals-de-claude-code-como-hecho-seria-especulacion
  type: supports
---

## What it is
Ver una porción filtrada de código no establece el mecanismo de ensamblado del system prompt: no muestra las condiciones de activación, ni el orden de las partes, ni la versión del producto. El clúster tiene un solo documento [abf61eeec75462f9] y corroboración 0.50, es decir, ninguna validación cruzada.

## Evidence
- El documento [abf61eeec75462f9] describe "docenas de partes condicionales", pero no especifica qué condiciones gatean qué secciones.
- El crítico indica que no existe corroboración independiente de que el código filtrado sea auténtico o representativo del sistema real.

## Why it matters
Un dev que decida reestructurar su propio system prompt imitando el patrón de Claude Code estaría copiando una descripción de segundo orden. La decisión de diseño —separar identidad, herramientas, políticas y contexto por fases— puede ser correcta en abstracto, pero no se sostiene en esta evidencia como práctica de un producto concreto.

Apoya a `afirmar-internals-de-claude-code-como-hecho-seria-especulacion`. Se relaciona con `claude-code-system-prompt-condicional-singleton-sin-artefacto-primario`, que registra la misma limitación desde el lado de la fuente primaria ausente.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- relates_to → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- relates_to → [[claude-code-system-prompt-condicional-singleton-sin-artefacto-primario]]
- supports → [[afirmar-internals-de-claude-code-como-hecho-seria-especulacion]]
