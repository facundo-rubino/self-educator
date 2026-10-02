---
id: prueba-con-proveedores-y-cuentas-especificas
title: 'Una política de rechazo observada en una frase no se generaliza: versión,
  cuenta y región la condicionan'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-02'
sources:
- 19cb8032958cd964
tags:
- metodologia
- politica-de-proveedor
- rechazo
- refusal-policy
- reproducibilidad
- vendors
- versionado
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-por-identidad-sin-metodologia-ni-fecha
  type: relates_to
- to: divergencia-de-rechazo-entre-proveedores
  type: relates_to
- to: stale-policy-rip-current-flows
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: probe-de-rechazo-por-identidad-en-produccion
  type: supports
---

## What it is
El reporte describe una divergencia de rechazo entre ChatGPT, Claude y Gemini basada en una sola frase sin fecha, versión, cuenta ni región [19cb8032958cd964]. Esa observación no es generalizable.

## Evidence
- El contraste ChatGPT/Claude vs. Gemini se enuncia sin metodología, fecha ni prompt — source: 19cb8032958cd964

## Why it matters
Las políticas de rechazo cambian con la versión, la cuenta y la región; hay que hacer un spike por proveedor antes de comprometer una feature.

Refuerza el patrón de spike por proveedor para comportamiento de rechazo y la nota específica de divergencia de rechazo. Se apoya en la nota de probe de rechazo por identidad en producción.

## Links
- relates_to → [[divergencia-de-rechazo-por-identidad-sin-metodologia-ni-fecha]]
- relates_to → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[stale-policy-rip-current-flows]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- supports → [[probe-de-rechazo-por-identidad-en-produccion]]
