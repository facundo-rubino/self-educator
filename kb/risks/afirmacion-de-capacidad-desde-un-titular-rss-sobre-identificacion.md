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
updated: '2026-10-08'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- afirmacion-sin-metodologia
- capacidad
- capacidad-vs-politica
- capacidades-llm
- claim-sin-evidencia
- claim-sin-metodologia
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
- riesgo-de-inferencia
- rss
- titular-rss
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-10-08'
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
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: derived_from
- to: afirmacion-de-novedad-sin-linea-base
  type: supports
- to: privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas
  type: relates_to
---

## What it is
El titular «LLMs can now identify public figures in images» sobre un documento RSS sin cuerpo [19cb8032958cd964] convierte una asimetría de rechazo entre proveedores en una afirmación de capacidad general. El «now» no tiene línea base: no se contrasta con una fecha ni con un modelo previo, y el clúster tiene novelty=0.00 (nada nuevo) y corroboración=0.50 (una sola fuente).

## Evidence
- El documento se limita a un titular sin cuerpo, datos de prueba ni fecha — source: 19cb8032958cd964
- Novelty 0.00 y corroboración 0.50 sin fuentes adicionales — source: sig-237cc97a9794
- El crítico ajusta la confianza a 0.08: lo que sobrevive es «algunos modelos multimodales a veces nombran a personas conocidas» — source: sig-237cc97a9794

## Why it matters
Tomar el titular como verdadero sin prompts, imágenes de prueba ni métricas es el modo de fallo que esta nota marca. Además, «el modelo no rechaza» (política) se lee como «el modelo ahora puede» (capacidad): son afirmaciones distintas con implicaciones distintas. Y la observación de un proveedor no sostiene un claim poblacional sobre LLMs en general. El efecto práctico de colar este ítem en un brief de agentes, liderazgo o docencia es desplazar señal relevante por ruido.

Deriva de `afirmacion-de-capacidad-multimodal-sin-metodologia` —la forma general del modo de fallo— y se apoya en `afirmacion-de-novedad-sin-linea-base`, porque el «now» del titular no se contrasta contra nada. Se relaciona con `identificar-no-es-reconocer-en-la-fuente`, que registra el mismo equívoco en el verbo, y con `privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas`, que apunta a las consecuencias no abordadas del claim.

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
- derived_from → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- supports → [[afirmacion-de-novedad-sin-linea-base]]
- relates_to → [[privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas]]
