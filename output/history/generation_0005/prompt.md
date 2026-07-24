Por favor, genera un archivo JSON que contenga exactamente 1 cápsulas de preguntas basadas en el tema: 'OWASP Top 10: Inyecciones SQL'.

## REGLAS DE GENERACIÓN
# Reglas de Generación de Preguntas - CyberSwipe-AI

Al generar el contenido de ciberseguridad, debes seguir estrictamente la estructura en español requerida por el videojuego desarrollado en Godot:

## 1. Estructura de Cápsula
* **id**: Entero secuencial único (ej. 1, 2, 3...). Representa la identificación numérica de la cápsula.
* **titulo**: El nombre del tema de aprendizaje (máximo 45 caracteres, ej: "Phishing y Correos Falsos").
* **subtitulo**: Resumen corto del contenido de la cápsula.
* **mini_descripcion**: Una descripción corta e introductoria del objetivo pedagógico.
* **contenido_estudio**: Texto teórico que el usuario leerá para aprender antes de jugar.
  * Debe incluir formato de texto en **BBCode** (por ejemplo: `[b]Conceptos Clave:[/b]`, `[b]MFA[/b]`).
  * Utiliza saltos de línea con `\n\n` para separar secciones de manera legible.
* **estado**: Debe configurarse estrictamente como `"Disponible"`.
* **cartas**: Un arreglo que contiene las tarjetas de juego (Swipe) asociadas a esta cápsula (generalmente entre 5 y 10 cartas).

## 2. Estructura de Carta (Swipe)
Cada carta representa un dilema de toma de decisiones rápido. Debe estructurarse con las siguientes propiedades exactas:
* **imagen**: Un número entero que representa el tipo o ID de ilustración (usa `0` o `1`).
* **contexto**: Explicación del escenario en segunda persona, situando al jugador en la acción (ej: "Llega un correo urgente de la tesorería solicitando...").
* **texto_izquierda**: Acción corta que realiza el jugador si arrastra la carta a la izquierda.
* **texto_derecha**: Acción corta que realiza el jugador si arrastra la carta a la derecha.
* **correcto**: El valor de la respuesta correcta. Debe ser estrictamente un decimal:
  * `-1.0` si la acción de la **izquierda** es la respuesta correcta/segura.
  * `1.0` si la acción de la **derecha** es la respuesta correcta/segura.
* **explicacion**: Retroalimentación pedagógica detallada. Debe fundamentar técnicamente por qué se prefiere esa opción y qué consecuencias tiene en ciberseguridad corporativa.
* **efecto_izquierda** y **efecto_derecha**: Objetos que representan el impacto cuantitativo de cada decisión en las 4 estadísticas de la PYME:
  * `presupuesto`: Impacto financiero (positivo o negativo).
  * `confidencialidad`: Impacto en la protección de datos corporativos.
  * `integridad`: Impacto en la confiabilidad de los datos y sistemas.
  * `disponibilidad`: Impacto en la operatividad de los servidores y servicios.
  * *Los valores de impacto deben estar en un rango habitual de -50 a 30.*


## REGLAS DE ESTILO
# Reglas de Estilo y Redacción - CyberSwipe-AI

Para asegurar la calidad pedagógica y consistencia del texto en el videojuego, aplica las siguientes reglas de estilo de redacción:

## 1. Tono y Voz
* **Segunda persona del singular (Tú / Usted)**: Habla directamente al jugador. Ej. "Detectas una anomalía en los logs del firewall..." en lugar de "El administrador detectó...".
* **Profesional y Serio**: El juego tiene fines educativos corporativos, por lo que el tono debe ser el de un entorno laboral técnico o administrativo real.
* **Neutralidad**: Utiliza un español neutro internacional, evitando localismos o modismos propios de un solo país.

## 2. Claridad y Precisión Técnica
* Define términos técnicos complejos o contextualízalos si se dirigen a niveles fáciles.
* No utilices abreviaturas ambiguas. Si mencionas estándares, hazlo explícitamente (ej. "ISO/IEC 27001" en vez de solo "la norma").
* Mantén las descripciones concisas para que puedan leerse fácilmente en dispositivos móviles u pantallas de juego pequeñas.

## 3. Ortografía y Gramática
* Respeta el uso estricto de tildes, mayúsculas y signos de puntuación de la Real Academia Española (RAE).
* En el feedback, argumenta utilizando lógica de causa-efecto basada en los estándares provistos en el contexto de conocimiento (RAG).


## REGLAS DE SALIDA Y ESTRUCTURA
# Reglas de Salida del JSON - CyberSwipe-AI

Tu respuesta debe consistir **únicamente** en un objeto JSON válido estructurado bajo el esquema de traducción al español y formateado según la plantilla especificada.

## Pautas de Salida Críticas:
1. **Sin texto externo**: No incluyas explicaciones preliminares, saludos ni bloques explicativos fuera de la estructura JSON.
2. **Encapsulado JSON**: Encapsula toda la estructura estrictamente dentro de un solo bloque de código de markdown:
   ```json
   {
     "capsulas": [ ... ]
   }
   ```
3. **Mapeo de Atributos**:
   * Utiliza únicamente el arreglo `"capsulas"` en la raíz. No agregues propiedades inglesas como `"capsules"`, `"version"` ni `"generated_at"` a menos que se te indique.
   * Respeta los nombres de variables en español: `imagen`, `contexto`, `texto_izquierda`, `texto_derecha`, `correcto`, `explicacion`, `efecto_izquierda`, `efecto_derecha`, `presupuesto`, `confidencialidad`, `integridad`, `disponibilidad`.
4. **Tipos de Datos**:
   * `id` de cápsula debe ser un **entero** (ej. 1, 2, 3...).
   * `correcto` en las cartas debe ser obligatoriamente un **decimal** (`-1.0` o `1.0`).
   * Los efectos de estadísticas (`presupuesto`, `confidencialidad`, `integridad`, `disponibilidad`) deben ser **enteros** (ej. -25, 0, 15).
5. **Codificación de Caracteres**: Escribe todo el texto de retorno con codificación UTF-8 adecuada. Los caracteres del español (tildes, eñes) deben ser codificados correctamente para evitar problemas de parseo en Godot.


### PLANTILLA DE REFERENCIA JSON
```json
{
  "capsulas": [
    {
      "id": 1,
      "titulo": "Bloqueo de Pantalla y Credenciales",
      "subtitulo": "Protege tus dispositivos y accesos con PIN, biometría y claves fuertes.",
      "mini_descripcion": "Aprende las claves fundamentales para evitar intrusos en tus dispositivos físicos y proteger tus accesos corporativos.",
      "contenido_estudio": "El bloqueo de pantalla y las contraseñas seguras son tu primera línea de defensa.\n\n[b]Conceptos Clave:[/b]\n* [b]PIN de 6 dígitos[/b]: Mucho más seguro que uno de 4 dígitos (1 millón vs 10 mil combinaciones posibles).\n* [b]Autenticación Multifactor (MFA)[/b]: Añade una segunda capa de seguridad (como un código enviado a tu celular) además de tu contraseña.\n* [b]Principio de Privacidad[/b]: Nunca dejes sesiones administrativas o financieras abiertas si te ausentas de tu puesto de trabajo.",
      "estado": "Disponible",
      "cartas": [
        {
          "imagen": 0,
          "contexto": "Un compañero de trabajo te pide tu teléfono desbloqueado para hacer una llamada rápida pero sale de la oficina con él.",
          "texto_izquierda": "Confiar en él",
          "texto_derecha": "Pedirle que lo devuelva",
          "correcto": 1.0,
          "explicacion": "Nunca dejes tu dispositivo desbloqueado fuera de tu vista, un tercero podría acceder a datos corporativos privados en segundos.",
          "efecto_izquierda": { "presupuesto": 0, "confidencialidad": -30, "integridad": -10, "disponibilidad": 0 },
          "efecto_derecha": { "presupuesto": 0, "confidencialidad": 10, "integridad": 0, "disponibilidad": 0 }
        },
        {
          "imagen": 1,
          "contexto": "Un nuevo practicante sugiere anotar la clave compartida del servidor en un post-it pegado debajo del teclado para no olvidarla.",
          "texto_izquierda": "Permitir el post-it",
          "texto_derecha": "Prohibir post-its",
          "correcto": 1.0,
          "explicacion": "Anotar contraseñas en lugares físicos expone las credenciales a cualquier persona o visitante que pase por la oficina.",
          "efecto_izquierda": { "presupuesto": 0, "confidencialidad": -25, "integridad": 0, "disponibilidad": 0 },
          "efecto_derecha": { "presupuesto": -5, "confidencialidad": 15, "integridad": 0, "disponibilidad": 0 }
        }
      ]
    }
  ]
}

```
