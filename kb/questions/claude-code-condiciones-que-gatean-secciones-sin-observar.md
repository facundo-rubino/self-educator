---
id: claude-code-condiciones-que-gatean-secciones-sin-observar
title: 'Qué condiciones gatean qué secciones en Claude Code: sin observación directa'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-10-19'
sources:
- abf61eeec75462f9
tags:
- claude-code
- condiciones
- evidencia-debil
- evidencia-faltante
- hipotesis
- observacion
- prompt-engineering
- prompting
- prompts
- system-prompt
- verificacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: control-de-agente-como-composicion-de-secciones
  type: relates_to
- to: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: supports
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: claude-code-system-prompt-singleton-rss-engagement-cero
  type: relates_to
---

## What it is
El documento afirma que hay "docenas de partes condicionales" pero no nombra ninguna condición, ningún disparador, ninguna sección gateada ni el orden de ensamblado. La pregunta abierta es qué contexto activa qué parte del prompt.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado de docenas de partes condicionales — source: abf61eeec75462f9
- El documento no especifica qué condiciones gatean qué secciones ni cómo se secuencian — source: abf61eeec75462f9

## Why it matters
Sin el mapeo condición→sección no se puede ni replicar el diseño ni evaluarlo. Contar partes condicionales es un claim frágil desde fuera; el contenido útil sería el mecanismo, que no está ingerido.

`derived_from` la nota de contenido: registra el hueco exacto que esa nota no cierra. Duplica temáticamente `claude-code-source-leak-condiciones-parts-unspecified`; debe integrarse ahí si aparece nueva evidencia con nombres de condiciones.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[control-de-agente-como-composicion-de-secciones]]
- relates_to → [[revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico]]
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- supports → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[claude-code-system-prompt-singleton-rss-engagement-cero]]
