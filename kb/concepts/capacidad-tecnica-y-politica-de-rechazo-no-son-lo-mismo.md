---
id: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
title: Capacidad técnica y política de rechazo no son lo mismo
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
- politicas-de-modelo
- rechazo
- capacidad-vs-politica
- multimodal
base_confidence: 0.65
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
---

## What it is
Que un modelo se niegue a realizar una acción no implica que no pueda hacerla. El rechazo puede ser una decisión de política del proveedor sobre una capacidad que el modelo conserva. Leer «no lo hará» como «no puede» o como «ahora puede» invierte la relación entre capacidad y política.

## Evidence
- El crítico señala que un modelo puede rechazar por política conservando la capacidad subyacente, o identificar en algunos contextos y no en otros — source: 19cb8032958cd964
- El mismo documento que reporta la divergencia entre proveedores no cita ninguna política publicada ni benchmark que separe capacidad de decisión — source: 19cb8032958cd964

## Why it matters
Define qué evidencia haría falta para afirmar un salto de capacidad: no una conducta observada puntual, sino aislamiento de la política (prompt directo, API vs. app, contexto). Sin esa separación, cualquier titular sobre «los LLM ahora pueden X» es ambiguo en el eje que importa.

Es la distinción que hace ilegible el titular de la nota sobre divergencia de rechazo al nombrar figuras públicas. Conecta con la nota sobre qué significa «identificar» en la fuente (no rechazar ≠ reconocer) y con la sonda de rechazo por identidad como método para separar ambos ejes.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
