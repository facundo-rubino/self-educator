---
id: errores-silenciosos-acumulados-en-flujos-agenticos-de-dias
title: Errores silenciosos acumulados en flujos agénticos de días
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-04'
updated: '2026-11-04'
sources:
- 5e81338675ea4d09
tags:
- agentes
- long-horizon
- evaluacion
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-11-04'
provenance:
  scale: S
  query: null
links:
- to: flujos-agenticos-de-varios-dias-como-horizonte-de-delegacion
  type: contradicts
- to: eval-especifica-por-tarea-como-infraestructura-de-fiabilidad
  type: supports
- to: tiempo-de-depuracion-a-ciegas-como-partida-de-estimacion-bajo-sin-trazas
  type: relates_to
---

## What it is
Un flujo agéntico de días acumula errores sin que nadie los vea hasta el resultado final. Sin evaluación intermedia, el dev-líder puede gastar más tiempo auditando la salida que haciendo el trabajo él mismo.

## Evidence
- Se describen flujos agénticos que abarcan varios días, no solo tareas puntuales — fuente: 5e81338675ea4d09

## Why it matters
El horizonte largo traslada el coste de la ejecución a la auditoría. La mitigación es diseñar criterios de aceptación por hito antes de lanzar el agente, lo que conecta con estimación y secuenciamiento de proyectos chicos.

Contradice la lectura del horizonte largo como ganancia limpia. Se apoya en la nota sobre eval específica por tarea como infraestructura de fiabilidad y se relaciona con presupuestar depuración a ciegas.

## Links
- contradicts → [[flujos-agenticos-de-varios-dias-como-horizonte-de-delegacion]]
- supports → [[eval-especifica-por-tarea-como-infraestructura-de-fiabilidad]]
- relates_to → [[tiempo-de-depuracion-a-ciegas-como-partida-de-estimacion-bajo-sin-trazas]]
