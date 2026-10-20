---
id: spike-por-proveedor-para-comportamiento-de-rechazo
title: Spike por proveedor antes de comprometer features que dependen del rechazo
  del modelo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-17'
updated: '2026-10-20'
sources:
- 19cb8032958cd964
tags:
- diseno-de-agentes
- estimacion
- multimodal
- proveedores
- rechazo
- spike
- verificacion
base_confidence: 0.3
half_life_days: 365
last_reinforced: '2026-10-20'
provenance:
  scale: XL
  query: null
links:
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: derived_from
- to: impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: relates_to
- to: divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor
  type: derived_from
- to: criterios-de-aceptacion-dependientes-de-proveedor
  type: supports
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: supports
- to: divergencia-de-rechazo-entre-proveedores
  type: derived_from
- to: aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales
  type: relates_to
- to: capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo
  type: supports
---

## What it is
Cuando una feature depende de que el modelo emita respuestas que un proveedor puede rechazar por política, el comportamiento de rechazo es una variable de diseño. La práctica: probar cada proveedor candidato con prompts y cuentas representativas antes de comprometer el flujo, y abstraer la capa de rechazo en el código del agente en lugar de asumir paridad.

## Evidence
- Prompts idénticos producen rechazo duro en un proveedor y respuesta en otro, según el contraste ChatGPT/Claude frente a Gemini — source: 19cb8032958cd964
- La conducta de rechazo se ajusta con system prompts y configuración de cuenta, y cambia con cadencia semanal — source: 19cb8032958cd964

## Why it matters
Convierte una observación anecdótica en una regla de ingeniería operativa: el guardrail del proveedor es parte del runtime. Un spike temprano evita descubrir la divergencia en producción, y hace explícitos los criterios de aceptación por proveedor.

Deriva de la divergencia observada en `divergencia-de-rechazo-entre-proveedores` y se relaciona con `aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales`. Apoya la distinción de `capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo`, que justifica tratar el rechazo como variable propia.

## Links
- derived_from → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- relates_to → [[impacto-de-corte-de-proveedor-en-flujos-de-coding-con-ia]]
- relates_to → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- derived_from → [[divergencia-de-rechazo-nombrar-figuras-publicas-por-proveedor]]
- supports → [[criterios-de-aceptacion-dependientes-de-proveedor]]
- supports → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- derived_from → [[divergencia-de-rechazo-entre-proveedores]]
- relates_to → [[aceptacion-de-criterios-dependientes-de-proveedor-en-features-multimodales]]
- supports → [[capacidad-tecnica-y-politica-de-rechazo-no-son-lo-mismo]]
