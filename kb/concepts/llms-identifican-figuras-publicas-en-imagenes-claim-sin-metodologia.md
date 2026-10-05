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
updated: '2026-10-05'
sources:
- 19cb8032958cd964
tags:
- claim-sin-metodologia
- figuras-publicas
- multimodal
- policy
- sin-metodologia
- vision
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-10-05'
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
---

## What it is
Un único documento [19cb8032958cd964] afirma que los LLMs ahora pueden identificar figuras públicas en imágenes, y concreta la asimetría entre proveedores: ChatGPT y Claude se niegan a hacerlo, Gemini sí lo hace. El documento no aporta metodología, prompts, versiones de modelo, fechas ni URLs a pruebas reproducibles. La observación es anecdótica y de segunda mano, sin verificación independiente dentro del clúster.

## Evidence
- ChatGPT y Claude no identifican figuras públicas en imágenes, pero Gemini sí — source: 19cb8032958cd964
- No se aportan URLs, imágenes de prueba, fechas, versiones de modelo ni comparación controlada — source: 19cb8032958cd964 (ausencia verificada en el reporte del clúster)
- Novedad reportada 0.00 y corroboración 0.50: la señal ya circulaba y no está confirmada por fuentes múltiples — source: sig-237cc97a9794

## Why it matters
Si la asimetría fuera real y estable, un dev que construye agentes multimodales tendría que elegir proveedor por tarea y no asumir paridad de capacidades. Pero con base de evidencia 0.10 y un solo documento anecdótico, la afirmación no sostiene ninguna decisión de adopción: queda como claim a verificar, no como hallazgo.

`identificacion-de-figuras-publicas-ya-existia` acota la novedad: la capacidad ya estaba sobre la mesa, y este documento solo la reafirma con una observación sin controles. `afirmacion-de-capacidad-multimodal-sin-metodologia` y `afirmar-capacidad-desde-un-titular-rss-sobre-identificacion` son el patrón de fallo que este ítem ilustra. `gemini-no-rechaza-nombrar-figuras-publicas` es la nota-actor que aporta el único dato concreto (el proveedor que sí lo hace).

## Links
- supports → [[relevancia-tangencial-de-identificacion-de-figuras-publicas-al-brief]]
- supports → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- supports → [[afirmar-capacidad-desde-un-titular-rss-sobre-identificacion]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- relates_to → [[identificacion-de-figuras-publicas-ya-existia]]
- derived_from → [[gemini-no-rechaza-nombrar-figuras-publicas]]
