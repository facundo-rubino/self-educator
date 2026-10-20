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
updated: '2026-10-20'
sources:
- abf61eeec75462f9
tags:
- claude-code
- ensamblado-condicional
- fuente-no-verificada
- leak
- prompt-assembly
- prompt-composition
- prompt-engineering
- prompts
- single-source
- system-prompt
- unverified
base_confidence: 0.1
half_life_days: 180
last_reinforced: '2026-10-20'
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
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: contradicts
- to: claude-code-system-prompt-sin-datos-de-eficacia
  type: contradicts
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: derived_from
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: claude-code-system-prompt-singleton-rss-engagement-cero
  type: supports
- to: claude-code-system-prompt-conclusion-circular-y-sin-poder-discriminativo
  type: supports
---

## What it is
Un ítem RSS (engagement=0) afirma que el código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de «docenas de partes condicionales». La afirmación llega como resumen de un artículo externo: el texto del prompt, el inventario de condiciones y cualquier muestra reproducible están ausentes del clúster.

## Evidence
- «Claude Code's leaked source reportedly shows a system prompt assembled from dozens of conditional parts.» — source: abf61eeec75462f9
- El ítem es una entrada de feed RSS con engagement=0, sin discusión ni corroboración observada aguas abajo. — source: abf61eeec75462f9

## Why it matters
Es un puntero a leer la fuente primaria, no un hallazgo accionable. Confirma como mucho que el patrón de ensamblado condicional es plausible en un producto comercial de agentes de código, lo que no autoriza cambiar flujos de trabajo ni materiales de docencia.

`relates_to` `ensamblado-condicional-de-prompts`: es una instancia concreta (no verificada) del patrón general. `derived_from` `claude-code-condiciones-que-gatean-secciones-sin-observar`: la pregunta abierta sobre qué condiciones gatean qué secciones es exactamente lo que este documento no responde. `supports` las notas de riesgo sobre singleton y sobre circularidad del leak: comparten la misma base documental única.

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
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- contradicts → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- contradicts → [[claude-code-system-prompt-sin-datos-de-eficacia]]
- derived_from → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- supports → [[claude-code-system-prompt-singleton-rss-engagement-cero]]
- supports → [[claude-code-system-prompt-conclusion-circular-y-sin-poder-discriminativo]]
