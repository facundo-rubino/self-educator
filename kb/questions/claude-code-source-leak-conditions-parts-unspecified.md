---
id: claude-code-source-leak-conditions-parts-unspecified
title: El leak de Claude Code no especifica condiciones, partes ni secuenciación
type: question
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-16'
updated: '2026-09-16'
sources:
- abf61eeec75462f9
tags:
- claude-code
- system-prompt
- evidencia-faltante
base_confidence: 0.5
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: derived_from
---

## What it is
La afirmación disponible sobre el prompt de Claude Code no responde a las preguntas que la harían verificable: ¿qué condiciones activan cada parte?, ¿cuántas partes hay y de qué tipo?, ¿en qué orden se ensamblan?, ¿cómo se evaluó el «filtrado»? Sin estas respuestas, el claim no es falsable y por tanto no hay nada que replicar ni contradecir.

## Evidence
- No hay detalles sobre qué condiciones, qué partes, cómo se secuencian, ni cómo se evaluó el «filtrado» — source: abf61eeec75462f9

## Why it matters
Nombrar las preguntas abiertas permite buscarlas en fuentes futuras: si aparece una descripción con condiciones y secuenciación concretas, la nota `claude-code-system-prompt-conditional-composition` puede subir de confianza; mientras tanto, queda como pregunta sin resolver y no como hallazgo.

`derived_from` `claude-code-system-prompt-conditional-composition`: esta nota es la lista de vacíos que impide tratar ese claim como un hallazgo cerrado.

## Links
- derived_from → [[claude-code-system-prompt-conditional-composition]]
