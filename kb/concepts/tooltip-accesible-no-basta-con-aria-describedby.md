---
id: tooltip-accesible-no-basta-con-aria-describedby
title: Un tooltip no queda accesible solo con aria-describedby
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-09-18'
sources:
- ded7560510c137bc
tags:
- accesibilidad
- aria
- tooltips
- frontend
base_confidence: 0.2
half_life_days: 180
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: aria-describedby-tooltip-sin-detalle-de-mecanismo
  type: relates_to
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: relates_to
---

## What it is
La afirmación de que `aria-describedby` no basta por sí solo para hacer accesible un tooltip. El documento que la sostiene se titula «Fixing my tooltip accessibility mistake» y su extracto se limita a la frase «aria-describedby isn't always enough» [ded7560510c137bc]. No hay en la evidencia disponible ningún desarrollo del mecanismo alternativo, del error concreto ni del alcance de la insuficiencia.

## Evidence
- El título del documento es «Fixing my tooltip accessibility mistake» — source: ded7560510c137bc
- El extracto afirma «aria-describedby isn't always enough» — source: ded7560510c137bc
- El documento es de tipo rss con engagement=0 y sin métricas de interacción — source: ded7560510c137bc

## Why it matters
Si la lección se confirmara, sería un recordatorio de que las soluciones ARIA de primera línea suelen requerir refuerzos (roles, gestión de foco o texto visible) para que un tooltip sea realmente accesible. Queda dentro del apartado de oficio de software engineering del topic, pero como está escrito no habilita ninguna decisión operativa: falta el caso, el fallo observado y la corrección aplicada.

Se relaciona con la nota ya existente sobre el mismo fallo sin detalle de mecanismo, que registra la misma laguna desde el ángulo del titular. La afirmación se apoya únicamente en el extracto de una línea del documento fuente, sin corroboración interna en el clúster.

## Links
- relates_to → [[aria-describedby-tooltip-sin-detalle-de-mecanismo]]
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
