---
id: react-for-two-computers-corroboracion-y-sorpresa-0-50-valores-por-defecto
title: En un clúster de un solo documento sin engagement, corroboración, velocidad
  y sorpresa de 0.50 son valores por defecto
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- dec9f3cc9a87f904
- sig-d0acf338c3a6
tags:
- scoring
- pipeline
- artefacto-de-scorer
- mcp-releases
base_confidence: 0.8
half_life_days: 365
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: corroboracion-y-velocidad-como-artefactos-del-scorer
  type: supports
- to: corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente
  type: supports
- to: scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido
  type: supports
- to: release-2026-8-31-relevance-baja-novelty-cero
  type: supports
- to: react-for-two-computers-singleton-engagement-cero
  type: relates_to
---

## What it is
Un clúster formado por un único documento sin engagement puede mostrar corroboración=0.50, velocidad=0.50 y sorpresa=0.50 sin que ninguno de esos valores proceda de observación. Son el punto neutro del scorer cuando no hay con qué comparar: con un solo documento no existe corroboración posible, y sin engagement no existe medida de velocidad ni de sorpresa.

## Evidence
- El clúster «React for Two Computers» reporta corroboración 0.50, velocidad 0.50 y sorpresa 0.50 sobre un único documento con engagement=0 — source: dec9f3cc9a87f904
- El release 2026.8.31 (señal sig-d0acf338c3a6) muestra el mismo patrón de corroboración plana 0.50 acompañando novelty 0.00 — source: sig-d0acf338c3a6

## Why it matters
Un 0.50 exacto se lee como «evidencia a medias» cuando en realidad significa «sin dato». Tratarlo como señal introduce un sesgo sistemático al alza en cualquier lista de clústeres: los artefactos vacíos quedan puntuados igual que los temas con evidencia parcial real, y compiten por cuota de análisis con los segundos.

Confirma `corroboracion-y-velocidad-como-artefactos-del-scorer` y extiende `corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente` al caso sin repetición de serie alguna: allí el 0.50 venía de boilerplate repetido, aquí ni siquiera hay eso. Coincide con `release-2026-8-31-relevance-baja-novelty-cero`, donde el mismo 0.50 plano aparece sobre otro artefacto de feed, y con `scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido`.

## Links
- supports → [[corroboracion-y-velocidad-como-artefactos-del-scorer]]
- supports → [[corroboracion-0-5-por-repeticion-de-serie-no-es-validacion-independiente]]
- supports → [[scores-neutrales-de-cluster-no-corroboran-una-lectura-de-contenido]]
- supports → [[release-2026-8-31-relevance-baja-novelty-cero]]
- relates_to → [[react-for-two-computers-singleton-engagement-cero]]
