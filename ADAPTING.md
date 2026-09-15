# ADAPTING.md — apuntarlo a otro tema

Un checklist, en el orden que funciona. Los pasos 1-3 lo dejan corriendo; los
4-6 son los que hacen que la salida sea buena.

**Para dárselo a otra persona** (tu vieja, un amigo, otro proyecto tuyo):
copiar el repo, borrar `kb/`, `store/`, `briefs/` y `docs/index.md`, y hacer
estos pasos con sus temas. No hay que tocar una línea de código.

---

## 1. Decir de qué se trata

En `config.yaml`:

```yaml
topic: >-
  Una frase que describa el sujeto. Se usa como query por defecto y queda
  como `topic` en cada nota.
```

Un KB, un sujeto. Si querés dos sujetos sin relación, corré dos copias con su
propio `kb/` y su propio `store/`: compartir el KB entre temas ajenos empeora
el agrupamiento y la puntuación de novedad, porque todo se compara contra todo.

---

## 2. Definir los temas del brief

Esto es lo que decide qué entra al brief y qué se descarta como ruido.

```yaml
themes:
  - name: cocina-fermentos
    label: "Fermentos y masa madre"
    quota: 4
    keywords: [sourdough, masa madre, fermentaci, levadura, hidrataci, koji]
```

- **`quota`** es cuántos items de ese tema entran por día. La suma de los cupos
  es el largo del brief. Siete items ≈ diez minutos de lectura.
- **`keywords`** se buscan como substring, sin distinguir mayúsculas. Poné
  raíces (`fermentaci`) en vez de palabras completas, así cubrís
  *fermentación*, *fermentaciones* y *fermentar* de una.
- Con tres keywords que peguen, el tema puntúa al máximo. No hace falta una
  lista enorme: hace falta que sean las correctas.

Un documento que no pega con ningún tema **no entra al brief**, por más ruido
que esté haciendo. Ese es el filtro.

---

## 3. Decidir qué es una nota en tu dominio

Es la decisión de sombra más larga y vale veinte minutos antes de escribir
nada. Los tipos que vienen (concept / pattern / actor / question / risk) sirven
para un sujeto de investigación abierto. El tuyo puede que no.

```yaml
kb:
  note_types:
    - name: tecnica
      dir: tecnicas
      half_life_days: 1095
      description: "Un procedimiento reproducible, con sus condiciones."
    - name: falla
      dir: fallas
      half_life_days: 365
      description: "Un resultado que salió mal, con su causa probable."
```

Tres preguntas para probar un conjunto propuesto:

- **¿Cada tipo es una *clase* distinta de cosa, o solo un tema distinto?**
  "Fermentos europeos" y "fermentos asiáticos" son un tipo con una etiqueta.
  Se parte por clase, no por asunto.
- **¿Alguna vez querrías leer todas las notas de ese tipo juntas?** Si no,
  probablemente sea una etiqueta y no un tipo.
- **¿Algún tipo tiene el tejido conectivo?** En casi todo KB útil hay un tipo
  transversal: el patrón, el mecanismo, la estructura que se repite. Dale la
  vida media más larga: esas observaciones envejecen más lento y son lo que
  hace que el grafo valga más que la suma de sus notas.

**Sobre `half_life_days`:** preguntate cuánto tiempo sigue siendo cierta una
afirmación de ese tipo sin que nadie la revise. Una ley: años. Un precio:
semanas. La confianza se calcula con esto en cada lectura, así que acertarle
aproximadamente significa que las notas viejas se delatan solas en vez de
mentirte en silencio.

Después `edu init` crea los directorios.

---

## 4. Apuntarlo a las fuentes

Empezá por lo que no necesita credenciales.

**Feeds** — casi todo tiene RSS, y más de lo que pensás:

```yaml
sources:
  order: [rss, web_api, files]
  rss:
    feeds:
      - https://ejemplo.com/blog/feed
```

- **Newsletters**: Substack y beehiiv exponen RSS siempre (`/feed`).
- **Podcasts**: RSS *es* el formato nativo del podcasting. Se ingiere el título
  y las notas del episodio. No se transcribe el audio: es caro y casi nunca
  hace falta.
- **YouTube**: `youtube.com/feeds/videos.xml?channel_id=...`
- **Reddit**: agregarle `/.rss` a cualquier subreddit.
- **GitHub**: `/releases.atom` o `/commits/main.atom` en cualquier repo.

**Lo que no tiene RSS y conviene saber de antemano:**

- **X/Twitter** no tiene API gratis desde 2023. Se puede usar RSSHub
  (`rsshub.app/twitter/user/:id`) pero es inestable. Casi siempre la misma
  persona publica un blog o newsletter con RSS: **seguí el canal durable, no el
  efímero.**
- **Instagram** es peor todavía, y para temas técnicos no tiene señal. Si tu
  tema *sí* vive en Instagram (cocina, diseño, entrenamiento), RSSHub es la
  única vía razonable y hay que asumir que se va a romper.

**Archivos locales** — lo que ya tenés:

```yaml
  files:
    paths: ["seed", "~/notas"]
    extensions: [".md", ".txt", ".json", ".csv"]
```

**Tu propia API o fuente**: copiá la plantilla.

```bash
cp self_educator/sources/_template.py self_educator/sources/mifuente.py
```

Renombrá la clase, poné `name`, implementá `fetch`, registrala (agregala a
`SOURCE_CLASSES` en `sources/__init__.py`, o llamá a `register(MiFuente)`) y
sumá su nombre a `sources.order`. Nada aguas abajo se entera: el agrupamiento,
la puntuación, el research y la compilación solo ven `Document`.

Dos cosas que conviene hacer bien en una fuente nueva:

- **`metrics`** — metele los números de interacción que dé la fuente (votos,
  comentarios, estrellas, vistas). Alimentan los scorers `velocity` y
  `surprise`. Si no tiene ninguno, dejalo vacío: esos scorers devuelven un
  valor neutro en vez de leer la ausencia como desinterés.
- **`required_env`** — nombrá las variables de entorno que necesita. Si falta
  una, la fuente se excluye con un aviso en vez de voltear la corrida.

Comprobá antes de confiar:

```bash
uv run edu sources          # cuáles van a correr
uv run edu sources --check  # cuáles responden, parsean y siguen vivas
```

---

## 5. Correr lo más barato que muestre todo el flujo

```bash
uv run edu run --scale XS   # ~US$0,003
uv run edu brief
```

Mirá `docs/index.md` a ojo. Si los titulares no son de lo tuyo, el problema
está en `themes` o en las fuentes, no en el modelo — y ninguno de los dos
cuesta plata de arreglar.

---

## 6. Editar `kb/SCHEMA.md`

Es el system prompt de la etapa 4 y el archivo de mayor apalancamiento del
proyecto: decide cómo se escribe cada nota. Describí ahí tus tipos de nota con
las mismas palabras que usaste en `config.yaml`, y contá qué es una buena nota
en tu dominio.

---

## Ajustes finos

- **`signal.weights`** — cuánto pesa cada scorer. Si el brief te trae cosas de
  tema pero aburridas, subí `velocity`. Si te trae ruido del tema, subí
  `relevance`. Si te repite variaciones de lo mismo, subí `novelty`.
- **`signal.promotion_threshold`** — la barra inicial. La calibración la mueve
  sola con el tiempo; este valor solo importa las primeras semanas.
- **`SCALE_PRESETS` en `config.py`** — la escala `S` es la que corre el cron.
  `top_signals` tiene que ser **al menos** la suma de los cupos de tus temas, o
  el brief nunca se llena.
- **El cron** en `.github/workflows/brief.yml` está en UTC. Para las 6 de la
  mañana en Uruguay/Argentina (UTC-3) son las `0 9`. Convertí antes de tocarlo.
