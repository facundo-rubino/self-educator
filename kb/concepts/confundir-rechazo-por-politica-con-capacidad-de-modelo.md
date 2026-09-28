---
id: confundir-rechazo-por-politica-con-capacidad-de-modelo
title: 'Confundir rechazo por política con capacidad: «won''t» no es «can now»'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- 19cb8032958cd964
tags:
- politica-vs-capacidad
- rechazo
- vision
base_confidence: 0.7
half_life_days: 180
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: relates_to
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: supports
---

## What it is
Que un proveedor no identifique figuras públicas en una imagen puede ser elección de política de producto, no límite de capacidad del modelo. «No lo hace» y «no puede hacerlo» son afirmaciones distintas, con evidencia y caducidad distintas: la política cambia por versión, región, nivel de cuenta y UI; la capacidad cambia por entrenamiento y arquitectura.

## Evidence
- La afirmación ingerida presenta como capacidad nueva («LLMs can now identify public figures in images») un comportamiento que en realidad describe sobre todo divergencia de rechazo entre proveedores (ChatGPT y Claude rechazan; Gemini cumple) — source: 19cb8032958cd964

## Why it matters
Sobre esta confusión se apoyan dos errores simétricos: prometer una función porque «ahora ya se puede» cuando solo cambió una política, y descartar una función porque «no lo hace» cuando solo la bloquea un filtro de un proveedor concreto. La distinción determina si un test de aceptación es estable o caduca al siguiente release.

Es la instancia concreta de `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`, aplicada al caso de visión. Se relaciona con `criterios-de-aceptacion-dependientes-de-proveedor` porque los criterios que dependen del rechazo deben serlo, y con `spike-por-proveedor-para-comportamiento-de-rechazo`, que es la práctica que se deriva de esta distinción.

## Links
- relates_to → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- relates_to → [[criterios-de-aceptacion-dependientes-de-proveedor]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- supports → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
