---
id: claude-code-condiciones-que-gatean-secciones-sin-observar
title: 'Qué condiciones gatean qué secciones en Claude Code: sin observación directa'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- abf61eeec75462f9
tags:
- claude-code
- prompts
- hipotesis
- verificacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
---

## What it is
La afirmación de ensamblado condicional no nombra qué condiciones gatean qué secciones. Determinar la correspondencia requeriría observación directa del comportamiento del agente bajo distintas configuraciones, algo que el cluster no reporta.

## Evidence
- El documento afirma partes condicionales sin nombrar los disparadores — source: abf61eeec75462f9
- No hay en el cluster registro de variación de comportamiento por configuración — source: abf61eeec75462f9

## Why it matters
Es la pregunta que convierte la hipótesis en algo testeable: si las condiciones son observables, el equipo puede diseñar su propio spike. El valor del cluster es haber formulado la hipótesis, no haberla respondido.

Extiende la pregunta ya registrada sobre condiciones no especificadas en el leak de Claude Code y apunta al mismo método que el spike por proveedor antes de comprometer features: observar antes de diseñar sobre la afirmación.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
