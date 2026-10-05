---
id: claude-code-system-prompt-conditional-composition
title: El system prompt de Claude Code se ensambla de partes condicionales
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-10-05'
sources:
- abf61eeec75462f9
tags:
- agentes
- agentes-de-codigo
- agentic-coding
- agents
- claude-code
- claude-code-leak
- composicion-condicional
- composición-condicional
- filtracion
- fuente-unica
- ingenieria-inversa
- leak
- prompt-architecture
- prompt-engineering
- prompting
- prompts-modulares
- system-prompt
base_confidence: 0.12
half_life_days: 180
last_reinforced: '2026-10-05'
provenance:
  scale: M
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: supports
- to: prompt-modular-sin-mecanica-verificable
  type: contradicts
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: supports
- to: system-prompt-como-artefacto-de-ingenieria
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: prompt-condicional-conocimiento-comun-en-productos-llm
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
- to: sobre-generalizacion-desde-claude-code
  type: contradicts
- to: leak-sin-autenticidad-establecida
  type: derived_from
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: leak-de-claude-code-sin-fragmentos-citados
  type: relates_to
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: entrega-de-prompt-monolitico-vs-condicional
  type: relates_to
- to: system-prompt-como-artefacto-de-ingenieria-claude-code
  type: relates_to
- to: claude-code-system-prompt-doc-sin-analisis-de-condiciones
  type: relates_to
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
- to: leak-sin-autenticidad-establecida
  type: supports
- to: claude-code-system-prompt-novelty-cero-ya-conocido
  type: supports
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: supports
---

## What it is
Afirmación de fuente única: el código fuente filtrado de Claude Code revelaría un system prompt ensamblado a partir de «docenas de partes condicionales», no un prompt monolítico. El clúster no expone ninguna de esas partes, su lógica de ensamblado ni sus disparadores. El único hecho verificable dentro del clúster es la existencia del documento y su enunciado.

## Evidence
- El código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales — source: abf61eeec75462f9

## Why it matters
Si se confirmara, implicaría que el comportamiento del agente se compone condicionalmente según contexto activo, y no solo según un texto base. Eso tendría consecuencias para reproducibilidad, estimación y auditoría de agentes internos. Nada de eso está respaldado por evidencia en el clúster: la afirmación se reduce a un rumor plausible sin artefacto chequeable.

Recoge el hilo ya presente en el grafo sobre el ensamblado condicional de prompts y lo extiende al caso Claude Code, pero queda anclado a las notas de alcance que registran la ausencia de condiciones, partes y secuenciación observadas. La nota sobre la vista filtrada del código es el soporte crítico: una vista filtrada no confirma composición condicional. La nota sobre no autenticidad establecida de un leak aplica directamente: sin verificar el artefacto, el leak no confirma lo que dice el leak.

## Links
- supports → [[system-prompt-como-artefacto-de-ingenieria]]
- contradicts → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- supports → [[ensamblado-condicional-de-prompts]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[ensamblado-condicional-de-prompts]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[prompt-condicional-conocimiento-comun-en-productos-llm]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- contradicts → [[sobre-generalizacion-desde-claude-code]]
- derived_from → [[leak-sin-autenticidad-establecida]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- relates_to → [[leak-de-claude-code-sin-fragmentos-citados]]
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[entrega-de-prompt-monolitico-vs-condicional]]
- relates_to → [[system-prompt-como-artefacto-de-ingenieria-claude-code]]
- relates_to → [[claude-code-system-prompt-doc-sin-analisis-de-condiciones]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[claude-code-system-prompt-novelty-cero-ya-conocido]]
- supports → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
