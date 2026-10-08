---
id: tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado
title: 'El caso de tooltip llega solo como título y un fragmento: cuerpo truncado'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-10-08'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- evidencia-insuficiente
- ingesta
- pipeline
- tooltip
- truncamiento
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: derived_from
- to: fixing-my-tooltip-accessibility-mistake-titulo-sin-contenido-ingerido
  type: relates_to
- to: inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion
  type: relates_to
- to: tooltip-accessibility-aria-describedby-insuficiente-sin-detalle
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: supports
---

## What it is
El documento de tooltip accessibility ingerido contiene únicamente título y una línea de tesis; no sobrevivieron cuerpo, ejemplos de código ni detalles técnicos. Cualquier generalización posterior desde este clúster se apoya sobre un artefacto de extracción incompleta.

## Evidence
- El contenido ingerido se reduce a título más una línea; sin código, WCAG, pruebas de lector de pantalla ni remediación — source: ded7560510c137bc
- La aserción «aria-describedby isn't always enough» funciona como tesis reciclada, no como hallazgo con metodología — source: ded7560510c137bc

## Why it matters
Confundir el titular con el contenido real del artículo introduce riesgo de misrepresentar un argumento que puede ser mucho más estrecho o más amplio que su extracto.

Se apoya en `pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss` e `ingesta-truncada-como-riesgo-sistemico-de-cobertura`: mismo patrón de ingestión incompleta. Relacionado con `tooltip-accessibility-aria-describedby-insuficiente-sin-detalle`, que documenta el caso.

## Links
- derived_from → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
- relates_to → [[fixing-my-tooltip-accessibility-mistake-titulo-sin-contenido-ingerido]]
- relates_to → [[inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion]]
- relates_to → [[tooltip-accessibility-aria-describedby-insuficiente-sin-detalle]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- supports → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
