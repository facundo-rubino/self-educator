---
id: afirmar-capacidad-multimodal-sin-metodologia
title: Una afirmación de capacidad multimodal sin metodología no es verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-13'
updated: '2026-10-20'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- capacidad
- claim-sin-evidencia
- claim-sin-metodologia
- metodologia
- multimodal
- verificabilidad
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: derived_from
- to: confirmacion-de-evaluacion-por-terceros-no-es-adopcion
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: derived_from
- to: segundo-corpus-necesario-para-afirmar-capacidad-multimodal
  type: supports
- to: identificar-no-es-reconocer-en-la-fuente
  type: relates_to
- to: llms-identifican-figuras-publicas-sin-metodologia
  type: relates_to
- to: afirmacion-de-capacidad-multimodal-sin-metodologia
  type: relates_to
---

## What it is
Un claim de capacidad («los LLM ahora identifican figuras públicas») exige precisión, tasas de error y cobertura. El documento no aporta ninguno: ni número de imágenes, ni versiones, ni redacción de prompts. Lo que sí reporta es qué proveedor nombra y cuál se niega. Sin medición, el claim no es verificable y el contraste puede ser un artefacto de sensibilidad al prompt.

## Evidence
- El documento no detalla cuántas imágenes, qué versiones de modelo ni cómo se formularon los prompts — source: 19cb8032958cd964
- La afirmación de capacidad se apoya en una sola fuente anecdótica («one outlet's testing») — source: 19cb8032958cd964

## Why it matters
Promover este claim a hallazgo del brief inflaría una anécdota periférica. Confundir rechazo con incapacidad produciría una conclusión engañosa y, en un tema de privacidad y derechos de imagen, tratar «Gemini lo hace» como recomendación sería irresponsable sin examinar consentimiento y jurisdicción.

Es el riesgo que pesa sobre `llms-identifican-figuras-publicas-sin-metodologia` y duplica el modo de fallo ya registrado en `afirmacion-de-capacidad-multimodal-sin-metodologia`.

## Links
- derived_from → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
- relates_to → [[confirmacion-de-evaluacion-por-terceros-no-es-adopcion]]
- derived_from → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- supports → [[segundo-corpus-necesario-para-afirmar-capacidad-multimodal]]
- relates_to → [[identificar-no-es-reconocer-en-la-fuente]]
- relates_to → [[llms-identifican-figuras-publicas-sin-metodologia]]
- relates_to → [[afirmacion-de-capacidad-multimodal-sin-metodologia]]
