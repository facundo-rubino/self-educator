---
id: relevance-1-00-por-keyword-matching-no-por-ajuste-tematico
title: relevance=1.00 probablemente refleja keyword matching en «AI agent», no ajuste
  temático
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-31'
updated: '2026-10-31'
sources:
- 127f90d84154dcf5
- b647bfde274dd2a1
- ee7d97417bb16595
tags:
- scoring-artifact
- relevance
- keyword-matching
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-31'
provenance:
  scale: S
  query: null
links:
- to: how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro
  type: relates_to
- to: relevance-0-67-del-titulo-llm-judge-como-artefacto-lexico
  type: relates_to
---

## What it is
La relevance de 1.00 del clúster probablemente refleja matching de keywords en «AI agent» más que ajuste con la pregunta dev-líder-docente. El score no es validación del clúster.

## Evidence
- El reporte señala que relevance=1.00 del filtro refleja keyword matching en «AI agent», no ajuste topical — fuente: 127f90d84154dcf5, b647bfde274dd2a1, ee7d97417bb16595

## Why it matters
Un tech lead que use este score para priorizar el clúster sobreestima su valor. La relevance alta con novelty cero Y cuerpos ausentes es un artefacto del scorer, no una señal.

Comparte el patrón con los falsos positivos léxicos del filtro en notas previas sobre «LLM patterns» y «LLM-as-a-Judge». Se relaciona con la nota de novelty/relevance como no independientes.

## Links
- relates_to → [[how-to-match-llm-patterns-titulo-como-falso-positivo-lexico-del-filtro]]
- relates_to → [[relevance-0-67-del-titulo-llm-judge-como-artefacto-lexico]]
