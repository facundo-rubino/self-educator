---
id: two-worlds-two-doors-no-es-evidencia-de-separacion-servidor-cliente
title: «Two worlds, two doors.» no es evidencia de la separación servidor/cliente
  en React
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-05'
updated: '2026-10-05'
sources:
- dec9f3cc9a87f904
tags:
- react
- sobreinterpretacion
- artefacto-rss
- false-positive
base_confidence: 0.85
half_life_days: 120
last_reinforced: '2026-10-05'
provenance:
  scale: XL
  query: null
links:
- to: afirmar-contenido-de-react-for-two-computers-seria-especulacion
  type: supports
- to: react-for-two-computers-etiqueta-react-sin-evidencia-de-practica
  type: relates_to
- to: two-things-one-origin-ambiguedad-del-fragmento-sin-contexto
  type: relates_to
---

## What it is
Riesgo de leer «Two things, one origin» como una tesis sobre la separación entre servidor y cliente en React. Esa separación es una arquitectura conocida del ecosistema, de modo que el fragmento puede parecer confirmarla; en realidad no contiene ninguna proposición sobre React, ni sobre dos runtimes, ni sobre ningún mecanismo concreto.

## Evidence
- El documento consiste únicamente en el título «React for Two Computers» y la frase «Two things, one origin», sin desarrollo posterior — source: dec9f3cc9a87f904

## Why it matters
Asignar al documento la tesis «React separa servidor y cliente» importaría conocimiento previo del ecosistema dentro de una nota que debe citar solo su fuente. El tema es lo bastante familiar como para que el error pase desapercibido y contamine notas posteriores que lo citen como respaldo.

Refuerza `afirmar-contenido-de-react-for-two-computers-seria-especulacion`: el modo de fallo concreto es rellenar la ambigüedad con arquitectura conocida. Se relaciona con `react-for-two-computers-etiqueta-react-sin-evidencia-de-practica`, que registra el mismo riesgo un nivel más arriba, al etiquetar el ítem como práctica de ingeniería en lugar de como artefacto de ingesta.

## Links
- supports → [[afirmar-contenido-de-react-for-two-computers-seria-especulacion]]
- relates_to → [[react-for-two-computers-etiqueta-react-sin-evidencia-de-practica]]
- relates_to → [[two-things-one-origin-ambiguedad-del-fragmento-sin-contexto]]
