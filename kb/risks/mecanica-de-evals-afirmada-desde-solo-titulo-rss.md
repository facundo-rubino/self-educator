---
id: mecanica-de-evals-afirmada-desde-solo-titulo-rss
title: Afirmar una mecánica de evaluación desde un título RSS sin cuerpo
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- 93963a5f93e58d05
tags:
- evals
- rss
- inferencia-desde-titular
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: task-families-evaluadas-en-el-documento-evals
  type: relates_to
- to: evals-llm-genericas-fuera-del-alcance-del-brief
  type: supports
---

## What it is
Riesgo de fabricar afirmaciones sobre qué evals de LLM funcionan o fallan a partir de un título y una lista de temas. El documento no aporta metodología, resultados ni la distinción real entre «do» y «don't work» [93963a5f93e58d05]. La frase «Do & Don't Work» es un encuadre editorial, no un hallazgo validado [93963a5f93e58d05].

## Evidence
- No hay información sobre en qué consiste la distinción «do» versus «don't work» — source: 93963a5f93e58d05
- Cualquier inferencia sobre qué prácticas específicas de eval funcionan en esas tareas sería inventada, no citada — source: 93963a5f93e58d05
- El cluster es un único documento con engagement=0: sin confirmación independiente — source: 93963a5f93e58d05

## Why it matters
Marca el límite de lo escribible: el documento sirve como puntero a un artículo externo potencialmente útil, no como evidencia sobre el tema del brief. Tratar el encuadre del título como resultado validado misrepresentaría la evidencia.

Se relaciona con `task-families-evaluadas-en-el-documento-evals` (lo único afirmable es la lista). Apoya a `evals-llm-genericas-fuera-del-alcance-del-brief`, porque la ausencia de cuerpo técnico es la razón de que no se pueda integrar contenido sustantivo.

## Links
- relates_to → [[task-families-evaluadas-en-el-documento-evals]]
- supports → [[evals-llm-genericas-fuera-del-alcance-del-brief]]
