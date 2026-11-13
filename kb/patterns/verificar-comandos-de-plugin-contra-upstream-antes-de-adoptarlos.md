---
id: verificar-comandos-de-plugin-contra-upstream-antes-de-adoptarlos
title: Verificar comandos de plugin contra upstream antes de adoptarlos en configuración
  de equipo
type: pattern
topic: 'Cómo un dev que lidera proyectos y también enseña a programar hace mejor su
  trabajo: agentes de IA aplicados a programar, gestionar y enseñar, liderazgo técnico
  de equipos chicos (estimación, secuenciamiento, alcance, organización personal),
  oficio de software engineering en general, y productividad y técnicas de estudio.
  # Docencia de programación entry-level se mudó al profile `teaching` de # pogba
  (KB acumulativa aparte); ya no compite por cupo en este brief.'
created: '2026-11-13'
updated: '2026-11-13'
sources:
- 541b1e7161ae8f43
tags:
- tooling
- verificacion
- evals
- config
base_confidence: 0.45
half_life_days: 365
last_reinforced: '2026-11-13'
provenance:
  scale: S
  query: null
links:
- to: anthropic-claude-code-eval-tooling-build-eval-hill-climb
  type: derived_from
- to: verificar-features-de-tooling-antes-de-citar-en-docencia-o-config
  type: supports
---

## What it is
Cuando una feature de tooling aparece solo en un reporte secundario y no en documentación oficial, la regla operativa es verificarla contra upstream (changelog del plugin, repositorio o docs del proveedor) antes de incluirla en configuración de equipo o en material de docencia. El caso de `build_eval` y `hill-climb` es una instancia: el nombre exacto, la interfaz y la disponibilidad no están confirmados más allá del reporte.

## Evidence
- La única fuente es un reporte secundario de feed RSS sobre `build_eval` y `hill-climb` — source: 541b1e7161ae8f43

## Why it matters
Adoptar un comando de plugin en la configuración de un equipo es barato; adoptarlo cuando no existe con ese nombre en la versión instalada cuesta el tiempo de descubrirlo en producción o en clase. La verificación previa es más barata que la corrección posterior.

Deriva del concepto del tooling. Es evidencia adicional para `verificar-features-de-tooling-antes-de-citar-en-docencia-o-config`, que enuncia la misma regla operativa.

## Links
- derived_from → [[anthropic-claude-code-eval-tooling-build-eval-hill-climb]]
- supports → [[verificar-features-de-tooling-antes-de-citar-en-docencia-o-config]]
