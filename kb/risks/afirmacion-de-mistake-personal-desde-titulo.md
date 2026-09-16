---
id: afirmacion-de-mistake-personal-desde-titulo
title: 'Reconstruir una lección personal desde un titular: narrativa impuesta al texto'
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
- ded7560510c137bc
tags:
- evidencia
- inferencia
- fuentes
- sesgo
base_confidence: 0.05
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: M
  query: null
links:
- to: relevancia-no-es-verdad
  type: relates_to
- to: afirmacion-de-novedad-sin-linea-base
  type: relates_to
---

## What it is
Riesgo de convertir un titular y una frase genérica en una observación sobre el autor: el material solo permite afirmar que el documento se titula «Fixing my tooltip accessibility mistake» y que contiene «aria-describedby isn't always enough.» [ded7560510c137bc]. La línea no afirma que el autor cometiera el error, ni describe el fallo, el usuario o la tecnología de asistencia observada [ded7560510c137bc].

## Evidence
- El documento no especifica modo de falla, corrección ni código — source: ded7560510c137bc
- La frase de encuadre tampoco sostiene que el autor haya enviado una implementación defectuosa — source: ded7560510c137bc
- engagement=0: sin corroboración ni contradicción de terceros — source: ded7560510c137bc

## Why it matters
Cualquier afirmación del tipo «el autor envió un tooltip con aria-describedby y concluyó que no basta» es una reconstrucción narrativa, no una observación del texto [ded7560510c137bc]. Escribirla como hallazgo contamina el grafo con una lección que la fuente no autoriza, y sienta precedente para leer los próximos titulares como casos.

Se enlaza con «relevancia-no-es-verdad» por el mecanismo de circularidad: el texto se lee a través de la expectativa que ya tenía el analista. Se enlaza con «afirmacion-de-novedad-sin-linea-base» porque ambos describen escribir más de lo que la evidencia y su contexto permiten.

## Links
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[afirmacion-de-novedad-sin-linea-base]]
