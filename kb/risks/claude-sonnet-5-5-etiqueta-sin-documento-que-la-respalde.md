---
id: claude-sonnet-5-5-etiqueta-sin-documento-que-la-respalde
title: '«Claude Sonnet 5.5»: etiqueta de señal sin documento que la respalde'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-29'
updated: '2026-09-29'
sources:
- sig-c718e5611ff4
tags:
- claude
- claude-sonnet-5-5
- ingesta
- etiquetado
- falso-positivo
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-29'
provenance:
  scale: XL
  query: null
links:
- to: hy3-identidad-no-establecida
  type: relates_to
- to: risk-de-over-indexar-nombres-de-modelos
  type: relates_to
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
Ninguno de los 20 documentos del clúster menciona «Claude Sonnet 5.5»; la etiqueta de la señal es un artefacto del pipeline, no un hallazgo del corpus [sig-c718e5611ff4]. Tratar el clúster como señal real fabricaría una narrativa sobre un modelo del que los documentos no hablan.

## Evidence
- La señal se etiquetó «Claude Sonnet 5.5» con relevance=0.20 y novelty=0.00, y ninguno de los 20 documentos ingeridos respalda esa etiqueta — source: sig-c718e5611ff4
- Los documentos son ítems RSS genéricos de blogs de desarrollo (CSS, gramática JSON, mantenimiento de Electron, incidentes, hardware, reading list de modelos abiertos) — source: sig-c718e5611ff4

## Why it matters
Un nombre de modelo en el campo `signal` no es evidencia de que el corpus hable de ese modelo. Antes de compilar cualquier afirmación sobre «Claude Sonnet 5.5», hace falta un documento que lo nombre y lo describa.

Comparte con `hy3-identidad-no-establecida` el patrón de etiqueta de modelo sin fuente primaria; con `risk-de-over-indexar-nombres-de-modelos` la advertencia de construir análisis sobre un nombre no verificado; con `relevancia-no-es-verdad` la distinción entre utilidad aparente y respaldo documental.

## Links
- relates_to → [[hy3-identidad-no-establecida]]
- relates_to → [[risk-de-over-indexar-nombres-de-modelos]]
- relates_to → [[relevancia-no-es-verdad]]
