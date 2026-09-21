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
updated: '2026-09-21'
sources:
- b0df1f50a76ba564
tags:
- css
- evidencia-ausente
- falso-positivo
- front-end
- riesgo
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-09-21'
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
---

## What it is
El clúster «Animating zooming using CSS: transform order is important… sometimes» es un único documento RSS [b0df1f50a76ba564] del que solo sobrevivieron el título y una glosa de una línea («How to get the right transform animation»). No hay cuerpo, ejemplos de código, versiones de navegador ni benchmarks. Cualquier regla concreta sobre qué orden de `transform` reproduce el comportamiento documentado sería fabricación: no está en la señal ingerida.

## Evidence
- El título enmarca el tema como condicional («sometimes»), no universal — source: b0df1f50a76ba564
- La glosa «How to get the right transform animation» promete guía sin detalle de soporte visible en lo ingerido — source: b0df1f50a76ba564
- El clúster tiene engagement=0 y novelty=0.00: sin corroboración de consumidores del feed — source: (métricas del pipeline sobre b0df1f50a76ba564)

## Why it matters
El modo de fallo aquí es doble. Primero, inferir una regla (p. ej. que cierto orden siempre reproduce el efecto) sería inventar. Segundo, el propio «sometimes» es un hedge que absorbe cualquier contraejemplo: si el orden importa, el claim se sostiene; si no, «sometimes» lo excusa. Sin distinguir orden dentro de una lista de `transform` frente al orden entre `transform` y otras propiedades animadas, el título no es falsable. La lectura honesta es: título de oficio convertido en apariencia de hallazgo.

Alimenta directamente `transform-order-en-css-afecta-el-zoom` y `transform-order-solo-importa-con-multiples-funciones`, que sí formulan el claim condicionado; este risk es el registro de que ese claim no descansa en cuerpo ingerido. Comparte mecanismo con `mecanica-css-afirmada-desde-solo-titulo-rss` y con `afirmar-constraint-de-diseno-desde-solo-titulo-rss` (mismo patrón: mecánica afirmada desde un titular). Se relaciona con `post-css-sin-engagement-y-relevancia-tangencial-al-brief`: relevancia 0.33 y engagement 0 sitúan el ítem en el margen del brief de agentes y liderazgo.

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
