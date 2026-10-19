---
id: claude-code-ensamblado-condicional-refuerza-prompt-por-contexto-pero-sin-evidencia-de-eficacia
title: El ensamblado condicional de prompts sugiere configurar agentes por contexto,
  sin datos de eficacia
type: pattern
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
- agentes
- prompt-engineering
- configuracion-por-rol
- sin-medicion
base_confidence: 0.35
half_life_days: 365
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
  type: relates_to
- to: ensamblado-condicional-no-implica-mejor-rendimiento
  type: relates_to
---

## What it is
Si los system prompts de producto se ensamblan de partes condicionales, la lectura práctica para un líder técnico es configurar el agente por contexto —rol, herramienta habilitada, etapa del proyecto— en lugar de un prompt monolítico genérico. Es una inferencia de diseño, no un resultado medido: ningún documento del clúster compara prompts monolíticos contra condicionales.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado de docenas de partes condicionales — source: abf61eeec75462f9
- Un líder técnico podría traducir esto en prompts o instrucciones por rol o etapa, pero eso sería extrapolación del analista, no claim del documento — source: abf61eeec75462f9

## Why it matters
Habilita una práctica concreta (instrucciones por rol/etapa) sin comprometerse a una afirmación de mejora de productividad. La ausencia de medición es la parte importante: adoptar la práctica es razonable; citarla como "mejora el rendimiento" sería invención.

`derived_from` el patrón general de ensamblado condicional y de la nota de contenido de Claude Code. Emparenta con `revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico` como recomendación operativa, y con `ensamblado-condicional-no-implica-mejor-rendimiento` como límite explícito.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico]]
- relates_to → [[ensamblado-condicional-no-implica-mejor-rendimiento]]
