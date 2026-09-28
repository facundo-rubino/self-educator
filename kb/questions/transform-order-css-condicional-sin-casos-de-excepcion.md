---
id: transform-order-css-condicional-sin-casos-de-excepcion
title: 'El orden de transform «importa a veces»: regla enunciada sin casos de excepción'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- b0df1f50a76ba564
tags:
- css
- transform
- pregunta-abierta
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: transform-order-en-css-afecta-el-zoom
  type: derived_from
- to: orden-de-transform-importa-a-veces-sin-detalle-de-casos
  type: supports
---

## What it is
Pregunta abierta: si el orden de `transform` solo importa «a veces» durante el zoom animado, ¿qué condiciones separan los casos en que importa de los que no? El documento no las enumera.

## Evidence
- El título enuncia la regla con un hedge condicional sin especificar condiciones — source: b0df1f50a76ba564
- No hay cuerpo ingerido del que extraer ejemplos (translate-then-scale vs scale-then-translate, interacción con `transform-origin`) — source: b0df1f50a76ba564

## Why it matters
Una regla hedged sin condiciones es infalsable: no puede testearse ni contradecirse. Para usarla como material de docencia haría falta primero recuperar el artículo y sus ejemplos concretos.

Deriva de `transform-order-en-css-afecta-el-zoom` y es el mismo hueco de detalle que ya registra `orden-de-transform-importa-a-veces-sin-detalle-de-casos` para la regla general de orden de transform.

## Links
- derived_from → [[transform-order-en-css-afecta-el-zoom]]
- supports → [[orden-de-transform-importa-a-veces-sin-detalle-de-casos]]
