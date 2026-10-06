---
id: shadow-roots-mismatch-lexico-clustering-css-frente-brief
title: «Shadow roots» como falso positivo léxico de clustering frente al brief
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-25'
updated: '2026-10-06'
sources:
- df4836a1d89bcba4
tags:
- brief
- clustering
- css
- falso-positivo
- falso-positivo-clustering
- falsos-positivos
- filtrado-determinista
- filtro
- gating-topico
- matching-lexico
- mismatch-lexico
- pipeline
- precisión
- shadow-roots
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-06'
provenance:
  scale: XL
  query: null
links:
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: derived_from
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: relates_to
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: relevancia-tematica-baja-no-es-ruido
  type: contradicts
- to: shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido
  type: relates_to
- to: shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada
  type: relates_to
- to: hypothe-rewrite-not-a-real-id
  type: relates_to
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
- to: shadow-roots-live-examples-singleton-sin-engagement
  type: supports
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: supports
- to: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
  type: relates_to
- to: shadow-roots-hay-interes-en-explicar-css-con-artefactos-interactivos
  type: relates_to
- to: deuda-tecnica-como-puente-lexico-al-brief
  type: relates_to
- to: accesibilidad-tooltip-como-falso-positivo-del-filtro-determinista
  type: relates_to
---

## What it is
El ítem de shadow roots trata sobre CSS, no sobre los ejes del brief (agentes de IA aplicados a programar, gestionar y enseñar; liderazgo técnico de equipos chicos; oficio de software engineering; productividad y técnicas de estudio). El match aparente es una coincidencia léxica —solapamiento en patrones de «explain»/«examples» y en el token de tema— no un hallazgo. Con relevance=0.33, novelty=0.00, corroboration=0.50 y engagement=0, es un singleton ruidoso que sobrevivió al filtrado determinista por solapamiento superficial.

## Evidence
- El documento lleva la etiqueta «css» y su sujeto son los shadow roots de CSS, no los temas del brief — source: df4836a1d89bcba4
- El clúster consta de un solo documento con engagement=0 — source: df4836a1d89bcba4
- El propio resumen del report describe el ítem como «a noisy singleton that survived deterministic filtering on keyword overlap rather than an actionable finding» — source: df4836a1d89bcba4

## Why it matters
Incluso un explicador de shadow roots bien desarrollado pertenecería a otro perfil o KB: el brief declara que la docencia de programación entry-level se mudó al profile `teaching`. Llevar este ítem adelante en el KB actual es riesgo de deriva temática. Además sugiere que las firmas de keywords del filtro determinista podrían necesitar ajuste, porque «explain» y «examples» no son señal de encaje topical.

Se relaciona con `shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido` y con `shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada` (el mismo ítem leído por título y por contenido). Es el mismo modo de fallo que `accesibilidad-tooltip-como-falso-positivo-del-filtro-determinista` y que `xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro`: ítems que entran al brief por tokens del título, no por tema.

## Links
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- derived_from → [[shadow-roots-live-examples-singleton-sin-engagement]]
- relates_to → [[shadow-roots-live-examples-singleton-sin-engagement]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- contradicts → [[relevancia-tematica-baja-no-es-ruido]]
- relates_to → [[shadow-roots-explained-with-live-examples-titulo-sin-contenido-ingerido]]
- relates_to → [[shadow-roots-artefacto-interactivo-css-prompt-sin-practica-demostrada]]
- relates_to → [[hypothe-rewrite-not-a-real-id]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
- supports → [[shadow-roots-live-examples-singleton-sin-engagement]]
- supports → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
- relates_to → [[xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro]]
- relates_to → [[shadow-roots-hay-interes-en-explicar-css-con-artefactos-interactivos]]
- relates_to → [[deuda-tecnica-como-puente-lexico-al-brief]]
- relates_to → [[accesibilidad-tooltip-como-falso-positivo-del-filtro-determinista]]
