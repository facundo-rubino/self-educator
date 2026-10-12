---
id: claude-code-system-prompt-condicional-singleton-sin-artefacto-primario
title: 'El claim de ensamblado condicional en Claude Code: singleton sin artefacto
  primario'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-12'
updated: '2026-10-12'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia-debil
- ingerimiento
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: leak-sin-autenticidad-establecida
  type: supports
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: supports
- to: afirmar-internals-de-claude-code-como-hecho-seria-especulacion
  type: supports
---

## What it is
Todo el hallazgo descansa en un solo doc_id [abf61eeec75462f9] cuyo único fundamento es una apelación a material «filtrado» ausente del clúster. No hay segundo doc_id, ni citas de código, ni artefacto primario inspeccionable.

## Evidence
- El hallazgo completo depende de un único doc_id — source: abf61eeec75462f9
- El ítem es RSS con engagement=0 y novelty=0.00, lo que indica bajo alcance y ausencia de información nueva frente al conocimiento previo — source: abf61eeec75462f9
- El artefacto subyacente («código filtrado») no está presente en el clúster, por lo que el claim no es verificable contra un documento primario — source: abf61eeec75462f9

## Why it matters
Es un caso de oído de oído: el analista no puede inspeccionar la fuente, no puede citar código y no puede corroborar con un segundo doc_id. El encuadre de «código filtrado» presta autoridad a un objeto inaccesible para sostener un claim arquitectónico. Un dev o docente no debería tratarlo como evidencia de cómo está construido ningún agente concreto.

Contradice directamente el claim de ensamblado condicional al negarle soporte. Refuerza los riesgos ya existentes sobre leaks sin autenticidad establecida y sobre documentos únicos sin engagement que no sostienen claims de práctica. Refuerza también la nota sobre afirmar internals de Claude Code como hecho.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- supports → [[afirmar-internals-de-claude-code-como-hecho-seria-especulacion]]
