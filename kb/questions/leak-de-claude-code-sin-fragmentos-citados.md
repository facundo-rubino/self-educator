---
id: leak-de-claude-code-sin-fragmentos-citados
title: El leak de Claude Code no trae fragmentos, disparadores ni versión
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- claude-code
- leak
- verificacion
- fuente-primaria
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: hy3-fuente-primaria-y-metodologia-ausentes
  type: relates_to
---

## What it is
El ítem que reporta el ensamblado condicional del system prompt de Claude Code no trae fragmentos citados del prompt, ni los disparadores condicionales nombrados, ni metodología de obtención del leak, ni ancla de versión o fecha. Queda abierto qué se filtró, cómo y de qué versión.

## Evidence
- No hay fragmentos de prompt citados, disparadores condicionales nombrados, metodología del leak ni ancla de versión o fecha — source: abf61eeec75462f9
- El documento es un ítem RSS único con engagement=0 — source: abf61eeec75462f9

## Why it matters
Sin esos elementos la afirmación no es contrastable con el producto observado. Cualquier uso en clase o en documentación interna debería llevar la caveat explícita de fecha y versión, o directamente reformularse como hipótesis a testear mediante observación del comportamiento del agente.

Es la pregunta que acompaña al concepto sobre el ensamblado condicional y comparte la laguna ya registrada sobre el leak de Claude Code: condiciones, partes y secuenciación sin especificar. Se relaciona con el riesgo general de que un leak sin autenticidad establecida no confirme lo que dice y con el caso análogo de ausencia de fuente primaria y metodología en el ranking de Hy3.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
