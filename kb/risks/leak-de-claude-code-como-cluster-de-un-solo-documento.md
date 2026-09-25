---
id: leak-de-claude-code-como-cluster-de-un-solo-documento
title: El clúster de Claude Code se sostiene en un único documento con engagement=0
  y novelty=0.00
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-25'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia
- evidencia-debil
- pipeline
- riesgo
- singleton
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: single-document-cluster-engagement-cero-no-generaliza
  type: derived_from
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: relates_to
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: supports
- to: promocion-personal-no-es-evidencia-de-practica
  type: relates_to
- to: ausencia-de-datos-temporales-y-engagement-limita-inferencia
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: relates_to
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: relates_to
---

## What it is
El clúster sobre el system prompt de Claude Code contiene un único documento (abf61eeec75462f9), servido por una fuente agregada con engagement=0, novelty=0.00 y corroboración 0.50. No hay una segunda pieza que confirme la afirmación ni métricas de interacción que indiquen que alguien la haya atendido.

## Evidence
- El clúster se compone de un solo documento, con engagement=0 y novelty=0.00 — source: abf61eeec75462f9

## Why it matters
Un clúster de un documento sin engagement no sostiene una afirmación sobre práctica de ingeniería: es un enlace desatendido, no un hallazgo. La puntuación de corroboración 0.50 no compensa la ausencia de una segunda fuente independiente.

Se refiere al enunciado en `claude-code-system-prompt-conditional-composition`. `generalizacion-desde-cluster-de-un-solo-documento` y `documento-unico-sin-engagement-no-sostiene-claim-sobre-practica` generalizan la pauta. `corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente` matiza que una corroboración de 0.50 no equivale a confirmación externa.

## Links
- derived_from → [[single-document-cluster-engagement-cero-no-generaliza]]
- relates_to → [[generalizacion-desde-cluster-de-un-solo-documento]]
- supports → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- relates_to → [[promocion-personal-no-es-evidencia-de-practica]]
- relates_to → [[ausencia-de-datos-temporales-y-engagement-limita-inferencia]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- relates_to → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
