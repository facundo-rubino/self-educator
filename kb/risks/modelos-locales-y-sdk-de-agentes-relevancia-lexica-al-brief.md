---
id: modelos-locales-y-sdk-de-agentes-relevancia-lexica-al-brief
title: 'Modelos locales y SDKs de agentes: relevancia léxica, no aplicación al brief'
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 7dfcf665b3804d53
- 8fcdcce4ee03a9ba
- ba7992c6345c2dd4
- bd6eeffe0eb9a235
tags:
- modelos-locales
- sdk
- brief
- lexico
base_confidence: 0.82
half_life_days: 120
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: cluster-muse-wen-mismatch-topico-sin-evidencia
  type: supports
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: derived_from
- to: relevancia-no-es-verdad
  type: relates_to
---

## What it is
Los documentos de este clúster comparten tokens de superficie con el brief («AI»), «models», «agents») pero ninguno discute la aplicación de esos modelos o SDKs a programar, estimar, secuenciar, gestionar o enseñar. La adyacencia es de vocabulario, no de contenido.

## Evidence
- El anuncio de soporte de modelos locales en el SDK Antigravity ([7dfcf665b3804d53]) describe una feature de tooling, no su uso ni resultados — source: 7dfcf665b3804d53
- El modelo local de 1B para asistente de conducción con ADAS ([8fcdcce4ee03a9ba]) es una aplicación embebida sin relación con liderazgo, docencia o productividad — source: 8fcdcce4ee03a9ba
- La arquitectura HySparse2 en MiMo-V3 ([ba7992c6345c2dd4]) es noticia de investigación de modelos, no de oficio de ingeniería — source: ba7992c6345c2dd4
- La petición de variantes hipotéticas de Gemma ([bd6eeffe0eb9a235]) es wishlisting sin bearing sobre el tópico — source: bd6eeffe0eb9a235

## Why it matters
Si los modelos locales y SDKs de agentes están genuinamente en alcance, el pipeline necesita documentos cuyo texto discuta su aplicación a coding, estimación o docencia — no anuncios de su existencia. Tomar la existencia de la herramienta como evidencia de su uso es el modo de fallo que este riesgo nombra.

Se deriva del patrón de mismatch por vocabulario genérico de infraestructura (mismatch-query-tema-por-vocabulario-generico-de-infraestructura), del que estos documentos son un caso concreto. Es evidencia de soporte para el diagnóstico de clúster desalineado (cluster-muse-wen-mismatch-topico-sin-evidencia) y se relaciona con la advertencia de que la relevancia no es verdad (relevancia-no-es-verdad).

## Links
- supports → [[cluster-muse-wen-mismatch-topico-sin-evidencia]]
- derived_from → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-no-es-verdad]]
