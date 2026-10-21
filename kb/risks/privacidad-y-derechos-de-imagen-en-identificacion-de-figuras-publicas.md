---
id: privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas
title: 'Identificación de figuras públicas: privacidad y derechos de imagen sin abordar'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-10-21'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- consentimiento
- derechos-de-imagen
- docencia
- etica
- face-recognition
- gdpr
- imagenes
- multimodal
- privacidad
- vision
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia
  type: relates_to
- to: nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria
  type: derived_from
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: riezgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
- to: privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia
  type: supports
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
---

## What it is
El ítem trata la identificación de figuras públicas como hecho de capacidad; no discute consentimiento, derechos de imagen ni qué ocurre con personas que no son figuras públicas. El hueco no es accidental del documento, pero sí relevante para quien adopte la función.

## Evidence
- El documento se limita a contrastar la conducta de ChatGPT/Claude frente a Gemini, sin apartado de consentimiento ni de derechos de imagen — source: 19cb8032958cd964

## Why it matters
En docencia de programación, usar imágenes de personas reales en demos o ejercicios con reconocimiento facial es una decisión con obligaciones legales y éticas. Un dev-líder que enseña puede convertir este hueco en ejercicio de discusión, no en feature adoptada.

Se apoya en `gemini-no-rechaza-nombrar-figuras-publicas` y conecta con `privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia`, que registra el mismo riesgo en el aula. Depende de `politica-de-face-recognition-como-variable-de-producto` para entender por qué el comportamiento no es estable.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- derived_from → [[nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- relates_to → [[riezgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes]]
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- supports → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
