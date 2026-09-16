---
id: promocion-de-evento-por-marca-como-senal
title: Promoción de evento por marca como señal falsa
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- d2a0c86ca8027978
tags:
- filtrado
- metadatos
- sesgo-de-marca
- rss
base_confidence: 0.75
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: juez-humano-en-hackathon-llm-as-a-judge-de-wandb
  type: derived_from
---

## What it is
Un filtro determinista de investigación puede dejar pasar contenido de tipo calendario/evento cuando el nombre del evento incluye un término del brief («LLM»). El resultado es ruido de metadatos que ocupa cupo sin aportar hallazgo.

## Evidence
- El clúster está formado por un único documento: una entrada RSS con engagement cero sobre un hackathon — source: d2a0c86ca8027978
- El desajuste temático combinado con engagement cero sugiere una fuga de contenido de eventos/calendario hacia un brief de investigación — source: d2a0c86ca8027978

## Why it matters
Confundir relevancia aparente (marca W&B, término «LLM» en el título del evento) con relevancia real infla el clúster de ruido y desplaza material sustantivo. La marca o el patrocinador de un evento no son evidencia de su contenido.

Deriva directamente del caso «juez-humano-en-hackathon-llm-as-a-judge-de-wandb»: es el mecanismo por el que ese ítem entró al pipeline. Conecta con la familia de riesgos sobre afirmar desde metadatos superficiales.

## Links
- derived_from → [[juez-humano-en-hackathon-llm-as-a-judge-de-wandb]]
