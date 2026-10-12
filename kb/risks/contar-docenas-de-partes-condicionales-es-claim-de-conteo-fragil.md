---
id: contar-docenas-de-partes-condicionales-es-claim-de-conteo-fragil
title: '«Docenas de partes condicionales»: un claim de conteo fácil de errar desde
  fuera'
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
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: contradicts
- to: mecanica-css-afirmada-desde-solo-titulo-rss
  type: supports
---

## What it is
Inferir cuántas partes componen un prompt desde fuera es frágil: el ensamblado puede haber cambiado y un conteo como «docenas de partes condicionales» es fácil de equivocar sin acceso al artefacto.

## Evidence
- El clúster advierte que inferir arquitectura interna desde fuera es frágil: el ensamblado puede cambiar y «docenas de partes condicionales» es un claim de conteo fácil de errar — source: abf61eeec75462f9

## Why it matters
Cualquier cifra o detalle estructural citado de segunda mano debería verificarse contra upstream antes de usarse en docencia o configuración. Un número específico da falsa precisión a un claim sin artefacto.

Contradice el claim de ensamblado condicional al cuestionar su especificidad. Refuerza el riesgo ya presente de afirmar mecánica desde títulos RSS sin cuerpo.

## Links
- contradicts → [[claude-code-system-prompt-conditional-composition]]
- supports → [[mecanica-css-afirmada-desde-solo-titulo-rss]]
