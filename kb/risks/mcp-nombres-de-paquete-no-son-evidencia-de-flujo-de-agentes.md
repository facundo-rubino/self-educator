---
id: mcp-nombres-de-paquete-no-son-evidencia-de-flujo-de-agentes
title: Los nombres de paquete MCP (memory, sequential-thinking, filesystem, git, fetch)
  no son evidencia de cómo un dev los usa
type: risk
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-10-22'
updated: '2026-10-22'
sources:
- 30a26335a9988ba2
- 9750590bbfe6b285
- 5a4df6bef0a4905f
- ffbd76916d1dfdc5
- 748f8b0a02cd7524
- b9106690f5dfd849
tags:
- mcp
- agentes
- inferencia
- off-topic
base_confidence: 0.6
half_life_days: 120
last_reinforced: '2026-10-22'
provenance:
  scale: XL
  query: null
links:
- to: release-2026-8-31-bumps-mcp-sin-changelog
  type: derived_from
- to: agentes-propios-no-se-sosten-desde-nombres-de-paquete
  type: supports
- to: mcp-como-infraestructura-de-agentes-relevancia-lateral-al-brief
  type: supports
- to: server-memory-como-primitiva-de-estado-para-agentes
  type: relates_to
- to: server-sequential-thinking-como-primitiva-de-razonamiento-para-agentes
  type: relates_to
---

## What it is
A lo sumo, los nombres de paquete (memory, sequential-thinking, filesystem, git, fetch) insinúan la superficie de tooling MCP que un dev asistido por IA podría usar. Ningún documento describe uso, guía ni evaluación de esas herramientas. Leer relevancia desde los nombres es inferencia no sostenida.

## Evidence
- Los documentos solo contienen encabezado de release y lista de paquetes bumpeados, sin prosa de uso — source: 30a26335a9988ba2, 9750590bbfe6b285, 5a4df6bef0a4905f, ffbd76916d1dfdc5, 748f8b0a02cd7524, b9106690f5dfd849

## Why it matters
Evita promover la nota de tooling MCP a evidencia de práctica o a recomendación de configuración para agentes. La relevancia del clúster con el brief es lateral y no está respaldada por sus documentos.

Deriva del clúster de bumps y refuerza los riesgos registrados de que la vinculación paquete → práctica es coincidencia de vocabulario. Se relaciona con las notas que tratan server-memory y server-sequential-thinking como primitivas, sin afirmar uso.

## Links
- derived_from → [[release-2026-8-31-bumps-mcp-sin-changelog]]
- supports → [[agentes-propios-no-se-sosten-desde-nombres-de-paquete]]
- supports → [[mcp-como-infraestructura-de-agentes-relevancia-lateral-al-brief]]
- relates_to → [[server-memory-como-primitiva-de-estado-para-agentes]]
- relates_to → [[server-sequential-thinking-como-primitiva-de-razonamiento-para-agentes]]
