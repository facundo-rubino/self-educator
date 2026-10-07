---
id: mcp-serie-2026-sin-diffs-ni-fuente-primaria
title: La serie de releases MCP 2025.11–2026.8 no trae diffs ni fuente primaria verificable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-10-07'
sources:
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 748f8b0a02cd7524
- 9750590bbfe6b285
- b9106690f5dfd849
- ffbd76916d1dfdc5
tags:
- argumento-ex-silentio
- fuente-primaria
- mcp
- trazabilidad
- verificabilidad
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-10-07'
provenance:
  scale: XL
  query: null
links:
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: supports
- to: timestamps-2026-de-la-serie-mcp-posiblemente-sinteticos
  type: supports
- to: mcp-release-stub-sin-changelog
  type: derived_from
- to: mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion
  type: relates_to
- to: mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia
  type: relates_to
- to: mcp-fechas-2026-sinteticas-no-corroborables
  type: relates_to
---

## What it is
Cada ítem llega como una etiqueta de release más nombres de paquete: sin diff, sin notas de cambio, sin enlace a un repositorio o commit. No hay forma, dentro de este corpus, de verificar qué cambió entre releases ni de contrastar la publicación con una fuente primaria.

## Evidence
- El documento semilla es un aviso de release: versión más lista de paquetes, sin más contenido — source: 30a26335a9988ba2
- Un release de julio de 2026 vuelve a la misma forma: fecha versionada más nombres de paquete — source: 5a4df6bef0a4905f

## Why it matters
Sin diff no se puede afirmar ninguna capacidad nueva ni ninguna conducta del ecosistema. La serie documenta que algo se publicó, no qué se publicó. Consumirla como si informara sobre features es el modo de fallo a evitar.

Se relaciona con la serie MCP y con el riesgo de fechas no corroborables: ambas apuntan a la trazabilidad limitada del feed. No lleva `contradicts`: no hay una versión alternativa en el corpus.

## Links
- supports → [[mcp-fechas-2026-sinteticas-no-corroborables]]
- supports → [[timestamps-2026-de-la-serie-mcp-posiblemente-sinteticos]]
- derived_from → [[mcp-release-stub-sin-changelog]]
- relates_to → [[mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion]]
- relates_to → [[mcp-serie-2025-11-a-2026-8-cadencia-de-alta-frecuencia]]
- relates_to → [[mcp-fechas-2026-sinteticas-no-corroborables]]
