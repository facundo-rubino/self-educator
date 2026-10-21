---
id: task-specific-llm-evals-candidato-a-retrieval-no-a-insight-nueva-evidencia
title: '«Task-Specific LLM Evals»: candidato a retrieval de texto completo, no a insight'
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 93963a5f93e58d05
tags:
- retrieval-candidate
- thin-signal
- open-question
base_confidence: 0.55
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: task-specific-llm-evals-recuperar-texto-completo-antes-de-citar
  type: supports
- to: evals-por-tarea-candidato-a-retrieval-no-a-insight
  type: supports
---

## What it is
Pregunta abierta: ¿el artículo original contiene la metodología, los benchmarks o la replicación que el ítem RSS no trae? La lectura honesta del clúster es que es un puntero a leer, no un resultado. Hasta recuperar el texto completo, la taxonomía sólo tiene valor como recordatorio de nombrar la familia de tarea.

## Evidence
- El clúster es un único ítem RSS con engagement cero, sin texto completo ni metodología ingerida — source: 93963a5f93e58d05
- El análisis concluye que debe tratarse como puntero a leer la pieza original, no como resultado validado — source: 93963a5f93e58d05

## Why it matters
Recuperar el texto completo es prerrequisito para cualquier claim positivo. Si el original resulta un listicle sin estudio metodológico, la dicotomía do/don't pierde todo peso; si trae datos, el ítem cambia de categoría. Hasta entonces, no se cita como hallazgo.

Se deriva de la nota de alcance declarado y coincide con `task-specific-llm-evals-recuperar-texto-completo-antes-de-citar` y `evals-por-tarea-candidato-a-retrieval-no-a-insight`.

## Links
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- supports → [[task-specific-llm-evals-recuperar-texto-completo-antes-de-citar]]
- supports → [[evals-por-tarea-candidato-a-retrieval-no-a-insight]]
