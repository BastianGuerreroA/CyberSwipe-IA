# Reglas de Salida del JSON - CyberSwipe-AI

Tu respuesta debe consistir **únicamente** en un objeto JSON válido estructurado bajo el esquema de traducción al español y formateado según la plantilla especificada para **UNA ÚNICA CÁPSULA**.

## Pautas de Salida Críticas:
1. **Sin texto externo**: No incluyas explicaciones preliminares, saludos ni bloques explicativos fuera de la estructura JSON.
2. **Encapsulado JSON**: Encapsula la estructura directamente como un objeto JSON único en un bloque de código markdown:
   ```json
   {
     "id": 1,
     "titulo": "...",
     "subtitulo": "...",
     "mini_descripcion": "...",
     "contenido_estudio": "...",
     "estado": "Disponible",
     "cartas": [ ... ]
   }
   ```
3. **Mapeo de Atributos**:
   * Genera el objeto cápsula directamente en la raíz (no envuelvas en un arreglo `"capsulas"` ni agregues arreglos externos).
   * Respeta los nombres de variables en español: `id`, `titulo`, `subtitulo`, `mini_descripcion`, `contenido_estudio`, `estado`, `cartas`, `imagen`, `contexto`, `texto_izquierda`, `texto_derecha`, `correcto`, `explicacion`, `efecto_izquierda`, `efecto_derecha`, `presupuesto`, `confidencialidad`, `integridad`, `disponibilidad`.
4. **Cero saltos de línea reales dentro de cadenas de texto**:
   * **REGLA CRÍTICA DE SINTAXIS JSON**: NUNCA insertes un salto de línea real (Enter/Return) dentro de los textos entre comillas ` "..." `. Todo valor de texto en JSON debe ser una sola línea continua de código. Para representar saltos de párrafo en `contenido_estudio`, escribe la secuencia literal `\n\n`.
5. **Tipos de Datos**:
   * `id` de la cápsula debe ser un **entero** exactamente coincidente con la cápsula solicitada (ej. 1, 2, 3...).
   * `correcto` en las cartas debe ser obligatoriamente un **decimal** (`-1.0` o `1.0`).
   * Los efectos de estadísticas (`presupuesto`, `confidencialidad`, `integridad`, `disponibilidad`) deben ser **enteros** (ej. -25, 0, 15).
   * `estado` debe ser `"Disponible"` o `"Bloqueado"`.
6. **Codificación de Caracteres**: Escribe todo el texto de retorno con codificación UTF-8 adecuada. Los caracteres del español (tildes, eñes) deben ser codificados correctamente para evitar problemas de parseo en Godot.
