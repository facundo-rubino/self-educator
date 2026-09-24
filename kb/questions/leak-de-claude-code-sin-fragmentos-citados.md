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
updated: '2026-09-24'
sources:
- abf61eeec75462f9
tags:
- claude-code
- evidencia-debil
- fuente-primaria
- leak
- prompt-engineering
- verificacion
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-09-24'
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
---

## What it is
El clúster no cita ningún fragmento, condición concreta, número de secciones ni versión de Claude Code. Solo afirma que el system prompt se ensambla a partir de «decenas de partes condicionales», sin mostrar el mecanismo que permitiría verificarlo. La pregunta abierta es qué condiciones gatean qué secciones y sobre qué versión del producto se observó.

## Evidence
- El único claim del clúster atribuye a una filtración de código fuente el ensamblado del system prompt a partir de decenas de partes condicionales — source: abf61eeec75462f9
- El clúster contiene un único documento, con engagement=0 y novelty=0.00 — source: abf61eeec75462f9
- El propio análisis fija la confianza inicial en 0.15 y el crítico la ajusta a 0.05 — source: abf61eeec75462f9

## Why it matters
Sin fragmentos ni condiciones nombradas, la afirmación no es contrastable. Cualquier lección de diseño que se extraiga de ella queda sin anclaje: no se puede distinguir entre una descripción genérica de un system prompt modular y una arquitectura concreta observada.

Continúa el hilo de `claude-code-source-leak-conditions-parts-unspecified` y `claude-code-condiciones-que-gatean-secciones-sin-observar`: la misma carencia de observación directa reaparece aquí. Se apoya en `leak-sin-autenticidad-establecida` (un leak sin autenticidad no confirma lo que dice) y en `vista-filtrada-del-codigo-no-confirma-composicion-condicional`.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
- relates_to → [[claude-code-source-leak-conditions-parts-unspecified]]
- relates_to → [[leak-sin-autenticidad-establecida]]
- relates_to → [[hy3-fuente-primaria-y-metodologia-ausentes]]
- relates_to → [[claude-code-condiciones-que-gatean-secciones-sin-observar]]
- relates_to → [[vista-filtrada-del-codigo-no-confirma-composicion-condicional]]
