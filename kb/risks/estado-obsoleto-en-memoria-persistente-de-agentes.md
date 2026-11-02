---
id: estado-obsoleto-en-memoria-persistente-de-agentes
title: 'Riesgo: estado obsoleto o contaminado en memoria persistente de agentes'
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
- memoria-persistente
- estado
- agentes
base_confidence: 0.28
half_life_days: 120
last_reinforced: '2026-11-02'
provenance:
  scale: S
  query: null
links:
- to: memoria-persistente-como-eje-de-agente-de-largo-horizonte
  type: contradicts
- to: server-memory-como-primitiva-de-estado-para-agentes
  type: relates_to
---

## What it is
La memoria persistente introduce el riesgo de que el agente recuerde decisiones, contexto o hechos ya inválidos; el caso Arca no menciona cómo se invalida ni cómo se audita lo recordado.

## Evidence
- El documento no describe mecanismos de invalidación ni auditoría de la memoria persistente — source: 5e81338675ea4d09 (ausencia verificable en el resumen)

## Why it matters
Toda propuesta de memoria entre sesiones para proyectos de software o para seguimiento de alumnos hereda este riesgo: sin política de invalidación, la persistencia puede ser peor que el reinicio de contexto.

Contradice la lectura de la memoria persistente como puro habilitador. Se relaciona con `server-memory` como primitiva de estado, que sin política de expiración reproduce el mismo problema.

## Links
- contradicts → [[memoria-persistente-como-eje-de-agente-de-largo-horizonte]]
- relates_to → [[server-memory-como-primitiva-de-estado-para-agentes]]
