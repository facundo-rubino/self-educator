---
id: gemini-no-rechaza-nombrar-figuras-publicas
title: Gemini no rechaza nombrar figuras públicas en imágenes, según un ítem RSS
type: actor
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-28'
sources:
- 19cb8032958cd964
tags:
- gemini
- multimodal
- politica-de-proveedor
- rechazo
- vision
base_confidence: 0.15
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: supports
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: supports
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: contradicts
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
- to: prueba-con-proveedores-y-cuentas-especificas
  type: relates_to
---

## What it is
Un ítem RSS reporta que Gemini sí nombra figuras públicas en imágenes mientras ChatGPT y Claude no lo hacen. La observación es una sola y no viene con versión de modelo, cuenta, región ni condiciones de prompt, así que describe un caso, no la conducta actual de ninguno de los tres productos.

## Evidence
- El documento ingerido afirma que ChatGPT y Claude no identifican figuras públicas en imágenes, pero Gemini sí — source: 19cb8032958cd964

## Why it matters
Si se confirma, es un dato de selección de proveedor para cualquier flujo donde la identificación de personas en imágenes sea un requisito. Sin versión ni fecha no se puede saber si sigue siendo cierto hoy, y la conducta de rechazo cambia con frecuencia.

Sostiene a `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`, que registra la asimetría entre Gemini y el resto en el caso específico de figuras públicas. Contradice a `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion` en el sentido de que el titular lo presenta como capacidad universal mientras este actor describe una diferencia de política entre productos concretos. Se relaciona con `divergencia-de-rechazo-entre-proveedores` (mismo prompt, distinta respuesta), con `probe-de-rechazo-por-identidad-en-produccion` como sonda operativa derivable, y con `prueba-con-proveedores-y-cuentas-especificas`, que exige acotar la observación a versión, cuenta y región antes de generalizar.

## Links
- supports → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- supports → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- contradicts → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
- relates_to → [[prueba-con-proveedores-y-cuentas-especificas]]
