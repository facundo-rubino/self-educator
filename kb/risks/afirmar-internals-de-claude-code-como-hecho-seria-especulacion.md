---
id: afirmar-internals-de-claude-code-como-hecho-seria-especulacion
title: Presentar los internals del system prompt de Claude Code como hecho a un equipo
  o clase sería especulación
type: risk
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
- docencia
- etica
- fuente-no-verificada
- claude-code
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: supports
- to: sobre-generalizacion-desde-claude-code
  type: supports
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: relates_to
---

## What it is
Riesgo de usar el ejemplo de Claude Code como contenido técnico enseñable sin marcar que proviene de una fuente filtrada no verificada. El diseño interno de un producto no es práctica recomendada, y menos si la fuente es un RSS que no muestra el artefacto.

## Evidence
- El documento afirma «leaked source» sin mostrar código ni prompt observado. — source: abf61eeec75462f9
- El propio analista reconoce que no es verificable desde dentro del clúster. — source: abf61eeec75462f9

## Why it matters
Si se enseña, hay que encuadrarlo como patrón arquitectónico general (composición condicional de instrucciones), no como detalle propietario reverse-engineered. Presentarlo como hecho excede lo que la evidencia soporta y arrastra a los estudiantes a repetir un claim no verificado.

Refuerza `claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente`. Coincide con `sobre-generalizacion-desde-claude-code`: el diseño interno de un producto no es la práctica recomendada para agentes propios. Se relaciona con `claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion`.

## Links
- supports → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- supports → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
