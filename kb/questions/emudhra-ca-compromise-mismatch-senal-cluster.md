---
id: emudhra-ca-compromise-mismatch-senal-cluster
title: Reporte keyed a «eMudhra» sería fabricación, no hallazgo
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-21'
updated: '2026-10-21'
sources:
- 00bd010c780beac7
- sig-66ffc7dbbbe7
tags:
- ingesta
- pki
- verificacion
- falso-positivo
base_confidence: 0.83
half_life_days: 120
last_reinforced: '2026-10-21'
provenance:
  scale: XL
  query: null
links:
- to: emudhra-intermediate-ca-compromise-senal-sin-documento
  type: derived_from
- to: argumento-ex-silentio-en-corpus-truncado
  type: relates_to
- to: descartar-senal-por-ausencia-de-contenido-no-es-hallazgo
  type: relates_to
---

## What it is
Pregunta abierta: ¿el desajuste nombre-contenido del clúster «eMudhra» es un error de etiquetado de un solo ítem o un síntoma de que el pipeline asigna la señal por un token compartido en el título? La evidencia disponible solo permite afirmar la ausencia, no su causa.

## Evidence
- El término «eMudhra Intermediate CA Compromise» no tiene documento de soporte en el clúster — source: 00bd010c780beac7
- Un reporte keyed a «eMudhra» sería fabricado dado que el clúster no contiene evidencia de PKI ni de compromiso de CA — source: sig-66ffc7dbbbe7

## Why it matters
Distinguir «el ítem está mal etiquetado» de «el pipeline etiqueta por título» cambia la mitigación: la primera se corrige caso a caso, la segunda exige un gate en el scorer.

Deriva de `emudhra-intermediate-ca-compromise-senal-sin-documento`. Toca `argumento-ex-silentio-en-corpus-truncado` (la ausencia se afirma sobre este corpus, no sobre el mundo) y se distingue de `descartar-senal-por-ausencia-de-contenido-no-es-hallazgo`: aquí la observación sobre el pipeline sí es el hallazgo load-bearing.

## Links
- derived_from → [[emudhra-intermediate-ca-compromise-senal-sin-documento]]
- relates_to → [[argumento-ex-silentio-en-corpus-truncado]]
- relates_to → [[descartar-senal-por-ausencia-de-contenido-no-es-hallazgo]]
