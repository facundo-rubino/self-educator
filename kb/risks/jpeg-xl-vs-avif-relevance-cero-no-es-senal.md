---
id: jpeg-xl-vs-avif-relevance-cero-no-es-senal
title: 'relevance=0.00 en «JPEG XL vs AVIF»: coincidencia léxica sin afinidad temática'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-15'
updated: '2026-10-15'
sources:
- sig-cd6a28301fec
- 5a141b0b02266571
tags:
- artefacto-de-scorer
- coincidencia-lexica
- falso-positivo
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-15'
provenance:
  scale: XL
  query: null
links:
- to: jpeg-xl-vs-avif-fuera-del-brief-de-agentes-y-liderazgo
  type: supports
- to: jpeg-xl-vs-avif-titular-sin-cuerpo-ni-datos
  type: derived_from
- to: jpeg-xl-vs-avif-titulo-como-match-lexico-trigger
  type: relates_to
---

## What it is
El clúster sobre JPEG XL frente a AVIF probablemente entró al pipeline por solapamiento léxico superficial de palabras del título, no por afinidad temática con el brief. El score de relevancia asignado es 0.00.

## Evidence
- El score de relevancia del clúster es 0.00 — source: sig-cd6a28301fec
- El crítico del pipeline identifica el mecanismo como «textbook lexical-coincidence artifact»: el tema nombra una comparación, pero la evidencia no contiene la comparación — source: sig-cd6a28301fec
- El documento fuente es un titular de RSS sin cuerpo analítico — source: 5a141b0b02266571

## Why it matters
Un relevance=0.00 sostenido por coincidencia léxica es un falso positivo del filtro: no aporta señal al brief y consume cupo de revisión. Registrarlo como riesgo evita que este tipo de ítem se promueva a hallazgo en futuras rondas.

Refuerza la nota sobre la exclusión del clúster de los ejes del brief. Deriva de la descripción del documento fuente y se relaciona con la nota que aísla el título como disparador léxico.

## Links
- supports → [[jpeg-xl-vs-avif-fuera-del-brief-de-agentes-y-liderazgo]]
- derived_from → [[jpeg-xl-vs-avif-titular-sin-cuerpo-ni-datos]]
- relates_to → [[jpeg-xl-vs-avif-titulo-como-match-lexico-trigger]]
