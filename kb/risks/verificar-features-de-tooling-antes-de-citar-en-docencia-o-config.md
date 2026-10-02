---
id: verificar-features-de-tooling-antes-de-citar-en-docencia-o-config
title: Verificar contra upstream antes de citar una feature de tooling en docencia
  o configuración
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-02'
sources:
- b5c67fa626902034
tags:
- verificacion
- llama.cpp
- tooling
- docencia
- equipo
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: decision-models-claim-sin-especificacion
  type: derived_from
- to: no-conflacionar-tres-claims-de-decision-model-en-una-tendencia
  type: relates_to
---

## What it is
Actuar sobre una feature de tooling no verificada (por ejemplo, un «New in llama.cpp» que solo existe como titular) puede propagar una capacidad falsa a documentación de equipo, material docente o configuraciones. Una retracción o renombre upstream invalidaría toda la premisa.

## Evidence
- La afirmación «New in llama.cpp: Decision Models» se sostiene solo en un título de submission sin commit ni spec — fuente: b5c67fa626902034.

## Why it matters
El coste de verificar contra el changelog upstream es bajo comparado con desaprender una feature inventada en clase o en el repo del equipo.

Deriva del claim principal del clúster y comparte con la nota de falso consenso la misma causa raíz: fuente primaria ausente.

## Links
- derived_from → [[decision-models-claim-sin-especificacion]]
- relates_to → [[no-conflacionar-tres-claims-de-decision-model-en-una-tendencia]]
