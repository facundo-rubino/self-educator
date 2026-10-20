---
id: claude-code-source-leak-sin-artefacto-primario
title: '«Leaked source» de Claude Code: fuente sin artefacto primario verificable'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-06'
updated: '2026-10-20'
sources:
- abf61eeec75462f9
tags:
- claude-code
- fuente-filtrada
- leak
- provenance
- rss
- unverifiable
- verificabilidad
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-ensamblado-condicional-de-system-prompt
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: supports
- to: leak-sin-autenticidad-establecida-claude-code
  type: supports
- to: claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion
  type: supports
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: supports
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: contradicts
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: view-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
---

## What it is
La provenance del claim es un «leak» afirmado: no hay prompt textual, ni inventario de ramas condicionales, ni muestreo reproducible. Un leak sin autenticidad establecida no puede validar lo que el propio leak afirma.

## Evidence
- El ítem enmarca la afirmación en un código fuente filtrado, sin adjuntar fragmentos ni versión. — source: abf61eeec75462f9
- El crítico señala la ausencia de artefacto primario y califica el claim como no superviviente al escrutinio. — source: abf61eeec75462f9

## Why it matters
Sin artefacto primario no hay verificación: la afirmación podría ser especulativa o parafraseada. Cualquier uso en docencia o configuración de agentes debería esperar a la fuente original.

`contradicts` la nota del claim principal en tanto que la nota afirma como hallazgo algo que esta nota declara no verificable; la contradicción se resuelve en `edu reconcile` con ambas evidencias. `supports` las notas existentes sobre leaks sin autenticidad establecida.

## Links
- relates_to → [[claude-code-ensamblado-condicional-de-system-prompt]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[leak-sin-autenticidad-establecida-claude-code]]
- supports → [[claude-code-system-prompt-artefacto-de-ingesta-sin-api-de-verificacion]]
- supports → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- contradicts → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[view-filtrada-del-codigo-no-confirma-composicion-condicional]]
