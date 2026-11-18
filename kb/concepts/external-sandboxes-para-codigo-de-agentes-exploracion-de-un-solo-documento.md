---
id: external-sandboxes-para-codigo-de-agentes-exploracion-de-un-solo-documento
title: 'External sandboxes para código ejecutado por agentes: exploración de una sola
  fuente'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-18'
updated: '2026-11-18'
sources:
- f759f88ee60da741
tags:
- sandboxing
- agent-safety
- prompt-injection
- local-models
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-11-18'
provenance:
  scale: S
  query: null
links:
- to: agentes-abatatan-ports-mantener-sigue-costoso
  type: relates_to
- to: external-sandboxes-single-source-engagement-modesto-no-sostiene-doctrina
  type: derived_from
---

## What it is
Trabajo exploratorio sobre nuevas formas de aislar (sandbox) el código que ejecutan agentes de codificación, con la motivación de poder probar modelos locales sin que un error o una inyección de prompt provoque acciones destructivas en la máquina — source: f759f88ee60da741. El trabajo se realizó en colaboración con Prime Radiant, descrito como el laboratorio de investigación en IA detrás de Superpowers y otros proyectos — source: f759f88ee60da741. El documento se presenta como write-up de proyecto con contenido más allá del extracto disponible; el texto completo no está en la fuente ingerida — source: f759f88ee60da741.

## Evidence
- Exploración de sandboxing externo para código ejecutado por agentes, motivada por seguridad al probar modelos locales frente a prompt injection y acciones destructivas — source: f759f88ee60da741
- Colaboración con Prime Radiant, laboratorio detrás de Superpowers — source: f759f88ee60da741
- El extracto termina a mitad de frase: mecanismo, modelo de amenaza y resultados no están en la fuente — source: f759f88ee60da741

## Why it matters
Aporta únicamente el encuadre: el sandboxing externo existe como área de práctica viva para quien lleva flujos asistidos por agentes. No entrega doctrina sobre estimación, secuenciación, alcance ni docencia, por lo que no se puede compilar como hallazgo sobre esos ejes.

Conecta con las notas sobre coste de mantenimiento y productividad de agentes solo de forma lateral: el aislamiento de ejecución condiciona el riesgo operativo, no la productividad. La nota de riesgo `external-sandboxes-single-source-engagement-modesto-no-sostiene-doctrina` documenta por qué este concepto no debe elevarse a hallazgo.

## Links
- relates_to → [[agentes-abatatan-ports-mantener-sigue-costoso]]
- derived_from → [[external-sandboxes-single-source-engagement-modesto-no-sostiene-doctrina]]
