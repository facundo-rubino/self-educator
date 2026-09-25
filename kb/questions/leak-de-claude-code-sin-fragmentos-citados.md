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
updated: '2026-09-25'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia
- evidencia-debil
- fuente-primaria
- leak
- prompt-engineering
- verificabilidad
- verificacion
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-25'
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
---

## What it is
El documento abf61eeec75462f9 reporta el ensamblado condicional del system prompt de Claude Code, pero no cita fragmentos del supuesto código filtrado, ni los disparadores que activarían cada parte, ni la versión a la que corresponde el leak. Queda sin respuesta qué condiciones gatean qué secciones y cuántas partes hay exactamente.

## Evidence
- La señal llega vía una fuente agregada de tipo rss con engagement=0, sin fragmentos ni disparadores citados — source: abf61eeec75462f9

## Why it matters
Sin fragmentos citables ni versión, la observación no es replicable ni fechable: no se puede distinguir si describe el diseño actual, una versión pasada o una lectura parcial del código. Cualquier afirmación sobre mecánica interna queda en el terreno de la reconstrucción, no de la verificación.

Se apoya en `claude-code-system-prompt-conditional-composition` como el enunciado que carece de soporte. `leak-de-claude-code-como-cluster-de-un-solo-documento` registra que el clúster se sostiene en un único documento con engagement=0. `leak-sin-autenticidad-establecida` recoge el problema general: un leak sin autenticidad establecida no confirma lo que dice el leak.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
- relates_to → [[leak-de-claude-code-como-cluster-de-un-solo-documento]]
