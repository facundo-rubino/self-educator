---
id: aria-describedby-no-basta-para-tooltips-accesibles-integracion
title: 'Fixing my tooltip accessibility mistake: aria-describedby no basta, sin detalle'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-30'
updated: '2026-09-30'
sources:
- ded7560510c137bc
tags:
- accessibility
- aria
- tooltip
- software-craft
- weak-signal
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-30'
provenance:
  scale: XL
  query: null
links:
- to: aria-describedby-no-basta-para-tooltips-accesibles
  type: relates_to
- to: tooltip-accesible-no-basta-con-aria-describedby
  type: relates_to
- to: tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado
  type: supports
- to: inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion
  type: supports
- to: criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo
  type: relates_to
- to: fixing-my-tooltip-accessibility-mistake-titulo-sin-contenido-ingerido
  type: supports
---

## What it is
El documento `ded7560510c137bc` («Fixing my tooltip accessibility mistake») sostiene que `aria-describedby` no basta para hacer accesible un tooltip. Es la única afirmación recuperable: el texto ingerido no incluye el error concreto, la implementación, el modo de fallo, ni la técnica correctiva.

## Evidence
- El clúster consta de un único documento, «Fixing my tooltip accessibility mistake», procedente de una fuente RSS con engagement=0 — source: ded7560510c137bc
- El documento afirma que «aria-describedby isn't always enough», es decir, la asociación de descripción ARIA por sí sola no garantiza la accesibilidad del tooltip — source: ded7560510c137bc
- No hay en el texto ingerido detalles del error, la implementación del tooltip, el modo de fallo ni la técnica correctiva — source: ded7560510c137bc

## Why it matters
Refuerza un principio ya codificado en las prácticas de autoría WAI-ARIA: la accesibilidad de un tooltip exige preocupaciones coordinadas (asociación de nombre/descripción, foco por teclado, exposición de rol y estado, comportamiento de descarte), no un solo atributo. Para un dev que lidera y enseña, sirve a lo sumo como ejemplo de «un atributo no es una solución», pero este clúster no aporta material para construir esa lección ni evidencia sobre agentes de IA, liderazgo técnico, estimación o docencia.

Ver la nota `aria-describedby-no-basta-para-tooltips-accesibles` y la variante `tooltip-accesible-no-basta-con-aria-describedby`, que registran la misma afirmación desde el mismo ítem; esta nota documenta la integración con el detalle (ausente) que la fuente proporciona. `tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado` documenta que el cuerpo llega truncado, lo cual sostiene el límite aquí descrito. `inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion` es el riesgo directo: cualquier reconstrucción del error o la corrección sería alucinación. `criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo` conecta con el patrón más amplio de que un criterio de accesibilidad se verifica con lector de pantalla, no con la presencia del atributo.

## Links
- relates_to → [[aria-describedby-no-basta-para-tooltips-accesibles]]
- relates_to → [[tooltip-accesible-no-basta-con-aria-describedby]]
- supports → [[tooltip-accessibility-solo-titulo-y-fragmento-cuerpo-truncado]]
- supports → [[inferir-error-y-alternativa-del-post-de-tooltip-seria-alucinacion]]
- relates_to → [[criterio-de-accesibilidad-verificado-con-lector-de-pantalla-no-desde-el-atributo]]
- supports → [[fixing-my-tooltip-accessibility-mistake-titulo-sin-contenido-ingerido]]
