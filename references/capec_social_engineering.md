# CAPEC (Common Attack Pattern Enumeration and Classification): Ingeniería Social en PYMEs

Este documento expone los patrones de ataque de ingeniería social según la clasificación CAPEC, adaptados para la concienciación de colaboradores en PYMEs chilenas. Proporciona la taxonomía completa y los disparadores psicológicos para estructurar dilemas de juego diversos y realistas.

---

## 1. Taxonomía de Patrones de Ataque CAPEC

### CAPEC-98: Phishing (Pesca de Datos por Correo o Portales Web)
* **Email Phishing:** Enlaces o archivos adjuntos maliciosos enviados por correo masivo imitando instituciones conocidas.
* **Typosquatting de Dominios:** Direcciones sutilmente alteradas (ej. `soporte@bancochile-validaciones.cl` en lugar de `bancochile.cl`).
* **Adjuntos con Doble Extensión o Macros:** Facturas `.xlsm` o `.pdf.exe` recibidas por correo o compartidas en la nube.
* **Clonación de Portales:** Páginas web de inicio de sesión que imitan Microsoft 365, Google Workspace o la banca electrónica.

### CAPEC-624: Spear Phishing (Phishing Altamente Dirigido)
* **Investigación OSINT previa:** El atacante estudia perfiles de LinkedIn, web corporativa o redes de la PYME para dirigirse al contador, la encargada de adquisiciones o el recepcionista llamándolos por su nombre y citando proveedores o proyectos reales.

### CAPEC-293: Pretexting (Creación de un Escenario o Identidad Falsa)
* **Soporte TI Impostor:** Un supuesto técnico llama o escribe por Teams/WhatsApp solicitando restablecer accesos o instalar software de control remoto (AnyDesk, TeamViewer).
* **Auditoría o Inspección Falsa:** Un supuesto inspector externo, contador o regulador exige revisar documentos contables en el acto.
* **Cambio de Cuenta de Proveedor:** Un correo o llamada de un supuesto proveedor anunciando un "cambio urgente de cuenta bancaria" para el pago de facturas.

### CAPEC-403: Impersonation (Suplantación de Identidad / Estafa del CEO)
* **Suplantación de Jefatura:** Un mensaje urgente atribuido al dueño de la empresa pidiendo comprar gift cards, enviar datos de clientes o autorizar pagos saltándose el flujo formal.

### CAPEC-294: Baiting y Quid Pro Quo
* **Baiting (Carnada Física o Digital):** Pendrives promocionales regalados en ferias o dejados en la recepción; enlaces a software "gratuito" o plantillas de diseño en la nube.
* **Quid Pro Quo (Algo a cambio de algo):** Promesas de soporte informático gratis, bonos u optimizaciones a cambio de entregar credenciales o desactivar protecciones.

### CAPEC-555: Smishing (SMS Phishing) y Vishing (Voice Phishing)
* **Smishing:** SMS alertando sobre bloqueos de cuenta, paquetes retenidos en courier o alertas bancarias con enlaces maliciosos.
* **Vishing:** Llamadas telefónicas donde se manipula al usuario haciéndose pasar por soporte, ejecutivos bancarios o entes de gobierno (SII).

### CAPEC-587: QRphishing / Quishing (Ataques mediante Códigos QR)
* **QR Falsos en Documentos u Oficinas:** Códigos QR pegados en folletos, mesas de reuniones o documentos impresos recibidos por correspondencia que redirigen a formularios de phishing.

### CAPEC-507: Physical Social Engineering (Tailgating y Shoulder Surfing)
* **Tailgating (Colado físico):** Una visita o persona externa que entra a la oficina o sala de servidores aprovechando que alguien le abre la puerta por cortesía.
* **Shoulder Surfing (Mirada sobre el hombro):** Observación discreta de pantallas o teclados mientras el trabajador opera en cafeterías, aeropuertos, buses o escritorios compartidos.

### Reverse Social Engineering (Ingeniería Social Inversa)
* Provocar que el propio empleado contacte al atacante (ej. dejar un aviso de "error en sistema, llame a este número de soporte" en una pantalla o impresora).

---

## 2. Disparadores Psicológicos y Mecanismos de Persuasión
Los dilemas del juego deben explotar estos resortes psicológicos:
1. **Urgencia / Presión Temporal:** Exigir acción inmediata antes de que la víctima piense o valide.
2. **Autoridad y Jerarquía:** Invocar cargos superiores, entes reguladores o consecuencias legales.
3. **Simpatía y Ayuda:** Fingir ser un nuevo compañero, cliente en apuros o colega de sucursal.
4. **Validación Social:** Afirmar que "todos los demás ya lo hicieron" o que "es el procedimiento normal".
5. **Miedo a Consecuencias:** Amenazar con retrasos operativos, pérdida de contratos o sanciones.
