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
updated: '2026-10-07'
sources:
- 19cb8032958cd964
tags:
- afirmacion-sin-metodologia
- capacidad
- capacidad-vs-politica
- capacidades-llm
- claim-sin-evidencia
- epistemologia
- evals
- evidencia
- falsa-capacidad
- fuente-unica
- identificacion-de-figuras-publicas
- metodologia
- modo-de-fallo
- multimodal
- politica-de-modelos
- politica-vs-capacidad
- rss
- titular-rss
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-10-07'
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
- to: identificacion-de-figuras-publicas-ya-existia
  type: relates_to
- to: segundo-corpus-necesario-para-afirmar-capacidad-multimodal
  type: supports
- to: legitimidad-de-identificacion-no-implica-practica-de-ingenieria
  type: relates_to
- to: identificacion-de-figuras-publicas-ya-existia
  type: contradicts
- to: relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: derived_from
- to: identificar-no-es-reconocer-en-la-fuente
  type: derived_from
- to: politica-de-face-recognition-como-variable-de-producto
  type: supports
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: derived_from
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: afirmar-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: relates_to
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: segundo-corpus-necesario-para-afirmar-capacidad-multimodal
  type: relates_to
---

## What it is
Tomar un único ítem RSS sobre la negativa de ChatGPT/Claude y la disposición de Gemini a nombrar figuras públicas, y compilarlo como «los LLM ahora identifican figuras públicas», confunde cumplimiento observado con capacidad demostrada. La disposición a responder no prueba la exactitud de la identificación, y el rechazo puede provenir de política, no de incapacidad.

## Evidence
- El clúster contiene un solo documento, sin replicación independiente, sin benchmark y sin tasa de error de identificación de personas no públicas — source: 19cb8032958cd964
- La puntuación de novelty de 0.00 registrada para el clúster indica que la capacidad subyacente no es nueva — source: 19cb8032958cd964

## Why it matters
Es un modo de fallo reproducible del pipeline de compilación: atribuir capacidad desde comportamiento de rechazo es circular. Cualquier afirmación sobre lo que un modelo multimodal puede hacer requiere corpus, versiones y condiciones, y el dato importante no medido aquí es la tasa de falsos positivos al identificar a personas que no son figuras públicas.

Es el modo de fallo del que depende la lectura de `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`. Se alinea con `afirmar-capacidad-desde-fragmento-de-una-linea`, `afirmacion-de-capacidad-multimodal-sin-metodologia`, `afirmacion-de-novedad-sin-linea-base`, `identificar-no-es-reconocer-en-la-fuente` y `segundo-corpus-necesario-para-afirmar-capacidad-multimodal`. Se apoya además en la distinción capacidad/política y no la contradice: la complementa para el caso multimodal.

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
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- supports → [[segundo-corpus-necesario-para-afirmar-capacidad-multimodal]]
- relates_to → [[legitimidad-de-identificacion-no-implica-practica-de-ingenieria]]
- contradicts → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief]]
- derived_from → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- derived_from → [[identificar-no-es-reconocer-en-la-fuente]]
- supports → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
- derived_from → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[afirmar-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- relates_to → [[segundo-corpus-necesario-para-afirmar-capacidad-multimodal]]
