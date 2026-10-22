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
updated: '2026-10-22'
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
- riesgo
- vision
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-22'
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
- to: politica-de-reconocimiento-facial-como-variable-de-producto
  type: relates_to
- to: impacto-de-politica-de-imagenes-en-agentes-de-screenshots
  type: relates_to
---

## What it is
Un claim casual de capacidad («ahora pueden identificar figuras públicas») no aborda consentimiento, derechos de imagen, difamación ni tratamiento de personas no públicas que aparezcan en las fotos.

## Evidence
- El documento enuncia la capacidad sin mención a privacidad ni consentimiento — source: 19cb8032958cd964

## Why it matters
En cualquier pipeline de agente que ingiera fotos, la identificación de personas debe ser checkpoint de diseño y review. Ignorar ese paso traslada un riesgo legal y ético al producto.

Se relaciona con la política de reconocimiento facial como variable de producto y con el impacto de la política de imágenes en agentes que procesan screenshots.

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
- relates_to → [[politica-de-reconocimiento-facial-como-variable-de-producto]]
- relates_to → [[impacto-de-politica-de-imagenes-en-agentes-de-screenshots]]
