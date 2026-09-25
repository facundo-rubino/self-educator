---
id: corroboracion-1-0-con-relevancia-0-20-como-artefacto-de-degenerate-matching
title: 'corroboration=1.00 con relevance=0.20: artefacto de matching léxico, no acuerdo
  topical'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-09-25'
sources:
- sig-e49b6f02c01e
tags:
- signal-quality
- pipeline
- scoring
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-25'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: ruido-de-agregacion-como-senal-falsa
  type: relates_to
---

## What it is
Un score de corroboration=1.00 acompañando a relevance=0.20 y novelty=0.00 es la firma de un match degenerado: tokens genéricos («AI», «models», «coding») producen solapamiento léxico sin coherencia topical. La corroboración alta no es evidencia de acuerdo entre fuentes; es un artefacto del scorer.

## Evidence
- El informe caracteriza el corroboration=1.00 como «casi con certeza un artefacto degenerado de matching sobre términos genéricos», no como acuerdo topical genuino — source: sig-e49b6f02c01e
- Los riesgos listados advierten que un corroboration=1.00 alto puede inducir a consumidores aguas abajo a tratar esto como un hallazgo bien soportado cuando es un artefacto — source: sig-e49b6f02c01e
- El crítico lo califica de «textbook degenerate-matching artifact»: solapamiento léxico sin coherencia topical — source: sig-e49b6f02c01e

## Why it matters
Cualquier consumidor que use corroboration como filtro de calidad debe saber que aquí 1.00 no implica consenso: implica que el mismo vocabulario de alta frecuencia aparece en documentos temáticamente disjuntos. El score de corroboración no es validación independiente en este régimen.

Refuerza `relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal` con un caso concreto y refuerza `corroboracion-y-velocidad-como-artefactos-del-scorer`. Se relaciona con `ruido-de-agregacion-como-senal-falsa`: agregación sin coherencia presentada como señal.

## Links
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- relates_to → [[ruido-de-agregacion-como-senal-falsa]]
