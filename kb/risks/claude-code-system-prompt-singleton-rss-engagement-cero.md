---
id: claude-code-system-prompt-singleton-rss-engagement-cero
title: 'Claude Code (system prompt): singleton RSS con engagement cero'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-19'
updated: '2026-10-19'
sources:
- abf61eeec75462f9
tags:
- calidad-de-evidencia
- rss
- n-1
- engagement-cero
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-19'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso
  type: derived_from
- to: documento-unico-con-engagement-cero-no-sostiene-practica-de-ensamblado-condicional
  type: relates_to
- to: claude-code-cluster-singleton-sin-corroboracion
  type: relates_to
---

## What it is
La evidencia del clúster es n=1: un solo ítem RSS [abf61eeec75462f9] con engagement nulo y novelty declarada 0.00. Corroboración=0.50 en un clúster de un documento no es consenso entre fuentes; es el valor por defecto de una muestra sin pares.

## Evidence
- El clúster contiene un único documento [abf61eeec75462f9], una nota RSS de engagement nulo — source: abf61eeec75462f9
- La novelty declarada es 0.00, lo que indica que el pipeline no lo considera información nueva — source: abf61eeec75462f9

## Why it matters
Tomar este ítem como base de decisión sobre arquitectura de prompts sería sobrepeso sobre una fuente sin verificación externa. El valor informativo marginal es bajo y la única lectura superviviente es "los prompts condicionales son un patrón", que es conocimiento de fondo, no un hallazgo sobre Claude Code.

`contradicts` la nota de contenido: el documento afirma algo específico, pero la base que lo sostiene no lo respalda. `derived_from` la regla general sobre corroboración en clústeres de un solo documento; familia con las demás notas de singleton sin corroboración de Claude Code.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- derived_from → [[corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso]]
- relates_to → [[documento-unico-con-engagement-cero-no-sostiene-practica-de-ensamblado-condicional]]
- relates_to → [[claude-code-cluster-singleton-sin-corroboracion]]
