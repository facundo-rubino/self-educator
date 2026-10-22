---
id: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
title: La divergencia de rechazo por identidad no viene con metodología ni fecha
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- chatgpt
- claude
- figuras-publicas
- gemini
- guardrails
- identificacion-facial
- imagenes
- metodologia
- multimodal
- politica-de-modelo
- politica-de-modelos
- politica-de-proveedor
- politicas-de-proveedor
- pregunta-abierta
- proveedores
- rechazo
- rechazo-por-proveedor
- refusal
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-22'
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
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: politica-de-face-recognition-como-variable-de-producto
  type: derived_from
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: contradicts
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: contradicts
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
- to: privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: relates_to
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
- to: asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas
  type: relates_to
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: contradicts
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: derived_from
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: supports
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: prueba-con-proveedores-y-cuentas-especificas
  type: relates_to
- to: politica-de-imagenes-cambia-sin-aviso
  type: relates_to
- to: reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria
  type: relates_to
---

## What it is
No se sabe si la conducta observada depende de la versión del modelo, de la cuenta, de la región, del idioma del prompt o del phrasing exacto. La fuente única no permite atribuir la divergencia a política de producto con confianza.

## Evidence
- El documento solo enuncia «ChatGPT and Claude won't, but Gemini will» sin condiciones de prueba — source: 19cb8032958cd964

## Why it matters
Una política de rechazo observada en una frase no se generaliza. La pregunta abierta es qué condición —proveedor, versión, cuenta, región o prompt— gobierna la respuesta; responderla exige un probe controlado por proveedor.

Deriva de la nota de divergencia de rechazo y se relaciona con la depuración de prompts como problema de ingeniería cuando la conducta depende de muchas condiciones.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- derived_from → [[politica-de-face-recognition-como-variable-de-producto]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- contradicts → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- contradicts → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas]]
- relates_to → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- relates_to → [[asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas]]
- contradicts → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- derived_from → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[prueba-con-proveedores-y-cuentas-especificas]]
- relates_to → [[politica-de-imagenes-cambia-sin-aviso]]
- relates_to → [[reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria]]
