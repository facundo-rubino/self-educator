---
id: merged-prs-triplicados-no-es-evidencia-de-productividad-por-agentes
title: «Merged PRs tripled» no es evidencia de productividad causada por agentes
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-29'
updated: '2026-10-29'
sources:
- 0aabafab1db5fa31
tags:
- metrica-mal-definida
- causalidad
- vendor-narrativa
base_confidence: 0.9
half_life_days: 120
last_reinforced: '2026-10-29'
provenance:
  scale: S
  query: null
links:
- to: octoverse-2026-220m-prs-mes-anuncio-en-github-universe
  type: derived_from
- to: ranking-openrouter-mide-consumo-no-calidad
  type: supports
---

## What it is
La atribución causal de que la «ingeniería agéntica» triplicó los PRs fusionados en GitHub es afirmada por el autor, no demostrada en el documento [0aabafab1db5fa31]. Los recuentos de PRs fusionados son inflables por PRs de bots o agentes, bumps de dependencias y ruido de CI; los propios agentes generan volumen de PRs, así que la métrica mide en parte aquello que se cita para probar [0aabafab1db5fa31].

## Evidence
- El autor enmarca las cifras como impacto de la ingeniería agéntica, sin demostrarlo — source: 0aabafab1db5fa31
- No hay artefacto primario, metodología ni replicación independiente; GitHub produce la métrica y se beneficia del marco de agentes — source: 0aabafab1db5fa31

## Why it matters
Si la cifra fuera cierta, el cuello de botella sería la capacidad de revisión y CI, no la autoría de código [0aabafab1db5fa31]. Pero sin definición de «fusionado» (¿bots? ¿bumps?) ni fuente primaria, el claim no sostiene ni esa implicación [0aabafab1db5fa31].

Deriva de la nota del anuncio de Octoverse: lo único que establece es que un ejecutivo de un vendor dijo un número en un evento del vendor. Se alinea con el patrón de métricas de plataforma que miden consumo o volumen, no calidad.

## Links
- derived_from → [[octoverse-2026-220m-prs-mes-anuncio-en-github-universe]]
- supports → [[ranking-openrouter-mide-consumo-no-calidad]]
