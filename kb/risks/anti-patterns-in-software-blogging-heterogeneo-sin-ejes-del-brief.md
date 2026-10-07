---
id: anti-patterns-in-software-blogging-heterogeneo-sin-ejes-del-brief
title: El clúster «Anti-Patterns in Software Blogging» es heterogéneo y no cubre ningún
  eje del brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-07'
updated: '2026-10-07'
sources:
- sig-168dcd41a1e2
tags:
- cluster-noise
- rss-ingest
- topic-mismatch
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: cluster-heterogeneo-como-vertedero-de-firehose
  type: supports
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: anti-patterns-in-software-blogging-etiqueta-sin-claim
  type: relates_to
---

## What it is
El clúster mezcla CSS esotérico (tic-tac-toe en CSS puro, gradientes, pseudo-clases estructurales, formatos de color, centrar divs), minucias de gramática JSON, comentario LLM/tooling, ensayos de craft de ingeniería y discusión de incidentes/chaos engineering. Ningún documento aborda agentes de IA aplicados a desarrollo, gestión o enseñanza, ni liderazgo técnico de equipos chicos, estimación, secuenciamiento u organización personal — source: sig-168dcd41a1e2.

## Evidence
- CSS puro para tres en raya con checkboxes ocultos y estados `:indeterminate`, sin conexión con los ejes del brief — source: 01121bf8491d2e95.
- Reglas de gramática JSON sobre comas finales, sin relación con agentes, docencia o liderazgo de equipo — source: 00bd010c780beac7.
- Temas CSS varios (formatos de color, centrar divs, patrones de gradiente, testers de pseudo-clases, debate de 80 columnas) que no intersectan el brief — source: 05144eead0862bb5.

## Why it matters
Alimentar este clúster aguas abajo diluirá resultados relevantes. Peor: puede enmascarar la ausencia real de señal sobre agentes de IA, docencia y liderazgo de equipos chicos, haciendo inferir al brief una cobertura que no existe — source: sig-168dcd41a1e2.

Instancia el patrón de clúster heterogéneo como vertedero de firehose. Ejemplifica que relevancia baja + novedad nula + corroboración alta no constituyen señal.

## Links
- supports → [[cluster-heterogeneo-como-vertedero-de-firehose]]
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- relates_to → [[anti-patterns-in-software-blogging-etiqueta-sin-claim]]
