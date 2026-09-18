---
id: react-for-two-computers-periferico-al-tema-de-agentes
title: '«React for Two Computers»: relevancia periférica al tema de agentes de IA'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-18'
sources:
- dec9f3cc9a87f904
- sig-fade19e1d50a
tags:
- agentes
- brief
- falso-positivo
- matching
- react
- relevancia
- topic-drift
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-tematica-baja-no-es-ruido
  type: relates_to
- to: relevancia-no-es-verdad
  type: relates_to
- to: react-for-two-computers-titulo-sin-contenido-ingerido
  type: relates_to
- to: react-hooks-call-order-como-fundamento-fuera-del-brief
  type: relates_to
- to: why-does-rsc-integrate-with-a-bundler-fuera-del-brief
  type: relates_to
- to: deuda-tecnica-como-puente-lexico-al-brief
  type: relates_to
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
- to: the-two-reacts-ruido-para-el-brief-de-agentes-y-liderazgo
  type: relates_to
- to: react-for-two-computers-etiqueta-react-sin-evidencia-de-practica
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: derived_from
---

## What it is

El documento apunta a React como tema, no a las prácticas de un dev que lidera proyectos y enseña a programar. Con relevance=0.33, el clúster es un falso positivo temático respecto al brief de agentes de IA aplicados a programar, gestionar y enseñar.

## Evidence

- El documento apunta a React como tema, no a las prácticas de un dev que lidera proyectos y enseña a programar — source: dec9f3cc9a87f904
- El cuerpo del documento se limita a «Two things, one origin.», sin desarrollo de argumentos sobre agentes de IA, liderazgo técnico, productividad o enseñanza — source: dec9f3cc9a87f904

## Why it matters

Si el pipeline depende de este clúster para cubrir el brief, no genera hallazgos útiles. La coincidencia con React es tangencial y refuerza el patrón de falsos positivos por vocabulario de infraestructura.

Es el mismo patrón que `the-two-reacts-ruido-para-el-brief-de-agentes-y-liderazgo`. Deriva del riesgo de mismatch por vocabulario genérico (`mismatch-query-tema-por-vocabulario-generico-de-infraestructura`). Contradice parcialmente la nota `relevancia-tematica-baja-no-es-ruido`, que sostiene que baja relevancia temática no equivale a ausencia de señal: aquí, con un documento sin cuerpo y engagement=0, no hay señal extraíble. Se liga al título sin contenido (`react-for-two-computers-titulo-sin-contenido-ingerido`).

## Links
- relates_to → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[react-for-two-computers-titulo-sin-contenido-ingerido]]
- relates_to → [[react-hooks-call-order-como-fundamento-fuera-del-brief]]
- relates_to → [[why-does-rsc-integrate-with-a-bundler-fuera-del-brief]]
- relates_to → [[deuda-tecnica-como-puente-lexico-al-brief]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[the-two-reacts-ruido-para-el-brief-de-agentes-y-liderazgo]]
- relates_to → [[react-for-two-computers-etiqueta-react-sin-evidencia-de-practica]]
- derived_from → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
