---
id: transform-order-solo-importa-con-multiples-funciones
title: El orden de transform solo importa cuando interactúan varias funciones
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- b0df1f50a76ba564
tags:
- css
- transform
- docencia
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: transform-order-en-css-afecta-el-zoom
  type: relates_to
- to: prompt-modular-sin-mecanica-verificable
  type: relates_to
---

## What it is
La dependencia de orden entre funciones `transform` es condicional: el título fuente la matiza con «sometimes», implicando que no es universal. Solo cabría esperar efecto cuando múltiples funciones transform interactúan (por ejemplo scale más translate, o rotate sobre un origen no por defecto). El documento no explica por qué ni cuándo exactamente.

## Evidence
- El título califica la dependencia de orden como «sometimes», es decir condicional y no universal — source: b0df1f50a76ba564
- No se ingirió cuerpo, ejemplos de código ni contexto de versión de navegador — source: b0df1f50a76ba564

## Why it matters
Encuadrar el gotcha como condicional evita sobre- o subestimar cuándo el orden cambia el render. Es la parte del hallazgo que un docente debería conservar incluso si el resto no se verifica.

Es la cara condicional de `transform-order-en-css-afecta-el-zoom`. Comparte forma con `prompt-modular-sin-mecanica-verificable`: una mecánica plausible afirmada sin comprobación en la evidencia disponible.

## Links
- relates_to → [[transform-order-en-css-afecta-el-zoom]]
- relates_to → [[prompt-modular-sin-mecanica-verificable]]
