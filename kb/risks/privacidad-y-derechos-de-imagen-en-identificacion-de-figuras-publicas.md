---
id: privacidad-y-derechos-de-imagen-en-identificacion-de-figuras-publicas
title: 'Identificación de figuras públicas: privacidad y derechos de imagen sin abordar'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-10-05'
sources:
- 19cb8032958cd964
- sig-237cc97a9794
tags:
- consentimiento
- derechos-de-imagen
- docencia
- etica
- gdpr
- imagenes
- multimodal
- privacidad
- vision
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia
  type: relates_to
- to: nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria
  type: derived_from
- to: confundir-rechazo-por-politica-con-capacidad-de-modelo
  type: relates_to
- to: riezgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes
  type: relates_to
- to: llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia
  type: relates_to
- to: privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia
  type: supports
---

## What it is
Identificar figuras públicas en imágenes tiene implicaciones legales y de privacidad (GDPR, derechos de imagen) que el documento no aborda. En el único escenario donde el brief podría tocarlo — docencia con capturas que contienen personas — estas obligaciones tendrían que gestionarse explícitamente antes de cualquier uso.

## Evidence
- El reporte lista como riesgo: implicaciones legales y de privacidad (GDPR, derechos de imagen) no abordadas, que «podrían invalidar su uso en productos reales» — source: sig-237cc97a9794
- El documento fuente se limita a la asimetría funcional entre proveedores, sin tratamiento legal — source: 19cb8032958cd964

## Why it matters
Un helper docente o un agente que analiza material con personas puede quedar bloqueado por cumplimiento incluso cuando el modelo funciona. El costo no es de capacidad, es de licitud y de derechos de terceros.

Extiende `privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia` desde el escenario pedagógico al de la identificación automática, y cuelga del claim multimodal como su cara de riesgo legal.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
- derived_from → [[nombrar-figuras-publicas-no-demuestra-practica-de-ingenieria]]
- relates_to → [[confundir-rechazo-por-politica-con-capacidad-de-modelo]]
- relates_to → [[riezgo-de-corte-silencioso-de-politica-en-flujos-de-imagenes]]
- relates_to → [[llms-identifican-figuras-publicas-en-imagenes-claim-sin-metodologia]]
- supports → [[privacidad-y-consentimiento-en-imagenes-de-personas-para-docencia]]
