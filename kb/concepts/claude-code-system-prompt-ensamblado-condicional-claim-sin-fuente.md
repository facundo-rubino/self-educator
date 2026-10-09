---
id: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
title: El system prompt de Claude Code se ensambla de partes condicionales (claim
  de fuente filtrada, no verificada)
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-09'
sources:
- abf61eeec75462f9
tags:
- claude-code
- ensamblado-condicional
- fuente-no-verificada
- prompt-composition
- prompts
- single-source
- system-prompt
- unverified
base_confidence: 0.1
half_life_days: 180
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-sin-artefacto-primario
  type: supports
- to: restatement-de-titulo-como-evidencia-de-composicion-condicional
  type: contradicts
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: afirmar-internals-de-claude-code-como-hecho-seria-especulacion
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
---

## What it is
Un ítem RSS (doc `abf61eeec75462f9`) afirma que el system prompt de Claude Code «se ensambla a partir de docenas de partes condicionales», atribuyéndolo a «leaked source». No hay código, versión, fecha ni confirmación independiente. La descripción es genérica y aplicable a casi cualquier system prompt moderno.

## Evidence
- El system prompt de Claude Code estaría ensamblado a partir de docenas de partes condicionales, según fuente filtrada reportada — source: abf61eeec75462f9
- El clúster contiene un único documento, con engagement cero, novelty 0.00 y sin corroboración — source: abf61eeec75462f9

## Why it matters
Como descripción factual de la arquitectura de Claude Code no es utilizable: la procedencia «leaked source» es inverificable y podría ser fabricada, mal atribuida o describir una herramienta distinta o desactualizada. Solo sirve como puntero para verificación posterior, nunca como hecho citable en decisiones técnicas ni en material de clase.

Se apoya en la nota sobre el system prompt como artefacto de ingeniería: si la composición condicional fuera real, reforzaría ese encuadre. También conecta con el patrón de ensamblado condicional de prompts, pero es evidencia de apoyo débil: el propio patrón no depende de este documento. Los riesgos de tratar un leak sin autenticidad establecida y de que una vista filtrada de código no confirme composición condicional son los límites que acotan esta nota.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- supports → [[claude-code-source-leak-sin-artefacto-primario]]
- contradicts → [[restatement-de-titulo-como-evidencia-de-composicion-condicional]]
- derived_from → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- supports → [[afirmar-internals-de-claude-code-como-hecho-seria-especulacion]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
