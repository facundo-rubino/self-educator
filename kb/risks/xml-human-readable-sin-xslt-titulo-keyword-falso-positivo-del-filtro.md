---
id: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
title: El ítem de XML sobrevivió al filtro determinista por solapamiento de keywords
  del título
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- 1bfe45ede61ee575
tags:
- pipeline
- filtrado
- falsos-positivos
- xml
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-solo-afirmacion-javascript
  type: derived_from
- to: xml-human-readable-entra-por-coincidencia-lexica
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: supports
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
---

## What it is
El ítem de XML entró al conjunto evaluado con relevance=0.33, novelty=0.00 y corroboration/velocity/surprise en 0.50 plano — un perfil de ítem de baja información retenido por coincidencia de keywords del título («XML», «human-readable» leídos como tooling de desarrollo). La acción correcta es cerrarlo como falso positivo y revisarlo solo si llegan documentos corroborantes.

## Evidence
- Relevance 0.33, novelty cero y corroboration/velocity/surprise planos en 0.50, consistente con retención por solapamiento de keywords del título — source: 1bfe45ede61ee575
- El ítem es una entrada RSS con engagement=0 — source: 1bfe45ede61ee575

## Why it matters
Refuerza que el filtro determinista deja pasar ítems cuyo único vínculo con el brief es léxico. Compute spend sobre este clúster debe ser cercano a cero; revisitarlo solo ante tutoriales, benchmarks o write-ups reales.

Deriva de la nota que describe el contenido real del ítem. Es evidencia adicional para `xml-human-readable-entra-por-coincidencia-lexica` y `xml-human-readable-singleton-engagement-cero`, y para el patrón general `clustering-por-embedding-produce-falsos-positivos`.

## Links
- derived_from → [[xml-human-readable-sin-xslt-solo-afirmacion-javascript]]
- supports → [[xml-human-readable-entra-por-coincidencia-lexica]]
- supports → [[xml-human-readable-singleton-engagement-cero]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
