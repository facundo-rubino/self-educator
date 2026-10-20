---
id: how-to-match-llm-patterns-bordes-taxonomia-no-validados
title: Los bordes de la dicotomía externo/interno y datos/no-datos no están validados
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 0248fdb60811e91e
tags:
- taxonomia
- sobre-generalizacion
- llm
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-taxonomia-dos-ejes
  type: contradicts
- to: how-to-match-llm-patterns-framework-opinion-sin-validar
  type: relates_to
---

## What it is
Los dos ejes propuestos son etiquetas amplias que admiten casos grises: RAG híbrido, modelos locales con datos sensibles, patrones que consultan datos desde un LLM externo. El documento no define cómo se clasifican esos casos.

## Evidence
- Los ejes se enuncian como dicotomías (externo vs. interno, datos vs. no-datos) sin criterio declarado para casos mixtos — source: 0248fdb60811e91e

## Why it matters
Aplicar la taxonomía sin reconocer los grises puede llevar a etiquetar mal un problema y elegir el patrón equivocado. El valor de la heurística depende de que los bordes sean operables, y aquí no están definidos.

Contradice en la práctica la claridad que sugiere la nota sobre los dos ejes. Se relaciona con el riesgo de que el marco sea opinión plausible sin validación.

## Links
- contradicts → [[how-to-match-llm-patterns-taxonomia-dos-ejes]]
- relates_to → [[how-to-match-llm-patterns-framework-opinion-sin-validar]]
