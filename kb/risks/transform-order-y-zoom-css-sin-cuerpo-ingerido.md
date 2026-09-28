---
id: transform-order-y-zoom-css-sin-cuerpo-ingerido
title: '«Animating zooming using CSS»: la afirmación sobre el orden de transform no
  tiene cuerpo ingerido'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-09-28'
sources:
- b0df1f50a76ba564
tags:
- css
- evidencia
- evidencia-ausente
- falso-positivo
- front-end
- inferencia
- ingesta
- ingesta-truncada
- pipeline
- riesgo
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: mecanica-css-afirmada-desde-solo-titulo-rss
  type: supports
- to: transform-order-en-css-afecta-el-zoom
  type: contradicts
- to: transform-order-solo-importa-con-multiples-funciones
  type: relates_to
- to: post-css-sin-engagement-y-relevancia-tangencial-al-brief
  type: supports
- to: mecanica-css-afirmada-desde-solo-titulo-rss
  type: relates_to
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: relates_to
- to: transform-order-en-css-afecta-el-zoom
  type: supports
- to: transform-order-solo-importa-con-multiples-funciones
  type: supports
- to: post-css-sin-engagement-y-relevancia-tangencial-al-brief
  type: relates_to
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: derived_from
- to: generalizacion-desde-cluster-de-un-solo-documento
  type: relates_to
- to: css-transform-order-importa-solo-a-veces
  type: derived_from
- to: pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss
  type: supports
- to: transform-order-en-css-afecta-el-zoom
  type: derived_from
- to: reconstruir-lecturas-desde-frase-ambigua-two-things-one-origin
  type: relates_to
- to: argumento-ex-silentio-en-corpus-truncado
  type: relates_to
---

## What it is
Riesgo de compilación: la única evidencia de este clúster es un título. Cualquier nota que afirme cómo se comporta el orden de `transform` bajo zoom estaría escrita desde memoria, no desde el documento.

## Evidence
- El clúster tiene un único miembro con engagement=0 y sin cuerpo ingerido — source: b0df1f50a76ba564
- La condicionalidad del título («sometimes») queda sin condiciones especificadas, por lo que no puede confirmarse ni refutarse — source: b0df1f50a76ba564

## Why it matters
Un downstream que cite este clúster sobrestima una fuente única y no leída. Además, la relevancia baja (0.33) frente al brief sugiere que admitirlo diluye el foco en agentes de IA, liderazgo y productividad sin aportar señal.

Deriva de `transform-order-en-css-afecta-el-zoom`, la nota que registra el claim. Comparte modo de fallo con `reconstruir-lecturas-desde-frase-ambigua-two-things-one-origin` (construir lecturas desde un fragmento sin contexto) y con `argumento-ex-silentio-en-corpus-truncado` (tratar ausencia de cuerpo como si autorizara inferencias).

## Links
- supports → [[mecanica-css-afirmada-desde-solo-titulo-rss]]
- contradicts → [[transform-order-en-css-afecta-el-zoom]]
- relates_to → [[transform-order-solo-importa-con-multiples-funciones]]
- supports → [[post-css-sin-engagement-y-relevancia-tangencial-al-brief]]
- relates_to → [[mecanica-css-afirmada-desde-solo-titulo-rss]]
- relates_to → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
- supports → [[transform-order-en-css-afecta-el-zoom]]
- supports → [[transform-order-solo-importa-con-multiples-funciones]]
- relates_to → [[post-css-sin-engagement-y-relevancia-tangencial-al-brief]]
- derived_from → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- relates_to → [[generalizacion-desde-cluster-de-un-solo-documento]]
- derived_from → [[css-transform-order-importa-solo-a-veces]]
- supports → [[pipeline-no-recupera-cuerpo-antes-de-evaluar-clusters-rss]]
- derived_from → [[transform-order-en-css-afecta-el-zoom]]
- relates_to → [[reconstruir-lecturas-desde-frase-ambigua-two-things-one-origin]]
- relates_to → [[argumento-ex-silentio-en-corpus-truncado]]
