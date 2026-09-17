---
id: politica-de-face-recognition-como-variable-de-producto
title: La política de reconocimiento facial como variable de producto, no de modelo
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-09-17'
sources:
- 19cb8032958cd964
tags:
- face-recognition
- gobernanza
- cumplimiento
- multimodal
base_confidence: 0.3
half_life_days: 180
last_reinforced: '2026-09-17'
provenance:
  scale: XL
  query: null
links:
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: relates_to
---

## What it is
Identificar figuras públicas a partir de imágenes de usuario activa regímenes de privacidad biométrica y términos de uso que difieren por API. La política de reconocimiento facial es, por tanto, una variable de gobernanza y cumplimiento del producto, no un atributo del modelo elegido.

## Evidence
- El análisis identifica la regulación de privacidad biométrica (GDPR, regímenes tipo BIPA) y los términos de uso por API como dominios relevantes para verificar la afirmación — source: 19cb8032958cd964
- Los riesgos enumerados incluyen la exposición legal y reputacional de construir features de identificación sin consentimiento — source: 19cb8032958cd964

## Why it matters
Desplaza la decisión de «qué modelo es mejor» a «qué proveedor permite qué, bajo qué términos y en qué jurisdicción». Es la pregunta que precede a cualquier feature de subida de imágenes orientada a identificar personas.

Se relaciona con la divergencia de rechazo entre proveedores, que es su manifestación observable, y con los criterios de aceptación dependientes de proveedor, que deben incorporar la capa de cumplimiento por región.

## Links
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
