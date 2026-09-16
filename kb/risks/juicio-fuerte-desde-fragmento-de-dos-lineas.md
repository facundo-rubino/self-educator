---
id: juicio-fuerte-desde-fragmento-de-dos-lineas
title: 'Colapsar un fragmento de dos líneas a juicio fuerte: modo de fallo del matching
  por título'
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
- db20384eecad29c2
tags:
- matching-por-titulo
- falsos-positivos
- pipeline
- calibracion
base_confidence: 0.8
half_life_days: 120
last_reinforced: '2026-09-16'
provenance:
  scale: XL
  query: null
links:
- to: clustering-por-embedding-produce-falsos-positivos
  type: relates_to
- to: mismatch-query-tema-por-vocabulario-generico-de-infraestructura
  type: relates_to
- to: relevancia-no-es-verdad
  type: relates_to
- to: confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido
  type: relates_to
---

## What it is
El clúster de «Coping with Feedback» [db20384eecad29c2] fue marcado por su título y obtuvo relevance=0.00, engagement=0, y corroboración/velocity de 0.50. El caso es un falso positivo del filtro determinista o del embedding con nombre propio: el título capta el match, el cuerpo no contiene claim alguno. La implicación declarada por el analista es que la etapa de matching debería ponderar el cuerpo por encima del título [db20384eecad29c2].

## Evidence
- El documento fue flagged principalmente por su título, con relevance=0.00 y sin claim extraíble en el cuerpo — source: db20384eecad29c2
- El documento tiene engagement=0 — source: db20384eecad29c2
- El analista concluye que el filtro debería ponderar cuerpo sobre título — source: db20384eecad29c2

## Why it matters
Registrar el modo de fallo permite tratarlo como señal estructural del pipeline y no como hallazgo temático. El critic advierte además que «relevance=0.00 no es un dato neutro, es una señal explícita» [db20384eecad29c2]; ignorarla y forzar un claim temático sería la fabricación que el brief prohíbe.

Se relaciona con «clustering-por-embedding-produce-falsos-positivos» por compartir el mecanismo de match superficial. Se relaciona con «mismatch-query-tema-por-vocabulario-generico-de-infraestructura» porque aquí el match proviene igualmente de vocabulario superficial. Se relaciona con «relevancia-no-es-verdad» porque el título relevante no valida afirmación alguna. Se relaciona con «confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido» por el mismo patrón: puntuar alto un hallazgo por ausencia.

## Links
- relates_to → [[clustering-por-embedding-produce-falsos-positivos]]
- relates_to → [[mismatch-query-tema-por-vocabulario-generico-de-infraestructura]]
- relates_to → [[relevancia-no-es-verdad]]
- relates_to → [[confianza-inflada-en-hallazgo-sobre-ausencia-de-contenido]]
