---
id: afirmacion-de-capacidad-multimodal-sin-metodologia
title: Una afirmación de capacidad multimodal sin metodología no es verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- capacidad-multimodal
- claim-sin-metodologia
- evals
- metodologia
- multimodal
- reproducibilidad
- riesgo
- verificabilidad
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: relates_to
- to: prueba-con-proveedores-y-cuentas-especificas
  type: supports
- to: benchmark-pp512-no-informa-generacion-interactiva
  type: relates_to
- to: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: derived_from
- to: segundo-corpus-necesario-para-afirmar-capacidad-multimodal
  type: relates_to
- to: divergencia-de-rechazo-por-identidad-sin-metodologia-ni-fecha
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: supports
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: supports
- to: ranking-de-figuras-publicas-sin-metodologia-ni-fecha
  type: relates_to
- to: verificar-features-de-tooling-antes-de-citar-en-docencia-o-config
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: contradicts
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: llms-identifican-figuras-publicas-sin-metodologia
  type: supports
- to: caso-multimodal-como-ejemplo-de-politica-vs-capacidad
  type: contradicts
---

## What it is
El ítem es un titular RSS con engagement cero y novelty cero; no trae error rate, condiciones de prueba, versiones de modelo ni verificación independiente. No es base para afirmar una capacidad poblacional de los LLMs.

## Evidence
- La evidencia disponible son dos frases atribuidas al documento 19cb8032958cd964, una de ellas un contraste de proveedores
- El crítico califica la señal de WEAK y ajusta la confianza a 0.12 — source: sig-237cc97a9794

## Why it matters
Tratar el titular como hallazgo produce una inferencia circular: la fuente afirma el claim y el claim cita la fuente. La divergencia de política es plausible pero no demostrada, y podría deberse a capacidad, a tolerancia al riesgo o a dependencia del prompt.

Respalda la nota de identificación sin metodología y contradice el uso del caso como ejemplo cerrado en docencia.

## Links
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- supports → [[prueba-con-proveedores-y-cuentas-especificas]]
- relates_to → [[benchmark-pp512-no-informa-generacion-interactiva]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
- derived_from → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[segundo-corpus-necesario-para-afirmar-capacidad-multimodal]]
- relates_to → [[divergencia-de-rechazo-por-identidad-sin-metodologia-ni-fecha]]
- supports → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- supports → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- relates_to → [[ranking-de-figuras-publicas-sin-metodologia-ni-fecha]]
- relates_to → [[verificar-features-de-tooling-antes-de-citar-en-docencia-o-config]]
- contradicts → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- supports → [[llms-identifican-figuras-publicas-sin-metodologia]]
- contradicts → [[caso-multimodal-como-ejemplo-de-politica-vs-capacidad]]
