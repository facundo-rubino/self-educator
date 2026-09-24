---
id: vulkan-int8-coopmat1-matmul-rdna3-rdna4
title: 'Implementación de matmul int8 coopmat1 en Vulkan para AMD RDNA3/RDNA4 (llama.cpp
  PR #70c4e15)'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-24'
updated: '2026-09-24'
sources:
- 481d2653708680a1
tags:
- vulkan
- llama.cpp
- amd-rdna
- inferencia-local
- quantization
base_confidence: 0.15
half_life_days: 180
last_reinforced: '2026-09-24'
provenance:
  scale: XL
  query: null
links:
- to: mejora-de-rendimiento-sin-delta-post-cambio
  type: supports
- to: benchmark-pp512-no-informa-generacion-interactiva
  type: relates_to
---

## What it is
Un PR de llama.cpp (#70c4e15) implementa matmul int8 con coopmat1 para el backend Vulkan, dirigido a GPUs AMD RDNA3 y RDNA4. El documento solo publica una tabla de benchmark «before» en una RX 7900 XTX con modelo etiquetado 'gemma4 26B.A4B Q4_0' (13.26 GiB, 25.23 B params, ngl=-1, n_ubatch=1024, fa=1), donde el único valor completo visible es pp512 = 3410.53 ± 22.72 t/s. No hay cifras «after» en el documento.

## Evidence
- El título indica matmul int8 con coopmat1 para Vulkan, dirigido a AMD RDNA3 y RDNA4 (commit 70c4e15 de ggml-org/llama.cpp) — source: 481d2653708680a1
- El autor afirma que el cambio «ha producido una mejora masiva de rendimiento» en su AMD RX 7900 XTX — source: 481d2653708680a1
- Baseline visible: backend Vulkan, ngl=-1, n_ubatch=1024, fa=1, modelo 'gemma4 26B.A4B Q4_0', pp512 = 3410.53 ± 22.72 t/s — source: 481d2653708680a1
- La tabla se trunca tras la fila pp512 ('| gemma4 26B.A4B …'); no hay mediciones «after» ni otras filas completas — source: 481d2653708680a1
- Engagement 0, origen RSS, sin corroboración en el cluster — source: 481d2653708680a1

## Why it matters
Si la mejora se confirmara, abarataría el costo por token de correr modelos de ~25B cuantizados en GPUs AMD consumer (7900 XTX), habilitando prototipado local de agentes y demos docentes sin GPU profesional. En el estado actual del documento no se puede sostener esa implicación: falta el delta cuantificado.

El patrón de mejora sin «after» medido se registra en `mejora-de-rendimiento-sin-delta-post-cambio`. Que el benchmark solo mida prefill (pp512) y no generación se registra en `benchmark-pp512-no-informa-generacion-interactiva`. La relevancia al brief (agentes, liderazgo, docencia, productividad) es indirecta: informa la capa de herramienta de inferencia local, no las prácticas centrales del brief.

## Links
- supports → [[mejora-de-rendimiento-sin-delta-post-cambio]]
- relates_to → [[benchmark-pp512-no-informa-generacion-interactiva]]
