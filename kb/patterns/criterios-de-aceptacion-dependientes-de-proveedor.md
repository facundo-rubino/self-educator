---
id: criterios-de-aceptacion-dependientes-de-proveedor
title: Los criterios de aceptación en features multimodales deben ser dependientes
  del proveedor
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- abf61eeec75462f9
tags:
- evaluación
- proveedores
- features-multimodales
- liderazgo-técnico
base_confidence: 0.4
half_life_days: 365
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: derived_from
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: relates_to
---

## What it is
Si la conducta de un modelo varía entre proveedores —rechazo divergente ante el mismo prompt, políticas distintas ante el mismo input— entonces un criterio de aceptación redactado como «el modelo responde X» no es verificable de forma única. El criterio debe redactarse por proveedor: qué se acepta de cada uno, con qué fallback, bajo qué condición. La evidencia acumulada de divergencia de rechazo sostiene la premisa; esta nota no añade evidencia nueva y su confianza refleja la de esa base.

## Evidence
- Los proveedores divergen en su comportamiento de rechazo ante el mismo prompt, por lo que un criterio único no puede cubrirlos a todos — source: abf61eeec75462f9
- La capacidad técnica de un modelo y su política de rechazo son variables independientes, de modo que un criterio debe fijar cuál de las dos se está evaluando — source: abf61eeec75462f9
- La evidencia disponible no incluye un caso de equipo aplicando criterios por proveedor; la formulación es una derivación de los patrones registrados — source: abf61eeec75462f9

## Why it matters
Un criterio de aceptación único sobre una feature multimodal genera falsos fallos cuando el proveedor cambia de política, y falsos pases cuando el proveedor tolerado responde pero otro no. Escribir el criterio por proveedor convierte una fuente de flakiness en una matriz explícita de aceptación y fallback, revisable en un PR.

`derived_from` → `divergencia-de-rechazo-entre-proveedores`: es la premisa empírica de la que depende el criterio por proveedor. `derived_from` → `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`: obliga a nombrar en el criterio cuál de las dos dimensiones se acepta. `supports` → `spike-por-proveedor-para-comportamiento-de-rechazo`: el spike por proveedor es el instrumento que produce los datos con los que se redacta el criterio. `relates_to` → `eval-especifica-por-tarea-como-infraestructura-de-fiabilidad`: ambos tratan la evaluación como infraestructura que fija lo que se considera funcionar.

## Links
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- derived_from → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
