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
updated: '2026-10-15'
sources:
- abf61eeec75462f9
- sig-979a04e33a30
tags:
- claude-code
- evidencia-debil
- ingerimiento
- singleton
- system-prompt
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-10-15'
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
- to: vista-filtrada-de-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: documento-unico-sin-engagement-no-sostiene-claim-sobre-practica
  type: derived_from
---

## What it is
La única evidencia de que el system prompt de Claude Code se ensambla de docenas de partes condicionales proviene de un clúster de un solo documento (abf61eeec75462f9) con engagement 0 y sin corroboración independiente. La atribución de autoridad es al «código fuente filtrado»: no hay artefacto, diff ni traza inspeccionable de forma independiente.

## Evidence
- El clúster contiene un único documento y su engagement reportado es 0 — fuente: sig-979a04e33a30.
- La afirmación se apoya en una fuente filtrada no autorizada, sin verificación independiente — fuente: sig-979a04e33a30.
- El crítico del pipeline marca el razonamiento como circular: «the leaked source shows X» solo se atestigua a sí mismo — fuente: sig-979a04e33a30.

## Why it matters
Cualquier uso de este claim en docencia, configuración de agentes o documentación de equipo queda sin respaldo verificable. El coste de citarlo como hecho es reproducir una fuente filtrada como si tuviera autoridad de ingeniería.

Contradice `claude-code-system-prompt-conditional-composition` en tanto que el claim ya compilado sobre la composición condicional carece de la base de evidencia que sugiere. Se deriva del patrón general `documento-unico-sin-engagement-no-sostiene-claim-sobre-practica` y se relaciona con `vista-filtrada-de-codigo-no-confirma-composicion-condicional`.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- supports → [[leak-sin-autenticidad-establecida]]
- supports → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
- supports → [[afirmar-internals-de-claude-code-como-hecho-seria-especulacion]]
- relates_to → [[vista-filtrada-de-codigo-no-confirma-composicion-condicional]]
- derived_from → [[documento-unico-sin-engagement-no-sostiene-claim-sobre-practica]]
