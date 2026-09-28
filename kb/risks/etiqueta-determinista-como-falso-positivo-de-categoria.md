---
id: etiqueta-determinista-como-falso-positivo-de-categoria
title: La etiqueta determinista puede crear un falso positivo de categoría
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-28'
sources:
- 00bd010c780beac7
- 19cb8032958cd964
tags:
- clustering
- falsos-positivos
- ingesta
- pipeline
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-28'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: relates_to
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: relates_to
---

## What it is
El clúster entra al brief con relevance 0.67 sobre la base de solapamiento de tokens («LLM», «AI capability») y no de alineación con la materia. Una etiqueta determinista que acepta por vocabulario puede crear así un falso positivo de categoría: el ítem sobrevive al filtro sin pertenecer al tema.

## Evidence
- La relevancia de 0.67 refleja solapamiento de palabras clave con «LLM/AI», no alineación con la materia del brief — source: 19cb8032958cd964

## Why it matters
El coste es de asignación de atención del analista: cada falso positivo consume cupo y diluye el foco del clúster en liderazgo técnico, estimación, secuenciamiento, alcance, agentes de IA para programar y enseñar, y técnicas de estudio. El modo de fallo es de precisión del pipeline, no del documento.

Se relaciona con `mismatch-query-tema-por-vocabulario-generico-de-infraestructura` y con `solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering`, que describen el mismo mecanismo desde otros pares de tokens. Contradice a `relevancia-tematica-baja-no-es-ruido`, que sostiene que la relevancia baja no implica ausencia de señal: en este caso la relevancia procede del token y no del contenido, y la conclusión es la contraria.

## Links
- relates_to → [[clustering-por-embedding-produce-falsos-positivos]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
