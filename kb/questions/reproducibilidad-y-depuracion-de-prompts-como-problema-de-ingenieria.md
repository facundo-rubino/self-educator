---
id: reproducibilidad-y-depuracion-de-prompts-como-problema-de-ingenieria
title: Si la conducta del agente depende de muchas condiciones, la depuración de prompts
  es un problema de ingeniería
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-10-22'
sources:
- 19cb8032958cd964
- abf61eeec75462f9
tags:
- agentes
- depuracion
- oficio
- pregunta-abierta
- prompt-engineering
- prompts
- proveedores
- reproducibilidad
base_confidence: 0.3
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: system-prompt-como-artefacto-de-ingenieria
  type: derived_from
- to: revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico
  type: relates_to
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: ensamblado-condicional-de-prompts
  type: relates_to
---

## What it is
Cuando la respuesta depende de proveedor, versión, cuenta, región y phrasing, reproducir una conducta de rechazo exige registrar y controlar todas esas variables. La divergencia ChatGPT/Claude/Gemini es un caso de esa dependencia, aunque la fuente no la documente.

## Evidence
- El documento solo reporta el resultado de la diferencia, sin declarar ninguna variable de control — source: 19cb8032958cd964

## Why it matters
Sin condiciones declaradas, la conducta no es depurable ni testeable. La pregunta abierta es qué mínima instrumentación por proveedor hace reproducible una política de rechazo observada.

Se relaciona con la pregunta sobre qué condiciones gobiernan la divergencia de rechazo y con el ensamblado condicional de prompts.

## Links
- derived_from → [[system-prompt-como-artefacto-de-ingenieria]]
- relates_to → [[revision-de-setup-de-agente-por-rama-condicional-no-por-prompt-monolitico]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- relates_to → [[afirmar-practica-desde-ausencia-de-contenido-en-feed-de-releases]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[ensamblado-condicional-de-prompts]]
