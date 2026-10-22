---
id: evals-por-tipo-de-tarea-como-criterio-de-aceptacion-de-salidas
title: Evals por tipo de tarea como criterio de aceptación de salidas de modelo
type: pattern
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
- llm
- aceptacion
- verificacion
base_confidence: 0.45
half_life_days: 365
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: evals-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
- to: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
  type: relates_to
---

## What it is
El documento apunta a que la evaluación de una salida de modelo debe definirse según la tarea (clasificar, resumir, traducir, evitar copyright, evitar toxicidad), no con una métrica única. Es una propuesta de estructura de verificación, no una medición de su eficacia.

## Evidence
- El documento se presenta como análisis de evals específicas por tarea que funcionan y no funcionan — source: 93963a5f93e58d05
- Enumera las tareas cubiertas — source: 93963a5f93e58d05

## Why it matters
Si se adopta, cambia el criterio de aceptación: cada flujo de LLM necesita su propia rúbrica. Pero el documento no demuestra que ese enfoque funcione mejor que una métrica única; el patrón queda como hipótesis de diseño plausible.

Se relaciona con `evals-especifica-por-tarea-como-infraestructura-de-fiabilidad`, que ya proponía evals específicas como infraestructura de fiabilidad. La analogía con `criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo` es estructural: en ambos casos el criterio de aceptación debe reflejar la tarea, no un atributo de superficie.

## Links
- relates_to → [[evals-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
