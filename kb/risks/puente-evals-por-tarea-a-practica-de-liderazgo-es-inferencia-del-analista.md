---
id: puente-evals-por-tarea-a-practica-de-liderazgo-es-inferencia-del-analista
title: El puente «evals por tarea → práctica de liderazgo y docencia» es inferencia
  del analista, no hallazgo
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-09-28'
sources:
- sig-c38460e0d9ca
tags:
- evals
- liderazgo
- docencia
- inferencia
- evidencia-debil
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-singleton-engagement-cero
  type: derived_from
- to: bridge-especulativo-de-eval-por-tarea-a-practica-de-liderazgo
  type: relates_to
- to: relevancia-no-es-verdad
  type: supports
---

## What it is
El informe construye la relevancia al brief razonando desde el topic hacia el artefacto: dado que el dev-líder usa agentes, y los agentes necesitan evals, entonces el documento sería relevante. Es circular: el documento no aporta ningún detalle que confirme o desmienta esa cadena.

## Evidence
- El propio informe admite que «el documento en sí no aporta detalle verificable que permita afirmarlo» — source: sig-c38460e0d9ca
- El crítico señala que el vínculo topical es «un puente plausible ensamblado por el analista, no un hallazgo soportado por el documento» — source: sig-c38460e0d9ca
- El informe declara novedad nula y ausencia de corroboración cruzada — source: sig-c38460e0d9ca

## Why it matters
Compilar las implicaciones del informe como hallazgos sería inventar evidencia. Las implicaciones sobre alcance, secuenciamiento o criterios de evaluación de ejercicios no tienen fuente primaria; el grafo debe registrarlas como pregunta, no como patrón.

Deriva de `task-specific-llm-evals-singleton-engagement-cero`. Es el mismo modo de fallo que `bridge-especulativo-de-eval-por-tarea-a-practica-de-liderazgo`; aquí se ancla al informe concreto. Apoya `relevancia-no-es-verdad`: que el puente sea plausible no lo convierte en evidencia.

## Links
- derived_from → [[task-specific-llm-evals-singleton-engagement-cero]]
- relates_to → [[bridge-especulativo-de-eval-por-tarea-a-practica-de-liderazgo]]
- supports → [[relevancia-no-es-verdad]]
