---
id: identificacion-de-figuras-publicas-ya-existia
title: La identificación de figuras públicas por modelos multimodales no es nueva
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-25'
sources:
- 19cb8032958cd964
tags:
- afirmacion-de-novedad
- figuras-publicas
- linea-base
- multimodal
- novedad
- politica-de-producto
- privacidad
- rechazo
base_confidence: 0.4
half_life_days: 180
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: afirmacion-de-novedad-sin-linea-base
  type: supports
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: supports
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
---

## What it is
La capacidad de identificar personas en imágenes no es un estado nuevo del arte de los LLM: es una función disponible desde hace años y su presencia o ausencia en un producto concreto está determinada por la política del proveedor, no por un salto de capacidad del modelo. La novedad de cualquier anuncio que la presente como reciente debe medirse contra esa línea base, no contra cero.

## Evidence
- El clúster aporta un único documento de feed RSS [19cb8032958cd964] que afirma que los LLM ya pueden identificar figuras públicas en imágenes.
- El propio documento matiza que ChatGPT y Claude no lo hacen, pero Gemini sí, con lo que la generalización «los LLM» recae sobre un solo producto [19cb8032958cd964].
- El documento no incluye metodología, métricas, fecha ni fuente primaria [19cb8032958cd964].
- El pipeline puntúa la novedad del clúster en 0.00, lo que contradice el encuadre temporal «ya/now» del titular [19cb8032958cd964].

## Why it matters
Si la novedad es 0.00, la afirmación describe una característica ya establecida y no un cambio de estado del arte; tratarla como hallazgo nuevo es una decisión de encuadre, no un dato. Para quien elige agentes multimodales para tareas con imágenes, lo relevante no es «puede o no puede» en abstracto, sino qué proveedor aplica qué filtro en qué versión y región.

Se apoya en `gemini-no-rechaza-nombrar-figuras-publicas`, que es la observación concreta que sostiene la única parte específica de la afirmación. Se relaciona con `politica-de-face-recognition-como-variable-de-producto`: la identificación de personas es una decisión de producto, no una capacidad del modelo. Alimenta el patrón `aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales`, porque fija como criterio de aceptación el proveedor concreto. Es tangencial a `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`. El riesgo `afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion` es la lectura que esta nota corrige.

## Links
- supports → [[afirmacion-de-novedad-sin-linea-base]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
