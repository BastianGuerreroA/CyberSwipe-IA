# Filosofía Pedagógica y Guía de Diseño Instruccional - CyberSwipe

Este documento establece las reglas fundamentales de diseño instruccional para la creación de cápsulas y cartas de dilemas en el videojuego serious game CyberSwipe. Debe ser utilizado por el modelo como directriz pedagógica primaria.

---

## 1. Progresión Pedagógica Obligatoria
La dificultad de cada cápsula se deriva estrictamente del nivel de aprendizaje requerido por sus objetivos pedagógicos.
No determines la dificultad por el número de cápsula, sino por la complejidad de la decisión necesaria para cumplir los objetivos.

Las decisiones evolucionan a lo largo del programa en 5 niveles:
1. **Reconocer un riesgo evidente** (identificar vulnerabilidad o mala práctica).
2. **Aplicar una buena práctica** (seguir la recomendación directa aprendida).
3. **Decidir entre productividad y seguridad** (asumir un retraso operativo breve o incomodidad a cambio de mantener la seguridad).
4. **Aplicar políticas organizacionales** (seguir protocolos formales ante presiones de terceros o jefaturas).
5. **Analizar escenarios con múltiples riesgos simultáneos** (identificar cadenas de ataques combinados).

---

## 2. Aislamiento Temático Estricto y No-Contaminación
* **Respeto estricto del tema asignado:** Cada cápsula debe tratar **única y exclusivamente** de los conceptos y objetivos asignados a su tema en `aprendizaje.md`.
* **Prohibición de filtración temática:** La Cápsula 1 (Contraseñas/MFA) **NO debe incluir** escenarios de Phishing, correos falsos ni soporte impostor, ya que esos corresponden a cápsulas posteriores.
* **Progresión de aprendizaje:** El jugador NO debe aprender ni ver conceptos de Phishing o Ingeniería Social antes de llegar a la cápsula específica donde se enseñan.

---

## 3. Prohibición Absoluta de Cartas Binarias u Obvias
* **Prohibido el sentido común obvio:** Está estrictamente prohibido generar cartas cuya respuesta correcta sea evidente para cualquier persona sin conocimientos de ciberseguridad (ej. "Dar contraseña" vs "No dar contraseña", "Hacer clic rápido" vs "Revisar").
* **Ambas opciones deben parecer razonables y estar bien redactadas:** Las dos opciones (izquierda y derecha) deben ser frases completas, plausibles y defendibles en el día a día laboral. La opción incorrecta debe representar un atajo tentador (ahorro de tiempo, evitar discusión, conveniencia inmediata), mientras que la opción correcta representa el cumplimiento de la política o procedimiento de verificación aprendido.
* **Requisito de contenido de estudio:** Toda carta debe obligar al jugador a aplicar un procedimiento o concepto aprendido en el `contenido_estudio`, no una reacción de intuición básica.

---

## 4. Vinculación 1-a-1 entre Contenido de Estudio y Cartas
* **Mapeo directo:** El `contenido_estudio` debe enseñar exactamente **5 conceptos clave distintos**.
* **Un concepto por carta:** Cada una de las 5 cartas asociadas evaluará **un concepto específico e individual** expuesto en el `contenido_estudio`.
* **Sin repetición:** Está prohibido repetir el mismo concepto o escenario dos veces dentro de una misma cápsula.

---

## 5. Diversidad Obligatoria de Canales y Entornos Laborales
Los escenarios deben variar drásticamente y no limitarse a la oficina/correo/jefe. Es obligatorio rotar entre:
* **Canales y Plataformas:** WhatsApp, Teams, Microsoft 365, Google Drive, OneDrive, llamadas telefónicas, SMS, códigos QR, impresoras corporativas, pendrives/USB promocionales, portales web de proveedores.
* **Entornos:** Oficina presencial, teletrabajo/hogar, viajes de negocios, cafeterías, aeropuertos, hoteles, recepción, salas de reuniones.
* **Roles:** Colegas, jefaturas, proveedores, clientes, contadores externos, personal de RRHH, finanzas, adquisiciones, recepción, soporte TI.

---

## 6. Explicaciones Didácticas "Por Qué" (Impacto Organizacional)
* **Explicación causal:** La retroalimentación debe explicar qué ocurrió, por qué ocurrió, qué patrón o vulnerabilidad se explotó y cuál es la consecuencia real en la PYME (multas Ley 21.719 en Chile, paralización del sistema de ventas, fuga de clientes, daño reputacional).
* **Evitar sermones vacíos:** Evita frases como "Nunca hagas esto" o "Debes ser más cuidadoso". Explicar la lógica del riesgo y el impacto en la empresa.
