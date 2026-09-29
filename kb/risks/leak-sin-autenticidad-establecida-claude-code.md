---
id: leak-sin-autenticidad-establecida-claude-code
title: Un leak sin autenticidad establecida no confirma lo que dice el leak
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidence-quality
- provenance
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: leak-sin-autenticidad-establecida
  type: relates_to
---

## What it is
La palabra «leaked» hace todo el trabajo probatorio del claim sin aportar verificabilidad. Material filtrado puede estar desactualizado, ser parcial o haber sido alterado, y nada en el clúster permite comprobarlo.

## Evidence
- El documento fuente referencia un leak cuya procedencia no es verificable dentro del clúster — source: abf61eeec75462f9
- No existe documento de corroboración en el clúster (corroboration 0.50) — source: abf61eeec75462f9

## Why it matters
Es la razón por la que la confianza del hallazgo debe quedarse en ~0.24 y no inflarse: la carga probatoria recae en un término, no en un artefacto.

Contradice la solidez implícita de `claude-code-system-prompt-conditional-composition` y reutiliza el riesgo ya registrado en `leak-sin-autenticidad-establecida`, aplicado ahora al caso concreto de Claude Code.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[leak-sin-autenticidad-establecida]]
