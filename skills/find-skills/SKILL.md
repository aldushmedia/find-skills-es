---
name: find-skills
description: Ayuda a descubrir e instalar skills para agentes cuando el usuario pregunta cosas como "cómo hago X", "busca una skill para X", "¿hay una skill que...?", "how do I do X", "find a skill for X", "is there a skill that can...", o muestra interés en ampliar lo que el agente puede hacer. Usa esta skill cuando el usuario busque una función que podría existir como skill instalable.
---

# Buscar skills

Esta skill te ayuda a descubrir e instalar skills del ecosistema abierto de skills para agentes.

## Cuándo usar esta skill

Usa esta skill cuando el usuario:

- Pregunta "cómo hago X" y X podría ser una tarea común que ya tiene una skill
- Dice "busca una skill para X" o "¿hay una skill para X?"
- Pregunta "¿puedes hacer X?" y X es una capacidad especializada
- Muestra interés en ampliar lo que el agente puede hacer
- Quiere buscar herramientas, plantillas o flujos de trabajo
- Menciona que le gustaría tener ayuda con un área concreta (diseño, testing, despliegue, etc.)

## ¿Qué es el CLI de skills?

El CLI de skills (`npx skills`) es el gestor de paquetes del ecosistema abierto de skills para agentes. Las skills son paquetes modulares que amplían lo que puede hacer un agente con conocimiento especializado, flujos de trabajo y herramientas.

**Comandos principales:**

- `npx skills find [query] [--owner <owner>]`: busca skills de forma interactiva o por palabra clave, y opcionalmente solo las de un dueño de GitHub
- `npx skills add <package>`: instala una skill desde GitHub u otras fuentes
- `npx skills update`: actualiza todas las skills instaladas

**Explora las skills en:** https://skills.sh/

## Cómo ayudar al usuario a encontrar skills

### Paso 1: Entiende qué necesita

Cuando el usuario pida ayuda con algo, identifica:

1. El área (por ejemplo React, testing, diseño, despliegue)
2. La tarea concreta (por ejemplo escribir tests, crear animaciones, revisar PRs)
3. Si es una tarea lo bastante común como para que probablemente exista una skill

### Paso 2: Revisa primero el ranking

Antes de buscar con el CLI, revisa el [ranking de skills.sh](https://skills.sh/) para ver si ya existe una skill conocida para esa área. El ranking ordena las skills por cantidad total de instalaciones y muestra las opciones más populares y probadas.

Por ejemplo, entre las skills más usadas para desarrollo web están:
- `vercel-labs/agent-skills`: React, Next.js, diseño web (más de 100K instalaciones cada una)
- `anthropics/skills`: diseño frontend, procesamiento de documentos (más de 100K instalaciones)

### Paso 3: Busca skills

Si el ranking no cubre lo que necesita el usuario, corre el comando de búsqueda:

```bash
npx skills find [query] [--owner <owner>]
```

Por ejemplo:

- El usuario pregunta "¿cómo hago que mi app de React sea más rápida?" → `npx skills find react performance`
- El usuario pregunta "¿me ayudas con las revisiones de PR?" → `npx skills find pr review`
- El usuario dice "necesito crear un changelog" → `npx skills find changelog`

Busca con palabras clave en inglés, porque la mayoría de las skills están descritas en inglés. Si el usuario pide algo en español, traduce la idea a términos de búsqueda en inglés (por ejemplo "carruseles de Instagram" → `npx skills find instagram carousel`).

### Paso 4: Verifica la calidad antes de recomendar

**No recomiendes una skill solo por aparecer en los resultados de búsqueda.** Verifica siempre:

1. **Cantidad de instalaciones**: prefiere skills con 1K o más instalaciones. Ten cuidado con cualquiera que tenga menos de 100.
2. **Reputación de la fuente**: las fuentes oficiales (`vercel-labs`, `anthropics`, `microsoft`) son más confiables que autores desconocidos.
3. **Estrellas en GitHub**: revisa el repositorio de origen. Trata con escepticismo una skill de un repo con menos de 100 estrellas.

### Paso 5: Presenta las opciones al usuario

Cuando encuentres skills relevantes, preséntaselas al usuario con:

1. El nombre de la skill y qué hace
2. La cantidad de instalaciones y la fuente
3. El comando de instalación que puede correr
4. Un link para saber más en skills.sh

Ejemplo de respuesta:

```
¡Encontré una skill que te puede servir! La skill "react-best-practices" trae
pautas de Vercel Engineering para optimizar el rendimiento de React y Next.js.
(185K instalaciones)

Para instalarla:
npx skills add vercel-labs/agent-skills@react-best-practices

Más información: https://skills.sh/vercel-labs/agent-skills/react-best-practices
```

### Paso 6: Ofrece instalarla

Si el usuario quiere seguir, puedes instalarle la skill:

```bash
npx skills add <owner/repo@skill> -g -y
```

La opción `-g` la instala de forma global (a nivel de usuario) y `-y` se salta las preguntas de confirmación.

## Categorías comunes de skills

Al buscar, ten en cuenta estas categorías comunes:

| Categoría             | Búsquedas de ejemplo                     |
| --------------------- | ---------------------------------------- |
| Desarrollo web        | react, nextjs, typescript, css, tailwind |
| Testing               | testing, jest, playwright, e2e           |
| DevOps                | deploy, docker, kubernetes, ci-cd        |
| Documentación         | docs, readme, changelog, api-docs        |
| Calidad de código     | review, lint, refactor, best-practices   |
| Diseño                | ui, ux, design-system, accessibility     |
| Productividad         | workflow, automation, git                |

## Consejos para buscar mejor

1. **Usa palabras clave específicas**: "react testing" es mejor que solo "testing"
2. **Prueba otros términos**: si "deploy" no funciona, prueba "deployment" o "ci-cd"
3. **Revisa las fuentes populares**: muchas skills vienen de `vercel-labs/agent-skills` o `ComposioHQ/awesome-claude-skills`

## Cuando no encuentras ninguna skill

Si no existe ninguna skill relevante:

1. Reconoce que no encontraste una skill existente
2. Ofrece ayudar con la tarea directamente con tus capacidades generales
3. Sugiere que el usuario puede crear su propia skill con `npx skills init`

Ejemplo:

```
Busqué skills relacionadas con "xyz" pero no encontré ninguna.
¡Igual te puedo ayudar con esta tarea directamente! ¿Quieres que siga?

Si es algo que haces seguido, puedes crear tu propia skill:
npx skills init my-xyz-skill
```
