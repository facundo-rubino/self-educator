---
id: ranking-de-figuras-publicas-sin-metodologia-ni-fecha
title: El claim de identificación de figuras públicas no viene con fecha, versión
  ni condiciones
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-08'
updated: '2026-10-08'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- multimodal
- metodologia-ausente
- pregunta-abierta
base_confidence: 0.2
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: derived_from
- to: prueba-con-proveedores-y-cuentas-especificas
  type: supports
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: relates_to
---

## What it is
El documento [19cb8032958cd964] no especifica qué modelos (ni versions), qué prompts, qué tipo de imágenes, ni cuándo se observó la divergencia entre ChatGPT, Claude y Gemini. Tampoco indica si se probó una caption con nombre frente a un rostro desconocido para el modelo, si la observación provino de interfaz de usuario o de API, ni si dependió de la cuenta o la región. Sin esos datos la observación no es reproducible y no se sabe si sigue vigente.

## Evidence
- Declaración explícita de ausencia de datos de prueba, fecha y enlace a evaluación independiente — source: 19cb8032958cd964
- El crítico ajusta a 0.08 y califica el claim de inestable: la política de rechazo puede cambiar de un día para otro — source: sig-237cc97a9794

## Why it matters
Una política de rechazo observada en una frase no se generaliza: la condicionan versión, cuenta y región. Si algo dependiera de este comportamiento —un flujo que clasifica imágenes, una demo o una clase— habría que probarlo contra el proveedor y la cuenta concretos antes de comprometerlo, y volver a comprobarlo si la política cambia. Mientras no exista ese protocolo, la pregunta queda abierta.

Deriva de `llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia`. Se apoya en `prueba-con-proveedores-y-cuentas-especificas`, que formula exactamente esta limitación: una política observada en una frase no se generaliza. Se relaciona con `spike-por-proveedor-para-comportamiento-de-rechazo` como el patrón práctico que resolvería la pregunta: medir la política por proveedor antes de depender de ella.

## Links
- derived_from → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- supports → [[prueba-con-proveedores-y-cuentas-especificas]]
- relates_to → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
