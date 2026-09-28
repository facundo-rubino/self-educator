---
id: afirmacion-de-capacidad-desde-fragmento-de-una-linea
title: 'Afirmar un salto de capacidad desde una línea sin método: modo de fallo'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-28'
sources:
- 19cb8032958cd964
tags:
- capacidad
- evidencia-delgada
- meta-riesgo
- metodo-ausente
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: contradicts
- to: juicio-fuerte-desde-fragmento-de-dos-lineas
  type: relates_to
- to: afirmacion-poblacional-desde-un-solo-proveedor
  type: relates_to
- to: documento-unico-como-base-de-afirmacion-de-estandar
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
- to: single-document-cluster-engagement-cero-no-generaliza
  type: supports
---

## What it is
Un fragmento de una o dos líneas sin metodología, sin versión de modelo y sin condiciones de prueba no sostiene una afirmación de salto de capacidad. La plausibilidad direccional de una afirmación («los modelos con visión pueden reconocer personas») no es evidencia de que la capacidad haya cambiado ni de cuándo.

## Evidence
- El único documento del clúster enuncia comportamiento diferenciado entre proveedores (ChatGPT/Claude rechazan; Gemini cumple) sin metodología, sin fijación de versión, sin condiciones de prompt ni test reproducible — source: 19cb8032958cd964

## Why it matters
Sin metodología ni versión no hay forma de falsar la afirmación ni de detectar cuándo expira. Cualquier decisión que se apoye en ella (elegir proveedor, prometer una función, diseñar un ejercicio) queda colgada de un comportamiento que puede cambiar en el siguiente release sin aviso.

Es el caso concreto de `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion`; ambas describen el mismo salto indebido de un texto mínimo a una afirmación general, y la segunda es la instancia. Se relaciona con `afirmacion-de-novedad-sin-linea-base` porque el «now» de la afirmación no tiene línea base contra la cual medirse. Se apoya en `single-document-cluster-engagement-cero-no-generaliza`, que establece la insuficiencia estadística del clúster.

## Links
- contradicts → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[juicio-fuerte-desde-fragmento-de-dos-lineas]]
- relates_to → [[afirmacion-poblacional-desde-un-solo-proveedor]]
- relates_to → [[documento-unico-como-base-de-afirmacion-de-estandar]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
- supports → [[single-document-cluster-engagement-cero-no-generaliza]]
