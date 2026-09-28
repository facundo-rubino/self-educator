---
id: shadow-roots-mismatch-lexico-clustering-css-frente-brief
title: «Shadow» como falso positivo léxico de clustering frente al brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-28'
sources:
- df4836a1d89bcba4
tags:
- clustering
- css
- falso-positivo
- falso-positivo-clustering
- gating-topico
- matching-lexico
- mismatch-lexico
- shadow-roots
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: derived_from
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: relates_to
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
---

## What it is
La alineación de este clúster con el tema de craft de software es una coincidencia léxica: aparecen los tokens «CSS» e «interactive examples», pero el documento es una instrucción de tarea a una herramienta externa, no un hallazgo, demostración o argumento. El matcher admite el ítem por vocabulario, no por contenido.

## Evidence
- El documento es una instrucción a una herramienta («Fable 5.1 Medium») para construir un artefacto, no un hallazgo, demostración o argumento — source: df4836a1d89bcba4

## Why it matters
Si el objetivo del pipeline es surfacear contenido sustantivo de liderazgo de ingeniería o agentes de IA, este clúster debe downweightarse o removerse: no contribuye señal usable y su presencia puede arrastrar el matching por vocabulario genérico hacia más prompts disfrazados de análisis.

Se relaciona con el singleton sin engagement del mismo ítem. Apoya el patrón conocido de que el clustering por embeddings produce falsos positivos temáticos. Contradice la regla de que relevancia temática baja no equivale a ausencia de señal: aquí la relevancia baja (0.33) sí corresponde a ausencia de señal sobre el brief.

## Links
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- derived_from → [[shadow-roots-live-examples-singleton-sin-engagement]]
- relates_to → [[shadow-roots-live-examples-singleton-sin-engagement]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
