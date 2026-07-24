Por favor, genera un archivo JSON que contenga exactamente 1 cápsulas de aprendizaje siguiendo estrictamente la estructura de temas y objetivos pedagógicos.

## PROGRAMA DE APRENDIZAJE SECUENCIAL Y OBJETIVOS
Numero_capsulas: 3

Programa de aprendizaje

Público:
Trabajadores de PYMEs chilenas sin conocimientos técnicos.

Marco de referencia:
CIS Controls IG1 y CAPEC Social Engineering.

Objetivo general:
Desarrollar hábitos de ciberhigiene y capacidad para reconocer ataques de ingeniería social.

Cápsula 1:
Tema:
Gestión de Contraseñas y MFA.

Objetivos:
- Crear contraseñas robustas.
- Evitar reutilización.
- Comprender MFA.

Cápsula 2:
Tema:
Phishing e Ingeniería Social.

Objetivos:
- Detectar señales de phishing.
- Verificar identidad.
- No actuar por presión.

Cápsula 3:
Tema:
Respaldos y Protección de Equipos.

Objetivos:
- Realizar respaldos.
- Mantener equipos actualizados.
- Bloquear sesiones.


## REGLAS DE GENERACIÓN
# Reglas de Generación de Preguntas - CyberSwipe-AI

Al generar el contenido de ciberseguridad, debes seguir estrictamente las siguientes reglas estructurales y pedagógicas en español:

---

## 1. Reglas Pedagógicas de la Cápsula y sus Cartas

*   **Coherencia entre Contenido de Estudio y Cartas:**
    *   El campo `contenido_estudio` debe ser denso en conocimiento práctico de ciberhigiene (basado en **CIS Controls** y **CAPEC**).
    *   Cada una de las cartas asociadas a la cápsula **debe requerir obligatoriamente haber comprendido la información expuesta en el `contenido_estudio`**. Si un jugador puede adivinar la respuesta correcta por pura intuición o sentido común general, la carta está mal diseñada y debe ser reformulada.
*   **Diseño de Dilemas Desafiantes y Ambiguos:**
    *   Cada carta debe situar al jugador ante una situación laboral verosímil y cotidiana.
    *   Las dos opciones presentadas (`texto_izquierda` y `texto_derecha`) deben ser gramatical y pragmáticamente plausibles. Ambas deben sonar razonables.
    *   Plantea dilemas realistas: a veces la opción segura implica reportar el problema (un retraso operativo temporal) o gastar más tiempo, mientras que la opción insegura ofrece comodidad inmediata, rapidez o evitar una llamada molesta.
    *   Los errores cometidos por el jugador deben representar fallas comunes (ej. exceso de confianza, presiones de tiempo, temor a contrariar a una jefatura).
*   **Enfoque de Impacto en el Negocio:**
    *   La `explicacion` didáctica debe fundamentar por qué la opción correcta es la mejor práctica y detallar las consecuencias en el mundo real de la PYME (reputación, multas de la Ley 21.719 en Chile, costo de recuperación, pérdida de continuidad operativa).
    *   Los efectos cuantitativos en las estadísticas (`presupuesto`, `confidencialidad`, `integridad`, `disponibilidad`) deben reflejar el impacto a nivel de la organización entera, no solo del computador individual.

---

## 2. Especificación de la Estructura JSON

### Estructura de Cápsula
*   **id**: Entero secuencial único (ej: 1, 2, 3...).
*   **titulo**: El tema específico de aprendizaje (máximo 45 caracteres, ej: "Phishing y Correos Falsos").
*   **subtitulo**: Resumen corto del contenido temático de la cápsula.
*   **mini_descripcion**: Una descripción muy corta del objetivo conductual esperado.
*   **contenido_estudio**: Texto educativo estructurado con formato **BBCode** (ej: `[b]Negrita[/b]`). Usa saltos de línea con `\n\n` para separar legibles subsecciones. Debe proveer las bases teóricas específicas necesarias para resolver las cartas asociadas.
*   **estado**: Configura estrictamente el valor literal `"Disponible"`.
*   **cartas**: Arreglo de exactamente 10 cartas que desafían los conceptos de la cápsula.

### Estructura de Carta (Swipe)
Cada carta representa un dilema y debe estructurarse estrictamente con:
*   **imagen**: Entero que representa el tipo de ilustración (usa `0` o `1`).
*   **contexto**: El escenario escrito en segunda persona (ej: "Recibes un correo de tu colega pidiendo que desactives temporalmente el antivirus para instalar un plugin rápido de planillas...").
*   **texto_izquierda**: Acción al deslizar a la izquierda (máximo 50 caracteres).
*   **texto_derecha**: Acción al deslizar a la derecha (máximo 50 caracteres).
*   **correcto**: Valor decimal estricto:
    *   `-1.0` si la acción correcta y segura es la de la **izquierda**.
    *   `1.0` si la acción correcta y segura es la de la **derecha**.
*   **explicacion**: Retroalimentación pedagógica detallada y convincente. Explica el porqué del riesgo en un lenguaje claro y su impacto potencial en la organización.
*   **efecto_izquierda** y **efecto_derecha**: Objetos que representan el impacto cuantitativo de la decisión en las 4 estadísticas de la empresa (rango de `-50` a `30`):
    *   `presupuesto`: Impacto financiero.
    *   `confidencialidad`: Impacto en la seguridad de los datos.
    *   `integridad`: Impacto en la veracidad y estado de los sistemas.
    *   `disponibilidad`: Impacto en la operatividad de los sistemas.


## REGLAS DE ESTILO
# Reglas de Estilo y Redacción - CyberSwipe-AI

Para asegurar la calidad pedagógica, consistencia del tono y efectividad instruccional de CyberSwipe, aplica rigurosamente las siguientes directrices en la redacción:

---

## 1. Público Objetivo y Tono
*   **Trabajadores No Técnicos de PYMEs en Chile:** Tu audiencia objetivo abarca personal administrativo, de ventas, secretarios, encargados de adquisiciones y dueños de pequeñas y medianas empresas en Chile. No tienen conocimientos técnicos profundos en redes o seguridad de la información.
*   **Segunda persona del singular (Tú):** Sitúa al jugador directamente en el papel protagónico. Redacta en presente del indicativo.
    *   *Correcto:* "Recibes una llamada urgente del supuesto soporte de telefonía indicando..."
    *   *Incorrecto:* "El colaborador de la empresa recibe una llamada..." o "Debes recibir una llamada..."
*   **Vocabulario Local y Natural (Español Chileno Laboral):** Utiliza términos que se emplean naturalmente en oficinas y comercios en Chile. Evita localismos exagerados o términos artificialmente neutros.
    *   Usa: "computador", "celular", "correo electrónico", "jefatura", "compañero de trabajo", "contraseña", "planilla de cálculo", "sucursal", "boleta", "factura".
    *   Evita: "ordenador", "móvil", "clave", "jefe de departamento", "fichero", "cartera".

---

## 2. Redacción de Dilemas y Ambigüedad
*   **Crear un Conflicto de Interés Real (Seguridad vs. Comodidad/Velocidad):**
    *   Un buen dilema no tiene una respuesta obvia que se resuelva por pura ética básica o sentido común.
    *   Estructura el contexto de modo que la opción incorrecta parezca atractiva porque ahorra tiempo, evita una discusión con una jefatura apresurada, o soluciona un problema inmediato de forma sencilla.
    *   *Ejemplo de dilema ambiguo:* "Tu jefatura te envía un correo apurado pidiéndote transferir $500.000 a un nuevo proveedor 'ahora mismo' porque está cerrando un negocio y no puede contestar llamadas. La política corporativa dice que todo nuevo proveedor debe validarse por llamada telefónica de 3 minutos."
        *   *Opción Izquierda:* "Haces la transferencia de inmediato para no hacer enojar a tu jefe." (Incorrecto, rompe la política de control de impersonation/pretexting).
        *   *Opción Derecha:* "Esperas y lo llamas para validar, asumiendo el retraso." (Correcto, aplica ciberhigiene y control a pesar del costo de tiempo y potencial molestia).
*   **Errores Plausibles:** El error del jugador debe justificarse por flojera natural, confianza en personas conocidas, cansancio, presiones de la operación o desinformación, haciendo que la caída en la trampa sea totalmente comprensible.

---

## 3. Explicaciones Didácticas y Consecuencias
*   **Analogías Cotidianas:** Si es necesario introducir un término técnico inevitable, explícalo inmediatamente usando analogías físicas o del día a día (ej. la doble llave de paso, el candado de la reja, la firma en notaría).
*   **Consecuencias con Foco Corporativo:** El feedback debe ilustrar qué pasaría en el contexto de negocio:
    *   *En lugar de:* "Tu computador tiene un virus espía."
    *   *Prefiere:* "El atacante accede a las planillas de sueldos de tus compañeros y las filtra a la competencia, lo que expone a la empresa a multas graves por la Ley de Datos Personales."
*   **Claridad BBCode:** Utiliza etiquetas `[b]negrita[/b]` para destacar los conceptos fundamentales en la pantalla de estudio y en la explicación, asegurando una lectura ágil en pantallas pequeñas de celulares.


## GUÍAS Y MARCOS DE REFERENCIA
### Fuente (Guía de Referencia): capec_social_engineering.md

# CAPEC (Common Attack Pattern Enumeration and Classification): Ingeniería Social en PYMEs

Este documento expone en detalle los patrones de ataque de ingeniería social según la clasificación CAPEC, adaptados para la concienciación de colaboradores en PYMEs chilenas. Proporciona el marco conceptual y los disparadores psicológicos que el modelo LLM empleará para estructurar dilemas de juego realistas y desafiantes.

---

## 1. Patrones de Ataque de Ingeniería Social

### CAPEC-98: Phishing (Pesca de Datos / Engaño por Correo)
*   **Mecanismo de acción:** El atacante envía comunicaciones electrónicas (principalmente correos electrónicos) falsificando la identidad de marcas, instituciones financieras o plataformas de confianza para incitar al usuario a revelar credenciales, realizar pagos o descargar malware.
*   **Tácticas de engaño sofisticadas:**
    *   **Typosquatting de dominios:** Usar direcciones de correo que parecen legítimas pero varían por una letra (ej: `contacto@bancochile-soporte.cl` en lugar de `bancochile.cl`, o `facturacion@servicios-sii.cl` en lugar de `sii.cl`).
    *   **Falsificación de remitente (Email Spoofing):** Manipular las cabeceras del correo para que en el campo "De:" aparezca un nombre conocido, aunque la dirección real sea externa.
    *   **Archivos adjuntos con macros o doble extensión:** Envío de facturas o cotizaciones falsas en formato `.xlsm` (con macros de Excel que descargan virus al activarse) o archivos con doble extensión como `factura_abril.pdf.exe` aprovechando que Windows oculta las extensiones por defecto.
    *   **Enlaces a portales de inicio de sesión falsificados:** Sitios que replican de forma exacta el diseño visual de Microsoft 365, Google Workspace o la banca electrónica de la empresa, pero el dominio de la barra de direcciones es fraudulento.

### CAPEC-624: Spear Phishing (Phishing Dirigido)
*   **Mecanismo de acción:** Ataque altamente personalizado dirigido a un empleado específico o a un rol concreto de la PYME (como la encargada de finanzas o recursos humanos).
*   **Uso de Inteligencia de Fuentes Abiertas (OSINT):** El atacante recopila información de la empresa y del empleado en redes sociales profesionales (LinkedIn) y en la web del negocio (nombres de jefes, proyectos recientes, proveedores habituales) para hacer que el pretexto parezca legítimo (ej: "Hola [Nombre], te escribo para el pago de la cotización del proyecto de redes que instalamos la semana pasada...").

### CAPEC-293: Pretexting (Creación de un Pretexto o Escenario Falso)
*   **Mecanismo de acción:** El atacante asume un rol falso para ganarse la confianza del colaborador y solicitar datos sensibles o accesos lógicos.
*   **Mecanismos comunes en oficinas:**
    *   **Soporte Técnico Impostor:** Un supuesto técnico de la compañía de internet o de soporte TI llama para "reparar una caída de servicio" o "aplicar una actualización urgente", solicitando al empleado su contraseña, el PIN del Wi-Fi de la oficina o instalar un programa de acceso remoto (como AnyDesk o TeamViewer).
    *   **Verificación del Proveedor:** El atacante se hace pasar por un proveedor frecuente y llama para notificar un supuesto "cambio de cuenta bancaria corporativa por auditoría" para los próximos pagos de facturas.

### CAPEC-403: Impersonation (Suplantación de Identidad / Estafa del CEO)
*   **Mecanismo de acción:** El atacante suplanta a una autoridad de alto nivel dentro de la organización (el dueño de la PYME, el gerente o la jefatura directa) para presionar al empleado.
*   **Ejemplo práctico:** El empleado de administración recibe un correo de "la gerenta" diciendo que está en una reunión confidencial importante y necesita con extrema urgencia y discreción que se realice una transferencia rápida a un proveedor específico, o que compre códigos de tarjetas de regalo virtuales.

### CAPEC-294: Baiting y Quid Pro Quo
*   **Baiting (Carnada):** Dejar un dispositivo físico de almacenamiento infectado (un pendrive USB o un disco duro) en un área común o estacionamiento de la oficina, etiquetado con nombres tentadores (ej: "Planilla de Sueldos 2026", "Despidos"). Al conectarlo por curiosidad, se ejecuta malware que infecta la red de la empresa.
*   **Quid Pro Quo (Algo a cambio de algo):** El atacante llama a varios números de la empresa ofreciendo una solución rápida a un problema tecnológico menor (ej: "Le ayudamos a liberar espacio en su correo") a cambio de las credenciales de acceso o de desactivar temporalmente el antivirus.

---

## 2. Disparadores Psicológicos y Mecanismos de Persuasión
Los ataques de ingeniería social tienen éxito explotando la psicología humana. Los escenarios dinámicos del LLM deben incluir estos resortes para forzar al jugador a discernir:

1.  **Urgencia:** Crear presión temporal ("Su cuenta será cancelada hoy mismo", "Pago inmediato antes de ir a juicio"). El cerebro cansado o estresado del empleado toma atajos y no verifica los detalles.
2.  **Autoridad:** Simular ser un jefe, la policía, el SII o una entidad reguladora. El colaborador chileno tiende a obedecer de forma automática a la autoridad para evitar problemas o amonestaciones.
3.  **Escasez:** Ofrecer un beneficio limitado ("Último día para actualizar el software corporativo con descuento", "Bono de productividad para los primeros 3 que hagan clic").
4.  **Simpatía o Empatía:** Establecer un tono amigable, de compañerismo o de auxilio ("Oye, soy nuevo en la sucursal y se me olvidó cómo entrar al portal, ¿me puedes dar el link?").
5.  **Consistencia / Validación Social:** Simular que otros ya han realizado la acción o que es parte de un proceso estándar ("Todo el equipo ya actualizó sus datos", "Como siempre lo hacemos...").


---
### Fuente (Guía de Referencia): cis_controls_ig1.md

# CIS Controls v8 - IG1 (Grupo de Implementación 1): Guía de Conocimiento Detallada para PYMEs

Este documento detalla las salvaguardas y especificaciones técnicas y administrativas de ciberhigiene básica que componen el Grupo de Implementación 1 (IG1) de CIS Controls v8. Está diseñado para proveer el conocimiento técnico detallado que el modelo LLM utilizará para formular escenarios educativos realistas y explicaciones con impacto organizacional.

---

## 1. Control 4: Configuración Segura de Activos y Software corporativos

### Salvaguardas Críticas:
*   **Procesos de Configuración Segura (CIS 4.1):** Mantener y aplicar plantillas de configuración segura documentadas para todos los sistemas operativos y aplicaciones de la empresa. Esto incluye desactivar servicios innecesarios, puertos abiertos no utilizados y cuentas de invitado predeterminadas.
*   **Desactivar Ejecución Automática (Autorun/Autoplay) (CIS 4.8):** Configurar los sistemas operativos de los computadores corporativos para que no ejecuten programas de forma automática al insertar medios extraíbles (discos externos, llaves USB). Esto previene infecciones automáticas por malware.
*   **Firewall Personal en Dispositivos Finales (CIS 4.4):** Habilitar y mantener activo el cortafuegos (firewall) nativo del sistema operativo en todos los computadores de los trabajadores, especialmente en aquellos que realizan teletrabajo, para bloquear conexiones entrantes sospechosas no solicitadas.

---

## 2. Control 5: Gestión de Cuentas y Control de Accesos

### Salvaguardas Críticas:
*   **Políticas de Contraseñas Fuertes (CIS 5.2):**
    *   **Longitud mínima:** Exigir contraseñas de al menos 14 caracteres de longitud si no se utiliza autenticación multifactor, o mínimo de 8 caracteres si se utiliza MFA.
    *   **Evitar la reutilización:** Las contraseñas de cuentas corporativas no deben coincidir con cuentas personales ni con el nombre de usuario o el nombre de la empresa.
    *   **Gestores de Contraseñas:** Fomentar el uso de gestores de credenciales autorizados para almacenar y generar claves robustas de forma aleatoria, reduciendo el hábito de escribirlas en post-its o archivos de texto plano.
*   **Autenticación Multifactor (MFA) Obligatoria (CIS 5.3):**
    *   **Cuentas críticas:** Exigir MFA para todo acceso remoto a la red corporativa (VPN), cuentas de correo institucional, plataformas financieras corporativas y accesos administrativos de sistemas en la nube.
    *   **Segundo Factor:** Implementar MFA mediante aplicaciones autenticadoras móviles (como Google Authenticator o Microsoft Authenticator) o llaves físicas de seguridad, evitando métodos vulnerables como SMS en la medida de lo posible.
*   **Bloqueo de Sesiones Inactivas (CIS 5.5):**
    *   Configurar los computadores y dispositivos móviles para que bloqueen la pantalla automáticamente tras un máximo de 15 minutos de inactividad (o 5 minutos en entornos altamente expuestos al paso de extraños).
    *   Fomentar el hábito de bloqueo manual inmediato al levantarse del escritorio mediante el atajo de teclado rápido `Windows + L` en Windows o `Control + Command + Q` en macOS.

---

## 3. Control 10: Defensas contra Malware y Amenazas de Correo

### Salvaguardas Críticas:
*   **Actualización de Firmas de Antivirus (CIS 10.1):** Asegurar que las herramientas de antimalware y antivirus corporativas estén configuradas para actualizar sus firmas y motores de detección de forma diaria y automática.
*   **Filtros de Correo Electrónico:** Implementar filtros antispam y antiphishing a nivel del servidor de correo corporativo para bloquear adjuntos ejecutables sospechosos (como `.exe`, `.vbs`, `.js`) o enlaces a dominios recientemente creados.

---

## 4. Control 11: Recuperación de Datos (Copias de Seguridad / Respaldos)

### Salvaguardas Críticas:
*   **Respaldos Frecuentes y Automatizados (CIS 11.1):** Realizar copias de seguridad automáticas semanales (o diarias para información crítica) de todos los datos clave del negocio (bases de datos de clientes, contabilidad, contratos).
*   **Protección y Aislamiento del Respaldo (CIS 11.2):**
    *   Al menos una copia de seguridad debe mantenerse físicamente aislada del sistema principal (offline) o protegida mediante mecanismos lógicos inmutables en la nube (copia desconectada).
    *   Esto es crítico para asegurar la restauración de la empresa frente a ataques de **ransomware** (virus secuestradores de datos) que buscan activamente y destruyen/cifran los respaldos conectados a la red local.
*   **Pruebas de Restauración (CIS 11.4):** Realizar simulacros de restauración de copias de seguridad de forma periódica (al menos trimestralmente) para comprobar la integridad de los datos y asegurar que el negocio pueda volver a operar rápidamente ante un incidente.

---

## 5. Control 12: Gestión de Infraestructura de Red y Actualizaciones

### Salvaguardas Críticas:
*   **Actualizaciones Automáticas de Software (CIS 12.1):** Habilitar las actualizaciones automáticas del sistema operativo y de aplicaciones críticas de terceros (navegadores web, suites de oficina, lectores de PDF). Los parches de seguridad corrigen vulnerabilidades conocidas que los atacantes usan para infiltrarse sin interactuar con el usuario.


---
### Fuente (Guía de Referencia): pedagogy.md

# Filosofía Pedagógica y Guía de Diseño Instruccional - CyberSwipe

Este documento establece las reglas fundamentales de diseño instruccional para la creación de cápsulas y cartas de dilemas en el videojuego serious game CyberSwipe. Debe ser utilizado por el modelo como directriz pedagógica primaria.

## Reglas Pedagógicas de Diseño

### 1. Aprendizaje Basado en Decisiones (Decision-Based Learning)
*   **Enseñar mediante situaciones prácticas:** El aprendizaje de conceptos de ciberseguridad debe ocurrir a partir del análisis y resolución de situaciones simuladas cotidianas, no de la memorización o repetición pasiva de teoría.
*   **No definir conceptos de forma abstracta:** Evita las cartas que solo pregunten por la definición de un término (ej: "¿Qué es el phishing?"). En su lugar, presenta un escenario real donde ocurra el ataque y el usuario deba decidir qué hacer.
*   **Foco en el cambio conductual:** El objetivo del contenido no es obtener una nota o aprobar un test académico, sino cambiar el comportamiento cotidiano del colaborador en su puesto de trabajo.

### 2. Evitar el "Sentido Común" y Obligar a Reflexionar
*   **Dilemas No Obvios:** Nunca generes escenarios o preguntas cuya respuesta correcta pueda deducirse únicamente por sentido común elemental (ej: "Un extraño te pide tu clave de banco por chat, ¿se la das o no?"). Si un usuario puede responder correctamente sin haber leído la cápsula de estudio, la carta está mal diseñada.
*   **Requisito de Estudio:** El jugador debe verse obligado a haber comprendido el concepto expuesto previamente en el `contenido_estudio` para saber cuál es la mejor práctica ante la situación.
*   **Plausibilidad de Errores:** Las opciones incorrectas deben representar errores realistas y plausibles que un empleado normal cometería por prisa, cansancio, comodidad, presiones de la jerarquía o confianza excesiva.

### 3. Ambigüedad y Alternativas Razonables
*   **Ambas opciones deben parecer correctas a primera vista:** Al leer el dilema, las opciones de la izquierda y de la derecha deben presentarse como cursos de acción razonables o comprensibles en el día a día laboral.
*   **Decisiones bajo dilemas empresariales:** A menudo, la decisión correcta de ciberseguridad puede implicar un coste de tiempo, dinero o comodidad para la empresa, mientras que la incorrecta ofrece conveniencia inmediata o rapidez.
*   **Diferenciación estricta:** Solo una de las dos opciones debe representar la mejor práctica estricta de seguridad digital de acuerdo con los marcos de referencia (CIS Controls y CAPEC).

### 4. Consecuencias con Impacto en la Organización (Negocio)
*   **Consecuencias Empresariales Reales:** Cuando el jugador comete un error, la explicación didáctica y el impacto numérico de la carta deben centrarse en el impacto real para el negocio o la PYME (pérdida de clientes, multas por la Ley 21.719 en Chile, paralización del sistema de ventas, daño a la reputación corporativa, costos de restauración), en lugar de limitarse a consecuencias individuales o abstractas del dispositivo (ej: "tu computador tiene un virus").
*   **Entender el porqué:** La explicación de retroalimentación inmediata debe argumentar el porqué del riesgo en un lenguaje no técnico pero corporativamente relevante.



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
