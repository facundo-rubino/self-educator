---
id: task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto-nueva-evidencia
title: '«Copyright regurgitation» como categoría de eval: riesgo de producto enunciado,
  no medido'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- 93963a5f93e58d05
tags:
- evals
- copyright
- riesgo-de-producto
- llm
base_confidence: 0.35
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto
  type: relates_to
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
---

## What it is
La regurgitación de contenido con copyright aparece como una de las tareas evaluadas. Que se enumere como categoría de eval señala que el riesgo de emitir texto protegido es un criterio de aceptación para salidas de modelo, pero el documento no aporta medición de incidencia ni método de detección.

## Evidence
- Enumera las tareas cubiertas, incluida la regurgitación de copyright — source: 93963a5f93e58d05

## Why it matters
Para un equipo que usa LLMs en producto, la categoría es un recordatorio de riesgo, no una guía operativa. Un solo documento no sostiene la afirmación de que esta eval «funciona».

Se relaciona con `task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto`, que ya registraba que la categoría toca riesgo de producto sin soporte. Deriva del alcance declarado del documento.

## Links
- relates_to → [[task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
