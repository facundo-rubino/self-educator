---
id: pipelines-que-evaluan-clusters-sin-recuperar-el-cuerpo-del-documento
title: 'Riesgo de pipeline: evaluar clústeres cuyo cuerpo no se recuperó'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-12'
updated: '2026-10-12'
sources:
- 19cb8032958cd964
tags:
- riesgo
- pipeline
- ingesta
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-12'
provenance:
  scale: XL
  query: null
links:
- to: coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido
  type: supports
- to: validacion-de-senal-por-contenido-no-por-titulo
  type: supports
---

## What it is
La confianza reportada del pipeline (0.02 tras crítica) se calcula sobre un clúster cuyo cuerpo nunca se recuperó. El propio crítico advierte que no hay benchmark, versión ni protocolo: nada que distinga un hallazgo real de una capacidad alucinada o una anécdota de proveedor. El veredicto es acertado, pero su base es el mismo artefacto de ingesta que evalúa, no el documento fuente.

## Evidence
- El único documento del cluster es un titular RSS sin cuerpo analítico que permita verificar la afirmación — source: 19cb8032958cd964
- El clúster tiene novelty=0.00 y corroboration=0.50, es decir, la evaluación se hace sobre metadatos del propio pipeline — source: 19cb8032958cd964

## Why it matters
Si el body del ítem no se recuperó, ningún veredicto sobre su contenido —ni positivo ni negativo— está anclado en la fuente. El riesgo correcto se aplica aquí, pero el modo de fallo del sistema es más amplio: veredictos calculados sobre cuerpos ausentes pueden coincidir por casualidad con la verdad y aun así propagarse como si fueran evidencia.

Se apoya en la regla de validar la señal por solapamiento de contenido y no por el título, y en el riesgo de que una coincidencia de título no sea corroboración de contenido. Complementa la crítica específica al claim sin sustituirla.

## Links
- supports → [[coincidencia-de-titulo-con-post-conocido-no-es-corroboracion-de-contenido]]
- supports → [[validacion-de-senal-por-contenido-no-por-titulo]]
