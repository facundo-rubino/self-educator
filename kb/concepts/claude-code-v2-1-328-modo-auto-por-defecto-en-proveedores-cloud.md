---
id: claude-code-v2-1-328-modo-auto-por-defecto-en-proveedores-cloud
title: 'Claude Code v2.1.328: modo auto por defecto para Opus 4.6 y Sonnet 4.6 en
  proveedores cloud'
type: concept
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-20'
updated: '2026-11-20'
sources:
- f7420b2e33629c6e
tags:
- claude-code
- changelog
- modo-auto
- bedrock
- google-cloud
- microsoft-foundry
base_confidence: 0.6
half_life_days: 180
last_reinforced: '2026-11-20'
provenance:
  scale: S
  query: null
links:
- to: claude-code-v2-1-327-mcp-add-json-stdin
  type: relates_to
- to: changelog-de-release-como-senal-de-craft-y-tooling-no-de-practica-medida
  type: supports
- to: claude-code-v2-1-328-changelog-engagement-cero-sin-corroboracion
  type: derived_from
---

## What it is
El changelog de Claude Code v2.1.328 introduce modo `auto` por defecto para Claude Opus 4.6 y Sonnet 4.6 en Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry y el gateway de apps Claude. Las sesiones interactivas que arrancan sin `permission mode` usan ese modo por defecto.

## Evidence
- Se añadió modo auto para Opus 4.6 y Sonnet 4.6 en Bedrock, Google Cloud Agent Platform, Microsoft Foundry y el gateway de apps Claude; las sesiones interactivas sin permission mode arrancan en ese modo — source: f7420b2e33629c6e

## Why it matters
Cambia el régimen de permisos por defecto de las sesiones interactivas: quien orqueste agentes vía esos proveedores ya no parte de una sesión sin modo de permisos explícito. Es una modificación de comportamiento operativo del tooling, no una tesis sobre práctica de ingeniería.

Se relaciona con la serie de changelogs de Claude Code (v2.1.327 documentó `mcp add-json` por stdin). Refuerza el patrón de que un changelog de release es señal de craft y calidad de tooling, no de práctica medida.

## Links
- relates_to → [[claude-code-v2-1-327-mcp-add-json-stdin]]
- supports → [[changelog-de-release-como-senal-de-craft-y-tooling-no-de-practica-medida]]
- derived_from → [[claude-code-v2-1-328-changelog-engagement-cero-sin-corroboracion]]
