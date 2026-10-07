---
id: xml-human-readable-sin-xslt-contexto-no-ingerido
title: El contexto que decidiría «JavaScript en lugar de XSLT» no está ingerido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-10-07'
sources:
- 1bfe45ede61ee575
tags:
- contexto-ausente
- evidence-gap
- evidencia-faltante
- ingesta
- ingesta-truncada
- javascript
- recomendacion-no-generalizable
- xml
- xslt
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: relates_to
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: relates_to
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: supports
- to: xml-pretexto-lexico-javascript-en-el-runtime
  type: supports
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: supports
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: derived_from
- to: ingesta-truncada-como-riesgo-sistemico-de-cobertura
  type: relates_to
---

## What it is
Riesgo de sobreinterpretación cuando se intenta reconstruir la comparación XSLT vs. JavaScript a partir de un ítem cuyo cuerpo entero es «JavaScript is right there.» El contexto —runtime asumido, tipo de documento XML, requisito de presentación— no está ingerido.

## Evidence
- El cuerpo entero del documento es la frase «JavaScript is right there», sin descripción del runtime ni del caso de uso. — source: 1bfe45ede61ee575
- No se aporta método, código, benchmark ni ejemplo que fije el contexto de la afirmación. — source: 1bfe45ede61ee575

## Why it matters
Cualquier lectura concreta de la comparación (por ejemplo, «en el navegador JS ya está disponible, XSLT es redundante») sería fabricación de contexto. El ítem no permite decidir entre varias interpretaciones incompatibles.

Se deriva de `xml-human-readable-without-xslt-afirmacion-sin-cuerpo`, que documenta la ausencia de método. Se relaciona con `xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido` por compartir la misma carencia de cuerpo. Conecta con `ingesta-truncada-como-riesgo-sistemico-de-cobertura` porque este caso es un ejemplo concreto de ese riesgo: el titular sobrevive pero el cuerpo no sostiene ninguna lectura.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
- relates_to → [[xml-human-readable-singleton-engagement-cero]]
- relates_to → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[xml-pretexto-lexico-javascript-en-el-runtime]]
- supports → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- derived_from → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- relates_to → [[ingesta-truncada-como-riesgo-sistemico-de-cobertura]]
