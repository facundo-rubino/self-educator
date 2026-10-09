---
id: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
title: '«LLMs can now identify public figures in images»: claim sin metodología'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-02'
updated: '2026-10-09'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- claim-sin-metodologia
- figuras-publicas
- identificacion-de-personas
- identificacion-figuras-publicas
- multimodal
- policy
- reconocimiento-facial
- rss
- rss-singleton
- sin-metodologia
- vision
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief
  type: supports
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: supports
- to: afirmar-capacidad-desde-un-titular-rss-sobre-identificacion
  type: supports
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: identificacion-de-figuras-publicas-ya-existia
  type: relates_to
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: derived_from
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
  type: supports
- to: concepto-precedente-identificacion-de-figuras-publicas
  type: relates_to
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: supports
- to: segundo-corpus-necesario-para-afirmar-capacidad-multimodal
  type: supports
---

## What it is
Un único ítem RSS afirma que ChatGPT y Claude no identifican figuras públicas en imágenes, mientras que Gemini sí lo haría. No hay metodología, ni versión de modelo, ni dataset, ni tasa de aciertos o falsos positivos; solo la aserción de comportamiento de producto. El critic lo degrada a coincidencia léxica/asertiva, no a hallazgo empírico, y el resultado final del pipeline es confidence 0.08 sobre un signal con novelty=0.00.

## Evidence
- «ChatGPT y Claude no identificarían figuras públicas en imágenes, mientras que Gemini sí lo haría» — source: 19cb8032958cd964
- El documento fue ingerido como RSS sin engagement (engagement=0), sin corroboración externa dentro del clúster — source: 19cb8032958cd964
- Veredicto del pipeline: novedad nula (novelty=0.00) y corroboración por debajo de umbral (0.50) — source: 19cb8032958cd964

## Why it matters
Una afirmación de capacidad multimodal que no cita versión, dataset ni condiciones es exactamente el modo de fallo descrito en las notas de riesgo del KB: se convierte en rumor operativo antes de ser resultado. Cualquier decisión sobre paridad entre proveedores basada en este ítem sería prematura; el coste real es que el brief recibe ruido etiquetado como hallazgo.

Se apoya directamente en `afirmacion-de-capacidad-multimodal-sin-metodologia` (el patrón general de claim multimodal sin condiciones), en `afirmacion-de-capacidad-desde-fragmento-de-una-linea` y en `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion` (variantes ya registradas del mismo error). Se conecta temáticamente con `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor` porque ambos dependen de la asimetría entre proveedores, y hereda la conclusión de `segundo-corpus-necesario-para-afirmar-capacidad-multimodal` y `relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief`: un singleton no sostiene una afirmación poblacional ni cubre los ejes del brief.

## Links
- supports → [[relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief]]
- supports → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- supports → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- supports → [[afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[concepto-precedente-identificacion-de-figuras-publicas]]
- supports → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[segundo-corpus-necesario-para-afirmar-capacidad-multimodal]]
