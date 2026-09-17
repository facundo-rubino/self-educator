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
updated: '2026-09-17'
sources:
- 00bd010c780beac7
tags:
- ingesta
- clustering
- falsos-positivos
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: supports
---

## What it is
La etiqueta de señal «datasette 1.0a40» asoció un clúster cuyo único documento trata de la coma final en JSON, sin relación con Datasette ni con ningún tema del brief. La etiqueta es una coincidencia léxica o un artefacto de disparo por palabra clave del filtro determinista, no un hallazgo semántico [00bd010c780beac7].

## Evidence
- El clúster contiene un solo documento RSS que discute la prohibición de separadores finales en JSON, enmarcada como cuestión de diseño y estética; ningún documento trata de Datasette, agentes de código, liderazgo técnico, estimación, secuenciamiento, alcance, organización personal ni técnicas de estudio — source: 00bd010c780beac7
- El contenido sustantivo del documento es la mecánica gramatical de JSON y su justificación estética, no ninguna herramienta de desarrollo ni flujo de trabajo con IA — source: 00bd010c780beac7

## Why it matters
Una etiqueta determinista que dispara por vocabulario puede arrastrar documentos fuera del tema hacia el análisis aguas abajo, y la confianza alta (0.83 inicial) queda conducida por la etiqueta y no por el contenido. La corrección barata es verificar que el cuerpo del documento mencione el tema antes de aceptar la etiqueta.

Se apoya en el patrón ya registrado de que el matching por vocabulario genérico admite ítems fuera del tema, y es una instancia concreta del riesgo general de falsos positivos temáticos en el clustering.

## Links
- relates_to → [[clustering-por-embedding-produce-falsos-positivos]]
- supports → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
