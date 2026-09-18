---
id: control-de-agente-como-composicion-de-secciones
title: 'Control del agente como composición de secciones: inferencia no demostrada'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-18'
sources:
- abf61eeec75462f9
tags:
- agentes
- control-de-agentes
- inferencia
- leak
- riesgo
- riesgo-epistemico
- system-prompt
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
- to: sobre-generalizacion-desde-claude-code
  type: relates_to
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
---

## What it is
Del hecho de que un system prompt se ensamble de partes no se sigue que el control del comportamiento del agente resida en esa composición. El salto de «se ensambla condicionalmente» a «así se controla al agente» no está respaldado por la evidencia del clúster. Es una inferencia plausible pero no demostrada.

## Evidence
- El reporte afirma que el system prompt se ensambla de docenas de partes condicionales, sin detallar el mecanismo de control asociado — source: abf61eeec75462f9
- El leak de Claude Code no especifica condiciones, partes ni secuenciación — source: abf61eeec75462f9

## Why it matters
Evita diseñar agentes propios copiando una arquitectura cuya función real se desconoce. La modularidad puede ser mantenimiento, caching, o experimentación A/B, no control semántico del comportamiento. Tratar la composición como mecanismo de control sin evidencia lleva a invertir esfuerzo en la dimensión equivocada.

Se relaciona con `claude-code-system-prompt-conditional-composition` como la afirmación de la que se infiere de más, con `claude-code-source-leak-conditions-parts-unspecified` por la falta de detalle mecánico, y con `sobre-generalizacion-desde-claude-code` como caso concreto de ese riesgo.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
- relates_to → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
