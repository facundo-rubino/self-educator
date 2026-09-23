---
id: mcp-serie-2026-sin-diffs-ni-fuente-primaria
title: La serie de releases MCP 2025.11–2026.8 no trae diffs ni fuente primaria verifiable
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-09-23'
updated: '2026-09-23'
sources:
- 30a26335a9988ba2
- 5a4df6bef0a4905f
- 9750590bbfe6b285
- b9106690f5dfd849
- 16a4e3995d6c827e
- 2221814efbefaa3b
- 748f8b0a02cd7524
- ffbd76916d1dfdc5
tags:
- mcp
- verificabilidad
- argumento-ex-silentio
base_confidence: 0.7
half_life_days: 120
last_reinforced: '2026-09-23'
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
---

## What it is
El corpus cubre versiones fechadas de 2025.11.25 a 2026.8.31 sin incluir diffs, changelogs ni enlace a una fuente primaria del proyecto. Sin esos artefactos no se puede verificar qué cambió ni si el versionado refleja un cambio sustantivo.

## Evidence
- Ocho notas fechadas entre 2025.11.25 y 2026.8.31 enumeran paquetes y versión, sin diffs — source: 16a4e3995d6c827e, 2221814efbefaa3b, 748f8b0a02cd7524, 5a4df6bef0a4905f, ffbd76916d1dfdc5, 9750590bbfe6b285, b9106690f5dfd849, 30a26335a9988ba2
- La nota 2026.1.26 no incluye ninguno de los paquetes de más de un año antes, sin declarar motivo — source: b9106690f5dfd849

## Why it matters
Cualquier afirmación sobre evolución del ecosistema MCP requiere los diffs, que no están en los documentos. La ausencia de un paquete en una release tampoco prueba deprecación.

Refuerza `mcp-fechas-2026-sinteticas-no-corroborables` y `timestamps-2026-de-la-serie-mcp-posiblemente-sinteticos`, y deriva de `mcp-release-stub-sin-changelog`. Se relaciona con `mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion` por el mismo límite inferencial.

## Links
- supports → [[mcp-fechas-2026-sinteticas-no-corroborables]]
- supports → [[timestamps-2026-de-la-serie-mcp-posiblemente-sinteticos]]
- derived_from → [[mcp-release-stub-sin-changelog]]
- relates_to → [[mcp-ausencia-de-paquete-en-release-no-prueba-deprecacion]]
