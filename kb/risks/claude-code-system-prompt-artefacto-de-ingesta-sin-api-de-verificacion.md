---
id: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
title: La evidencia sobre Claude Code es artefacto de ingesta, no fuente verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-10-02'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- leak
- pipeline
- signal-quality
- verificabilidad
base_confidence: 0.65
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: supports
---

## What it is
El único soporte del claim sobre el system prompt de Claude Code es un documento RSS con engagement=0 y novelty=0.00, cuya procedencia se declara como leak. No hay documentación oficial, inspección reproducible ni verificación independiente. La procedencia «leaked source» es inverificable y podría ser inexacta o quedar obsoleta respecto del producto actual.

## Evidence
- Un solo documento, engagement=0, noveldad=0.00, sin corroboración más allá de un medio-score binario — source: abf61eeec75462f9
- La procedencia declarada es un leak, no documentación oficial ni inspección reproducible — source: abf61eeec75462f9
- El leak no viene acompañado de fragmentos, disparadores ni versión — source: abf61eeec75462f9

## Why it matters
Un leak sin autenticidad establecida no confirma lo que el leak afirma. Cualquier uso de esta nota como base para decisiones de arquitectura de agentes propios debe degradarse a la categoría de anécdota, no de hallazgo.

Contradice la solidez implícita en el claim de composición condicional; refuerza el riesgo general de leaks sin autenticidad. Es la cara de fiabilidad del mismo artefacto que `claude-code-system-prompt-conditional-composition` describe en su cara de contenido.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[validacion-de-senal-por-contenido-no-por-titulo]]
- supports → [[leak-sin-autenticidad-establecida]]
