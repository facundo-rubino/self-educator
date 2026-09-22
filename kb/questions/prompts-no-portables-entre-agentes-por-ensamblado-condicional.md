---
id: prompts-no-portables-entre-agentes-por-ensamblado-condicional
title: Los prompts no son portables entre agentes si la conducta se ensambla condicionalmente
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-22'
updated: '2026-09-22'
sources:
- abf61eeec75462f9
tags:
- agentes
- prompts
- portabilidad
- system-prompt
base_confidence: 0.1
half_life_days: 120
last_reinforced: '2026-09-22'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
- to: test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes
  type: relates_to
- to: control-de-agente-como-composicion-de-secciones
  type: relates_to
---

## What it is
Si el system prompt de un agente se ensambla de partes condicionales en runtime (doc:abf61eeec75462f9), entonces un prompt, archivo de reglas o skill escrito para un agente no se traslada verbatim a otro: habría que re-derivar la lógica de ensamblado por herramienta. La pregunta es si esto se sostiene empíricamente o es extrapolación desde una sola observación. La evidencia disponible no responde: el documento no compara ensamblados entre herramientas ni mide portabilidad.

## Evidence
- El ensamblado condicional del system prompt implicaría que la configuración de conducta es específica por herramienta y contexto — source: abf61eeec75462f9
- El documento no ofrece comparación entre agentes ni medición alguna de portabilidad de prompts — source: abf61eeec75462f9
- La única fuente es un ítem RSS con engagement 0, sin corroboración — source: abf61eeec75462f9

## Why it matters
Afecta directamente decisiones operativas: cuánto invertir en un rules file, si versionar prompts por herramienta, y si enseñar «el prompt» o «la lógica de ensamblado». Mientras la pregunta esté abierta, la práctica razonable es tratar los prompts como configuración re-derivable y no como artefactos portátiles, y no citar esta nota como prueba de que el ensamblado condicional sea la causa de la no-portabilidad.

`derived_from` → `claude-code-system-prompt-conditional-composition`: la pregunta solo existe por ese hallazgo, y hereda su fragilidad. `relates_to` → `test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes`: si la conducta depende de condiciones, el test debe cubrir condiciones, no el prompt completo. `relates_to` → `control-de-agente-como-composicion-de-secciones`: mismo límite, la inferencia de control por composición no está demostrada.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[test-de-regresion-por-condicion-habilitada-en-prompts-de-agentes]]
- relates_to → [[control-de-agente-como-composicion-de-secciones]]
