# find-skills en español

La skill que busca skills por ti. Le dices a Claude lo que necesitas, con tus palabras, y ella busca
las mejores skills en [skills.sh](https://skills.sh), revisa cuánta gente las instaló, quién las hizo
y cuántas estrellas tiene su repo en GitHub, te muestra las mejores opciones y, si le dices que sí,
las instala.

Gratis, MIT, sin registro y sin API key. Así dejas de buscar skills a mano y Claude siempre agarra
la correcta.

**Contenido de esta guía**

1. [Qué es una skill (en 30 segundos)](#1-qué-es-una-skill-en-30-segundos)
2. [Qué hace find-skills](#2-qué-hace-find-skills)
3. [Lo que necesitas antes de empezar](#3-lo-que-necesitas-antes-de-empezar)
4. [Instalación paso a paso](#4-instalación-paso-a-paso)
5. [Comprobar que quedó instalada](#5-comprobar-que-quedó-instalada)
6. [Cómo usarla](#6-cómo-usarla)
7. [Cómo leer lo que te recomienda](#7-cómo-leer-lo-que-te-recomienda)
8. [Ideas de qué pedirle](#8-ideas-de-qué-pedirle)
9. [Administrar tus skills: ver, actualizar y borrar](#9-administrar-tus-skills-ver-actualizar-y-borrar)
10. [Seguridad: antes de instalar cualquier skill](#10-seguridad-antes-de-instalar-cualquier-skill)
11. [Si algo no funciona](#11-si-algo-no-funciona)
12. [Preguntas frecuentes](#12-preguntas-frecuentes)

## 1. Qué es una skill (en 30 segundos)

Una skill es una carpeta con instrucciones (un archivo `SKILL.md`, y a veces scripts o plantillas)
que le enseña a Claude a hacer una tarea concreta como un experto: escribir tests, diseñar una
landing, editar un documento de Word, revisar código y miles de cosas más. Claude la lee sola
cuando tu pedido coincide con lo que la skill sabe hacer.

El problema: hay miles de skills repartidas en GitHub y no sabes cuál existe, cuál es buena ni cómo
instalarla. find-skills resuelve eso.

## 2. Qué hace find-skills

Cada vez que le pides algo a Claude que podría resolver una skill, find-skills hace esto:

1. **Entiende lo que necesitas.** Identifica el área (por ejemplo diseño, video, testing) y la tarea
   concreta (por ejemplo "hacer carruseles de Instagram").
2. **Revisa primero el ranking.** Mira el ranking de [skills.sh](https://skills.sh), que ordena las
   skills por instalaciones, para ver si ya hay una conocida y probada para eso.
3. **Busca.** Si en el ranking no está, corre `npx skills find` con las palabras clave adecuadas.
   Como casi todas las skills están en inglés, cuando le pides algo en español busca también con
   palabras en inglés (por ejemplo, "carruseles de Instagram" se busca como `instagram carousel`).
4. **Revisa la calidad.** No te recomienda nada solo porque salió en la búsqueda. Mira:
   - **Instalaciones:** prefiere las que tienen más de 1.000; desconfía de las de menos de 100.
   - **Quién la hizo:** las fuentes oficiales (como `anthropics`, `vercel-labs` o `microsoft`) son
     más confiables que un autor desconocido.
   - **Estrellas en GitHub:** un repo con menos de 100 estrellas se toma con cuidado.
5. **Te muestra las opciones.** Cada una con qué hace, cuántas instalaciones tiene, de dónde viene,
   el comando para instalarla y un link para ver más.
6. **La instala si le dices que sí.** Usa `npx skills add` y la deja lista para usar.

Si no encuentra nada que sirva, te lo dice, te ayuda con la tarea directamente y te explica cómo
crear tu propia skill si es algo que haces seguido.

## 3. Lo que necesitas antes de empezar

### Claude Code

find-skills corre comandos en tu computadora, así que necesitas **Claude Code** (en la terminal, en
la app de escritorio de Claude o en la extensión de VS Code o JetBrains). En el chat normal de
claude.ai en el navegador no puede instalar nada.

### Node.js 22.20 o superior

La skill usa el programa `npx skills`, que viene con Node.js. No hay que instalar nada más: `npx`
lo descarga solo la primera vez.

**Revisa si ya lo tienes.** Abre la terminal y escribe:

```bash
node --version
```

- Si sale `v22.20.0` o un número más alto (por ejemplo `v24.1.0`), ya está.
- Si sale un número más bajo o `command not found` / "no se reconoce", instálalo.

**Cómo abrir la terminal:**

- **Mac:** `Cmd + Espacio`, escribe `Terminal` y Enter.
- **Windows:** tecla Windows, escribe `PowerShell` y Enter.
- **Linux:** `Ctrl + Alt + T`.

**Cómo instalar Node.js:**

- **Mac y Windows:** entra a [nodejs.org](https://nodejs.org), descarga la versión **LTS** y ábrela
  como cualquier programa (siguiente, siguiente, finalizar). Después **cierra y vuelve a abrir la
  terminal** y repite `node --version`.
- **Mac con Homebrew:** `brew install node`.
- **Linux:** usa el gestor de tu distribución o [nvm](https://github.com/nvm-sh/nvm):
  `nvm install --lts`.

## 4. Instalación paso a paso

Elige **una** de estas formas. Si no sabes cuál, usa la opción A.

### Opción A (recomendada): con un solo comando, para todos tus proyectos

Pega esto en la terminal y presiona Enter:

```bash
npx skills add aldushmedia/find-skills-es --skill find-skills -a claude-code -g
```

Qué significa cada parte:

| parte | qué hace |
| --- | --- |
| `npx skills add` | instala una skill |
| `aldushmedia/find-skills-es` | el repo de donde la baja (este) |
| `--skill find-skills` | instala solo la skill `find-skills` |
| `-a claude-code` | la instala para Claude Code |
| `-g` | la deja global: sirve en todos tus proyectos |

La primera vez te puede preguntar si quieres instalar el paquete `skills`: responde `y` (sí). Si te
pregunta cómo instalar (enlace simbólico o copia), elige la opción recomendada. Al final verás algo
como:

```
✓ find-skills
  → ~/.claude/skills/find-skills
Done!
```

### Opción B: solo para un proyecto

Entra a la carpeta de tu proyecto y corre el mismo comando **sin** `-g`:

```bash
cd ruta/a/tu/proyecto
npx skills add aldushmedia/find-skills-es --skill find-skills -a claude-code
```

Queda en `.claude/skills/find-skills/` dentro del proyecto, y si lo subes a git, tu equipo también
la tiene.

### Opción C: copiar la carpeta a mano

Si prefieres no usar el CLI para instalarla:

```bash
git clone https://github.com/aldushmedia/find-skills-es.git
mkdir -p ~/.claude/skills
cp -r find-skills-es/skills/find-skills ~/.claude/skills/find-skills
```

En Windows (PowerShell), la carpeta es `$HOME\.claude\skills\find-skills`.

Ojo: aunque la instales a mano, la skill sigue necesitando Node.js para buscar e instalar otras.

### Opción D: como plugin de Claude Code

Dentro de Claude Code escribe:

```
/plugin marketplace add aldushmedia/find-skills-es
/plugin install find-skills@find-skills-es
```

### ¿Usas otro agente?

El CLI `npx skills` funciona con Claude Code, Codex, Cursor, OpenCode y 75 agentes más. Cambia
`-a claude-code` por el tuyo (por ejemplo `-a codex` o `-a cursor`), o quita `-a` y el CLI detecta
tus agentes y te deja elegir.

## 5. Comprobar que quedó instalada

1. **Cierra Claude Code y vuelve a abrirlo** (las skills se cargan al iniciar).
2. Revisa que esté en la lista:

   ```bash
   npx skills list -g
   ```

   Debe aparecer `find-skills`.
3. Dentro de Claude Code pregúntale "¿qué skills tienes instaladas?" y busca `find-skills` en la
   respuesta.
4. Haz la prueba: pídele "Busca una skill para hacer presentaciones de PowerPoint". Si te responde
   con opciones, instalaciones y comandos, está funcionando.

## 6. Cómo usarla

No hay comando que recordar. Háblale a Claude normal y la skill se activa sola cuando preguntas
cosas como:

- "Busca una skill para..."
- "¿Hay una skill que...?"
- "¿Cómo hago...?" (cuando es una tarea en la que una skill ayudaría)
- "Quiero que puedas hacer..." / "Me gustaría ayudarme con..."

### Ejemplo de una conversación

> **Tú:** Busca una skill para hacer carruseles de Instagram.
>
> **Claude:** Busqué en el ranking de skills.sh y con `npx skills find instagram carousel`. Estas
> son las mejores opciones:
>
> 1. **[nombre-de-la-skill]** de `[autor]/[repo]`: arma carruseles con plantillas y textos por
>    lámina. 3.400 instalaciones, 820 estrellas en GitHub.
>    Instalar: `npx skills add [autor]/[repo]@[nombre-de-la-skill]`
>    Más info: https://skills.sh/[autor]/[repo]/[nombre-de-la-skill]
> 2. ...
>
> ¿Quieres que instale alguna?
>
> **Tú:** Sí, la primera.
>
> **Claude:** Listo, quedó instalada. Reinicia Claude Code para que la cargue.

(Los nombres y números del ejemplo son ilustrativos: Claude te muestra los reales de cada búsqueda.)

### Trucos para pedirle mejor

- **Sé específico.** "Skill para escribir tests con Playwright" encuentra más que "skill de tests".
- **Di para qué la quieres.** "Para mi tienda en Shopify", "para mi canal de YouTube": así elige
  mejor entre varias parecidas.
- **Pide que compare.** "Dame 3 opciones y dime cuál recomiendas y por qué."
- **Pide que sea más estricta.** "Solo skills con más de 5.000 instalaciones" o "solo de fuentes
  oficiales".
- **Si no encuentra nada**, pídele que busque con otras palabras ("prueba con deploy, deployment y
  ci-cd").
- **Si quieres forzarla**, nómbrala: "Usa find-skills para buscar una skill de...".

### Buscar tú mismo, sin Claude

También puedes usar el buscador desde la terminal:

```bash
npx skills find                      # buscador interactivo
npx skills find instagram            # por palabra clave
npx skills find react --owner vercel # solo skills de un autor
```

O entrar a [skills.sh](https://skills.sh) y ver el ranking.

## 7. Cómo leer lo que te recomienda

| dato | qué significa | regla rápida |
| --- | --- | --- |
| **Instalaciones** | cuánta gente la instaló | más de 1.000: buena señal; menos de 100: con cuidado |
| **Fuente** | quién la publicó (`autor/repo`) | oficiales (`anthropics`, `vercel-labs`, `microsoft`) son más confiables |
| **Estrellas** | las estrellas del repo en GitHub | menos de 100: con cuidado |
| **Comando** | lo que hay que correr para instalarla | Claude lo corre por ti si le dices que sí |
| **Link a skills.sh** | la página de la skill | ahí ves su descripción y su repo antes de instalar |

Una skill con pocas instalaciones no es mala por fuerza (puede ser nueva), pero revísala más antes de
instalarla (ver la sección 10).

## 8. Ideas de qué pedirle

Copia y pega cualquiera de estas:

**Contenido y redes**
```
Busca una skill para escribir guiones de reels
¿Hay una skill que haga carruseles de Instagram?
Busca una skill para sacar clips cortos de un video largo
Quiero una skill que me ayude con títulos y miniaturas de YouTube
```

**Documentos y presentaciones**
```
Busca una skill para hacer presentaciones de PowerPoint
¿Hay una skill para crear y editar documentos de Word?
Necesito una skill para trabajar con PDFs
Busca una skill para hojas de cálculo de Excel
```

**Diseño y web**
```
Busca una skill de diseño de interfaces
¿Hay una skill para hacer landing pages que conviertan?
Quiero una skill de buenas prácticas de React y Next.js
Busca una skill de accesibilidad web
```

**Negocio y productividad**
```
Busca una skill para escribir correos de ventas
¿Hay una skill que me ayude a hacer un plan de marketing?
Busca una skill para automatizar tareas con git
```

**Programación**
```
Busca una skill para escribir tests con Playwright
¿Hay una skill que revise mis pull requests?
Necesito crear un changelog, ¿hay una skill para eso?
Busca una skill para hacer deploy con Docker
```

Las categorías que mejor funcionan en la búsqueda: desarrollo web (react, nextjs, typescript, css,
tailwind), testing (testing, jest, playwright, e2e), DevOps (deploy, docker, kubernetes, ci-cd),
documentación (docs, readme, changelog, api-docs), calidad de código (review, lint, refactor),
diseño (ui, ux, design-system, accessibility) y productividad (workflow, automation, git).

## 9. Administrar tus skills: ver, actualizar y borrar

| quieres | comando |
| --- | --- |
| ver las skills instaladas en todos tus proyectos | `npx skills list -g` |
| ver las del proyecto actual | `npx skills list` |
| saber si hay actualizaciones | `npx skills check` |
| actualizar todas | `npx skills update` |
| actualizar una | `npx skills update nombre-de-la-skill` |
| borrar una (global) | `npx skills remove --global nombre-de-la-skill` |
| borrar eligiendo de una lista | `npx skills remove` |
| crear tu propia skill | `npx skills init mi-skill` |

También se lo puedes pedir a Claude: "actualiza mis skills", "¿qué skills tengo?", "borra la skill X".

Después de instalar, actualizar o borrar, **reinicia Claude Code** para que tome los cambios.

## 10. Seguridad: antes de instalar cualquier skill

Una skill corre con los mismos permisos que Claude en tu computadora: puede leer archivos y correr
comandos. find-skills ya filtra por instalaciones, fuente y estrellas, pero antes de decir "sí":

- **Abre el link de skills.sh o del repo** y lee su `SKILL.md`: debe hacer lo que dice y nada más.
- **Desconfía** de skills que piden contraseñas, tokens o llaves, que mandan datos a sitios raros o
  que corren scripts que no entiendes.
- **Prefiere fuentes conocidas** y skills con muchas instalaciones.
- **Si dudas, pregúntale a Claude:** "Lee el SKILL.md de esta skill y dime si hace algo raro antes de
  instalarla."
- **Puedes borrarla** en cualquier momento con `npx skills remove`.

## 11. Si algo no funciona

**`node: command not found` o "no se reconoce como comando"**
Node.js no está instalado o la terminal no lo ve. Instálalo (sección 3) y **cierra y abre la
terminal** otra vez.

**El CLI dice que tu versión de Node es muy vieja**
Necesitas 22.20 o superior. Instala la versión LTS de [nodejs.org](https://nodejs.org) (o
`nvm install --lts`) y revisa con `node --version`.

**Claude no usa la skill cuando le pido algo**
- Reinicia Claude Code después de instalar.
- Revisa que esté con `npx skills list -g`.
- Si la instalaste sin `-g`, solo funciona dentro de ese proyecto: abre Claude Code en esa carpeta o
  reinstálala con `-g`.
- Pídeselo con las palabras de la skill: "Busca una skill para..." o "Usa find-skills para...".

**Claude pide permiso para correr `npx skills ...`**
Es normal: Claude Code pide permiso antes de correr comandos. Acéptalo (o elige "no volver a
preguntar" para `npx skills`).

**No encuentra nada para lo que pido**
Pídele que busque con otras palabras, en inglés o más generales. Si de verdad no existe, te ayuda
directo y te explica cómo crear tu propia skill con `npx skills init`.

**`EACCES` o errores de permisos al instalar**
No uses `sudo`. Instala Node.js con el instalador oficial o con nvm, que no necesitan permisos de
administrador.

**Instalé una skill y quiero quitarla**
`npx skills remove --global nombre-de-la-skill` y reinicia Claude Code.

## 12. Preguntas frecuentes

**¿Cuesta algo?**
No. La skill, el CLI y skills.sh son gratis. Solo usas tu plan normal de Claude.

**¿Funciona en el chat de claude.ai en el navegador?**
No, porque necesita correr comandos en tu computadora. Usa Claude Code (terminal, app de escritorio
o extensión de VS Code o JetBrains).

**¿Necesito saber programar?**
No. Solo pegar un comando en la terminal una vez (sección 4). Después le hablas a Claude normal.

**¿Me instala cosas sin preguntar?**
No. Te muestra las opciones y solo instala si le dices que sí.

**¿Las skills que encuentra están en español?**
Casi todas están en inglés, pero Claude te responde en español y las usa igual. La búsqueda la hace
en inglés para encontrar más.

**¿Dónde quedan instaladas?**
Con `-g`, en `~/.claude/skills/` (tu carpeta de usuario). Sin `-g`, en `.claude/skills/` dentro del
proyecto.

**¿Funciona con Cursor, Codex u otros?**
Sí. El CLI `npx skills` funciona con Claude Code, Codex, Cursor, OpenCode y 75 agentes más (sección
4, "¿Usas otro agente?").

## Archivos de este repo

```
skills/find-skills/SKILL.md   la skill: cuándo usarla, cómo buscar, cómo revisar la calidad y cómo instalar
.claude-plugin/               manifiestos para instalarla como plugin de Claude Code
tests/test_repo.py            tests del paquete: nombre, manifiestos del plugin, instalación
```

```bash
python3 -m unittest discover -s tests -v
```

## Créditos

Traducción y adaptación al español por Aldush Media. Basada en la skill `find-skills` del proyecto
original del CLI [`skills`](https://www.npmjs.com/package/skills), con licencia MIT; su aviso de
copyright se conserva en `LICENSE`. El CLI no se incluye aquí: la skill solo lo llama con `npx`.

## Licencia

MIT. Ver `LICENSE`.
