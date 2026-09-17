---
id: json-no-admite-coma-final
title: La gramática de JSON no admite coma final
type: concept
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
- json
- sintaxis
- gramatica
base_confidence: 0.85
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: argumento-ex-silentio-en-corpus-truncado
  type: relates_to
---

## What it is
La gramática de JSON permite una coma únicamente para separar dos miembros de un objeto; por tanto una coma final antes del cierre de la llave no es válida. Un objeto válido muestra pares separados por comas y sin coma tras el último miembro; uno inválido incluye una coma después del último miembro [00bd010c780beac7].

## Evidence
- Un objeto JSON válido separa pares con comas y no lleva coma antes de la llave de cierre; uno inválido lleva coma tras el último miembro — source: 00bd010c780beac7
- La gramática de JSON especifica que una coma puede separar dos miembros de un objeto, por lo que la coma final no está permitida — source: 00bd010c780beac7
- El documento trata de separadores no finales y de la justificación estética de rechazar la coma final, no de ninguna herramienta de desarrollo — source: 00bd010c780beac7

## Why it matters
Es un hecho de sintaxis estable y no negociable: cualquier parser conforme a la especificación rechazará un documento con coma final. Enseñar esto evita el error frecuente de arrastrar hábitos de JavaScript o Python (donde la coma final sí es válida) a payloads JSON.

Se relaciona con el riesgo de argumentar desde corpus truncado: la ausencia de contenido sobre Datasette en el clúster no demuestra nada sobre Datasette, solo que este documento habla de otra cosa.

## Links
- relates_to → [[argumento-ex-silentio-en-corpus-truncado]]
