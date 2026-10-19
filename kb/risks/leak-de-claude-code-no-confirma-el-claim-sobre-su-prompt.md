---
id: leak-de-claude-code-no-confirma-el-claim-sobre-su-prompt
title: 'Material filtrado no confirmado: la fuente no puede validar lo que afirma'
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
- fuente-filtrada
- no-verificable
- autenticidad
- claude-code
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: claude-code-source-leak-sin-artefacto-primario
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: derived_from
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
---

## What it is
El hallazgo procede de código fuente filtrado y no confirmado oficialmente. Una fuente filtrada es inherentemente no falsable desde fuera: puede ser inexacta, desactualizada, fabricada o reinterpretada selectivamente, y el documento no aporta artefacto primario que verifique su autenticidad.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado de docenas de partes condicionales — source: abf61eeec75462f9
- El documento no es verificable por sí mismo y la novelty declarada es 0.00 — source: abf61eeec75462f9

## Why it matters
Un leak sin autenticidad establecida no confirma lo que dice el leak. Presentar esto a un equipo o en clase como hecho sobre cómo funciona Claude Code sería especulación con formato de dato.

`contradicts` la nota de contenido: el vehículo de la afirmación socava la afirmación. `derived_from` la regla general de leak sin autenticidad; se relaciona con las notas existentes de vista filtrada y ausencia de artefacto primario.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-sin-artefacto-primario]]
- derived_from → [[leak-sin-autenticidad-establecida]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
