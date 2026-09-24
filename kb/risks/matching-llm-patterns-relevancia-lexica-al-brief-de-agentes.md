---
id: matching-llm-patterns-relevancia-lexica-al-brief-de-agentes
title: «LLM patterns» solapa léxicamente con «agentes de IA» sin cubrir ningún eje
  del brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 0248fdb60811e91e
tags:
- falso-positivo-lexico
- matching
- filtrado-determinista
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: matching-llm-patterns-relevancia-baja-sin-ejes-del-topic
  type: relates_to
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: supports
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
---

## What it is
El match del clúster [0248fdb60811e91e] con el topic declarado es de vocabulario: la cadena «LLM patterns» comparte términos con «AI agents aplicados a programar» sin que ningún contenido del clúster nombre agentes aplicados a programar, gestionar o enseñar, ni liderazgo técnico de equipos chicos, ni oficio de software, ni productividad. El propio topic excluye por construcción el ángulo de docencia entry-level, que se mudó a otro profile.

## Evidence
- Ningún contenido del clúster nombra agentes de IA aplicados a programar, gestionar o enseñar; ningún contenido aborda liderazgo técnico de equipos chicos (estimación, secuenciación, alcance, organización personal); ningún contenido aborda oficio de software ni productividad y técnicas de estudio — source: 0248fdb60811e91e
- El topic declara explícitamente que la docencia de programación entry-level se mudó a un profile `teaching` separado y ya no compite por cupo en este brief — source: 0248fdb60811e91e
- relevance=0.33, por debajo del punto medio, consistente con un candidato débil — source: 0248fdb60811e91e

## Why it matters
Un match por vocabulario genérico admite ítems fuera del tema y consume cupo de evaluación. Si «LLM patterns» basta para pasar el filtro determinista, el umbral de relevancia no está distinguiendo solapamiento léxico de cobertura temática.

Refuerza `solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering` y `mismatch-query-tema-por-vocabulario-generico-de-infraestructura`: es el mismo modo de fallo del matcher con otro par de términos. Se relaciona con `relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista` por compartir la pregunta sobre qué deberían suprimir los umbrales del pipeline, y con la nota existente de relevancia baja para este clúster.

## Links
- relates_to → [[matching-llm-patterns-relevancia-baja-sin-ejes-del-topic]]
- supports → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
