---
id: precio-de-token-no-es-coste-total-de-tarea
title: El precio por token no es el coste por tarea completada
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-26'
updated: '2026-10-26'
sources:
- aa8b1e11c47162e3
tags:
- coste-llm
- coste-por-tarea
- inferencia
- evaluacion-practica
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-10-26'
provenance:
  scale: S
  query: null
links:
- to: coste-real-de-un-token-como-gancho-editorial
  type: derived_from
- to: corte-de-precios-llm-80-por-ciento-pregunta-sin-evidencia
  type: relates_to
---

## What it is
El precio de catálogo por token no equivale al coste de completar una tarea: entran reintentos, longitud de contexto, latencia y calidad. Seguir el coste por tarea completada es más informativo que seguir el precio por token, aunque esta fuente no aporte cifras ni método para hacerlo.

## Evidence
- El único soporte es el encuadre «true cost of a token» del titular, que apunta a que el precio no lo es todo sin detallar los componentes — source: aa8b1e11c47162e3
- Ningún documento del clúster mide coste por tarea, reintentos, contexto ni latencia — source: aa8b1e11c47162e3

## Why it matters
Para un líder chico que evalúa incrustar LLMs en tooling interno o en flujos de docencia, la métrica de decisión es el coste por tarea completada. El principio es plausible pero queda sin operacionalizar por esta evidencia.

`derived_from` la nota del gancho editorial, que es su origen. `relates_to` la pregunta del recorte de precios, que es el contexto donde el principio se aplicaría.

## Links
- derived_from → [[coste-real-de-un-token-como-gancho-editorial]]
- relates_to → [[corte-de-precios-llm-80-por-ciento-pregunta-sin-evidencia]]
