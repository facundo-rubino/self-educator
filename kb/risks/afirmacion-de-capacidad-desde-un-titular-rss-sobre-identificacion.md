---
id: afirmacion-de-capacidad-desde-un-titular-rss-sobre-identificacion
title: 'Afirmar «LLMs can now identify public figures» desde un titular RSS: capacidad
  confundida con cumplimiento'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-09-21'
sources:
- 19cb8032958cd964
tags:
- epistemologia
- multimodal
- politica-de-modelos
- falsa-capacidad
base_confidence: 0.25
half_life_days: 120
last_reinforced: '2026-09-21'
provenance:
  scale: XL
  query: null
links:
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: relates_to
- to: una-observacion-no-sostiene-claim-poblacional-sobre-llm
  type: relates_to
- to: politica-de-face-recognition-como-variable-de-producto
  type: relates_to
---

## What it is
Un titular RSS afirma que «los LLM ahora pueden identificar figuras públicas en imágenes». El «ahora» sugiere capacidad nueva y generalizada; la evidencia subyacente es una comparación de disposición a responder entre tres proveedores, con metodología, versión y muestra sin especificar. La afirmación de capacidad no se sigue de la observación de cumplimiento.

## Evidence
- «El documento enmarca el hecho como una afirmación de capacidad ("LLMs can now identify public figures in images"), es decir, que el comportamiento es nuevo o recién notable» — source: 19cb8032958cd964
- «La evidencia es una comparación de comportamiento entre vendedores sin metodología, tamaño de muestra ni versionado especificados» — source: 19cb8032958cd964

## Why it matters
Tratar esto como un salto de capacidad lleva a conclusiones equivocadas: que el análisis visual de personas es ampliamente desplegable, o que un proveedor es «más capaz». Reconocer una cara es una tarea de visión de larga data; que un modelo la nombre depende de su política. Antes de citar este hallazgo como capability, hace falta fuente primaria y comparación controlada.

Es un caso concreto del modo de fallo descrito en `afirmacion-de-capacidad-desde-fragmento-de-una-linea` y refuerza `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`. Se relaciona con `una-observacion-no-sostiene-claim-poblacional-sobre-llm` (un proveedor no sostiene un claim poblacional) y con `politica-de-face-recognition-como-variable-de-producto` (la política como variable, no la capacidad). Conecta con `divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor`, el hallazgo observable del que se extrae la afirmación.

## Links
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- relates_to → [[una-observacion-no-sostiene-claim-poblacional-sobre-llm]]
- relates_to → [[politica-de-face-recognition-como-variable-de-producto]]
