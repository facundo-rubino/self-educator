---
id: decision-models-claim-sin-especificacion
title: '«Decision Models» en llama.cpp: claim de titular sin especificación ni commit'
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
- llama.cpp
- decision-models
- claim-sin-metodologia
- artefacto-de-ingesta
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-10-02'
provenance:
  scale: XL
  query: null
links:
- to: mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades
  type: relates_to
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
- to: subestimar-verificacion-upstream-de-features-de-tooling
  type: supports
---

## What it is
La afirmación «New in llama.cpp: Decision Models» existe únicamente como título de un envío a Reddit, sin spec, commit, PR ni documentación técnica extraída. Cualquier inferencia de que llama.cpp incorporó «decision models» es coincidencia léxica entre un titular y una frase, no un desarrollo técnico establecido.

## Evidence
- La publicación «New in llama.cpp: Decision Models» se atribuye solo a un título de submission y su subreddit, sin detalle enlazado — fuente: b5c67fa626902034.
- Todos los ítems del clúster tienen engagement=0 y son títulos RSS; ninguno incluye el commit, benchmark o design doc que corroboraría el claim — fuente: 2739eac7c4f07798.

## Why it matters
Actuar sobre un «New in llama.cpp» no verificado propaga una feature falsa a documentación de equipo, material docente o configuración de tooling. Antes de citarlo, verificar contra el changelog del repositorio upstream.

Comparte con las notas de releases MCP el modo de fallo «feed sin changelog»: la ausencia de detalle impide afirmar capacidades. Se apoya en la nota sobre el coste de no verificar upstream, que es exactamente el paso omitido aquí.

## Links
- relates_to → [[mcp-feed-de-releases-sin-changelog-impide-afirmar-capacidades]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- supports → [[subestimar-verificacion-upstream-de-features-de-tooling]]
