---
id: leak-sin-autenticidad-establecida
title: Un leak sin autenticidad establecida no confirma lo que dice el leak
type: risk
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
- provenance
- leaks
- circularidad
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: claude-code-system-prompt-conditional-composition
  type: relates_to
---

## What it is
Usar un «código fuente filtrado» como fuente de un claim sobre el contenido de ese código crea circularidad: la autenticidad del leak se afirma, no se establece. Sin corroboración independiente, el leak solo prueba que alguien publicó una afirmación, no que el sistema descrito funcione así. El contenido puede ser inexacto, desactualizado o malinterpretado.

## Evidence
- La fuente del clúster es un leak y su procedencia «filtrado» se afirma sin examen — source: abf61eeec75462f9
- No hay fuentes independientes en el clúster que confirmen el contenido del leak — source: abf61eeec75462f9

## Why it matters
Cualquier nota derivada de un leak hereda una confianza que la fuente no sostiene. El riesgo no es solo que el dato sea falso, sino que la circularidad impide detectarlo: el leak se usa para confirmar lo que el leak dice. Antes de elevar la confianza de `claude-code-system-prompt-conditional-composition` hace falta corroboración externa o verificación directa del comportamiento descrito.

`relates_to` con `claude-code-system-prompt-conditional-composition`: esta nota condiciona la confianza de aquella; es la razón por la que su `base_confidence` queda en 0.05 en lugar de subir con la mera existencia del documento.

## Links
- relates_to → [[claude-code-system-prompt-conditional-composition]]
