---
id: coste-y-latencia-de-workflows-de-varios-dias-no-discutidos
title: 'Riesgo: coste y latencia de workflows agénticos de varios días, no discutidos'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-02'
updated: '2026-11-02'
sources:
- 5e81338675ea4d09
tags:
- coste
- latencia
- agentes
- largo-horizonte
base_confidence: 0.32
half_life_days: 120
last_reinforced: '2026-11-02'
provenance:
  scale: S
  query: null
links:
- to: arca-agentes-largo-horizonte-memoria-harness
  type: relates_to
- to: precio-de-token-no-es-coste-total-de-tarea
  type: relates_to
- to: ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados
  type: supports
---

## What it is
El documento no discute el coste ni la latencia de un workflow que corre durante días; son precisamente los factores que pueden hacer inviable el patrón para un equipo chico o un curso con presupuesto limitado.

## Evidence
- El caso Arca describe workflows de varios días sin cifras de coste ni latencia — source: 5e81338675ea4d09 (ausencia verificable en el resumen, no afirmación del documento)

## Why it matters
Un líder técnico que evalúe memoria persistente y workflows largos necesita esos números antes de comprometer alcance. Sin ellos, la decisión se toma sobre una anécdota.

Se relaciona con la nota de que el precio por token no es el coste por tarea, y con el riesgo paralelo ya registrado de riesgos de latencia y coste no declarados en un loop agéntico de voz.

## Links
- relates_to → [[arca-agentes-largo-horizonte-memoria-harness]]
- relates_to → [[precio-de-token-no-es-coste-total-de-tarea]]
- supports → [[ai-coach-voz-loop-riesgos-latencia-stt-tts-coste-no-declarados]]
