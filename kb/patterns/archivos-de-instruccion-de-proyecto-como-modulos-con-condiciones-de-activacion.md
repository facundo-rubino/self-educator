---
id: archivos-de-instruccion-de-proyecto-como-modulos-con-condiciones-de-activacion
title: Archivos de instrucción de proyecto (CLAUDE.md, roles de agente) como módulos
  con condiciones de activación
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- abf61eeec75462f9
tags:
- agentes
- claude-code
- configuracion
- depurabilidad
base_confidence: 0.2
half_life_days: 365
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: ensamblado-condicional-de-prompts
  type: derived_from
- to: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
  type: supports
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: supports
---

## What it is
Consecuencia operativa del modelo de ensamblado condicional: escribir los archivos de instrucción de proyecto (estilo CLAUDE.md, archivos de rol de agente) como módulos componibles con condiciones de activación explícitas, e inspeccionar qué se inyectó realmente antes de depurar «el modelo ignoró mis instrucciones».

## Evidence
- Derivado del claim único de que el system prompt de Claude Code se ensambla de partes condicionales. — source: abf61eeec75462f9
- El mismo documento es un RSS con engagement=0, sin corroboración independiente. — source: abf61eeec75462f9

## Why it matters
Convierte un fallo aparente de modelo en un problema de configuración: ¿qué rama no se activó? Sin un mecanismo para inspeccionar lo ensamblado, se pierde depurabilidad — el mismo problema que un sistema de build opaco. La recomendación es condicional a que el ensamblado condicional sea real, y la evidencia aquí no lo verifica.

Se deriva de `ensamblado-condicional-de-prompts`. Refuerza `revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico` y se relaciona con `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes`: si la conducta depende de condiciones, la regresión debe probar cada condición. Hereda su base del claim único sobre Claude Code.

## Links
- derived_from → [[ensamblado-condicional-de-prompts]]
- supports → [[revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- supports → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
