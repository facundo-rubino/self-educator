---
id: feed-de-dependencias-no-es-evidencia-de-practica-profesional
title: Un feed de releases de dependencias no es evidencia de práctica profesional
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-25'
sources:
- 16a4e3995d6c827e
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 9750590bbfe6b285
- b9106690f5dfd849
tags:
- evidencia
- firehose
- infraestructura
- metodologia
- off-topic
base_confidence: 0.75
half_life_days: 365
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: mcp-release-stub-sin-changelog
  type: derived_from
- to: mcp-release-bumps-no-revelan-practica-de-ingenieria
  type: supports
- to: mcp-release-stubs-como-artefacto-de-feed
  type: supports
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: supports
---

## What it is
Un conjunto de notas de release autogeneradas registra que se publicaron versiones, no que exista práctica de ingeniería, liderazgo o docencia. El formato (encabezado más lista de bumps) no contiene el tipo de claim que el brief pide.

## Evidence
- Ninguno de los documentos del clúster contiene afirmaciones sobre agentes de IA para programar, estimación, secuenciamiento, alcance, organización personal, oficio de software, productividad ni técnicas de estudio — source: 30a26335a9988ba2
- Los documentos solo registran que paquetes fueron bumpeados a una versión fechada — source: 16a4e3995d6c827e
- Las releases adyacentes se limitan a listas de paquetes sin rationale — source: 9750590bbfe6b285

## Why it matters
Es la razón por la que este clúster no puede sostener ninguna nota sobre cómo un dev que lidera y enseña hace mejor su trabajo. El valor máximo extraíble es describir la cadencia y el formato, no inferir conducta.

`derived_from` la nota sobre release stubs sin changelog: la ausencia de contenido expositivo es lo que invalida tratar el feed como evidencia de práctica.

## Links
- derived_from → [[mcp-release-stub-sin-changelog]]
- supports → [[mcp-release-bumps-no-revelan-practica-de-ingenieria]]
- supports → [[mcp-release-stubs-como-artefacto-de-feed]]
- supports → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
