---
id: afirmacion-de-capacidad-multimodal-sin-metodologia
title: Una afirmación de capacidad multimodal sin metodología, versiones ni condiciones
  no es verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-10-12'
sources:
- 19cb8032958cd964
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
last_reinforced: '2026-10-12'
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
---

## What it is
No hay benchmark, versión de modelo, protocolo de evaluación, conjunto de imágenes ni cifra de precisión que distinga un hallazgo real de una capacidad alucinada o una anécdota de proveedor. Sin esos elementos, el claim no es verificable.

## Evidence
- El documento no aporta metodología, ejemplos ni fuentes primarias — source: 19cb8032958cd964
- No se indica cuándo se observó el comportamiento ni con qué versiones, prompts o cuentas — source: 19cb8032958cd964

## Why it matters
Sin protocolo, el comportamiento de rechazo observado en una frase no se generaliza: versión, cuenta y región lo condicionan. Cualquier spike de proveedor debe fijar esas variables antes de citarse en decisiones de equipo o de clase.

Reitera la necesidad de probar con proveedores y cuentas específicas antes de generalizar una política de rechazo observada de forma anecdótica.

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
