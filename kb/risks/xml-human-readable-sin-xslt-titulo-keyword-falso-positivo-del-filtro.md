---
id: xml-human-readable-sin-xslt-titulo-keyword-falso-positivo-del-filtro
title: El ítem de XML sobrevivió al filtro determinista por solapamiento de keywords
  del título
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-28'
updated: '2026-10-07'
sources:
- 1bfe45ede61ee575
tags:
- clustering
- falso-positivo
- falsos-positivos
- filtrado
- filtro-determinista
- pipeline
- xml
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-solo-afirmacion-javascript
  type: derived_from
- to: xml-human-readable-entra-por-coincidencia-lexica
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: supports
- to: clustering-por-embedding-produce-falsos-positivos
  type: supports
- to: solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering
  type: relates_to
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: relates_to
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: supports
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: supports
- to: xml-human-readable-without-xslt-afirmacion-sin-cuerpo
  type: derived_from
- to: relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal
  type: supports
- to: relevancia-0-67-sin-evidencia-extraible-como-artefacto-del-scorer
  type: relates_to
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: relates_to
---

## What it is
El ítem pasó el filtrado determinista con métricas relevance=0.33, novelty=0.00 y corroboration=0.50 pese a que su cuerpo entero es una sola frase. El match probable con el vocabulario del brief es léxico, no semántico: «programar» o términos de tooling pueden haber disparado la retención.

## Evidence
- El clúster consiste en un único ítem RSS [1bfe45ede61ee575] de bajo engagement cuyo cuerpo es la frase «JavaScript is right there.» — source: 1bfe45ede61ee575
- El signal reporta relevance=0.33, novelty=0.00 y corroboration=0.50. — source: 1bfe45ede61ee575
- El analista señala que el ítem queda tangencial a los ejes del brief (estimación, secuenciación, alcance, pedagogía). — source: 1bfe45ede61ee575

## Why it matters
Confirma el patrón de que un título con vocabulario técnico afín puede sobrevivir al filtro sin que el cuerpo respalde ningún eje del brief. Si estos ítems consumen cupo de compilación, desplazan señal real.

Se deriva de `xml-human-readable-without-xslt-afirmacion-sin-cuerpo`, que documenta la vacuidad del cuerpo. Da soporte empírico a `relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal` con un caso concreto. Se relaciona con `relevancia-0-67-sin-evidencia-extraible-como-artefacto-del-scorer` porque ambos describen desajustes entre score y contenido, y con `etiqueta-determinista-como-falso-positivo-de-categoria`, que generaliza el mismo fenómeno.

## Links
- derived_from → [[xml-human-readable-sin-xslt-solo-afirmacion-javascript]]
- supports → [[xml-human-readable-entra-por-coincidencia-lexica]]
- supports → [[xml-human-readable-singleton-engagement-cero]]
- supports → [[clustering-por-embedding-produce-falsos-positivos]]
- relates_to → [[solapamiento-lexico-agents-servers-como-falso-positivo-de-clustering]]
- relates_to → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- supports → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
- derived_from → [[xml-human-readable-without-xslt-afirmacion-sin-cuerpo]]
- supports → [[relevancia-baja-novedad-nula-corroboracion-alta-no-son-senal]]
- relates_to → [[relevancia-0-67-sin-evidencia-extraible-como-artefacto-del-scorer]]
- relates_to → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
