---
id: overfitting-tematico-desde-mecanica-ajena
title: Inferir prácticas propias desde la mecánica de un sistema ajeno sin evidencia
  de transferibilidad
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-18'
sources:
- abf61eeec75462f9
tags:
- analogia
- extrapolacion
- inferencia
- overfitting
- patrones
- riesgo
- transferibilidad
base_confidence: 0.65
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: a-chain-reaction-metricas-no-son-evidencia-independiente
  type: relates_to
---

## What it is
El reporte propone que si un agente se construye con bloques condicionales, un dev-líder puede replicar el patrón con perfiles por rol («pair programming», «code review», «diseño de ejercicio»). Ese salto es analógico: no hay evidencia en el clúster que conecte la mecánica de un producto con contextos de liderazgo o enseñanza. La utilidad sugerida es especulativa.

## Evidence
- El reporte admite que pasar de «cómo se construye un system prompt de producto» a «cómo liderar, estimar o enseñar» es un salto analógico no respaldado por la evidencia del clúster — source: abf61eeec75462f9
- El critic señala que el movimiento a relevancia analógica es especulativo y sin evidencia que conecte el patrón con contextos educativos o de liderazgo — source: abf61eeec75462f9

## Why it matters
Permite conservar la analogía como hipótesis de diseño sin contarla como hallazgo. Si se promueve a recomendación sin validación, el KB acumula consejos sin respaldo y pierde valor de predicción.

Se relaciona con `claude-code-system-prompt-conditional-composition` como el hecho del que se parte. Se relaciona con `a-chain-reaction-metricas-no-son-evidencia-independiente` como otro caso donde una señal interna del pipeline se trata como evidencia externa.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[a-chain-reaction-metricas-no-son-evidencia-independiente]]
