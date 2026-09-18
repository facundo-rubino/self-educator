---
id: ataques-a-mantenedores-open-source-como-senal-lexica
title: «Attack» más contexto técnico no licencia la inferencia de ataques a personas
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-18'
updated: '2026-09-18'
sources:
- sig-ab0291e19631
tags:
- epistemologia
- falacias
- nlp
- señales
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-09-18'
provenance:
  scale: XL
  query: null
links:
- to: senal-ataques-a-rustaceans-no-sostenida-por-el-cluster
  type: derived_from
- to: ataque-de-agentes-openai-a-rubygems-no-es-ataque-a-rustaceans
  type: derived_from
---

## What it is
Emparejar la palabra «attack» con un contexto tecnológico y etiquetar el resultado como «ataques dirigidos a Rustaceans prominentes» es una falacia de similitud léxica. La señal es un significante flotante sin anclaje en el texto: ninguna cadena documental conecta el término con una persona o comunidad concretas.

## Evidence
- El clúster no contiene ningún documento que nombre un Rustacean atacado — source: sig-ab0291e19631
- La única coincidencia léxica es «attack» en un incidente de RubyGems, ecosistema distinto al señalado — source: 0173bcc038bed4eb

## Why it matters
El modo de fallo — retrofitar una etiqueta sobre documentos no relacionados por coincidencia de vocabulario — es una fuente de contaminación de señales que conviene detectar y nombrar explícitamente. La coincidencia de una palabra clave no es evidencia de un fenómeno social.

Se deriva de `senal-ataques-a-rustaceans-no-sostenida-por-el-cluster` y de `ataque-de-agentes-openai-a-rubygems-no-es-ataque-a-rustaceans`: aísla el mecanismo inferencial específico (parecido léxico) que produce la señal falsa.

## Links
- derived_from → [[senal-ataques-a-rustaceans-no-sostenida-por-el-cluster]]
- derived_from → [[ataque-de-agentes-openai-a-rubygems-no-es-ataque-a-rustaceans]]
