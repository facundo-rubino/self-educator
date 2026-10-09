---
id: ai-coach-telefono-como-canal-asincrono-baja-friccion-hipotesis
title: 'El número virtual como canal asíncrono de baja fricción: intención, no patrón
  de decisión demostrado'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-09'
sources:
- 49140f9d5133d3c7
tags:
- ai-coach
- telefonia
- interaccion
- hipotesis
base_confidence: 0.04
half_life_days: 120
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: ai-coach-stack-stt-tts-llm-numero-virtual
  type: derived_from
- to: hipotesis-de-coach-de-voz-como-accountability-de-equipo
  type: relates_to
---

## What it is
La inclusión de un número virtual sugiere la intención de que el coach sea accesible por teléfono, es decir un canal asíncrono y de baja fricción frente a una herramienta atada a una UI [49140f9d5133d3c7]. El documento no describe cómo se usa ese canal, ni si externaliza checkpoints de decisión o monitoreo.

## Evidence
- El número virtual es uno de los cuatro componentes enumerados — source: 49140f9d5133d3c7
- No hay descripción del flujo de interacción ni de su función — source: 49140f9d5133d3c7

## Why it matters
Es el único indicio de diseño —canal telefónico en lugar de app— que el documento aporta, y por eso merece registrarse como intención y no como patrón. Verificarlo requeriría un documento con el flujo real; hoy sostener que externaliza puntos de decisión sería especulación.

Deriva del stack enumerado. Se relaciona con la hipótesis ya registrada de un coach de voz como accountability ligero, que también carece de evidencia de implementación.

## Links
- derived_from → [[ai-coach-stack-stt-tts-llm-numero-virtual]]
- relates_to → [[hipotesis-de-coach-de-voz-como-accountability-de-equipo]]
