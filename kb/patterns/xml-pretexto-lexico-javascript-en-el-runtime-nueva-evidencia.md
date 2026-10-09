---
id: xml-pretexto-lexico-javascript-en-el-runtime-nueva-evidencia
title: '«JavaScript is right there»: el ítem entra al brief por coincidencia léxica,
  no por evidencia de práctica'
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-09'
sources:
- 1bfe45ede61ee575
tags:
- filtro
- clustering
- falso-positivo
- xml
- javascript
base_confidence: 0.6
half_life_days: 365
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: xml-pretexto-lexico-javascript-en-el-runtime
  type: supports
- to: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
  type: supports
- to: relevancia-no-es-verdad
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
---

## What it is
El ítem sobre XML legible sin XSLT sobrevive al filtro determinista porque su titular contiene términos que solapan con el vocabulario del brief («JavaScript», «XML», «sin XSLT»), no porque su contenido cubra ningún eje temático. El cuerpo ingerido —«JavaScript is right there.»— no describe práctica de ingeniería, liderazgo, docencia ni estudio [1bfe45ede61ee575].

## Evidence
- El documento entero es una entrada RSS con engagement=0 y novelty=0.00 cuyo único contenido es «JavaScript is right there.» — source: 1bfe45ede61ee575
- Las puntuaciones del clúster (novelty 0.00 y engagement 0 frente a relevance 0.33 y corroboration/velocity 0.50) describen un ítem familiar y sin respuesta, no un hallazgo — source: 1bfe45ede61ee575

## Why it matters
Refuerza la regla operativa ya establecida: validar la señal por solapamiento de contenido y no por el título. Un ítem que pasa el filtro determinista por keywords del titular infla el conteo de clústeres sin sumar señal compilable. Este caso es una instancia más del mismo modo de fallo.

Es evidencia convergente para `xml-pretexto-lexico-javascript-en-el-runtime` y `xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro`, ambas ya en el grafo. Apoya también la regla general de `validacion-de-senal-por-contenido-no-por-titulo` y el riesgo de `relevancia-no-es-verdad`: que un ítem sea relevante al filtro no lo vuelve evidencia.

## Links
- supports → [[xml-pretexto-lexico-javascript-en-el-runtime]]
- supports → [[xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro]]
- relates_to → [[relevancia-no-es-verdad]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
