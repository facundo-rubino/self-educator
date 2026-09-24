---
id: react-for-two-computers-pasa-filtro-determinista-con-cuerpo-vacio
title: Un ítem con novelty 0.00 y cuerpo vacío pasa el filtro determinista
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- dec9f3cc9a87f904
tags:
- pipeline
- filtrado
- falso-positivo
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista
  type: relates_to
- to: etiqueta-determinista-como-falso-positivo-de-categoria
  type: relates_to
- to: react-for-two-computers-singleton-engagement-cero
  type: derived_from
---

## What it is
El documento pasó el filtro determinístico pese a tener novedad 0.00 y un cuerpo prácticamente vacío. Eso indica una posible debilidad del filtro para descartar contenido no sustantivo antes de llegar a análisis.

## Evidence
- El clúster tiene un único documento con engagement 0 y novedad 0.00 — source: dec9f3cc9a87f904
- El analista señala como riesgo el falso positivo de filtrado — source: dec9f3cc9a87f904
- La relevancia reportada es 0.33, sobre un cuerpo de una sola frase — source: dec9f3cc9a87f904

## Why it matters
Si el filtro no descarta cuerpos vacíos, el coste se paga en cada etapa posterior: análisis, crítica y compilación de notas sobre ruido. Un umbral mínimo de longitud de cuerpo o de novedad evitaría este gasto.

Se relaciona con `relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista` y con `etiqueta-determinista-como-falso-positivo-de-categoria`: misma familia de fallos de precisión del pipeline. Deriva de la nota del singleton.

## Links
- relates_to → [[relevancia-cero-en-cluster-sobrevive-al-filtrado-determinista]]
- relates_to → [[etiqueta-determinista-como-falso-positivo-de-categoria]]
- derived_from → [[react-for-two-computers-singleton-engagement-cero]]
