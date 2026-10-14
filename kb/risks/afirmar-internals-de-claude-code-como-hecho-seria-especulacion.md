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
updated: '2026-10-14'
sources:
- abf61eeec75462f9
tags:
- claude-code
- docencia
- etica
- fuente-no-verificada
- system-prompt
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-14'
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
- to: claude-code-source-leak-sin-artefacto-primario
  type: relates_to
- to: leak-sin-autenticidad-establecida-claude-code
  type: derived_from
---

## What it is
El documento [abf61eeec75462f9] afirma que el código fuente filtrado de Claude Code muestra un system prompt ensamblado a partir de docenas de partes condicionales. El crítico ajusta la confianza a 0.05 y marca el veredicto como WEAK. Con esa base, tratar la composición exacta del prompt como hecho verificable ante un equipo o una clase sería especulación, no reporte de un hallazgo.

## Evidence
- El único documento del clúster [abf61eeec75462f9] afirma el ensamblado condicional citando un leak.
- El crítico señala que el pipeline evalúa clústeres cuyo cuerpo no se recuperó y que no existe segunda fuente independiente: "el documento dice que el leak muestra X".

## Why it matters
Un dev-líder o docente que cite este caso como evidencia de diseño tendría que presentar como hecho una cadena de testimonios no verificados. El coste de equivocarse no es solo factual: erosiona la credibilidad al exponer internals de un producto ajeno que pueden estar desactualizados, incompletos o malinterpretados por el autor del documento.

Depende de `leak-sin-autenticidad-establecida-claude-code`: sin autenticidad establecida, el leak no confirma lo que dice el leak. Se relaciona con `claude-code-source-leak-sin-artefacto-primario`, que documenta la ausencia del artefacto verificable.

## Links
- supports → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- supports → [[sobre-generalizacion-desde-claude-code]]
- relates_to → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- relates_to → [[claude-code-source-leak-sin-artefacto-primario]]
- derived_from → [[leak-sin-autenticidad-establecida-claude-code]]
