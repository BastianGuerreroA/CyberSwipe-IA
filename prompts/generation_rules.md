# Reglas de Generación de Preguntas - CyberSwipe-AI

Al generar el contenido de ciberseguridad, debes seguir estrictamente las siguientes reglas estructurales y pedagógicas en español:

---

## 1. Reglas Pedagógicas de la Cápsula y sus Cartas

*   **Aislamiento Temático Estricto:**
    *   La cápsula debe abordar **única y exclusivamente** el tema asignado en `aprendizaje.md`.
    *   Está prohibido incluir conceptos de cápsulas futuras (ej. NO hables de Phishing ni correos falsos en la Cápsula 1 de Contraseñas).
*   **Prohibición de Dilemas Binarios u Obvios:**
    *   Está **estrictamente prohibido** generar cartas cuya respuesta correcta sea evidente para una persona sin conocimientos de ciberseguridad.
    *   Las dos opciones (`texto_izquierda` y `texto_derecha`) deben ser **frases completas, plausibles y defendibles** en el contexto laboral diario.
    *   Mal ejemplo (PROHIBIDO): `"Dar contraseña"` vs `"No dar contraseña"`, `"Hacer clic rápido"` vs `"Verificar"`.
    *   Buen ejemplo (OBLIGATORIO): `"Aceptar el enlace porque viene del correo habitual del proveedor"` vs `"Suspender la acción y confirmar por llamada directa con el proveedor"`.
    *   La opción incorrecta debe representar una conducta atractiva por conveniencia, prisa o evitar una molestia; la correcta debe representar el cumplimiento del procedimiento de seguridad aprendido.
*   **Vinculación 1-a-1 entre Contenido de Estudio y Cartas:**
    *   El `contenido_estudio` debe enseñar exactamente **5 conceptos clave distintos**.
    *   Cada una de las 5 cartas evaluará **un concepto específico e individual** expuesto en el `contenido_estudio`.
    *   Está prohibido repetir el mismo concepto o escenario dentro de una misma cápsula.
*   **Diversidad Obligatoria de Canales y Entornos:**
    *   Los escenarios **no deben limitarse** al cliché de la oficina, el correo o el jefe.
    *   Es obligatorio rotar entre canales: WhatsApp, Teams, Microsoft 365, Google Drive, OneDrive, llamadas (vishing), SMS (smishing), QR, impresoras corporativas, pendrives promocionales, portales web.
    *   Es obligatorio rotar entre entornos: teletrabajo/hogar, oficina presencial, viajes de negocios, cafeterías, aeropuertos, recepción, sucursales.
    *   Es obligatorio rotar entre roles: colegas, clientes, proveedores, contadores externos, personal de RRHH, finanzas, adquisiciones, recepción.
*   **Enfoque de Impacto en el Negocio y Explicaciones Cuestionadoras:**
    *   La `explicacion` debe detallar **qué ocurrió, por qué ocurrió, qué patrón o vulnerabilidad se explotó (citando el patrón CAPEC o salvaguarda CIS)** y el impacto real en la PYME (multas Ley 21.719 en Chile, pérdida de clientes, paralización operativa).

---

## 2. Especificación de la Estructura JSON

### Estructura de Cápsula
*   **id**: Entero secuencial único (ej: 1, 2, 3...).
*   **titulo**: El tema específico de aprendizaje (máximo 45 caracteres, ej: "Gestión Segura de Credenciales").
*   **subtitulo**: Resumen corto del contenido temático de la cápsula.
*   **mini_descripcion**: Una descripción corta del objetivo conductual esperado.
*   **contenido_estudio**: Texto educativo estructurado con formato **BBCode de Godot** (máximo 150 a 200 palabras). Usa `[b]Texto[/b]` para negritas (NUNCA uses Markdown `**`). Para viñetas usa el símbolo `• ` (NUNCA asteriscos `*`). Usa saltos de línea con `\n\n` para separar subsecciones legibles. Debe proveer las 5 bases teóricas necesarias para resolver las 5 cartas asociadas.
*   **estado**: Configura estrictamente el valor literal `"Disponible"`.
*   **cartas**: Arreglo de **EXACTAMENTE 5 cartas pedagógicas** que desafían los 5 conceptos de la cápsula.

### Estructura de Carta (Swipe)
Cada carta representa un dilema y debe estructurarse estrictamente con:
*   **imagen**: Entero que representa el tipo de ilustración (usa `0` o `1`).
*   **contexto**: El escenario escrito en segunda persona (ej: "Estás teletrabajando y un compañero te escribe por Teams pidiendo compartir un documento confidencial mediante un enlace abierto de OneDrive para agilizar la entrega...").
*   **texto_izquierda**: Acción al deslizar a la izquierda (frase completa y razonable, máximo 50 caracteres).
*   **texto_derecha**: Acción al deslizar a la derecha (frase completa y razonable, máximo 50 caracteres).
*   **correcto**: Valor decimal estricto:
    *   `-1.0` si la acción correcta y segura es la de la **IZQUIERDA** (`texto_izquierda`).
    *   `1.0` si la acción correcta y segura es la de la **DERECHA** (`texto_derecha`).
    *   REGLA DE COHERENCIA OBLIGATORIA: 'correcto' DEBE coincidir con el lado que posee la acción de seguridad correcta y los efectos de métricas positivos.
*   **explicacion**: Retroalimentación pedagógica detallada y convincente. Explica qué ocurrió, qué patrón/salvaguarda se aplicó y el impacto potencial en la organización.
*   **efecto_izquierda** y **efecto_derecha**: Objetos que representan el impacto cuantitativo en las 4 estadísticas de la empresa (rango de `-50` a `30`):
    *   `presupuesto`: Impacto financiero.
    *   `confidencialidad`: Impacto en la seguridad de los datos.
    *   `integridad`: Impacto en la veracidad y estado de los sistemas.
    *   `disponibilidad`: Impacto en la operatividad de los sistemas.
