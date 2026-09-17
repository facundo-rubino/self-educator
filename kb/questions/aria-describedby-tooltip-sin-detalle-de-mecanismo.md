---
id: aria-describedby-tooltip-sin-detalle-de-mecanismo
title: El fallo de aria-describedby en tooltips no viene con mecanismo ni alcance
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- tooltip
- laguna
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: derived_from
---

## What it is
La evidencia ingerida afirma que `aria-describedby` no siempre alcanza para un tooltip accesible, pero no especifica en qué casos falla, para qué combinaciones de tecnología asistiva y navegador, ni cuál es el fix. La laguna es el hallazgo: el documento aporta el aviso, no la mecánica.

## Evidence
- El corpus ingerido del documento contiene solo título y una frase de cuerpo; no hay código, reproducción ni discusión de semántica de tooltips — source: ded7560510c137bc
- El propio análisis del clúster declara que el documento «no dice en qué casos, para qué combinaciones AT/browser, o cuál es el fix» — source: ded7560510c137bc

## Why it matters
Bloquea cualquier recomendación técnica derivada: afirmar el patrón correcto de tooltip accesible desde este clúster sería fabricar, no citar. Queda como pregunta abierta para una búsqueda dirigida (fuente primaria del autor, guías ARIA de tooltip).

Deriva de `aria-describedby-no-basta-para-tooltips-accesibles`: la nota conceptual fija qué se afirma y esta fija qué falta.

## Links
- derived_from → [[aria-describedby-no-basta-para-tooltips-accesibles]]
