---
id: xml-human-readable-sin-xslt-contexto-no-ingerido
title: El contexto que decidiría «JavaScript en lugar de XSLT» no está ingerido
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-23'
sources:
- 1bfe45ede61ee575
tags:
- contexto-ausente
- evidence-gap
- javascript
- recomendacion-no-generalizable
- xml
- xslt
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-23'
provenance:
  scale: XL
  query: null
links:
- to: xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido
  type: derived_from
- to: afirmar-constraint-de-diseno-desde-solo-titulo-rss
  type: supports
- to: xml-human-readable-singleton-engagement-cero
  type: relates_to
---

## What it is
El documento afirma que JavaScript está disponible como alternativa a XSLT para hacer XML legible para humanos, pero no ingiere ninguna de las condiciones que harían operable esa elección: tipo de XML, volumen, pipeline de despliegue, ecosistema preexistente, quién mantiene el resultado. La pregunta queda abierta porque la evidencia no la responde.

## Evidence
- El cuerpo visible es solo «JavaScript is right there.» — source: 1bfe45ede61ee575
- No hay código, benchmark ni análisis de trade-offs en la evidencia — source: 1bfe45ede61ee575

## Why it matters
Sin ese contexto no se puede saber si la afirmación es una preferencia personal, una observación situada o una regla generalizable. XSLT sigue siendo apropiado en pipelines con transformaciones definidas por estándar o ecosistemas XSLT ya existentes, y el documento no aborda esos casos. Registrar la pregunta evita que el compilador fabrique el contexto faltante.

Deriva de `xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido`, que documenta el déficit de cuerpo. Se relaciona con `xml-human-readable-singleton-engagement-cero` porque ambos describen el mismo cluster desde el ángulo de la evidencia ausente.

## Links
- derived_from → [[xml-human-readable-sin-xslt-titulo-sin-contenido-ingerido]]
- supports → [[afirmar-constraint-de-diseno-desde-solo-titulo-rss]]
- relates_to → [[xml-human-readable-singleton-engagement-cero]]
