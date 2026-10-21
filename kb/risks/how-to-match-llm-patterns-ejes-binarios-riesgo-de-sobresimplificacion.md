---
id: how-to-match-llm-patterns-ejes-binarios-riesgo-de-sobresimplificacion
title: Ejes binarios (externo/interno, datos/no-datos) arriesgan sobresimplificar
  trade-offs de ingeniería
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 0248fdb60811e91e
tags:
- llm-patterns
- taxonomia
- trade-offs
- sobresimplificacion
base_confidence: 0.4
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: how-to-match-llm-patterns-taxonomia-dos-ejes
  type: contradicts
- to: how-to-match-llm-patterns-bordes-taxonomia-no-validados
  type: relates_to
- to: how-to-match-llm-patterns-framework-opinion-sin-validar
  type: relates_to
---

## What it is
Dos ejes binarios no capturan trade-offs reales de ingeniería: latencia, coste, privacidad y dificultad de evaluación no se reducen a externo/interno ni a datos/no-datos. La taxonomía, si se usa como criterio único, aplana decisiones que son continuas.

## Evidence
- La taxonomía propuesta se limita a dos ejes: externo vs. interno y datos vs. no-datos — source: 0248fdb60811e91e
- No hay en el clúster contenido que discuta latencia, coste, privacidad o evaluación — source: 0248fdb60811e91e

## Why it matters
Un líder que adopte los dos ejes como checklist puede descartar opciones válidas o subestimar el coste de una integración por no tener dimensión donde puntuarla. La taxonomía sirve como primer filtro, no como criterio de decisión.

Contradice la lectura de la taxonomía como heurística suficiente. Se relaciona con los riesgos previos sobre bordes no validados del marco y sobre el marco como opinión sin validar.

## Links
- contradicts → [[how-to-match-llm-patterns-taxonomia-dos-ejes]]
- relates_to → [[how-to-match-llm-patterns-bordes-taxonomia-no-validados]]
- relates_to → [[how-to-match-llm-patterns-framework-opinion-sin-validar]]
