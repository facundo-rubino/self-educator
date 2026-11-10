---
id: llm-anthropic-0-31-anade-fable-5-2-y-mythos-5-2
title: llm-anthropic 0.31 añade Fable 5.2 y Mythos 5.2
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-10'
updated: '2026-11-10'
sources:
- a75d770ba6d17355
tags:
- llm-anthropic
- releases
- anthropic
- plugins
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-11-10'
provenance:
  scale: S
  query: null
links:
- to: llm-anthropic-0-29-anuncio-de-release
  type: relates_to
- to: llm-anthropic-0-29-contenido-solo-operativo-sin-claims-sobre-practica
  type: relates_to
- to: release-de-plugin-no-es-evidencia-de-practica
  type: supports
---

## What it is
La versión 0.31 del plugin `llm-anthropic` añade soporte para dos modelos de Anthropic: Fable 5.2 y Mythos 5.2, publicados el mismo día. El efecto operativo es que los prompts pueden ejecutarse contra esos modelos a través de la CLI `llm`; no se documenta ningún cambio de diseño de flujo ni de agente.

## Evidence
- `llm-anthropic` 0.31 añade Fable 5.2 y Mythos 5.2, liberados el mismo día, de modo que los prompts pueden correrse contra esos modelos vía el plugin — source: a75d770ba6d17355

## Why it matters
Para quien usa el plugin, el único ítem accionable es un bump de versión: actualizar da acceso a los nuevos IDs de modelo. No implica cambio de workflow, de diseño de agente ni de práctica de ingeniería.

Es un eslabón más de la serie de anuncios de release de `llm-anthropic` (0.29 previo) y confirma el patrón de que un release de plugin es contenido operativo, no evidencia de práctica profesional.

## Links
- relates_to → [[llm-anthropic-0-29-anuncio-de-release]]
- relates_to → [[llm-anthropic-0-29-contenido-solo-operativo-sin-claims-sobre-practica]]
- supports → [[release-de-plugin-no-es-evidencia-de-practica]]
