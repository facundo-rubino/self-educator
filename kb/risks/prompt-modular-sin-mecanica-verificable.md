---
id: prompt-modular-sin-mecanica-verificable
title: La modularidad de prompts es plausible pero no verificable en esta evidencia
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- agentic-coding
- evidence-quality
- system-prompt
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: ensamblado-condicional-de-prompts
  type: relates_to
---

## What it is
La afirmación de que los system prompts de agentes serios se componen condicionalmente circula como conocimiento comunitario, pero la evidencia disponible aquí no especifica condiciones, reglas de prioridad ni interacción con herramientas o MCP. Sin mecánica, la afirmación no es falsable.

## Evidence
- No hay detalles técnicos en el documento más allá del titular: no se especifican qué condiciones, cómo se priorizan bloques, ni cómo interactúan con herramientas/MCP — source: abf61eeec75462f9
- Novelty media (0.50): la idea de system prompts compuestos por bloques condicionales ya circula en la comunidad, por lo que el documento confirma lo ya asumido en vez de aportar evidencia nueva — source: abf61eeec75462f9
- El supuesto leak no está citado, ni cotizado, ni verificado; la evidencia es una paráfrasis de titular, no un artefacto técnico — source: abf61eeec75462f9

## Why it matters
Cualquier recomendación de arquitectura de prompts derivada de esta fuente es una apuesta sobre un rumor. El riesgo no es creer algo falso, sino diseñar un ensamblador propio copiando mecanismos que nunca fueron observados.

Contradice `claude-code-system-prompt-conditional-composition` en el sentido operativo de la regla de contradicciones: no niega el hecho, niega que la evidencia lo sostenga. Se relaciona con `ensamblado-condicional-de-prompts` como su versión normativa: el riesgo vive exactamente donde el patrón se aplica sin mecánica verificada.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[ensamblado-condicional-de-prompts]]
