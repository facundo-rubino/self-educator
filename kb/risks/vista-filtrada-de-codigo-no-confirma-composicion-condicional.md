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
updated: '2026-10-07'
sources:
- 49140f9d5133d3c7
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- prompt-engineering
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-07'
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
---

## What it is
Una vista parcial o filtrada del código de un producto no permite confirmar cómo se ensambla su system prompt ni qué condiciones activan qué secciones. La inspección incompleta sostiene la sospecha, no la afirmación.

## Evidence
- El clúster de AI coach, aunque sin relación con Claude Code, comparte el mismo modo de fallo: inferir mecánicas internas desde fragmentos — source: 49140f9d5133d3c7
- El documento único sin engagement no aporta mecanismo verificable — source: 49140f9d5133d3c7

## Why it matters
Antes de citar una feature de tooling en docencia o configuración de equipo hay que verificar contra upstream. Una vista filtrada no es un artefacto primario.

Apoya a `claude-code-source-leak-sin-artefacto-primario` (misma exigencia de artefacto primario) y se relaciona con su homónima previa en el grafo.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- relates_to → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
