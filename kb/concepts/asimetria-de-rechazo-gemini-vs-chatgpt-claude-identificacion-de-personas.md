---
id: asimetria-de-rechazo-gemini-vs-chatgpt-claude-identificacion-de-personas
title: Asimetría entre Gemini (identifica) y ChatGPT/Claude (no) al nombrar figuras
  públicas en imágenes
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-09'
updated: '2026-10-09'
sources:
- 19cb8032958cd964
tags:
- gemini
- chatgpt
- claude
- multimodal
- politica-de-modelo
- reconocimiento-de-personas
base_confidence: 0.08
half_life_days: 180
last_reinforced: '2026-10-09'
provenance:
  scale: XL
  query: null
links:
- to: gemini-no-rechaza-nombrar-figuras-publicas
  type: supports
- to: divergencia-de-rechazo-al-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica
  type: supports
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
- to: spike-por-proveedor-para-comportamiento-de-rechazo
  type: supports
- to: probe-de-rechazo-por-identidad-en-produccion
  type: relates_to
---

## What it is
La aserción central del documento [19cb8032958cd964] es una asimetría por proveedor: ChatGPT y Claude no identificarían figuras públicas en imágenes, Gemini sí. La afirmación no distingue entre que el modelo no pueda hacerlo y que el proveedor no quiera hacerlo, lo que abre la lectura alternativa de política de uso antes que de capacidad técnica.

## Evidence
- «ChatGPT y Claude no identificarían figuras públicas en imágenes, mientras que Gemini sí lo haría» — source: 19cb8032958cd964

## Why it matters
Si la diferencia fuese de política y no de rendimiento, entonces la pregunta correcta no es «qué modelo acierta» sino «qué proveedor permite este caso de uso», y la implicación operativa es hacer spike por proveedor antes de comprometer cualquier flujo que dependa de reconocimiento de personas (verificación, moderación, accesibilidad). Tratarla como capacidad llevaría a elegir el modelo equivocado por el criterio equivocado.

Es evidencia directa de `gemini-no-rechaza-nombrar-figuras-publicas` y coincide con la línea de `divergencia-de-rechazo-al-nombrar-figuras-publicas-por-proveedor`. El puente analítico correcto es `afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica` (la lectura política del mismo dato) y `politica-de-face-recognition-como-variable-de-producto` (la política como variable de selección, no de benchmark). La conclusión práctica se articula en `spike-por-proveedor-para-comportamiento-de-rechazo` y `probe-de-rechazo-por-identidad-en-produccion`.

## Links
- supports → [[gemini-no-rechaza-nombrar-figuras-publicas]]
- relates_to → [[divergencia-de-rechazo-al-nombrar-figuras-publicas-por-proveedor]]
- supports → [[afirmacion-de-capacidad-por-defecto-vs-rechazo-por-politica]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
- supports → [[spike-por-proveedor-para-comportamiento-de-rechazo]]
- relates_to → [[probe-de-rechazo-por-identidad-en-produccion]]
