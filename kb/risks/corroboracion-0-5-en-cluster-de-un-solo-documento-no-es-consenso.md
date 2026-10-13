---
id: corroboracion-0-5-en-cluster-de-un-solo-documento-no-es-consenso
title: Una corroboración de 0.50 en un clúster de un solo documento no es consenso
  entre fuentes
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-13'
sources:
- abf61eeec75462f9
tags:
- corroboracion
- metricas
- pipeline
- clustering
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-10-13'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: supports
- to: corroboration-1-00-con-relevance-0-20-metrica-degenerada
  type: relates_to
- to: claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente
  type: supports
---

## What it is
En este clúster, el score de corroboración es 0.50 pero el clúster contiene un único documento [abf61eeec75462f9]. El score no se corresponde con la presencia de fuentes adicionales, por lo que no puede leerse como consenso independiente.

## Evidence
- El clúster es de un solo documento y su engagement es 0 — source: abf61eeec75462f9 (crítico)
- La corroboración reportada es 0.50 sin segundo documento que la respalde — source: abf61eeec75462f9

## Why it matters
Cualquier lectura de "varias fuentes coinciden" a partir de este clúster es una sobreinterpretación. La métrica de corroboración debe cruzarse con el número de documentos antes de sostener un claim.

Refuerza `corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente` y se relaciona con `corroboration-1-00-con-relevance-0-20-metrica-degenerada` como otras formas de métrica de corroboración no indicativa. Apoya la nota del claim principal porque limita su fuerza.

## Links
- supports → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- relates_to → [[corroboration-1-00-con-relevance-0-20-metrica-degenerada]]
- supports → [[claude-code-system-prompt-ensamblado-condicional-claim-sin-fuente]]
