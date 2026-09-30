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
updated: '2026-09-30'
sources:
- 19cb8032958cd964
tags:
- evals
- metodologia
- reproducibilidad
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-30'
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
---

## What it is

Una afirmación de capacidad multimodal —«los LLMs ahora identifican figuras públicas en imágenes»— sin nombre y versión de modelo, sin fecha, sin condiciones de prueba, sin cifras de accuracy y sin baseline no es una afirmación evaluable. El documento se limita al titular; no aporta metodología, ejemplos, enlaces ni mediciones.

## Evidence

- El texto completo del documento es el titular más una frase: sin metodología, ejemplos, enlaces ni mediciones — source: 19cb8032958cd964
- No se especifican versiones de modelo, fecha ni condiciones de prueba — source: 19cb8032958cd964
- engagement=0 y novelty=0.00 en el cluster de un solo documento — source: 19cb8032958cd964

## Why it matters

Sin condiciones no hay forma de reproducir ni de comparar: la capacidad queda declarada, no establecida. La consecuencia práctica de una asimetría observada en una frase es la misma que la de un benchmark de prefill frente a la generación interactiva: el número o la anécdota no informan la tarea real. Verificar por proveedor, con versión y cuenta concretas, es el único paso útil desde esta evidencia.

Se relaciona con «task-specific-llm-evals...»: ambas dependen del alcance declarado como único contenido verificable. Apoya «prueba-con-proveedores-y-cuentas-especificas»: la observación no se generaliza sin versión, cuenta y región. Se relaciona con «benchmark-pp512...» y con «criterio-de-accesibilidad-verificado-con-lector-de-pantalla...»: medir la tarea real, no el sustituto.

## Links
- relates_to → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- supports → [[prueba-con-proveedores-y-cuentas-especificas]]
- relates_to → [[benchmark-pp512-no-informa-generacion-interactiva]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
