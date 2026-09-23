---
id: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
title: 'Afirmar «LLMs can now identify public figures» desde un titular RSS: capacidad
  confundida con cumplimiento'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-23'
sources:
- 19cb8032958cd964
tags:
- capacidad
- capacidad-vs-politica
- epistemologia
- evidencia
- falsa-capacidad
- fuente-unica
- modo-de-fallo
- multimodal
- politica-de-modelos
- titular-rss
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: una-observacion-no-sostiene-claim-poblacional-sobre-llm
  type: relates_to
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: contradicts
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
---

## What it is
Leer el titular «LLMs can now identify public figures in images» como hallazgo de capacidad es un non sequitur: una negativa del proveedor es una decisión de política de producto, no prueba de incapacidad técnica. El ítem además no desambigua «identify» entre reconocer, emparejar con una base y nombrar en la salida.

## Evidence
- El único contenido es el titular y una frase de cuerpo; no hay benchmark, protocolo fechado, captura, prompt reproducido ni replicación independiente. — source: 19cb8032958cd964
- El ítem carece de fechas y versiones de modelo, por lo que no puede sostener una afirmación en presente («now»). — source: 19cb8032958cd964
- La afirmación mezcla reconocimiento (el modelo sabe quién es) con cumplimiento de política (el proveedor decide si responde con identidad). — source: 19cb8032958cd964

## Why it matters
Es el modo de fallo canónico de este clúster: confundir un «no» de política con un «no puedo» de capacidad, y sostener una afirmación poblacional sobre LLM desde un proveedor con una única observación sin método. La confianza calibrada del ítem es 0.08.

Contradice `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`: el concepto sostiene una lectura de política, este riesgo señala que la lectura de capacidad no está licenciada por la fuente. Se apoya en `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`, que es el principio que la afirmación viola.

## Links
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[una-observacion-no-sostiene-claim-poblacional-sobre-llm]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- contradicts → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
