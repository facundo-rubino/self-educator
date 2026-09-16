# self-educator

Un brief diario de lo que importa en lo que estoy aprendiendo, y una base de
conocimiento que crece sola y se abre con Obsidian.

```
sources/*  →  [1] ingesta    Document[]      determinista, sin LLM, $0
              [2] señal      Signal[]        agrupa, puntúa, promueve, $0
              [3] research   Report[]        analista + crítico, LLM, con presupuesto
              [4] compila    notas en kb/    LLM, guiado por kb/SCHEMA.md
              [5] brief      docs/index.md   render puro, sin LLM, $0
```

## La idea

Casi todo lo que se llama "resumen con IA" gasta la plata en el lugar
equivocado: le da cientos de documentos crudos a un modelo y le pide que
encuentre lo que importa. Es la forma más cara posible de hacer la parte más
barata del trabajo.

Acá está al revés. **Las etapas 1 y 2 no tienen una sola llamada a un LLM.**
Los documentos se agrupan y se puntúan con reglas deterministas: qué tan rápido
acumula interés, cuántas fuentes independientes lo ven, qué tan distinto es de
todo lo que las corridas anteriores ya cubrieron, y si es del tema o es ruido.
Solo el puñado que pasa la barra cuesta una llamada al modelo.

Lo que llega al LLM es poco, así que se puede tratar bien: un analista escribe
un informe donde cada afirmación cita el documento del que salió, y un crítico
lo ataca y le baja la confianza si no aguanta.

Después los informes se **compilan** en un grafo de notas markdown. Compilados,
no apilados: cada informe se parte en ideas atómicas y cada idea se integra en
la nota que ya la posee.

## Las dos salidas

**El brief** (`docs/index.md`) es efímero: se lee con el café y se tira.
Titulares primero, una línea de por qué importa, un link. Un cupo por tema
evita que el tema más ruidoso de la semana se coma a los otros dos. Y nada se
repite nunca: cada item emitido queda anotado en `store/briefed.json`.

**El KB** (`kb/`) es permanente y se acumula. Son notas markdown con
front-matter YAML y links `[[wikilink]]`, o sea **una vault de Obsidian tal
cual**. Ver [Obsidian](#obsidian) abajo.

## Arrancar

```bash
uv sync --group dev      # Python 3.13 + dependencias
uv run pytest -q         # 111 tests, todos offline
uv run edu init          # crea kb/ según los tipos de nota de config.yaml
uv run edu sources --check   # ¿responden los feeds? ¿hace cuánto no publican?
uv run edu status        # qué hay en el KB y qué conviene hacer ahora
```

Las etapas 1 y 2 no necesitan credencial. Para las etapas 3 y 4:

```bash
cp .env.example .env     # y poné tu DEEPSEEK_API_KEY
uv run edu run --scale XS   # ~US$0.003 — la forma más barata de ver todo el flujo
uv run edu brief
```

## Comandos

| Comando | Qué hace |
|---|---|
| `edu init` | Crea un directorio en `kb/` por cada tipo de nota de `config.yaml`. |
| `edu sources` | Qué fuentes van a correr y por qué las otras no. `--check` prueba cada feed por HTTP. |
| `edu run` | El pipeline completo. `--scale XS…XL` es la palanca de costo; `--from-gaps` deja que el KB elija el objetivo. |
| `edu brief` | Renderiza el brief del día. Sin LLM, sin costo. `--dry-run` no lo marca como emitido. |
| `edu compile` | Re-corre **solo** la etapa 4 sobre los informes guardados. |
| `edu gaps` | El libro de deudas: qué no sabe el KB, ordenado. |
| `edu review` | Calibración: juzga señales viejas y mueve la barra de promoción. |
| `edu reconcile` | Resuelve las contradicciones abiertas del grafo. |
| `edu lint` | Links rotos, huérfanos, títulos duplicados, notas decaídas. Sale con código != 0, o sea sirve en CI. |
| `edu ask "..."` | Pregunta al KB. Responde solo desde las notas, o dice que no puede. |
| `edu learn "..."` | Suma un concepto a mano — sin scraping, sin señal, directo a enrich+compile. `--label` le pone título, `--no-critic` se salta el crítico. |

Todo comando que gasta plata muestra el costo antes de gastarlo.

## Escala — la palanca de costo

| Escala | docs/fuente | fuentes | señales top | crítico | presupuesto | costo/corrida |
|--------|------------:|--------:|------------:|:-------:|------------:|-------------:|
| XS | 50 | 1 | 1 | – | 5.000 | ~US$0,003 |
| S | 250 | 3 | 9 | ✓ | 25.000 | ~US$0,015 |
| M | 600 | 3 | 14 | ✓ | 60.000 | ~US$0,036 |
| L | 1.000 | 4 | 12 | ✓ | 150.000 | ~US$0,090 |
| XL | 3.000 | 6 | 25 | ✓ | 400.000 | ~US$0,240 |

`S` es la que corre el cron: **unos US$0,33 por mes** con DeepSeek. Tiene que
promover al menos tantas señales como suman los cupos de los temas (hoy 7) o el
brief nunca se llena.

## El cron

`.github/workflows/brief.yml` corre 09:00 UTC (6:00 en Uruguay/Argentina), de
lunes a viernes. Commitea el brief, el KB y el store, y abre un issue con los
tres titulares de arriba y el link a la página — **el mail es el disparador, no
tu memoria.** Una mañana sin nada relevante no abre issue ni manda mail.

Tres cosas hay que hacer a mano una sola vez:

1. **Settings → Secrets and variables → Actions**: cargar `DEEPSEEK_API_KEY`.
2. **Settings → Pages**: Source = rama por defecto, carpeta `/docs`.
3. **Watch → All Activity** en el repo, para que los issues lleguen al mail.

Si DeepSeek falla o se queda sin presupuesto, el paso sigue igual y el brief se
renderiza con lo que ya había. **El brief nunca deja de llegar por un error de
API.**

## Obsidian

No hay nada que instalar ni configurar del lado del proyecto. Las notas ya se
escriben con front-matter YAML y links `[[wikilink]]`:

1. Cloná el repo.
2. En Obsidian: *Open folder as vault* → elegí la carpeta `kb/`.
3. Listo. El graph view funciona, los backlinks funcionan, la búsqueda funciona.

`kb/.obsidian/` está en `.gitignore`: tu configuración local es tuya.

## Hacerlo tuyo (o de otra persona)

Dos archivos, en este orden:

1. **`config.yaml`** — el tema, los `themes` del brief con sus cupos, los tipos
   de nota y las fuentes.
2. **`kb/SCHEMA.md`** — el system prompt del compilador. Es el archivo de mayor
   apalancamiento del proyecto: decide cómo se escribe cada nota.

Para dárselo a otra persona con otros intereses: copiar el repo, cambiar esos
dos archivos. **No hay que tocar código.** Agregar una fuente es copiar
`self_educator/sources/_template.py`. Agregar un tipo de nota son cuatro líneas
de `config.yaml`. El checklist completo está en **[ADAPTING.md](ADAPTING.md)**.

## Estructura

```
config.yaml            qué se ingiere, los temas del brief, la ontología del KB
kb/                    la base de conocimiento (la salida permanente)
  SCHEMA.md            el contrato del compilador — editar esto
  GAPS.md              el libro de deudas (generado)
docs/index.md          el brief de hoy (lo que sirve GitHub Pages)
briefs/                el histórico, una entrada por día
seed/                  corpus semilla que se ingiere como fuente `files`
store/                 documentos, señales, informes y la memoria de no-repetir
self_educator/
  config.py models.py storage.py llm.py kb.py pipeline.py brief.py cli.py
  sources/             ingesta     — files, rss, web_api, _template.py
  signal/              puntuación  — embedder, cluster, scorers, engine
  enrich/              research    — analyst, critic
  synthesis/           compilación — compiler
  learning/            el loop     — decay, gaps, calibration, reconcile
docs/architecture.md   cómo encajan las etapas, y por qué
docs/extending.md      extensiones del mismo grafo
```

## El loop que mejora solo

- **Decaimiento.** Cada nota tiene una vida media. La confianza se calcula al
  leer, así que una nota que nadie reforzó en seis meses se ve visiblemente más
  débil que una de la semana pasada — sin que nadie la mantenga.
- **Deudas.** El KB deriva su propia lista de lo que no sabe: contradicciones,
  evidencia flaca, huérfanos, afirmaciones decaídas. `edu run --from-gaps` deja
  que el KB elija el próximo objetivo.
- **Calibración.** Las señales promovidas hace semanas se vuelven a juzgar:
  acierto, error o prematuro. El historial de cada fuente mueve su barra de
  promoción. Una fuente que miente seguido tiene que saltar más alto, sola.
- **Reconciliación.** Las contradicciones nunca se pisan al escribir. Se
  registran y se resuelven después, con las dos evidencias a la vista — y
  "las dos valen, y el desacuerdo es el hallazgo" es un veredicto válido.
