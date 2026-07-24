Por favor, genera un archivo JSON que contenga exactamente 1 cápsulas de preguntas basadas en el tema: 'Higiene de Contraseñas y Bloqueo de Pantallas'.

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
* **cartas**: Un arreglo que contiene las tarjetas de juego (Swipe) asociadas a esta cápsula (generalmente 10 cartas).

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

## 1. Público Objetivo y Tono
* **Trabajadores No Técnicos de PYMEs en Chile**: Tu audiencia son secretarios, administrativos, vendedores o directores de pequeñas y medianas empresas en Chile. No tienen formación técnica.
* **Segunda persona del singular (Tú)**: Habla directamente al jugador. Ej. "Recibes un correo urgente de tu jefatura solicitando..." en lugar de "El empleado recibe...".
* **Lenguaje Cercano y Claro**: Evita tecnicismos complejos de bases de datos o redes (ej: no hables de *inyecciones SQL*, *endpoints de API*, o *salts criptográficos*). Si debes mencionar un término (ej: *phishing*, *malware*), explícalo de inmediato con una analogía simple de la vida cotidiana.
* **Vocabulario chileno/latinoamericano natural**: Usa palabras naturales del entorno de oficina en Chile como "computador", "celular", "correo", "jefatura", "compañero de trabajo", "contraseña" en lugar de terminologías rígidas o neutras artificiales (como "ordenador", "móvil", "clave").

## 2. Explicaciones y Analogías Pedagógicas
* **Uso de Analogías**: Explica conceptos de ciberseguridad con equivalentes físicos del día a día:
  * *Contraseña robusta*: Como la cerradura de seguridad de la reja exterior de la oficina.
  * *Autenticación Multifactor (MFA)*: Como una puerta doble con guardia físico donde muestras tu cédula además de la llave.
  * *Phishing*: Como un cartero falso que te pide firmar un documento en la calle para quedarse con tus llaves.
* **Explicación Directa**: El feedback pedagógico debe explicar claramente las consecuencias en el mundo real de la PYME (pérdida de dinero, fuga de clientes, multas, detención de actividades).

## 3. Formato y Lectura
* Mantén las descripciones concisas para que puedan leerse rápidamente en pantallas pequeñas sin saturar visualmente al usuario.
* Utiliza formato BBCode (`[b]Texto en negrita[/b]`) en el cuerpo del estudio para resaltar las ideas clave.
* Respeta el uso estricto de ortografía y gramática en español.


## GUÍAS Y MARCOS DE REFERENCIA
### Fuente (Guía de Referencia): capec_social_engineering.md

# CAPEC: Ingeniería Social - Guía de Referencia para PYMEs

Esta guía resume las principales tácticas de ingeniería social adaptadas para la concientización en pequeñas y medianas empresas.

## Tácticas de Ataque Comunes

### 1. Phishing (Pesca de Datos por Correo)
*   **Definición**: Correos electrónicos falsos que imitan a entidades legítimas (bancos, servicios públicos, o jefaturas) para engañar al usuario.
*   **Puntos de Detección**:
    *   Urgencia desmedida ("Su cuenta será bloqueada en 2 horas").
    *   Enlaces sospechosos que no corresponden al dominio oficial.
    *   Archivos adjuntos inesperados (ej: facturas en formato `.zip` o `.exe`).

### 2. Pretexting (Creación de un Pretexto o Escenario Falso)
*   **Definición**: El atacante inventa una historia creíble para ganarse la confianza del trabajador y solicitar información confidencial.
*   **Ejemplos**:
    *   Llamada telefónica simulando ser un técnico de soporte de internet que necesita la contraseña del Wi-Fi de la oficina para "hacer mantenimiento".
    *   Un supuesto proveedor que pide cambiar la cuenta corriente de depósito para el pago de facturas.

### 3. Impersonation (Suplantación de Identidad de Jefaturas)
*   **Definición**: Hacerse pasar por un superior jerárquico (CEO, gerente o dueño de la PYME).
*   **Ejemplos**:
    *   Un correo de "la gerenta" solicitando comprar tarjetas de regalo de forma rápida o transferir fondos a un proveedor urgente de forma discreta.


---
### Fuente (Guía de Referencia): cis_controls_ig1.md

# CIS Controls - IG1: Ciber Higiene Básica para PYMEs

Este documento detalla las salvaguardas esenciales de ciberhigiene básica que todo colaborador de una PYME debe aplicar en su rutina diaria para proteger a la organización.

## Salvaguardas Críticas (Ciber Higiene)

### 1. Gestión de Contraseñas y Accesos
*   **Contraseñas Robustas**: No usar datos obvios (como "123456", "pyme2026" o el nombre de la empresa). Usar combinaciones de letras, números y símbolos.
*   **MFA (Autenticación Multifactor)**: Activar siempre el segundo factor de seguridad en correos y accesos bancarios. Es la capa adicional que pide un código temporal al celular.
*   **Bloqueo de Pantallas**: Bloquear el computador siempre al levantarse del puesto de trabajo (tecla `Windows + L`). Evita que terceros usen accesos administrativos.

### 2. Copias de Seguridad (Respaldos)
*   **Respaldo Frecuente**: Guardar la información clave de la empresa en la nube corporativa oficial o en un disco duro externo designado de forma periódica.
*   **Protección del Respaldo**: El respaldo debe estar desconectado o protegido para que en caso de un ataque (ej: virus secuestrador de datos) no se infecte también.

### 3. Actualizaciones de Software
*   **Actualizar Computador y Celular**: Mantener activas las actualizaciones automáticas del sistema operativo (Windows/macOS) y de las aplicaciones para corregir fallos que los atacantes aprovechan.



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
