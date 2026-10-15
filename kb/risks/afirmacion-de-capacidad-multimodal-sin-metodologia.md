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
updated: '2026-10-15'
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
last_reinforced: '2026-10-15'
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
---

## What it is
Afirmar que «los LLM ahora pueden identificar figuras públicas en imágenes» a partir de un único ítem RSS sin fecha, versión de modelo, condiciones ni reproducción es un sobrealcance. La observación de un proveedor no sostiene un claim poblacional sobre LLM.

## Evidence
- El clúster se apoya en un solo post RSS con engagement cero: sin segunda fuente, sin reproducción, sin fecha y sin versión de modelo fijada — source: sig-237cc97a9794
- El propio documento describe una asimetría de política entre proveedores, no un umbral técnico alcanzado — source: sig-237cc97a9794

## Why it matters
Un claim de capacidad sin metodología no debe entrar en un estándar de equipo ni en un currículo. La acción correcta es verificar en un test controlado antes de que algo derive de él.

Contradice `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor` en el nivel del titular, no del hecho: el hecho reportado es una divergencia de rechazo, no un salto de capacidad. Relacionado con `afirmacion-poblacional-desde-un-solo-proveedor`.

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
