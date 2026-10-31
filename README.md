# find-skills en español

La skill que busca skills por ti. Le pides a Claude lo que necesitas, con tus palabras, y ella busca
las mejores skills en [skills.sh](https://skills.sh), revisa cuántas instalaciones tienen, de qué
fuente vienen y cuántas estrellas tiene su repo en GitHub, te muestra las opciones y, si quieres, las
instala.

Gratis, MIT, sin registro y sin API key.

## Qué hace

1. **Entiende lo que necesitas.** Le dices "cómo hago X", "busca una skill para X" o "¿hay una skill
   que...?" y Claude identifica el área y la tarea.
2. **Busca.** Primero revisa el ranking de skills.sh y, si ahí no está, corre `npx skills find` con
   las palabras clave adecuadas.
3. **Revisa la calidad.** No te recomienda nada solo por aparecer en la búsqueda: mira la cantidad de
   instalaciones, la reputación de la fuente y las estrellas del repo en GitHub.
4. **Te muestra las opciones.** Cada una con qué hace, sus instalaciones, su fuente, el comando para
   instalarla y un link a skills.sh.
5. **La instala.** Si le dices que sí, la instala con `npx skills add`.

Si no encuentra nada, te lo dice y te ayuda con la tarea directamente.

## Requisitos

- [Node.js](https://nodejs.org) 22.20 o superior. La skill usa el CLI `npx skills`, que se descarga
  solo con `npx`; no hay que instalar nada más.
- Un agente compatible. El CLI `npx skills` funciona con Claude Code, Codex, Cursor, OpenCode y 75
  agentes más.

## Instalación en Claude Code

Con el CLI de skills, desde tu proyecto:

```bash
npx skills add aldushmedia/find-skills-es --skill find-skills -a claude-code
```

Así queda en el proyecto actual. Agrega `-g` para tenerla en todos tus proyectos:

```bash
npx skills add aldushmedia/find-skills-es --skill find-skills -a claude-code -g
```

O copia la carpeta tú mismo:

```bash
git clone https://github.com/aldushmedia/find-skills-es.git
mkdir -p ~/.claude/skills
cp -r find-skills-es/skills/find-skills ~/.claude/skills/find-skills
```

O como plugin:

```
/plugin marketplace add aldushmedia/find-skills-es
/plugin install find-skills@find-skills-es
```

Para otro agente, cambia `-a claude-code` por el tuyo (por ejemplo `-a codex` o `-a cursor`), u
omite `-a` y el CLI te deja elegir.

## Cómo se usa

No hay comando que recordar. Pídele a Claude lo que necesitas:

```
Busca una skill para hacer carruseles de Instagram
¿Cómo hago que mi app de React sea más rápida?
¿Hay una skill que revise mis pull requests?
Necesito crear un changelog, ¿hay algo para eso?
Quiero una skill para escribir tests con Playwright
```

Claude busca, te muestra las mejores opciones con sus instalaciones y su fuente, y te pregunta si
quieres instalar alguna. Si dices que sí, la instala de forma global con `npx skills add <owner/repo@skill> -g -y`.

Por dentro usa estos comandos del CLI:

| comando | qué hace |
| --- | --- |
| `npx skills find [query]` | busca skills |
| `npx skills add <package>` | instala una skill |
| `npx skills update` | actualiza las skills instaladas |
| `npx skills init [name]` | crea la plantilla de una skill nueva |

## Archivos

```
skills/find-skills/SKILL.md   la skill: cuándo usarla, cómo buscar, cómo revisar la calidad y cómo instalar
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
