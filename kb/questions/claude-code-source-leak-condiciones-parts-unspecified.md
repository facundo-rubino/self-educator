---
id: claude-code-source-leak-condiciones-parts-unspecified
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-02'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- evidencia-debil
- evidencia-faltante
- leak
- prompt-engineering
- system-prompt
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: supports
- to: claude-code-system-prompt-conditional-composition
  type: supports
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: leak-sin-autenticidad-establecida
  type: relates_to
---

## What it is
La descripción del system prompt de Claude Code llega como un leak, no como documentación oficial ni inspección reproducible. Quedan abiertas las preguntas que decidirían si la observación tiene valor arquitectónico: qué condiciones gatean qué secciones, cuáles son los fragmentos, y si el ensamblado es intencional o resultado de acumulación.

## Evidence
- La descripción se remonta a un supuesto leak de un prompt interno, sin documentación oficial ni inspección reproducible — source: abf61eeec75462f9
- No se aportan detalles concretos sobre la estructura condicional — source: abf61eeec75462f9

## Why it matters
Sin especificar condiciones, partes ni secuenciación, cualquier inferencia sobre el diseño del agente es extrapolación. La pregunta delimita el techo de lo que este cluster puede sostener.

Deriva del claim de composición condicional; se relaciona con el problema general de autenticidad de leaks, ya registrado para el mismo artefacto.

## Links
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- supports → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- supports → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[leak-sin-autenticidad-establecida]]
