---
id: task-specific-llm-evals-sin-conexion-con-agentes-o-docencia
title: «Task-Specific LLM Evals» no conecta con agentes de código, gestión ni docencia
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-08'
sources:
- 93963a5f93e58d05
tags:
- agentes
- alcance
- brief
- brief-mismatch
- docencia
- evals
- riesgo
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-08'
provenance:
  scale: XL
  query: null
links:
- to: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
  type: supports
- to: task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: supports
- to: aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion
  type: supports
- to: task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo
  type: derived_from
- to: task-specific-llm-evals-adyacencia-al-brief-no-demostrada
  type: relates_to
- to: task-specific-llm-evals-relevancia-lexica-no-tematica
  type: relates_to
- to: task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad
  type: derived_from
- to: task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: relates_to
---

## What it is
El documento entra al corpus por el encuadre amplio «IA aplicada a la práctica profesional», pero su alcance declarado —clasificación, resumen, traducción, copyright, toxicidad— no cubre agentes de codificación, estimación, secuenciamiento, gestión de equipo ni docencia. La conexión es de vocabulario, no de dominio.

## Evidence
- El alcance declarado es exclusivamente tareas NLP generales — source: 93963a5f93e58d05
- No hay documento en el clúster que establezca conexión con los ejes del brief — source: 93963a5f93e58d05

## Why it matters
Evita que futuras compilaciones citen este ítem como referencia sobre fiabilidad de agentes de código. El material utilizable se agota en la taxonomía de tareas, sin consecuencia para ningún eje del brief.

Refuerza desde el lado del brief el límite declarado en `task-specific-llm-evals-singleton-engagement-cero`; se relaciona con otros casos de evals genéricas fuera del alcance recogidos en el grafo.

## Links
- supports → [[task-specific-llm-evals-adyacencia-al-brief-no-demostrada]]
- relates_to → [[task-specific-llm-evals-copyright-regurgitation-como-riesgo-de-producto]]
- supports → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
- supports → [[aplicar-evals-nlp-a-agentes-de-codigo-seria-extrapolacion]]
- derived_from → [[task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo]]
- relates_to → [[task-specific-llm-evals-adyacencia-al-brief-no-demostrada]]
- relates_to → [[task-specific-llm-evals-relevancia-lexica-no-tematica]]
- derived_from → [[task-specific-llm-evals-alcance-declarado-clasificacion-resumen-traduccion-copyright-toxicidad]]
- relates_to → [[task-specific-llm-evals-tareas-nlp-no-cubren-evals-de-codigo]]
- relates_to → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
