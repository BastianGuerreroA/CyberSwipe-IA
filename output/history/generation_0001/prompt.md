Por favor, genera un archivo JSON que contenga exactamente 1 cápsulas de preguntas basadas en el tema: 'OWASP Top 10: Inyecciones SQL'.

## REGLAS DE GENERACIÓN
# Reglas de Generación de Preguntas - CyberSwipe-AI

Al generar el contenido de ciberseguridad, debes seguir estrictamente las siguientes pautas estructurales:

## 1. Estructura de Cápsula
* Cada cápsula representa una unidad temática de aprendizaje (ej. "Phishing Corporativo").
* Debe tener un identificador único (ej. `capsule_phishing_01`).
* Debe especificar el tema principal (`topic`) y el nivel de dificultad (`difficulty`: `Fácil`, `Medio`, `Difícil`).
* Debe contener un número definido de cartas asociadas (generalmente entre 3 y 5 cartas por cápsula).

## 2. Estructura de Carta
Cada carta representa una decisión o dilema que el jugador debe resolver. Debe contener:
* `id`: Identificador único que asocie la carta a su cápsula (ej. `card_phishing_01_01`).
* `title`: Un título corto y llamativo para el evento (máximo 30 caracteres).
* `description`: Explicación del escenario en segunda persona, situando al jugador en la acción (ej. "Recibes un correo sospechoso solicitando cambiar tu contraseña urgente...").
* `category`: Categoría técnica (ej. `Ingeniería Social`, `Seguridad Web`, `Redes`, `Criptografía`).
* `level`: Nivel numérico de la carta.
* `effects`: Un diccionario de efectos numéricos que afectarán las métricas del jugador en el videojuego (ej. `reputation`, `budget`, `security_level`).
* `feedback`: Respuestas de retroalimentación pedagógica para cada opción disponible, detallando por qué fue una buena o mala decisión basándose en el RAG.


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


## CONTEXTO DE CONOCIMIENTO (RAG)
### Fuente: cybersecurity_guidelines.md

# Directrices Generales de Ciberseguridad

Estas son directrices prácticas que sirven como base para crear dilemas en los niveles del juego:

## Contraseñas y Autenticación:
* Uso de gestores de contraseñas.
* Activación mandatoria de MFA (Multifacto Authentication) en todas las cuentas corporativas.
* Evitar reutilizar contraseñas en múltiples servicios.

## Ingeniería Social:
* Desconfiar de correos electrónicos no solicitados con archivos adjuntos u enlaces de origen sospechoso (Phishing).
* Reconocer tácticas de urgencia o suplantación de identidad de altos ejecutivos (CEO Fraud).
* Evitar conectar memorias USB encontradas en zonas públicas (Baiting).

## Seguridad en el Puesto de Trabajo:
* Bloquear la pantalla de la computadora al levantarse del escritorio (Clean Desk Policy).
* No divulgar contraseñas o datos corporativos confidenciales por canales de mensajería informal.
* Reportar inmediatamente la pérdida de dispositivos corporativos al equipo de TI.


---
### Fuente: iso27001.md

# Contexto de Ciberseguridad: ISO/IEC 27001

La norma **ISO/IEC 27001** es un estándar internacional para los Sistemas de Gestión de la Seguridad de la Información (SGSI).

## Objetivos de Control Clave
* **Políticas de seguridad de la información (A.5)**: Definición y difusión de directrices organizacionales.
* **Seguridad de los recursos humanos (A.7)**: Concienciación sobre ciberseguridad antes, durante y después de la relación laboral.
* **Control de acceso (A.9)**: Principio de mínimo privilegio (Least Privilege) y autenticación robusta.
* **Criptografía (A.10)**: Uso correcto de cifrado para confidencialidad e integridad.
* **Seguridad física y del entorno (A.11)**: Protección de perímetros, oficinas y equipos.
* **Seguridad de las operaciones (A.12)**: Gestión de malware, copias de seguridad (backups), logs de auditoría y monitoreo.
* **Seguridad de las comunicaciones (A.13)**: Protección de redes y tráfico de datos.
* **Gestión de incidentes de seguridad de la información (A.16)**: Reportar eventos y debilidades a tiempo para mitigar el impacto.


---
### Fuente: nist.md

# Contexto de Ciberseguridad: Marco NIST (Cybersecurity Framework)

El Marco de Ciberseguridad del **NIST** (National Institute of Standards and Technology) se organiza en cinco funciones continuas y concurrentes:

## Funciones del NIST CSF:
1. **Identificar (Identify)**:
   - Entender el entorno de negocio, los activos físicos y de software, y las vulnerabilidades para gestionar los riesgos.
2. **Proteger (Protect)**:
   - Implementar salvaguardas para garantizar la entrega de servicios de infraestructura crítica. Incluye control de accesos, concientización, y protección de datos.
3. **Detectar (Detect)**:
   - Desarrollar e implementar actividades para identificar la ocurrencia de eventos de ciberseguridad a tiempo (monitoreo continuo).
4. **Responder (Respond)**:
   - Actividades relacionadas con la reacción ante incidentes detectados. Planificación, comunicación, análisis y mitigación del ataque.
5. **Recuperar (Recover)**:
   - Planes de resiliencia para restaurar las capacidades o servicios que fueron afectados debido a un incidente de seguridad (backups, planes de contingencia).


---
### Fuente: owasp.md

# Contexto de Ciberseguridad: OWASP Top 10

El proyecto **OWASP** (Open Web Application Security Project) documenta los diez riesgos de seguridad más críticos en aplicaciones web:

## Categorías Principales (OWASP Top 10):
1. **A01:2021 - Control de Acceso Roto (Broken Access Control)**:
   - Los usuarios pueden actuar fuera de sus permisos (ej. acceder a cuentas ajenas o endpoints de administración sin autenticar).
2. **A02:2021 - Fallas Criptográficas (Cryptographic Failures)**:
   - Exposición de datos sensibles en tránsito o almacenamiento debido a falta de cifrado o algoritmos débiles.
3. **A03:2021 - Inyección (Injection)**:
   - SQL Injection, XSS, o inyección de comandos debido al filtrado deficiente de inputs del usuario.
4. **A04:2021 - Diseño Inseguro (Insecure Design)**:
   - Falta de modelado de amenazas y principios de diseño seguro durante el ciclo de vida del software.
5. **A05:2021 - Configuración de Seguridad Incorrecta (Security Misconfiguration)**:
   - Cuentas con contraseñas por defecto activas, verbose error pages habilitados, puertos innecesarios abiertos.
6. **A06:2021 - Componentes Vulnerables y Desactualizados**:
   - Uso de librerías o dependencias con vulnerabilidades conocidas sin parchear.
7. **A07:2021 - Fallas de Identificación y Autenticación**:
   - Falta de protección contra ataques de fuerza bruta, credenciales débiles aceptadas, fallas en la invalidación de sesiones.
8. **A08:2021 - Fallas en la Integridad del Software y de los Datos**:
   - Actualizaciones de código o deserialización de datos sin verificar su origen y firma digital.
9. **A09:2021 - Fallas en el Registro y Monitoreo de Seguridad (Security Logging and Monitoring Failures)**:
   - Los incidentes pasan desapercibidos porque no se registran o auditan los eventos sospechosos en logs.
10. **A10:2021 - Falsificación de Solicitudes del Lado del Servidor (SSRF)**:
    - Ocurre cuando una aplicación web obtiene un recurso remoto sin validar la URL introducida por el usuario.


---
### Fuente: writing_style.md

# Estilo de Escritura Educativa

El contenido pedagógico de CyberSwipe-AI debe orientarse a provocar reflexión crítica en el jugador:

## Pautas del Tono
* **Desafiante**: Plantea la decisión como un dilema real en el que ambas opciones parecen viables a primera vista para que el jugador deba analizar el riesgo.
* **No condescendiente**: Evita regañar al jugador si toma la opción incorrecta. Explica las consecuencias del error basándote en la seguridad corporativa e industrial.
* **Vocabulario preciso**: Usa términos estándar (firewall, malware, spoofing, phishing, token, hash) en lugar de traducciones forzadas si el término original es el estándar de la industria.



## REGLAS DE SALIDA Y ESTRUCTURA
# Reglas de Salida del JSON - CyberSwipe-AI

Es crítico que tu respuesta consista **únicamente** en un objeto JSON válido que cumpla con el formato estructurado requerido. Cualquier texto adicional, explicaciones o saludos fuera del bloque JSON romperá el sistema de validación del pipeline.

## Pautas de Salida:
1. **Salida limpia**: No agregues textos introductorios (como "Aquí tienes tu JSON:") ni explicaciones posteriores.
2. **Bloque de código JSON**: Encapsula el JSON estrictamente dentro de un único bloque de markdown `json ... `.
3. **Valores nulos y vacíos**: Está terminantemente prohibido utilizar valores nulos (`null`) o cadenas de texto vacías (`""`) para propiedades requeridas. Todos los campos de texto deben estar poblados con información relevante y redactada.
4. **Codificación**: Asegúrate de que todos los caracteres especiales del español (tildes, eñes) estén correctamente escapados o representados en codificación UTF-8.
5. **IDs Únicos**: Verifica que no se duplique ningún valor de la propiedad `id` a lo largo de toda la respuesta.


### PLANTILLA DE REFERENCIA JSON
```json
{
  "version": "1.0.0",
  "generated_at": "2026-07-06T20:00:00Z",
  "capsules": [
    {
      "id": "capsule_phishing_01",
      "title": "Ingeniería Social en el Trabajo",
      "topic": "Phishing y Concienciación",
      "difficulty": "Fácil",
      "cards": [
        {
          "id": "card_phishing_01_01",
          "title": "El Correo del Director",
          "description": "Recibes un correo que simula ser del Director de Finanzas solicitando la transferencia urgente de fondos para cerrar una adquisición confidencial. Pide no hablarlo con nadie más.",
          "category": "Ingeniería Social",
          "level": 1,
          "options": [
            {
              "text": "Proceder con la transferencia para evitar retrasos organizacionales.",
              "effects": {
                "reputation": -15,
                "budget": -30,
                "security_level": -10
              },
              "feedback": "¡Incorrecto! Has caído en una estafa de 'CEO Fraud' (Fraude del CEO). Los procesos financieros siempre deben seguir canales formales de aprobación y doble verificación, independientemente de la supuesta urgencia."
            },
            {
              "text": "Llamar directamente al Director de Finanzas para corroborar la solicitud.",
              "effects": {
                "reputation": 10,
                "budget": 0,
                "security_level": 15
              },
              "feedback": "¡Correcto! Verificar por un canal alternativo (fuera de banda) la autenticidad de peticiones financieras inusuales es el protocolo estándar de seguridad para frustrar ataques de ingeniería social."
            }
          ]
        }
      ]
    }
  ]
}

```
