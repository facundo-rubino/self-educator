---
id: docenas-de-partes-condicionales-claim-de-conteo-inverificable
title: '«Docenas de partes condicionales»: un claim de conteo sin mecanismo nombrado'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-15'
updated: '2026-10-15'
sources:
- abf61eeec75462f9
- sig-979a04e33a30
tags:
- claude-code
- system-prompt
- claim-inverificable
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-10-15'
provenance:
  scale: XL
  query: null
links:
- to: contar-docenas-de-partes-condicionales-es-claim-de-conteo-fragil
  type: relates_to
- to: claude-code-system-prompt-condicional-singleton-sin-artefacto-primario
  type: derived_from
---

## What it is
La formulación «docenas de partes condicionales» no nombra ensamblador, archivo ni comportamiento en runtime. Sin un mecanismo identificable, el conteo no es falsable y colapsa a la idea genérica de que los prompts de agente son modulares o templated, ya común en ingeniería de LLM antes de este clúster.

## Evidence
- El crítico del reporte señala la frase como vaga e inverificable, sin mecanismo, archivo ni comportamiento en runtime identificados — fuente: sig-979a04e33a30.
- El reporte aguas arriba reformula la misma afirmación sin añadir mecanismo — fuente: abf61eeec75462f9.

## Why it matters
Un conteo inverificable no se puede revisar, testear ni versionar. Presentarlo a un equipo o a una clase como detalle del diseño de un producto lo convierte en folklore técnico.

Se deriva de `claude-code-system-prompt-condicional-singleton-sin-artefacto-primario` y se relaciona con el patrón existente `contar-docenas-de-partes-condicionales-es-claim-de-conteo-fragil`.

## Links
- relates_to → [[contar-docenas-de-partes-condicionales-es-claim-de-conteo-fragil]]
- derived_from → [[claude-code-system-prompt-condicional-singleton-sin-artefacto-primario]]
