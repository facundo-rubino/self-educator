---
id: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
title: 'Divergencia de rechazo al nombrar figuras públicas: Gemini sí, ChatGPT y Claude
  no'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 19cb8032958cd964
tags:
- multimodal
- politicas-de-proveedor
- rechazo
- identificacion-facial
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: supports
- to: identificacion-de-figuras-publicas-ya-existia
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
---

## What it is
Un único documento RSS afirma que, ante imágenes con figuras públicas, Gemini las identifica mientras que ChatGPT y Claude se niegan. La afirmación describe una divergencia de política de proveedor, no una capacidad general de los LLM: el documento no distingue si los modelos no pueden o no quieren hacerlo.

## Evidence
- El cuerpo del documento dice, textualmente: «ChatGPT and Claude won't, but Gemini will» sobre identificar figuras públicas en imágenes — source: 19cb8032958cd964
- El título del mismo documento enuncia la afirmación como capacidad general: los LLM ya pueden identificar figuras públicas en imágenes — source: 19cb8032958cd964
- No hay metodología, versión de modelo, fecha, prompt, conjunto de imágenes ni cita de política de proveedor — source: 19cb8032958cd964

## Why it matters
Si se toma al pie de la letra, cualquier feature de subida de imágenes opera con comportamiento dependiente del proveedor y requiere verificación explícita por API, no una asunción de paridad. Pero con una sola fuente sin cuerpo ni corroboración, lo accionable es la cautela: no tratar «Gemini will» como contrato de producto.

Refuerza la nota existente sobre Gemini y figuras públicas, que registra el mismo ítem. Se relaciona con la divergencia de rechazo entre proveedores y con la sonda de rechazo por identidad en producción: es el mismo fenómeno de comportamiento diferenciado por política, no por capacidad. También toca la nota sobre identificación de figuras públicas preexistente y el riesgo de sostener un claim poblacional desde una sola observación de un proveedor.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
