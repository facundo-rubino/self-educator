---
id: tooltip-accesible-no-basta-con-aria-describedby
title: Un tooltip no queda accesible solo con aria-describedby
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-09-29'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- front-end
- frontend
- tooltips
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: aria-describedby-tooltip-sin-detalle-de-mecanismo
  type: relates_to
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: relates_to
- to: accesibilidad-de-tooltip-no-cubre-ejes-del-brief-de-agentes-y-liderazgo
  type: supports
- to: accesibilidad-de-tooltip-sin-corroboracion-ni-engagement-no-es-hallazgo
  type: relates_to
- to: generalizacion-desde-tooltip-accessibility-singleton-engagement-cero
  type: relates_to
---

## What it is
Implementar un tooltip apoyándose únicamente en `aria-describedby` no basta para que sea accesible. El fragmento recuperado de la fuente enuncia la premisa «aria-describedby isn't always enough» [ded7560510c137bc], pero no desarrolla mecanismo, alcance ni la alternativa correcta.

## Evidence
- El único contenido recuperable del documento es el título «Fixing my tooltip accessibility mistake» y el fragmento «aria-describedby isn't always enough» — source: ded7560510c137bc
- El ítem registra engagement 0 en el dataset ingerido — source: ded7560510c137bc

## Why it matters
Es una lección de oficio de nivel front-end: asumir que un solo atributo ARIA satisface un requisito de accesibilidad es un error de implementación documentado, no una afirmación sobre agentes de IA, liderazgo técnico ni técnicas de estudio.

El caso es una corrección de implementación de fuente única. No hay corroboración independiente: ver `accesibilidad-de-tooltip-sin-corroboracion-ni-engagement-no-es-hallazgo` para por qué este ítem no escala a hallazgo, y `generalizacion-desde-tooltip-accessibility-singleton-engagement-cero` para el límite de generalización. La nota preexistente `accesibilidad-de-tooltip-no-cubre-ejes-del-brief-de-agentes-y-liderazgo` ya fija que este tema no cubre los ejes del brief.

## Links
- relates_to → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- supports → [[accesibilidad-de-tooltip-no-cubre-ejes-del-brief-de-agentes-y-liderazgo]]
- relates_to → [[accesibilidad-de-tooltip-sin-corroboracion-ni-engagement-no-es-hallazgo]]
- relates_to → [[generalizacion-desde-tooltip-accessibility-singleton-engagement-cero]]
