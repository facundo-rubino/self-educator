---
id: leak-de-claude-code-sin-fragmentos-citados
title: El leak de Claude Code no trae fragmentos, disparadores ni versión
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-21'
updated: '2026-10-05'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia
- evidencia-debil
- fuente-primaria
- leak
- prompt-engineering
- prompts-condicionales
- verificabilidad
- verificacion
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
- to: claude-code-source-leak-conditions-parts-unspecified
  type: relates_to
- to: leak-sin-autenticidad-establecida
  type: relates_to
- to: hy3-fuente-primaria-y-metodologia-ausentes
  type: relates_to
- to: claude-code-condiciones-que-gatean-secciones-sin-observar
  type: relates_to
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: relates_to
- to: leak-de-claude-code-como-cluster-de-un-solo-documento
  type: relates_to
- to: afirmacion-de-capacidad-desde-fragmento-de-una-linea
  type: supports
- to: vista-filtrada-del-codigo-no-confirma-composicion-condicional
  type: supports
- to: legibilidad-de-la-afirmacion-sin-fuente-primaria
  type: relates_to
- to: claude-code-source-leak-condiciones-parts-unspecified
  type: relates_to
- to: claude-code-system-prompt-doc-sin-analisis-de-condiciones
  type: relates_to
---

## What it is
El documento del clúster afirma que el system prompt de Claude Code se ensambla de «docenas de partes condicionales», pero no cita fragmentos de prompt, no describe la lógica de ensamblado, no enumera disparadores y no fija una versión del producto. Es una pregunta abierta que el corpus actual no puede cerrar.

## Evidence
- El clúster no contiene evidencia sobre el contenido real de las partes condicionales, cómo se ensamblan ni sus consecuencias para la calidad del agente — source: abf61eeec75462f9

## Why it matters
Sin fragmentos citados ni reglas de ensamblado, la afirmación no es accionable para un líder técnico: no hay nada que copiar, versionar o auditar. Cualquier inferencia sobre composición condicional en agentes propios partiría de una premisa no verificada.

Es la cara de laguna de la nota de concepto sobre el ensamblado condicional de Claude Code, y comparte terreno con las notas que ya registran la ausencia de condiciones, partes y secuenciación observadas en el leak.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- relates_to → [[leak-de-claude-code-como-cluster-de-un-solo-documento]]
- supports → [[afirmacion-de-capacidad-desde-fragmento-de-una-linea]]
- supports → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- relates_to → [[legibilidad-de-la-afirmacion-sin-fuente-primaria]]
- relates_to → [[claude-code-source-leak-condiciones-parts-unspecified]]
- relates_to → [[claude-code-system-prompt-doc-sin-analisis-de-condiciones]]
